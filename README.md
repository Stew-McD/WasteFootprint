# WasteDemand
## Contents

#### Central script

* **main.py** :  
from here you can run the entire package and also modify the search parameters.  

#### Sub-scripts and their functions

1. **dbExplode() in  dbExplode.py** :  
uses wurst to open up the ecoinvent database, explode to a list of all exchanges, and save in a DataFrame as a .pickle binary file. The default is that the database is called "cutoff38" in the project "default".  This function will copy 'default' to a new project called 'WasteDemand'. If 'WasteDemand'  exists, it will be deleted and re-made each time. 

2. **WasteSearch() in WasteSearch.py** :  
loads '*_exploded.pickle', runs the search query, and produces a .csv to store the results (and a log entry). The query is a dictionary that holds the variables NAME, CODE, and the search terms keywords_AND keywords_OR and keywords_NOT. The function will iterate over UNIT = 'kilogram' and UNIT = 'cubic meter'. Each search took around 15 seconds for me.  

3. **dbWriteExcel() in dbMakeCustom.py** :  
makes an xlsx file in the format of a Brightway2 database. For each .csv in the folder 'WasteSearchResults' a database entry will be added.  

4. **dbExcel2BW() in dbMakeCustom.py** :  
Takes the custom database produced by dbWriteExcel() and imports it into Brightway2. Defaults: project = 'WasteDemand', db = 'db_waste'  

5. **ExchangeEditor() in ExchangeEditor.py** :  
For every activity found by WasteSearch(), this function will add the relevant exchange from the db_waste. This function takes the longest time to run (~10 min for me). 

6. **AddMethods() in AddMethods.py ** :  
Takes each entry in the custom biosphere database 'waste_db' and creates a new method from it. Eg., ('Waste Footprint', 'Total Waste Demand', waste_hazardous_cubicmeter)  

## Install and run
1. Clone the repo or download the .py files
2. Make a new virtual environment if you want
3. Install bw2io and wurst, they will install all of the other dependencies themselves
4. Probably you want to make a new directory for this
5. Run main.py in your terminal (If you want to run in your usual Spyder installation, add spyder-kernels==2.3.*)

### For example: 
#### Make virtual environment (I use venv, but conda will also work) 
##### In linux (and Mac, I guess)
pip install virtualenv  
python3 -m venv ~/venvs/WasteDemand  
pip install bw2io==0.8.7 wurst  
source ~/venvs/WasteDemand/bin/activate  

##### In windows (I think... not tested)
pip install virtualenv  
cd WasteDemand  
virtualenv --python C:\Path\To\Python\python.exe venv  
.\venv\Scripts\activate  

#### Download and run
##### Via GitHub
gh repo clone https://github.com/SC-McD/WasteDemand  
python3 main.py

##### Manual download
mkdir WasteDemand  
cd WasteDemand # put the .py files here  
python3 main.py  

## Requirements
bw2io==0.8.7 (to match with ecoinvent 3.8)  
wurst  
(see requirements.txt for the full list, but it should be enough to just intall those two, they will install their own dependencies)  

## Usage
* Package is setup to run from 'main.py', you can also run the other scripts separately
* There is an example folder for the files that the should be produced each time (except the .pickle, it is too big for github)
* Defaults assume you have a project 'default' with database 'cutoff38'. It will prompt you for input if you don't have these names (or just crash)
* You can change the defaults and it will (probably) still work, otherwise: re-import ei38 into "default" with the name 'cutoff38'
* The scripts will make a copy of the default project and run everything in a project called "WasteDemand", this is deleted and remade each time
* It took about 16 minutes to run for me


