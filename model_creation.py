import tensorflow as tf
import re
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.models import Sequential

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

#transforma as frases em lowercase
a = (map(lambda x: x.lower(), new_list))
nova_lista = list(a)

#remove multiplos espacos em branco
a = (map(lambda x: re.sub("\s\s+" , " ", x), nova_lista))
new_list = list(a)

#remove titulos
new_list[:] = [x for x in new_list if "title" not in x]

#remove caracteres especiais
a = (map(lambda x: re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", x), new_list))
nova_lista = list(a)

#tokeniza
tokenizer = Tokenizer(num_words = 750)
tokenizer.fit_on_texts(nova_lista)
word_index = tokenizer.word_index
print(word_index)


# +1 for the index 0
total_words = len(tokenizer.word_index)+1

input_sequences = []
# Loop por cada linha (cada frase)
for line in nova_lista:
	token_list = tokenizer.texts_to_sequences([line])[0]
	# Loop pela frase para gerar sub-frases
	for i in range(1, len(token_list)):
		n_gram_sequence = token_list[:i+1]
		input_sequences.append(n_gram_sequence)

# qual a linha mais comprida? (pra padronizar)
max_sequence_len = max([len(x) for x in input_sequences])
max_sequence_len

input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

input_sequences

# criando categorias e dados, a partir das sequencias
x      = input_sequences[:,:-1]
labels = input_sequences[:,-1]

input_sequences[5]
x[5]
labels[5]

y = tf.keras.utils.to_categorical(labels, num_classes=total_words)


# O modelo:
model = Sequential([
          Embedding(total_words, 64, input_length=max_sequence_len-1),
          Bidirectional(LSTM(20)),
          Dense(total_words,
          activation='softmax') #Sigmoid se fosse binário... agora é multiclasse
])

# categorical crossentropy pelo mesmo motivo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print the model summary
model.summary()

# Save model