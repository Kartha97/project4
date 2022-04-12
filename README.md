# Project Setup

[![Production Workflow](https://github.com/kaw393939/docker_flask/actions/workflows/prod.yml/badge.svg)](https://github.com/Kartha97/project/blob/master/.github/workflows/prod.yml)

* [Production Deployment](https://karthat-project4-prod.herokuapp.com/)


[![Development Workflow](https://github.com/kaw393939/docker_flask/actions/workflows/dev.yml/badge.svg)](https://github.com/Kartha97/project/blob/master/.github/workflows/dev.yml)

* [Developmental Deployment](https://karthat-project4-dev.herokuapp.com/)

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest