#!/Users/robertpoenaru/.pyenv/shims/python
import os
import subprocess

# create a preprint mode from the original paper draft
# special_command='% !TEX options=--shell-escape\n'
# tex_copy.write(special_command)
# for line in tex_file.readlines():
#     if(count == 2):
#         line = 'p'+line[1:]
#     tex_copy.write(line)
#     count = count+1

draft_mode = False

if(draft_mode):
    print('Building the latex file [draft-mode]...')
    p1 = subprocess.run(['pdflatex', '-shell-escape',
                         './latex-content/my_prc.tex'])
    print('Cleaning-up the remaining files...')
    os.system('rm *.log')
    os.system('rm *.aux')
    os.system('rm *.bib')

preprint_mode = False
if(preprint_mode):
    print('Building the latex file [preprint-mode]...')
    try:
        subprocess.check_call(['pdflatex', '-shell-escape', '-interaction=nonstopmode',
                               './latex-content/my_prc2.tex'], capture_output=True, text=True)
    except:
        print('Latex compilation failed...')

    # print('Cleaning-up the remaining files...')
    # os.system('rm *.log')
    # os.system('rm *.aux')
    # os.system('rm *.bib')
    # print(p1.stderr.decode())


clean_pdf_files = True

if(clean_pdf_files):
    try:
        subprocess.check_call(['rm', '*.pdf'], capture_output=True, text=True)
    except:
        print('failed to delete')
