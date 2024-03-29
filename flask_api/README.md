# Flask
Flask Readme

## Create environment 
```bash
$(bash): python3.10 -m venv .venv

$(bash): conda create -n venv python=3.10.0 # create virtual environment with python 3.10.0
$(bash): conda activate venv # activate environment
$(bash): conda deactive venv # deactivate environment
```

## Run flask
```bash
$(bash): flask run
```

## Build Docker Image
```bash
$(bash): docker build -t rest-apis-flask-python .
```

## Run Docker Container
```bash
$(bash): docker run -d -p 5000:5000 -w /app -v "${pwd}:/app" --name flask_api flask-image-name
```