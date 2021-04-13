# Coalesce API for insurance data

This project uses a mix of creational design patterns to abstract logic from the different components.

It's intended use is to be deployed as a container.

## Development Env

It's recommended to use a virtual environment to test and develop this app:

### Create using venv
`python3 -m venv venv`

### Activate virtual-env
`. venv/bin/activate`

### Deactivate virtual-env
`deactivate`

## Build

`docker build . -t insurance_api`

## Run

`docker run -p5000:5000 -d --name insurance_api insurance_api`

Once this container is up and running, you can deploy the auxiliary api contained in the `./mockapi` folder.

## Endpoints

This api consists of a single endpoint:

`http://localhost:5000/insurance-info?member_id=1`


## Tests

In order to run the tests, you first have to create a virtual environment, and then execute the following commands:

- `python -m pip install -r requirements.txt`

- `python -m coverage run -m unittest discover`

- `python -m coverage report -m`

