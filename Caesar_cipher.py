# Caesar Cipher
#
# Jirawat Yuktawathin
# start  : 18/8/2017
# finish : 18/8/2017

alphabet_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,\
                'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,'n': 14,\
                'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,\
                'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 0}
num_alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',\
                8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',\
                15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',\
                22: 'v', 23: 'w', 24: 'x', 25: 'y', 0: 'z'}

def encrypt(plain, key):
    ''' Encrypt words to Caesar cipher with key.'''
    global alphabet_num, num_alphabet
    key = key.lower()
    plain = plain.lower()
    cipher = ''

    # Repeat a key if lenght less than a plain text.
    while len(key) < len(plain):
        key += key

    # Change plain to cipher.
    for i in range(len(plain)):
        try:
            hash_code = (alphabet_num[plain[i]] + alphabet_num[key[i]]) % 26
            cipher += num_alphabet[hash_code]
        except KeyError:
            cipher += plain[i]

    return cipher

def decrypt(cipher, key):
    ''' Decrypt Caesar cipher to words with key.'''
    global alphabet_num, num_alphabet
    cipher = cipher.lower()
    key = key.lower()
    plain = ''

    # Repeat a key text if lenght less than a cipher code.
    while len(key) < len(cipher):
        key += key

    # Change cipher to plain.
    for i in range(len(cipher)):
        try:
            hash_code = (alphabet_num[cipher[i]] - alphabet_num[key[i]]) % 26
            plain += num_alphabet[hash_code]
        except KeyError:
            plain += cipher[i]

    return plain

print(encrypt('attack at dawn','diamond'))
print(decrypt('ecunry ec qpkr','diamond'))
