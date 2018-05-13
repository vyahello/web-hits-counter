# Simple flask web server
- `server.py` tool allows to launch web server. 

## Run flask web server
```bash
~ python server.py
```

## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vjagello93@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages

### Run unittests
Run `pytest -v tests/unitests` from shell in the root directory of the repository.

### Run functional tests
Run `pytest -v tests/functional` from shell in the root directory of the repository.
