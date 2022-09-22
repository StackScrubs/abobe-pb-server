from flask import Flask, request
import logging
import os
import json
import pymysql

app = Flask(__name__)

@app.route("/getkey", methods=["GET"])
def getLicenseKey():
        content = request.get_json(force = True)
        email = content['email']

        sql = "SELECT license_key FROM user_license WHERE user='" + email + "'"
        result = mycursor.execute(sql)
        mydb.commit()

        result = mycursor.fetchall()
        json_result = json.dumps(result)

        return json_result


app.logger.info("%s" % os.environ.get("DB"))
conn = {
        "host": os.environ.get('HOST'),
        "db": os.environ.get('DB'), 
        "user": os.environ.get('DB_USERNAME'), 
        "password": os.environ.get('DB_PASSWORD'),
}

global mydb
mydb = pymysql.connect(**conn)

global mycursor
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS user_license")
mydb.commit()

mycursor.execute("CREATE TABLE user_license (user VARCHAR(40), license_key VARCHAR(100), claimed tinyint(1))")

sql = "INSERT INTO user_license (user, license_key, claimed) VALUES (%s, %s, %s)"
val = [
        ("tommathon@skiff.com", "TEM8S2-2ET83-W3K7", 1),
        ("maggen@gmail.com", "CGKP1-DPSI2-EPZO1", 1),
        ("krisa@chrysler.com", "FLAG{yOu_f0unD_7hE_flAg}", 0)
]

mycursor.executemany(sql, val)
mydb.commit()
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

if __name__ == "__main__":
        app.run()
