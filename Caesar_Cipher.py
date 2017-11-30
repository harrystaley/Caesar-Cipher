#!/usr/bin/env python2.7
# This is a simple module that defines a Caesar Cipher

MAX_KEY = 26


def getMode():
    '''Prompts the user for encrypt or decrypt mode'''
    while True:
        print('encrypt or decrypt a message?')
        mode = raw_input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter "encrypt", "e", "decrypt", or "d".')


def getMessage():
    '''Prompts the user for their input'''
    print('Input Message:')
    return raw_input()


def getKey():
    ''' Prompts the user for their key size.'''
    key = 0
    while True:
        print('Input key size (1-%s)' % (MAX_KEY))
        key = int(raw_input())
        if (key >= 1 and key <= MAX_KEY):
            return key


def translateMessage(mode, message, key):
    ''' takes in mode, message, and key as funciton inputs.
    ENcryption translates plain text into cypther text.
    Decryption translates cypher text into plain text.'''

    if mode[0] == 'd':
        key = -key
    translated = ''

    for character in message:
        if character.isalpha():
            num = ord(character)
            num += key

            if character.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif character.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += character
    return translated


mode = getMode()
key = getKey()
message = getMessage()

print('Your translated text is:')
print(translateMessage(mode, message, key))
