# WasteDemand

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
(see requirements.txt for the full list, but it should be enought to just intall those two, they will install their own dependencies)

## Usage
* Package is setup to run from 'main.py', you can also run the other scripts separately
* There is an example folder for the files that the should be produced each time (except the .pickle, it is too big for github)
* Defaults assume you have a project 'default' with database 'cutoff38'. It will prompt you for input if you don't have these names (or just crash)
* You can change the defaults and it will (probably) still work, otherwise: re-import ei38 into "default" with the name 'cutoff38'
* The scripts will make a copy of the default project and run everything in a project called "WasteDemand", this is deleted and remade each time
* It took about 16 minutes to run for me


