# growtopia-auto-farm

Farm in Growtopia automatically.

This should work with multiple instances of Growtopia open.

Note that it selects all windows containing "Growtopia" (case insensitive) in the title.\
This can cause issues if you have windows containing "Growtopia" in the title, but aren't Growtopia.\
This is a know issue and is being worked on (#4).

## Requirements

- Python 3 (tested on python 3.10.5)
- Windows

## Setup

### Install the dependencies

Optionally setup a virtual environment to avoid installing requirements globally:

```sh
python3 -m venv venv
venv\Scripts\activate.bat
```

Then install the dependencies:

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### Configure

It is your job to configure the walking and punching times.

Create a `.env` file and add the following values (see `example.env` for examples):

| Variable | Type | Description |
| :-: | :-: | :-: |
| **WALK\_SECONDS\_PER\_BLOCK** | float | The number of seconds it takes to walk from one block to the next. |
| **PUNCH\_SECONDS\_PER\_BLOCK** | float | The number of seconds it takes to punch (destroy) a block. |

## Run

```
venv\Scripts\python.exe main.py
```
