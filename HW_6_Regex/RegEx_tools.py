import os.path
import re


def ftp_finder(filename: str, pattern: str = r"\bftp[\w\d\\/\._#]+?\s",
               returning: bool = False, writing: bool = True, outname: str = 'ftps') -> list:
    """
    wef
    """
    with open(filename, 'r') as file:
        ftp_links = []
        for line in file:
            line = line.strip()
            ftp_links.extend(re.findall(pattern, line))
    if writing:
        with open(outname, 'w') as output_file:
            for link in ftp_links:
                output_file.write(f'{link}\n')
    if returning:
        return ftp_links


if __name__ == '__main__':
    ftp_finder('data/1_references')
