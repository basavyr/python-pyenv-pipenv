#!/Users/robertpoenaru/.pyenv/shims/python
import os
import subprocess

# create a copy of the file

# file_name = subprocess.run(
#     ['cp', './latex-content/my_prc.tex', './latex-content/my_prc_preprint.tex'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)


paper_draft_mode = False


with open('./latex-content/my_prc.tex', 'rt') as draft:
    preprint = open('./latex-content/my_prc_preprint.tex', 'wt')
    lines = draft.readlines()
    count = 1
    for line in lines:
        if(count == 2):
            newline = 'preprint,\n'
            preprint.write(newline)
        else:
            preprint.write(line)
        count = count+1


# draft mode
if(paper_draft_mode):
    try:
        # f=open("out.dat","w+")
        # subprocess.check_output(
        #     ['rm', '*.pdf'], stderr=subprocess.PIPE)
        proc = subprocess.Popen(
            ['pdflatex', './latex-content/my_prc.tex'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate()
    # ['ls', './dir'], capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError:
        print(err.decode())
        # print(e.stderr.decode())
    else:
        print(out.decode())


paper_preprint_mode = False

# preprint mode
if(paper_preprint_mode):
    try:
        # f=open("out.dat","w+")
        # subprocess.check_output(
        #     ['rm', '*.pdf'], stderr=subprocess.PIPE)
        proc = subprocess.Popen(
            ['pdflatex', './latex-content/my_prc_preprint.tex'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate()
    # ['ls', './dir'], capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError:
        print(err.decode())
        # print(e.stderr.decode())
    else:
        print(out.decode())

# try:
#     p = os.system('rm *.bib')
# except p.OSError as e:
#     print(e)

# try:
#     os.system('rm *.aux')
# except OSError as e:
#     print(e)

# try:
#     os.system('rm *.log')
# except OSError as e:
#     print(1)

abs_clean = False

if (abs_clean == True):
    try:
        os.system('rm *.pdf')
    except OSError as e:
        print(1)
