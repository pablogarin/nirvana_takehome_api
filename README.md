# Coalesce API for insurance data

This project uses a mix of creational design patterns to abstract logic from the different components.

It's intended use is to be deployed as a container.

## Build

`docker build . -t insurance_api`

## Run

`docker run -p5000:5000 -d --name insurance_api insurance_api`

Once this container is up and running, you can deploy the auxiliary api contained in the `./mockapi` folder.

## Endpoints

This api consists of a single endpoint:

`http://localhost:5000/insurance-info?member_id=1`


