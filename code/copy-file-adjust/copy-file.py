import os
import subprocess

path = './latex-content/'

tex_file = open(f'{path}draft.tex', 'r')

tex_copy = open(f'{path}preprint.tex', 'w+')

# create a preprint mode from the original paper draft
count = 1
# special_command='% !TEX options=--shell-escape\n'
# tex_copy.write(special_command)
for line in tex_file.readlines():
    if(count == 2):
        line = 'p'+line[1:]
    tex_copy.write(line)
    count = count+1

print('...Finished generating the preprint...')

compile_draft = 'pdflatex ./latex-content/draft.tex'
compile_preprint = 'pdflatex -shell-escape  ./latex-content/preprint.tex'

# os.system(compile_draft)
# # Clean content
# os.system('rm *.log')
# os.system('rm *.aux')
# os.system('rm *.bib')

# os.system(f'pdflatex -shell-escape -interaction=nonstopmode ./latex-content/preprint.tex')

# Clean content
# subprocess.run(['pdflatex','-shell-escape ./latex-content/preprint.tex'],shell=True)
# subprocess.run(['pdflatex','-shell-escape','-interaction=nonstopmode','./latex-content/draft.tex']) 

# subprocess.run(['cp','./latex-content/preprint.tex', 'preprint.tex']) 

subprocess.run(['pdflatex','-interaction=nonstopmode','-shell-escape','preprint.tex']) 

# os.system('rm *.log')
# os.system('rm *.aux')
# os.system('rm *.bib')
