import sys
from collections import Counter
import math

def KSA(K):
    n = len(K)
    j = 0
    T = [K[i%n] for i in range(256)]
    S = list(range(256))
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, data):
    S = KSA([ord(c) for c in key])
    keystream = PRGA(S)
    return bytes([c ^ next(keystream) for c in data])


def main():
    # message
    # input output
    if len(sys.argv) == 3:
        message = bytearray(sys.argv[1], 'utf-8')
        key = sys.argv[2]
        encrypted = RC4(key, message)
        
        f_text = open("cyphertext.txt", 'w+')
        f_text.write(str(encrypted))
        f_text.close()
        f_key = open("key.txt", 'w+')
        f_key.write(str(key))
        f_key.close()
        print(encrypted)
        
    return


if __name__ == "__main__":
    main()
    
# usage:
# python3 rc4_encode.py wiadomosc123ew23eds klucz874wficdh98