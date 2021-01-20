# FastAPI Lambda Layer

```
cd layers/fastapi
mkdir -pv python/lib/python3.8/site-packages
docker run -v "$PWD":/var/task "lambci/lambda:build-python3.8" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.8/site-packages/"
```