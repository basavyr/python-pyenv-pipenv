strings = ('Windows', ['lib1', 'lib2', 'lib3', 'lib4'], [
           'app1', 'app2', 'app3', 'app4'], '2022-02-09 21:01:16.065217')


first = strings[0]

# print(first)


n_position = first.find('n')

s_position = first.find('s')

print(first[n_position:s_position])
