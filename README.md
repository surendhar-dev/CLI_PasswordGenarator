# Password Generator CLI

A lightweight command-line password generator built with Python using secure randomness and local JSON file storage.

## Project Structure

```text
password_generator/
│
├── generator/
│   ├── __init__.py
│   ├── cli.py          # Terminal display & formatting
│   ├── core.py         # Password generation & strength checking
│   └── storage.py      # JSON file I/O operations
│
├── data/
│   └── history.json    # Local password history
│
├── main.py             # Main execution entry point
└── README.md           # Documentation
```

## Features

* Generate customizable passwords
* Choose password length
* Include uppercase, lowercase, numbers & symbols
* Password strength checker
* Validate password configurations
* Save password history locally in JSON
* View password history
* Clear password history

## How to Run

```bash
python main.py
```

No external dependencies are required.

## Storage

Password history is stored locally in:

```text
data/history.json
```
