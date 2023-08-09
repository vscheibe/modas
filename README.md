# MODAS
Investigating bird flocking behavior in an agent-based simulation using the Python Mesa Framework.


[![DOI](https://zenodo.org/badge/674607038.svg)](https://zenodo.org/badge/latestdoi/674607038)



## Installation

Usage of python 3.10 is recommended

## Usage

After installation configure desired parameters in the config.py.
Run either with a visual run or a batch run which saves results into the output folder.


### Install required packages

`pip install -r requirements.txt`

### Run the webview (visual run)

`python main.py -vrun`

### Run a batch run
Warning! Can use high amounts of RAM which can crash your computer.
Output files can become really large.(multiple Gbs)  
`python main.py -brun`


