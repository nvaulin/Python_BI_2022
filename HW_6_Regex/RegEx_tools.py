import os.path
import re


def ftp_finder(filename: str, pattern: str = r"\bftp[\w\d\\/\._#]+?\s",
               returning: bool = False, writing: bool = True, outname: str = 'ftps') -> list:
    """
    Find any FTP links in a particular file and write it into new file.
    Also function can be set to return the list of links and not write them to the file as well.
    Moreover, the output file name and searching pattern can be manually specified, so, actually,
    in that case function can be utilized to look for any substrings.

        Parameters:
            filename (str): name of a file to search in (can be path as well)

        Optional parameters:
            pattern (str): pattern to search, ftp-link pattern by default
            returning (bool): whether to return the list of found matches
            writing (bool): whether to write to a file the list of found matches
            outname (str): name of a file to write in (can be path as well)

        Retunrs:
            (list[str]): list of found ftp-links (or found matches in general)
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
