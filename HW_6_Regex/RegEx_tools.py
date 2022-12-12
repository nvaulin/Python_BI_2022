import os.path
import re
import matplotlib.pyplot as plt


def file_scanner(filename: str, pattern: str, as_set: bool = True, returning: bool = True,
                 writing: bool = False, outname: str = 'file_scanner_output.txt') -> set:
    """
    Find any patterns in a particular file. Can return them or write into new a file.

        Parameters:
            *filename* (str): name of a file to search in (can be path as well)\n
            *pattern* (str): pattern to search\n
            *as_set* (bool): whether to convert results to a set, default = True\n
            *returning* (bool): whether to return found matches, default = True\n
            *writing* (bool): whether to write found matches to a file, default = False\n
            *outname* (str): name of a file to write in (can be path as well)

        Returns:
            set[str]: set of found patterns (can be a list)
    """
    pattern = re.compile(pattern)
    with open(filename, 'r') as file:
        matches = []
        for line in file:
            line = line.strip()
            matches.extend(re.findall(pattern, line))
    if as_set:
        matches = set(matches)
    if writing:
        with open(outname, 'w') as output_file:
            for match in matches:
                output_file.write(f'{match}\n')
    if returning:
        return matches


def ftp_finder(filename: str,
               returning: bool = False, writing: bool = True, outname: str = 'ftps') -> set:
    """
    Find any FTP links in a particular file and write it into new file.
    Also function can be set to return the list of links and not write them to the file as well.

        Parameters:
            *filename (str): name of a file to search in (can be path as well)

        Optional parameters:
            *returning* (bool): whether to return found matches\n
            *writing* (bool): whether to write found matches to a file\n
            *outname* (str): name of a file to write in (can be path as well)

        Returns:
            set[str]: set of found ftp-links (can be list)
    """
    return file_scanner(filename, r"\bftp[\w\d\\/\._#]+?\s", returning=returning, writing=writing, outname=outname)


def numbers_extractor(filename: str, is_float: bool = True, is_exponential: bool = True,
                      decimal_sep: str = '\.', radix_sep: str = '', print_as_is: bool = False) -> set:
    """
    Find any decimal numbers in file. Non-decimal numbers can be extracted as well but considered as decimal numbers.

    Decimal and radix separator can be set manually with respect to regex notation, but for common separators there
    provided a translation of a human-format string into a regex-format. If many, please, provide separators as regex
    collection [].

    If both separators specified as '\.' only the last '.' considered as a decimal separator.

    *Examples*:

    Radix separator is needed to extract as a single number such numbers as: 10 000 000 or 10.000.000.

    is_exponential flag is needed to extract numbers in scientific notation suc as: 6.26e6

        Parameters:
            *filename (str): name of a file to search in (can be path as well)

        Optional parameters:
            *is_float* (bool): whether to consider last "." as a decimal separator\n
            *is_exponential* (bool): whether to consider "e" or "E" as a power separator in scientific notation\n
            *float_sep* (str): decimal separator of float numbers, can be regex collection []\n
            *radix_sep* (str): separator of decimal number radixes (bases), can be regex collection []\n
            *print_as_is* (bool): whether to print found numbers as strings as they are, or to translate into
                                numerical data (with respect to is_float option)

        Returns:
            set[num]: set of found numbers (set of float/integer numbers or strings if specified)
    """
    separators = {' ': r'\s',
                  '.': r'\.'
                  }

    # Convert human-written separators into regex notation
    if radix_sep in separators:
        radix_sep = separators[radix_sep]
    if decimal_sep in separators:
        decimal_sep = separators[decimal_sep]

    number_pattern = r'[+-]?(?:\d+)'

    # Add radix inner parts if some radix specified
    if radix_sep not in ['', None]:
        inner_parts = fr'(?:{radix_sep}\d+)*'
        number_pattern += inner_parts

    # Add float ending for float numbers
    if is_float:
        float_ending = fr'(?:{decimal_sep}\d+)?'
        number_pattern += float_ending

    # Add the same pattern as an exponential part for scientific notation
    if is_exponential:
        exponential_part = fr'(?:[eE]{number_pattern})?'
        number_pattern += exponential_part

    numbers_found = file_scanner(filename, number_pattern)
    if not print_as_is:
        if is_float:
            numbers_found = set(map(float, numbers_found))
        else:
            numbers_found = set(map(int, numbers_found))
    return numbers_found


