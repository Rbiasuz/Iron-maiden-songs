
import tensorflow as tf

file = 'iron-maiden-songs.txt'

lista = []

with open(file,'r',encoding='latin-1') as f:
    for line in f:
        try:
            lista.append(line)
        except:
            pass

new_list = []
for line in lista:
    if len(line) < 5:
        print(line)
    else:
        new_list.append(line)

#limpar texto
#tokenizar

