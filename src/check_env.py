import os

from constants import KEYS


# List of all environment variables that are required and will be used
ENVIRONMENT_VARIABLE_NAMES = [
    'WALK_SECONDS_PER_BLOCK',
    'PUNCH_SECONDS_PER_BLOCK',
    'WALK_KEY',
    'PUNCH_KEY',
]


def warn_missing_environment_variable(name):
    # Warn user about missing environment variable and exit

    print(f'The environment variable {name} is missing.')
    print('Did you follow the steps in README.md and did you see example.env?')
    exit()


def warn_invalid_environment_variable(name):
    # Warn user about invalid environment variable and exit

    print(f'The environment variable {name} is invalid.')
    print('See example.env for examples of valid values.')
    exit()


def check_environment_variables():
    # Check if the environment variables are correct and exit if not

    # Check if all required environment variables exist
    for environment_variable_name in ENVIRONMENT_VARIABLE_NAMES:
        if os.getenv(environment_variable_name) is None:
            warn_missing_environment_variable(environment_variable_name)

    # Check if the time environment variables are valid
    for environment_variable_name \
        in filter(lambda n: n.endswith('SECONDS_PER_BLOCK'),
                  ENVIRONMENT_VARIABLE_NAMES):

        try:
            float(os.getenv(environment_variable_name))
        except ValueError:
            warn_invalid_environment_variable(environment_variable_name)

    # Check if the key environment variables are valid
    for environment_variable_name in filter(lambda n: n.endswith('KEY'),
                                            ENVIRONMENT_VARIABLE_NAMES):

        if os.getenv(environment_variable_name) not in KEYS:
            warn_invalid_environment_variable(environment_variable_name)
