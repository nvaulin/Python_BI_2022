# UNIX tools

### Homework 8 [BI](https://bioinf.me/) Python course solution

> *by* Nikita Vaulin, Skoltech <br />
> Nikita.Vaulin@skoltech.ru


Theese **UNIX tools** allow you to run your favorite UNIX commands from Windows or other OS: <br />

1. *wc* —  print newline, word, and byte counts for FILE <br />
2. *rm* — remove (unlink) the FILE(s)  <br />
3. *ls* — list the FILEs, sort entries alphabetically <br />
4. *sort* — write sorted concatenation of FILE(s) to the stdout <br />
5. *cat* — concatenate FILE(s) to standard output <br />
6. *ln* — create a hard or symbolic link <br />
7. *mkdir* — create the DIRECTORY(ies), if they do not exist <br />
8. *tail* — print the last 10 lines of each FILE to standard output
9. *uniq* — filter adjacent matching lines from INPUT

This tools copy the way how UNIX one tools are working. By the way, some options are restricted in this release.


The tools were tested with *python 3.10.8*.

## Installation

To get UNIX tools download the particular tool you need or the whole  `HW_8_UNIX_tools` folder.

To download the tool, use the raw-link. For example, for Linux:

```bash
wget https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_8_UNIX_tools/HW_8_UNIX_tools/ln.py
```

To get the whole folder, download it by the [link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fnvaulin%2FPython_BI_2022%2Ftree%2FHW_8_UNIX_tools%2FHW_8_UNIX_tools) as a zip archive and unzip it. 
For example, for Windows use [WinRAR](https://www.win-rar.com/start.html?&L=4). For Linux:

```bash
 unzip 'nvaulin Python_BI_2022 HW_6_Regex HW_6_Regex.zip' -d unix_tools   
```


## Usage

To run the script, just call it from the directory where the tools is located:

```bash
./script.py some_file.txt
```

To get more information about the particular script, run:

```bash
./script.py --help
```

### Troubleshooting

- *The script is not executable*:

```bash
chmod a+x script.py
```

- *The script is not working as expected*

Run the script with the *python 3.10.8* interpreter. You can create a new environment for install it to your system globally. 


- *I want to run the tools from any folder*

To do so, you can add your scripts into the some location from your system PATH or add the scripts-containig folder to the PATH. For the bash shell, you may also need to add the specific command to the `~/.basrc` file in order to save it for the next sessions. Example command:
```bash
export PATH=$PATH:<new_path>
```

### Uninstallation

To uninstall this file, simply delete the script or folder from your computer. You may need to delete it also from PATH, if the PATh was modified. 

### If any questions

Do not hesitate to write me by email Nikita.Vaulin@skoltech.ru
