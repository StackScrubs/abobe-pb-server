from flask import Flask, request
import os
import pymysql

app = Flask(__name__)

@app.route("/redeem", methods=["POST"])
def claimLicenseKey():
        content = request.get_json(force = True)
        email = content['email']
        license_key = content['license_key']

        sql = "UPDATE user_license SET claimed=1 WHERE user='" + email + "' AND license_key='" + license_key + "' AND claimed=0"
        mycursor.execute(sql)
        mydb.commit()

        mycursor.execute("SELECT * FROM user_license WHERE user='" + email + "' AND license_key='" + license_key + "' AND claimed=1")
        result = mycursor.fetchall()

        if(len(result) == 1):
                return "License-key successfully claimed!"
        else:
                return "No matching entries found in DB"

        
if __name__ == "__main__":
        app.run()

app.logger.info("%s" % os.environ.get("DB"))
global mydb
mydb = pymysql.connect(
        host= os.environ.get('HOST'),
        db=os.environ.get('DB'), 
        user=os.environ.get('DB_USERNAME'), 
        passwd=os.environ.get('DB_PASSWORD'), 
)

global mycursor
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE user_license")
mycursor.execute("CREATE TABLE user_license (user VARCHAR(40), license_key VARCHAR(100), claimed tinyint(1))")

sql = "INSERT INTO user_license (user, license_key, claimed) VALUES (%s, %s, %s)"
val = [
        ("tommathon@skiff.com", "TEM8S2-2ET83-W3K7", 1),
        ("maggen@gmail.com", "CGKP1-DPSI2-EPZO1", 1),
        ("krisa@chrysler.com", "FLAG{yOu_f0unD_7hE_flAg}", 0)
]

mycursor.executemany(sql, val)
mydb.commit()
