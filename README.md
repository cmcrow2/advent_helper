# advent_helper

Connects to OpenAI and uses it to run tools related to the Advent of Code challenges.

## Setup Instructions

### Install pipx:

https://pipx.pypa.io/stable/installation/

### Install poetry:

https://python-poetry.org/docs/

You can run `pipx install poetry` in your computer’s root directory

Make sure it is installed by running `poetry`.

### Navigate to the directory of the cloned repository:

run `poetry install --no-root`

This command should install everything in your `pyproject.toml` file.

### Setup Environment Variable

Create a `.env` file in the root directory.

Add `OPENAI_API_KEY=YOUR_VARIABLE_HERE` at the top of the file.

### Activate the Poetry Shell Enviroment

Run `poetry shell` in your terminal.

### Bug fix

You may still see squiggly lines under imported packages in VSCode. To fix this, poetry should log your virtual environment path in the console. `spawning shell within YOUR_FILE_PATH`

Copy that file path, then enter an interpreter using VSCode’s command palette and paste in the path. The squiggles should go away.

### Running the Program

Run `python3 main.py` in your terminal.
