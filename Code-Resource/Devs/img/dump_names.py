from os import system as zsh
from datetime import datetime
import time

dict_path="../../resources/"

unix_stamp=int(time.time())
chosen_word="mega"
dict_file=dict_path+chosen_word+"-"+str(unix_stamp)+".txt"


# copy the custom words into the clipboard
zsh(f'cat /usr/share/dict/words | grep {chosen_word} | pbcopy')
# paste the words into the custom file
zsh(f'pbpaste >> {dict_file}')

