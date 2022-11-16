# RegEx tools

### Homework 6 [BI](https://bioinf.me/) Python course solution

> *by* Nikita Vaulin, Skoltech <br />
> Nikita.Vaulin@skoltech.ru


Theese **RegEx tools** allow the following operations with natural language: <br />

1. *ftp_finder* — find all ftp-links in a given file <br />
2. *numbers_extractor* — extract numbers from a given file <br />
    <ul> 
   That might be a integer or float number or even in scientific notation or with radix separator (ex. 3.14, 10e-6, 10 000)
   </ul>
3. *words_extractor* — extract words from a given file <br />
    <ul>
    Also words can be filtered by some presence of some pattern
    </ul>
4. *words_len_distr_hist* — plost histogram of unique words lengths distribution
5. *sentences_extractor* — extract sentences from a given file <br />
    <ul>
    Also sentences can be filtered by a particular stop-sign
    </ul>
6. *extract_n_word_sentences* — extract sentences from a given file with a given number of words
7. *transsalter* — translate russian and english text to salted language

The tools were tested with *python 3.10.8*.

## Installation

To run tools download `RegEx_tools.py` file. For Linux:

```bash
wget -c https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_6_Regex/HW_6_Regex/RegEx_tools.py
```

You also need to install some dependecies listed in `requirments.txt`

```commandline
pip install -r requirments.txt
```

## Usage

Import it within your python script:

```python
import RegEx_tools as rt
```

Example usage:

```python
rt.transsalter('Live long and процветай')  # -> Lisivese losong asand просоцвесетасай
```

### Uninstallation

To uninstall this file, simply delete it as a regular file from your computer. For example, for Linux:

```bash
rm RegEx_tools.py
```

### If any questions

Do not hesitate to write me by email Nikita.Vaulin@skoltech.ru
