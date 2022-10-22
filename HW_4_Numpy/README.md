# Numpy exercise

### Homework 4 [BI](https://bioinf.me/) Python course solution

> *by* Nikita Vaulin, Skoltech <br />
> Nikita.Vaulin@skoltech.ru

This is the solution to the 4th homework assignment for the Python course at the Bioinformatics Institute.

The file `numpy_challenge.py` contains several functions for working with Numpy arrays:

1. **matrix_multiplication** — multiplies two matrices <br />
2. **multiplication_check** — checks whether it is possible to multiply the given matrices <br />
3. **multiply_matrices** — multiplies consecutively several matrices from the list <br />
4. **compute_2d_distance complement** — calculates the Euclidean distance between two vectors in the plane <br />
5. **compute_multidimensional_distance** — calculates the Euclidean distance between two vectors in multidimensional
   space <br />
6. **compute_pair_distances** — calculates all pairwise Euclidean distance between rows given in a matrix <br />


Also it contains several examples of Numpy arrays creation. Feel free to check!

The perfomance was tested with Python 3.9.10 

## Dependencies

To use this functions the Numpy library is needed (the perfomance was tested with Numpy 1.23.4).
To get this library, run in the Command Line:
```CommandLine
pip install numpy==1.23.4
```
Also, you can use `requirements.txt` file from this repository:
```commandline
pip install -r requirements.txt
```

## Installation and usage

To run this functions download `numpy_challenge.py` script, store in the same folder with your python code you are
working with and import as a module.

For Linux:

```bash
wget -c https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_4_Numpy/HW_4_Numpy/numpy_challenge.py
mv numpy_challenge.py /path/to/your/project/folder/numpy_challenge.py
```

In your python script add:

```python
import numpy_challenge as nc
```

And call this functions as `nc.function_name()`, for example:

```python
import numpy as np
import numpy_challenge as nc


a = np.array([1, 2])
b = np.ones((8, 8))
nc.multiplication_check(a, b) # -> False
```

## Uninstallation

To uninstall this file, simply delete it as a regular file from your computer. For example, for Linux:
```bash
rm numpy_challenge.py
```

### If any questions

Do not hesitate to write me by email Nikita.Vaulin@skoltech.ru
