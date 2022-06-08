# from traceback import print_tb
# import termcolor as tc

# ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# def caeser_decrypt(cipher_text):
#   for KEY in range(1, 27):
#     plain_text = ''
#     for c in cipher_text:
#       if c in ALPHABET:
#         index = ALPHABET.find(c)
#         index = (index - KEY) % len(ALPHABET)
#         plain_text = plain_text + ALPHABET[index]
#       else:
#         plain_text += c
#     # if plain_text[:4] == 'actf':
#     #   print(tc.colored(f'KEY {KEY} : {plain_text}', 'red', attrs=['reverse', 'blink']))
#     # else:
#     print(f'KEY {KEY} :', plain_text)


# cipher_text = input('Enter the cipher text : ')
# # cipher_text = open('chall.txt', 'r')
# # print(cipher_text.read())

# caeser_decrypt(cipher_text)
