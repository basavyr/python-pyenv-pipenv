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

    # failsafe
    # OK[0] -> +1 AFTER CREATING THE LIST OF REFS
    # OK[1] -> +1 AFTER WRITING THE LIST OF REFS TO EXTERNAL FILE
    OK = [1, 1]

    # reading the latex file
    # extracting each citation line-by-line
    # append individual reference to a list
    with open(input_file, 'r+') as reader:
        latex_file = reader.readlines()
        read_count = 0
        for latex_line in latex_file:
            line = latex_line.strip()
            line_cites = Get_Line_Citations(line)
            # print(line_cites)
            for cite in line_cites:
                REFERENCES.append(cite)
            read_count += 1
        if(read_count != len(latex_file)):
            OK[0] = 0

    # remove duplicate citations
    # print(REFERENCES)
    REFERENCES = list(dict.fromkeys(REFERENCES))
    # print(REFERENCES)

    # save each reference from the list into an external file
    with open(ref_file, 'w+') as writer:
        write_count = 0
        for ref in REFERENCES:
            writer.writelines(ref)
            writer.writelines('\n')
            write_count += 1
        if(write_count != len(REFERENCES)):
            OK[1] = 0

    print(OK)
    return REFERENCES


TEST_INPUT_FILE = 'latex-file.tex'

REFERENCES_FILE = 'references.dat'

Create_Reference_File(TEST_INPUT_FILE, REFERENCES_FILE)
