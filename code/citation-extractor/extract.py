#!/Users/robertpoenaru/.pyenv/shims/python

import re

TEST_INPUT_FILE = 'test.tex'

with open(TEST_INPUT_FILE, 'r+') as reader:
    lines = reader.readlines()
    CITATIONS = []
    count = 0
    test_line = lines[0].strip()
    m = re.finditer(r'cite{', test_line)
    for mx in m:
        # print(test_line)
        f_start = mx.span()[1]
        # print(f'{f_start}')
        f_stop = test_line.find('}', f_start)
        my_string = test_line[f_start:f_stop]
        # print(my_string)


def Get_Line_Citations(LINE):
    LINE_CITATIONS = re.finditer(r'cite{', LINE)
    CITATIONS = []
    for line_cite in LINE_CITATIONS:
        cite_start = line_cite.span()[1]
        cite_stop = LINE.find('}', cite_start)
        line_citation = LINE[cite_start:cite_stop].split(',')
        for cite in line_citation:
            CITATIONS.append(cite)
    print(CITATIONS)


Get_Line_Citations(test_line)
