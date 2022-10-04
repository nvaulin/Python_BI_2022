def read_fastq(input_fastq):
    names = []
    sequences = []
    qualities = []

    with open(input_fastq, 'r') as fastq:
        while True:
            name = fastq.readline().strip()
            if not name:  # End of reading the file if there is no line with the name of the read
                break
            sequence = fastq.readline().strip()
            fastq.readline().strip()  # Reading without saving the technical string with the "+" sign
            quality = fastq.readline().strip()

            names.append(name)
            sequences.append(sequence)
            qualities.append(quality)

    return names, sequences, qualities


def write_fastq(output_file, names, sequences, qualities, indexes):
    with open(output_file, 'w') as file:
        for i in indexes:
            file.write(f'{names[i]}\n')
            file.write(f'{sequences[i]}\n')
            file.write('+\n')
            file.write(f'{qualities[i]}\n')


def calculate_gc(sequence):
    length = len(sequence)
    if length == 0:
        return 0
    else:
        g_count = sequence.upper().count("G")
        c_count = sequence.upper().count("C")
        return (g_count + c_count) * 100 / length


def gc_check(sequence, gc_bounds):
    return gc_bounds[0] <= calculate_gc(sequence) <= gc_bounds[1]


def length_check(sequence, length_bounds):
    return length_bounds[0] <= len(sequence) <= length_bounds[1]


def quality_check(quality, quality_threshold, ascii_dict):
    letters_scores = [ascii_dict[q] - 33 for q in quality]  # translate ASCII quality encoding into numeric
    length = len(letters_scores)
    if length == 0:
        return 0 >= quality_threshold
    else:
        mean_score = sum(letters_scores) / len(letters_scores)
        return mean_score >= quality_threshold


def reads_filter(sequences, qualities, gc_bounds, length_bounds, quality_threshold, ascii_dict):
    """Return two lists with indexes of reads passed and not passed filtering."""
    passed, filtered = [], []
    for i in range(len(sequences)):
        gc_ok = gc_check(sequences[i], gc_bounds)
        len_ok = length_check(sequences[i], length_bounds)
        q_ok = quality_check(qualities[i], quality_threshold, ascii_dict)
        if gc_ok and len_ok and q_ok:
            passed.append(i)
        else:
            filtered.append(i)
    return passed, filtered


def main(input_fastq, output_file_prefix,
         gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0, save_filtered=False):
    """
    Open .fastq file and proceed it filtering by desired GC content, length and quality.

    Save reads passed filtering into new *_passed.fastq file and, if `save_filtered` parameter
    is set to True, save filtered reads to *_failed.fastq file.

    For gc_bounds and length_bounds lower border is optionally.
    Providing a single number will result of bounds from 0 to a number. Example:

    `gc_bounds` = 66 means `gc_bounds` = (0, 66)

    :param input_fastq: Path to input .fastq file
    :param output_file_prefix: Output file name prefix
    :param gc_bounds: upper and (optionally) lower  borders of read's GC content
    :param length_bounds: upper and (optionally) lower borders of read's length
    :param quality_threshold: lower border of reads quality
    :param save_filtered: logical indicator whether to save or discard reads do not passed filtering
    """
    if not isinstance(gc_bounds, tuple):
        gc_bounds = (0, gc_bounds)
    if not isinstance(length_bounds, tuple):
        length_bounds = (0, length_bounds)

    ascii_dict = {chr(i): i for i in range(33, 74)}  # ascii dictionary for illumina reads quality decoding
    names, sequences, qualities = read_fastq(input_fastq)

    passed, filtered = reads_filter(sequences, qualities, gc_bounds, length_bounds, quality_threshold, ascii_dict)

    output_file = f'{output_file_prefix}_passed.fastq'
    write_fastq(output_file, names, sequences, qualities, passed)
    if save_filtered:
        output_file = f'{output_file_prefix}_failed.fastq'
        write_fastq(output_file, names, sequences, qualities, filtered)
