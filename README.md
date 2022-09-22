# abobe-pb-server

# Build instructions
Make sure docker and docker-compose is installed and running.
```bash
$ make build
```

Alternatively if make is not available run:
```bash
$ docker build -t flask-app .
```


# Run instructions
Make sure docker and docker-compose is installed and running.
```bash
$ make run
```

Alternatively if make is not available run:
```bash
# Must build an image atleast once before the first run
$ docker build -t flask-app . 
$ docker-compose up
```
