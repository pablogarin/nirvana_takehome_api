# Small mock API

This mock API works as a testin tool for the main application.

## Build

`docker build . -t mock_api`

## RUN

`docker run -d --network="container:$(docker ps|grep insurance_api|awk '{print $1}')" --name mock_api mock_api`