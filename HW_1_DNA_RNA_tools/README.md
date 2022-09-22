# DNA/RNA tools
### Homework 1 BI Python course solution
> *by* Nikita Vaulin, Skoltech <br />
> Nikita.Vaulin@skoltech.ru

Theese **DNA/RNA tools** allow the following operations with nucleic acid sequences without installing any additional modules: <br />
1. *transcribe* — prints transcribed sequence <br />
2. *reverse* — prints reversed sequence <br />
3. *complement* — prints complement sequence <br />
4. *reverse complement* — prints reverse complement sequence <br />


## Installation

To run tools download *Vaulin_HW_1_DNA_RNA_tools.py* script and run it in your terminal using python interpreter

For Linux:
```bash
wget -c https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_1_DNA_RNA_tools/HW_1_DNA_RNA_tools/Vaulin_HW_1_DNA_RNA_tools.py
python Vaulin_HW_1_DNA_RNA_tools.py
```

## Usage

The tool will ask you to enter the desired command from the list above. *Note:* it will ask until it receives a familiar command.

After that it will ask to enter the DNA **OR** RNA sequence. In case of any input erroros, he will ask you to repeat the input.

Example usage:
```
Enter command: reverse
Enter sequence: ATCccG
```
Result output:
```
GccCTA
```

## Exiting

To stop the script execution in the `Enter command:` field type `exit` or `:q`. 
