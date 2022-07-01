# Safari to Yacy: 

[![CI](https://github.com/rob-luke/safari-to-yacy/actions/workflows/main.yml/badge.svg)](https://github.com/rob-luke/safari-to-yacy/actions/workflows/main.yml)

Send your current Safari URL to Yacy for indexing.
This project contains a python script which handles the heavy lifting,
and an Alfred workflow which provides a convenient interface to call the script.

## Usage

* Use your hotkey to show Alfred
* Type `ysend` and the foremost Safari web page will be sent to Yacy
* Simple!


## Installation

1. Clone this repository 
   ```console
   cd /path/where/projects/live
   git clone https://github.com/rob-luke/safari-to-yacy.git
   ```
   
2. Create poetry environment (you may need to install poetry first):
   ```console
   cd safari-to-yacy
   poetry install
   ```
   
3. Determine the python executable created by poetry:
   ```console
   which python  # copy this output for later
   ```
   
4. Install the Alfred workflow by doubling clicking the workflow in the repository.
   You can enter the following items:
   * pythonpath: the python executable that was copied above
   * yacy_url: url of the yacy instance
   * yacy_auth_username: (optional) yacy username
   * yacy_auth_password: (optional) yacy password
   * verbose: (optional) do you want extra information printed out
   
5. Try running the workflow by typing `ysend` at the Alfred prompt
