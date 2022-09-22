def read_command():
    while True:
        action = input("Enter command:")
        if action not in actions:
            print("What-what i have to do?")
        else:
            return action


def read_seq():
    while True:
        seq = input("Enter seq:")
        if is_dna(seq) or is_rna(seq):
            return seq
        else:
            print("Invalid alphabet. Try again!")


def is_dna(seq):
    for nucleotide in set(seq.upper()):
        if nucleotide not in DNA:
            return False
    return True


def is_rna(seq):
    for nucleotide in set(seq.upper()):
        if nucleotide not in RNA:
            return False
    return True


def transcribe(seq):
    return ''.join([TranscriptDict[i] for i in seq])


def reverse(seq):
    return seq[::-1]


def complement(seq):
    if is_dna(seq):
        result = ''.join([ComplementDNA[i] for i in seq])
    else:
        result = ''.join([ComplementRNA[i] for i in seq])
    return result


def reverse_complement(seq):
    return complement(reverse(seq))


actions = {
    'transcribe': transcribe,
    'reverse': reverse,
    'complement': complement,
    'reverse complement': reverse_complement,
    'exit': exiting,
    ':q': exiting
}

DNA = {"A", "T", "G", "C"}
RNA = {"A", "U", "G", "C"}

TranscriptDict = {
    "a": "a", "A": "A",
    "t": "u", "T": "U",
    "u": "t", "U": "T",
    "g": "g", "G": "G",
    "c": "c", "C": "C"
}

ComplementDNA = {
    "a": "t", "A": "T",
    "t": "a", "T": "A",
    "g": "c", "G": "C",
    "c": "g", "C": "G"
}

ComplementRNA = {
    "a": "u", "A": "U",
    "u": "a", "U": "A",
    "g": "c", "G": "C",
    "c": "g", "C": "G"
}

while True:
    command = read_command()
    if command == "exit" or command == ":q":
        print("Good luck!")
        break
    else:
        sequence = read_seq()
        print(actions[command](sequence))
