# Serverless FastAPI Boilerplate

> Yuri Niitsuma <ignitzhjfk@gmail.com>

Deploy a [FastAPI](https://fastapi.tiangolo.com/) on AWS Lambda with APIGateway.

## Quick Start

Of course you need [NodeJS](https://nodejs.org/en/) with [npm](https://www.npmjs.com/).

Install serverless framework with npm.

```shell
npm install -g serverless
```

Download Lambda Layer libaries with [Docker](https://www.docker.com/).

```shell
# On Linux/Unix
cd serverless/layers/fastapi && \
mkdir -pv python/lib/python3.8/site-packages && \
docker run -v "$PWD":/var/task "lambci/lambda:build-python3.8" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.8/site-packages/" && \
cd ../../../
```

\[Optional\] If you want to use deployment bucket, change in `serverless.yml` to your desired bucket in `deploymentBucket: YOUR_BUCKET`. This will avoid to create unnecessary buckets to deploy the zip file to Lambda.

Deploy.

```shell
sls deploy -v
```