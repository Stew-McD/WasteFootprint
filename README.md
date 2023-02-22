# WasteFootprint: a flexible tool to track waste flows in LCA
## Contents

#### Central script

* **main.py** :
from here you can run the entire package and also modify the search parameters and the names of the projects/databases.

#### Sub-scripts

1. **dbExplode() in  dbExplode.py** :
uses wurst to open up the ecoinvent database, explode to a list of all exchanges, and save in a DataFrame as a .pickle binary file. The default is that the database is called "cutoff38" in the project "default".  This function will copy 'default' to a new project called 'WasteFootprint'. If 'WasteFootprint'  exists, it will be deleted and re-made each time.

2. **WasteSearch() in WasteSearch.py** :
loads '*_exploded.pickle', runs the search query, and produces a .csv to store the results (and a log entry). The query is a dictionary that holds the variables NAME, CODE, and the search terms keywords_AND keywords_OR and keywords_NOT.

3. **dbWriteExcel() in dbMakeCustom.py** :
makes an xlsx file in the format of a Brightway2 database. For each .csv in the folder 'WasteSearchResults' a database entry will be added.

4. **dbExcel2BW() in dbMakeCustom.py** :
Takes the custom database produced by dbWriteExcel() and imports it into Brightway2. Defaults: project = 'WasteFootprint', db = 'db_waste'

5. **ExchangeEditor() in ExchangeEditor.py** :
For every activity found by WasteSearch(), this function will add the relevant exchange from the db_waste. This function takes the longest time to run (~10 min for each database).

6. **AddMethods() in MethodEditor.py** :
Takes each entry in the custom biosphere database 'waste_db' and creates a new method from it. Eg., ('Waste Footprint', 'Total Waste Footprint', waste_hazardous_cubicmeter)

## Install and run
1. Clone the repo or download the .py files
2. Make a new virtual environment if you want
3. Install bw2io and wurst, they will probably install all of the other dependencies themselves
4. Check to see if the names of the projects and databases in the script will work with your set up
5. Run main.py in your terminal

### For example:
#### Make virtual environment (I use venv, but conda will also work)
##### In linux (and Mac, I guess)
pip install virtualenv
python3 -m venv ~/venvs/WasteFootprint
pip install brightway2 wurst numpy=1.23.5 # newest version of numpy gives errors
source ~/venvs/WasteFootprint/bin/activate

##### In windows (I think... not tested)
pip install virtualenv
cd WasteFootprint
virtualenv --python C:\Path\To\Python\python.exe venv
.\venv\Scripts\activate

#### Download and run
##### Via GitHub
gh repo clone https://github.com/SC-McD/WasteFootprint
python3 main.py

##### Manual download
mkdir WasteFootprint
cd WasteFootprint # put the .py files here
python3 main.py

## Requirements
brightway2: https://github.com/brightway-lca/brightway2
wurst:  https://github.com/polca/wurst
(see requirements.txt for the full list, but it should be enough to just install those two, they will install their own dependencies)

## Usage
* Package is setup to run from 'main.py', you can also run the other scripts separately
* There is an example folder for the files that the should be produced each time (except the .pickle, it is too big for github)
* Defaults assume you have a project 'default_<db_name>' with database '<db_name>'.
* You can change the defaults and it will (probably) still work, otherwise: re-import or copy to a new project: eg. put ei38 into "default_cutoff38" with the name 'cutoff38'
* The scripts will make a copy of the default project and run everything in a project called "WasteFootprint"
* It took about 16 minutes to run for me, for each database