def words_extractor(filename: str, word_contains: str = '', as_set: bool = True,
                    case_sensitive: bool = False, ) -> set:
    """
    Extract words containing some pattern from a particular file. Also can be used just to extract the words.

        Parameters:
            *filename* (str): name of a file to search in (can be path as well)\n
            *word_contains* (str): pattern to search in words (default '' not to filter words)\n
            *as_set* (bool): whether to convert results to a set, default = True\n
            *case_sensitive* (bool): whether to consider words with capital and small letters
                                     as different, default = True

        Returns:
            set[str]: set of found patterns (can be a list)
    """
    word_pattern = fr'\b[\w\']*{word_contains}[\w\']*\b'
    words_found = file_scanner(filename, word_pattern, as_set=as_set)
    if not case_sensitive:
        words_lowered = map(lambda x: x.lower(), words_found)
        if as_set:
            words_found = set(words_lowered)
        else:
            words_found = list(words_lowered)
    return words_found


def sentences_extractor(filename: str = None, text: str = None, stop_sign: str = '(?:[\.?!]|.$)') -> list:
    """
    Extract the whole sentences from a particular file or text.

        Parameters:
            *filename* (str): name of a file to search in (can be path as well)\n
            *text* (str): single-line text to search in\n
            *word_contains* (str): pattern to search in words (default '' not to filter words)\n
            *stop_sign* (bool): which symbols to consider as a sentence terminator (by default there are
                                a '.', '!', '?' or l\n

        Returns:
            list[str]: list of found sentences
    """
    sentence_pattern = fr'([A-ZА-Я](?:[^[\.])*?{stop_sign})'
    sentences = []
    if filename is not None:
        sentences.extend(file_scanner(filename, sentence_pattern, as_set=False))
    if text is not None:
        sentences.extend(re.findall(sentence_pattern, text))
    return sentences


def words_len_distr_hist(filename: str):
    """
    Extract unique words from a particular file and plot histogram of their lengths distribution

        Parameters:
            *filename* (str): name of a file to search in (can be path as well)\n

        Output:
            Saves a .png plot file to the 'pictures' subdirectory

        Returns:
            None
    """
    words = words_extractor(filename, as_set=True)
    words_lens = list(map(len, words))
    max_len = max(words_lens)

    plt.figure()
    plt.hist(words_lens, color='blue', edgecolor='black', align='right', bins=max_len, density=True)
    plt.xticks(range(1, max_len + 1))
    plt.xlabel('Length of word')
    plt.ylabel('Amount')
    plt.title('Histogram of word lengths distribution')
    name = re.split(r'[\\/]', filename)[-1]
    path = os.path.join("pictures", f'Words_lengths_distribution_{name}.png')
    plt.savefig(path)


def transsalter(text: str) -> str:
    """
    Translate russian and english text to salted language.
    Unsupported types of languages will be return without any changes.

        Parameters:
            *text* (str): an english or russian text to translate\n

        Returns:
            str: translated text
    """
    vowels_eng = 'aeiouy'
    vowels_ru = 'ауоыиэяюёе'
    text = re.sub(fr'([{vowels_eng}])', fr'\1s\1', text)
    text = re.sub(fr'([{vowels_ru}])', fr'\1с\1', text)
    return text


def text_word_count(text: str) -> int:
    """
    Count number words in a string

        Parameters:
            *text* (str): a text to count words\n

        Returns:
            int: number of words
    """

    return len(re.findall(r'\b', text)) // 2


def extract_n_word_sentences(n: int, filename: str = None, text: str = None) -> list:
    """
    Filter sentences in text or file by number of words and retirns list of sententes with a given number of words.

        Parameters:
            *n* (int): a number of words
            *filename* (str): name of a file to process (can be path as well)\n
            *text* (str): a text string to process\n

        Returns:
            list[str]: number of words
    """
    sentences = sentences_extractor(filename=filename, text=text)
    good_sentences = list(filter(lambda x: text_word_count(x) == n, sentences))
    return good_sentences


if __name__ == '__main__':
    # 1. FTP-links parser
    ftp_finder('data/1_references')

    # 2. Numbers extraction
    numbers = numbers_extractor('data/2_2430AD', print_as_is=True)

    # 3. Words with 'a' extraction
    words_with_a = words_extractor('data/2_2430AD', word_contains='[aA]')

    # 4. Exlamation sentances extractor
    exclamations = sentences_extractor('data/2_2430AD', '!')

    # 5. Unique word distribution (saves hist to .png)
    words_len_distr_hist('data/2_2430AD')

    # 6. Translation to salted language
    salted_text = transsalter('Сьешь еще этих мягких французских булок and drink tea')

    # 7. Extraction sentences with n words
    n_word_sentences_from_file = extract_n_word_sentences(filename='data/2_2430AD', n=3)
    n_word_sentences_from_text = extract_n_word_sentences(text='Здесь три слова. Здесь тоже три', n=3)
