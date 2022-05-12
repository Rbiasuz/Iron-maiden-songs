
import tensorflow as tf

file = 'iron-maiden-songs.txt'

lista = []

with open(file,'r',encoding='latin-1') as f:
    for line in f:
        try:
            lista.append(line)
        except:
            pass

#limpar texto
#tokenizar

