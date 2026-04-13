# Web hits counter (Flask)

Small Flask web server that:

- **Counts** how many times the root endpoint (`/`) was requested (GET).
- **Appends** a line to `logs/data.log` for each hit.
- **Exposes** an endpoint (`/logs`) to read the log back.

## Requirements

- **Python**: 3.9+
- **Dependencies**: see `requirements.txt` (Flask + pytest + requests)

## Install

From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Start the server (binds to `localhost:9999`):

```bash
python3 server.py
```

## Endpoints

- **`GET /`**
  - Increments an in-memory counter
  - Returns: `Get request occurred N time(s)\n`
  - Appends the same line to `logs/data.log`

- **`GET /logs`**
  - Returns the full contents of `logs/data.log`

Quick manual check:

```bash
curl -s http://localhost:9999/
curl -s http://localhost:9999/logs
```

## Logging behavior

- The log file path is **`logs/data.log`** (relative to the repo root).
- The log is **cleared on server startup** (when routes are imported), so restarting the server resets the log contents.

## Demo

![Screenshot](server/demo/server.png)

## Tests

Run **unit** tests (no server required):

```bash
pytest -v tests/unittests
```

Run **functional** tests (server must be running on `localhost:9999` in another terminal):

```bash
pytest -v tests/functional
```

### Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.9+` is required to run the code
- run `pip install -r requirements.txt` to install required python packages
