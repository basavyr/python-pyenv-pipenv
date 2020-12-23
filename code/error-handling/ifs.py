#! /Users/robertpoenaru/.pyenv/shims/python

x = 1
# y=1
with open('logs.log', 'w') as fil:
    try:
        x = y+1
    except NameError as err:
        fil.write(str(err))
        print(f'issue: {err}')
    else:
        print('all good')
