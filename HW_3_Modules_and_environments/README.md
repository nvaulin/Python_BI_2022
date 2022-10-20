# Running Ultraviolence 
### Homework 3 [BI](https://bioinf.me/) Python course solution
> *by* Nikita Vaulin, Skoltech <br />
> Nikita.Vaulin@skoltech.ru

Theese instructions explain the necessary steps to run the *Ultraviolence.py* script. 

The instruction were tested on **Ubuntu 20.04.5 LTS** (Focal Fossa) with **python3.11.0rc2**

## Update the system

Firstly, to update the system for futher steps, run theese commands:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt install software-properties-common
```

## Install Python3.11

The *ultraviolence.py* script is run by a new **python3.11.0rc2** that is under development.
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install python3.11

curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
sudo apt-get install python3.11-distutils
sudo apt-get install python3.11-dev
sudo apt install python3.11-venv
sudo apt install python-lxml
```

## Set up your python 3.11 pip

```bash
python3.11 -m pip install --upgrade pip
```
If you meet any problems here - see the **Troubleshooting** section

## Set up the environment

> This step is optional but highly recommended.

Also, you may want to create a separate folder for this environment first.

```bash
python3.11 -m venv env_name
source env/bin/activate
```
You can use Conda or PyCharm environments as well if you have any

## Last preparational step - make a coffee
> This step is optional but highly recommended.

To run this script, you need courage and patience, so the regular coffee won't work. We will use a heavy weapon - Swedish coffee with rum. 

For one serving you need
```recepie
Freshly brewed coffee - 120 ml
Egg yolk - 1
Dark rum - 40 ml
Sugar - 1 tea spoon
```

Mix egg yolk, dark rum and sugar and beat them thoroughly. Add freshly brewed coffee and mix them gentely. 
You can add double cream if pyu wish and serve with whipped cream on top.

May the Odin be with us. **Skål!**

## Download the script

You can clone theese repository:
```bash
git clone git@github.com:nvaulin/Python_BI_2022.git
cd Python_BI_2022
git checkout HW_3_Modules_and_environments
cd HW_3_Modules_and_environments
```

Or dowload only the script manually:
```bash
wget -c https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_3_Modules_and_environmets/HW_3_Modules_and_environments/ultraviolence.py
```

To get **requrments.txt** file as well:
```bash
wget -c https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_3_Modules_and_environmets/HW_3_Modules_and_environments/requerments.txt
```

## Installation of required libraries

To install all the required libraries:

```bash
python3.11 -m pip install -r requirements.txt
```
In this case, certain libraries will be installed in addition to these as dependencies. Also there is a file `requirements_long.txt` in the `troubleshooting` folder  that contains all the libraries including their dependencies, but it is excessive and contains unnecessary libraries too.

If you meet any problems here - see the **Troubleshooting** section

## Running the script 

```bash
python3.11 ultraviolence.py
```
 You can also run this script in the your preferable python IDE, for instance, in PyCharm Community. 


## Troubleshooting

- **The script is not executable**

```bash
chmod a+x ultraviolence.py
```

- **There is no pip found**

If the is now `pip` found, try to use `pip3` instead or install it by:
```bash
sudo apt-get install python3-pip
```

- **Problems with pandas==1.4.3 installation**

If you have a problem installing pandas, for example, the process freezes when trying to build the wheel, you can use another way. 

Install the newer `pandas==1.5.1`. For example, you can edit the `requirements.txt` file, or take the `requirements_pandas151.txt` file from the `troubleshooting` folder. After installation, find the directory where this library is located (`pip show pandas`). Go to the `<pandas-library>/core/` directory and edit line 636 of the `frame.py` file with whatever editor you prefer. if you use *nano*, run:
```bash
nano +636 frame.py
```

On line 636 you need to comment out the error message and add a new line that translates the index from the set to the list. 

In other words, find this code 

```python
if index is not None and isinstance(index, set):
    raise ValueError("index cannot be a set")`
```
And correct it into
```python
if index is not None and isinstance(index, set):
    index = list(index) # The index was converted here from set to list by *your name* at *current date*
    #raise ValueError("index cannot be a set")`
```
> *Important* : do not use tab-indentation in *nano*. Use 4-spaces-indentation instead. 

### In case of any other troubles, please, contact me by email Nikita.Vaulin@skoltech.ru

(This is not a recommendation, but the part of instruction)
