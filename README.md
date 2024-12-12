# MadPy Meetup Dec 2024

## Overview
Repo to accompany my MadPy talk ([slides](https://docs.google.com/presentation/d/1VuJPRbY5_FsNfnrJYjHGK-19T0lhvaWSE1efW4sANZo)) on testing.

### Quck Start
```
uv venv --python 3.12.7
uv pip install -r pyproject.toml --extra dev
```

### Running Tests
More details are in the slidedeck but the majority of tests can be run simply using [pytest](https://docs.pytest.org/en/stable/). To run all non integration tests:
```
pytest . -m "not integration"
```

To run all tests. You will need to start the [Docker](https://www.docker.com/):
```
docker-compose up -d
```
Once the postgres service is up, you can run all the tests.
