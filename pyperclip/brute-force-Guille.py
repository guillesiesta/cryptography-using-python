import pyperclip

message  = 'GUVF VF ZL FRPERG ZRFFNTR'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num-key + len(LETTERS)
            dcipher = num % len(LETTERS)
            translated = translated + LETTERS[dcipher]
    print('Key #%s: %s' %(key,translated))
