#!/Users/robertpoenaru/.pyenv/shims/python
import os
import subprocess


clean_pdf_files = True

# draft mode
if(clean_pdf_files):
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


clean_pdf_files = True

# preprint mode
if(clean_pdf_files):
    try:
        # f=open("out.dat","w+")
        # subprocess.check_output(
        #     ['rm', '*.pdf'], stderr=subprocess.PIPE)
        proc = subprocess.Popen(
            ['pdflatex', './latex-content/my_prc2.tex'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate()
    # ['ls', './dir'], capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError:
        print(err.decode())
        # print(e.stderr.decode())
    else:
        print(out.decode())

os.system('rm *.bib')
os.system('rm *.log')
os.system('rm *.aux')
# os.system('rm *.dat')
