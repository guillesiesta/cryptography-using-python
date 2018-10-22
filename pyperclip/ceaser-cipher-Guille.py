import pyperclip

message = 'This is my secret message'
key = 13
mode = 'encrypt'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''

message = message.upper() # ponemos las letras todas  mayusculas

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # se hace el modulo
        mod = len(LETTERS)
        # print(num)
        cipher = num % mod
        # print(cipher)
        translated = translated + LETTERS[cipher]

    else:

        translated = translated + symbol


print(translated)
pyperclip.copy(translated)
