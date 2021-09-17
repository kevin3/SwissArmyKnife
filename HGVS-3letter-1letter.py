import sys
"""convert between 1 letter to 3 letter amino acid nomenclature. Expects TSV file with column header of "HGVS_P" to replace 3 or 1 letter AA code.BEWARE when applying on non HGVS information column when converting from 1 letter to 3 letter"""

def replace(text, replacement):
    new = ''

    for c in text:
        try:
            new += replacement[c]
        except KeyError:
            new += c

    return new


aa_code1 = {'Three Letter Code':'One Letter Code','Ala':'A','Asx':'B','Cys':'C','Asp':'D','Glu':'E','Phe':'F','Gly':'G','His':'H','Ile':'I','Lys':'K','Leu':'L','Met':'M','Asn':'N','Pro':'P','Gln':'Q','Arg':'R','Ser':'S','Thr':'T','Sec':'U','Val':'V','Trp':'W','Xaa':'Xa','Tyr':'Y','Glx':'Z','Ter':'*'}


aa_code3 = {
    'One Letter Code':'Three Letter Code',"A": "Ala", "C": "Cys", "D": "Asp", "E": "Glu", "F": "Phe",
    "G": "Gly", "H": "His", "I": "Ile", "K": "Lys", "L": "Leu",
    "M": "Met", "N": "Asn", "P": "Pro", "Q": "Gln", "R": "Arg",
    "S": "Ser", "T": "Thr", "V": "Val", "W": "Trp", "Y": "Tyr",
    "*": "Ter"
}
hgvs_p = -1

with open(sys.argv[1], "r") as csv:
    for line in csv:
        data = line.strip().split("\t")

        if hgvs_p == -1:
            hgvs_p = data.index("HGVS_P")
        else:
            aa = data[hgvs_p]
            data[hgvs_p] = replace(aa, aa_code3)

        print("\t".join(data))
