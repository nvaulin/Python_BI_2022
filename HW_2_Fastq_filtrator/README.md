# FastQ Filtrator
### Homework 2 [BI](https://bioinf.me/) Python course solution
> *by* Nikita Vaulin, Skoltech <br />
> Nikita.Vaulin@skoltech.ru

This FastQ Filtrator allows to filter data from input .fastq files by GC content, length and quality. 
Reads passed the filtering are saved into new *_passed.fastq file and, if *save_filtered* parameter is set to True, filtered reads are saved into *_failed.fastq file.


## Installation

To run filtrator download *fastq_filtrator.py* script and run *main* function from it with necessary parameterss.

For Linux:
```bash
wget -c https://raw.githubusercontent.com/nvaulin/Python_BI_2022/HW_2_DNA_RNA_tools/HW_2_DNA_RNA_tools/fastq_filtrator.py
```

## Parameters

The *main* function of filtrator takes following parameters:

- input_fastq - path to input .fastq file
- output_file_prefix - output file name prefix
- gc_bounds - upper and (optionally) lower  borders of read's GC content, *by default* - (0, 100)
- length_bounds - upper and (optionally) lower borders of read's length, *by default* - $(0, 2^{32})$
- quality_threshold - lower border of reads quality, *by default* - 0
- save_filtered - logical indicator whether to save or discard reads do not passed filtering
  
For gc_bounds and length_bounds lower border is optionally. roviding a single number will result of bounds from 0 to a number. 

Example: ` gc_bound = 66 ` means  ` gc_bounds = (0, 66) `
