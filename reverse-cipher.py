#Reverse cipher algorithm


message = "Three can keep a secret, if two of them are dead"

#variable for cipher text
translated = ''

i = len(message) -1 #index variable for creating cipher
while i>=0:
    translated = translated+message[i]
    i = i-1

#to print this cipher text message
print(translated)
