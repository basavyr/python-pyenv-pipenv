#!/Users/robertpoenaru/.pyenv/shims/python

import re


def Get_Line_Citations(LINE):
    LINE_CITATIONS = re.finditer(r'cite{', LINE)
    CITATIONS = []
    for line_cite in LINE_CITATIONS:
        cite_start = line_cite.span()[1]
        cite_stop = LINE.find('}', cite_start)
        line_citation = LINE[cite_start:cite_stop].split(',')
        for cite in line_citation:
            CITATIONS.append(cite)
    return CITATIONS


def Create_Reference_File(input_file, ref_file):
    REFERENCES = []
    with open(input_file, 'r+') as reader:
        latex_file = reader.readlines()
        for latex_line in latex_file:
            line = latex_line.strip()
            line_cites = Get_Line_Citations(line)
            # print(line_cites)
            for cite in line_cites:
                REFERENCES.append(cite)
    with open(ref_file, 'w+') as writer:
        for ref in REFERENCES:
            writer.writelines(ref)
            writer.writelines('\n')

    return REFERENCES


TEST_INPUT_FILE = 'test.tex'

REFERENCES_FILE = 'references.dat'

Create_Reference_File(TEST_INPUT_FILE, REFERENCES_FILE)
