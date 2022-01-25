# Importa biblioteca regex (expressões regulares)

import re

frase = 'O rato roeu a roupa do rei rato de Roma'

if 'rato' in frase:
    print('Palavra encontrada')
    print('Ocorre: ',frase.count('rato'))
else:
    print ('Palavra não encontrada')


mpax = 'O motorista me tratol mal e foi mal educado na viagem.' \
       'Acho que por ser tão mal educado, deve ser punido'

if 'mal' in mpax:
    print('Palavra encontrada')
    print('Ocorre: ', mpax.count('mal'))