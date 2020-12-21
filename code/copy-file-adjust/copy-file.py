import os

path = './latex-content/'

tex_file = open(f'{path}draft.tex', 'r')

tex_copy = open(f'{path}preprint.tex', 'w+')

# create a preprint mode from the original paper draft
count = 1
for line in tex_file.readlines():
    if(count == 2):
        line = 'p'+line[1:]
    tex_copy.write(line)
    count = count+1

print('...Finished generating the preprint...')

compile_draft = 'pdflatex ./latex-content/draft.tex'
compile_preprint = 'sudo pdflatex ./latex-content/preprint.tex'

# os.system(compile_draft)
# # Clean content
# os.system('rm *.log')
# os.system('rm *.aux')
# os.system('rm *.bib')

os.system(compile_preprint)
# Clean content
os.system('rm *.log')
os.system('rm *.aux')
os.system('rm *.bib')
