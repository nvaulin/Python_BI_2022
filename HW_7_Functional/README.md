# Functional tools

### Homework 7 [BI](https://bioinf.me/) Python course solution

> *by* Nikita Vaulin, Skoltech <br />
> Nikita.Vaulin@skoltech.ru


Theese **Functional tools** allow the following operations with natural language: <br />

1. *sequential_map* — sequential apply the functions to each element of the container <br />
2. *consensus_filter* — sequential apply the filters to each element of the container  <br />

3. *conditional_reduce* — apply filter and 2-valued 1-value-returning function to reduce a container <br />

4. *func_chain* — combine any number of functions into a single pipeline <br />
5. *multiple_partial* — pass some arguments to several functions in advance <br />

6. *my_print* — dispaly objects without print!

The tools were tested with *python 3.10.8*.

## Installation

To run tools download `functional.py` file. For Linux:

```bash
wget -c https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_7_Functional_programming/HW_7_Functional/functional.py
```

## Usage

Import it within your python script:

```python
import functional as ft
```

Example usage:

```python
fr.conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) # -> 4
```

### Uninstallation

To uninstall this file, simply delete it as a regular file from your computer. For example, for Linux:

```bash
rm functional.py
```

### If any questions

Do not hesitate to write me by email Nikita.Vaulin@skoltech.ru
