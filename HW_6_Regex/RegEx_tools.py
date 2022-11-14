import os.path
import re

def file_scanner(filename: str, pattern: str, returning: bool = True,
                 writing: bool = False, outname: str = 'file_scanner_ouput.txt') -> list:
    """
    Find any patterns in a particular file. Can return them or write into new a file.

        Params:
            filename (str): name of a file to search in (can be path as well)

            pattern (str): pattern to search, ftp-link pattern by default

            returning (bool): whether to return the list of found matches, default = True

            writing (bool): whether to write to a file the list of found matches, default = False

            outname (str): name of a file to write in (can be path as well)

        Returns:
            (list[str]): list of found patterns
    """
    pattern = re.compile(pattern)
    with open(filename, 'r') as file:
        matches = []
        for line in file:
            line = line.strip()
            matches.extend(re.findall(pattern, line))

    if writing:
        with open(outname, 'w') as output_file:
            for match in matches:
                output_file.write(f'{match}\n')
    if returning:
        return matches


def ftp_finder(filename: str,
               returning: bool = False, writing: bool = True, outname: str = 'ftps') -> list:
    """
    Find any FTP links in a particular file and write it into new file.
    Also function can be set to return the list of links and not write them to the file as well.

        Parameters:
            filename (str): name of a file to search in (can be path as well)

        Optional parameters:
            returning (bool): whether to return the list of found matches
            writing (bool): whether to write to a file the list of found matches
            outname (str): name of a file to write in (can be path as well)

        Retunrs:
            (list[str]): list of found ftp-links
    """
    return file_scanner(filename, r"\bftp[\w\d\\/\._#]+?\s", returning, writing, outname)


def numbers_extractor(filename: str) -> set:
    basic_digits = r'(?:\d+)'
    inner_sections = r'(?:(?:\s\d+)*|(?:\.\d+)*)'
    float_ending = r'(?:\.\d+)?'
    number = fr'[+-]?{basic_digits}{inner_sections}{float_ending}'
    exponential_part = fr'(?:[eE]{number})?'
    number_pattern = fr'{number}{exponential_part}'
    return set(file_scanner(filename, number_pattern))


if __name__ == '__main__':
    ftp_finder('data/1_references')
    numbers = numbers_extractor('data/2_2430AD')
    print(numbers)
