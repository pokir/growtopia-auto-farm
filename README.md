## Setup

### Install the requirements

Optionally setup a virtual environment to avoid installing requirements globally:

```sh
python3 -m venv venv
venv\Scripts\activate.bat
```

Install the requirements:

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### Configure

Create a `.env` file and add the following values (see `example.env` for examples):

| Variable | Type | Description |
| :-: | :-: | :-: |
| WALK\_SECONDS\_PER\_BLOCK | float | The number of seconds it takes to walk from one block to the next. |
| PUNCH\_SECONDS\_PER\_BLOCK | float | The number of seconds it takes to punch (destroy) a block. |

## Run

```
venv\Scripts\python.exe main.py
```
