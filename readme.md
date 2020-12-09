# Outpost Kodelia - The Black Hole

The Black Hole is a custom pinball game created by Outpost Kodelia. It is a retheme of Williams's Phoenix (1978) but has been modified to suit the needs of a modern game. It is based off of the P3-ROC hardware system and Mission Pinball Framework.

## Installation

The game can be run on either Windows or Ubuntu Linux. Prior to setting up, download and install Python v3.6.8.

After cloning the repo, use the following commands to create a virtual Python environment, update pip, and install the MPF software and its dependencies.

```bash
python -m venv <gamedir>\mpfenv
<gamedir>\mpfenv\Scripts\activate.bat
python -m pip install pip setuptools --upgrade
python -m pip install -r <gamedir>\requirements.txt
```

## Usage

Prior to running the game, ensure the virtual environment is activated  by running the activate.bat file.

**Windows:**

* To start the game on a system that is not connected to the P3-ROC system: **\<gamedir\>\mpf-NoHw.bat**
* To start the game on a system that is connected to the P3-ROC system: **\<gamedir\>\mpf-Hw.bat**
* To start the MPF Monitor app (before starting the game): **\<gamedir\>\mpf-Monitor.bat**

## Contributing
This is a private project. Contributions are not allowed.

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)