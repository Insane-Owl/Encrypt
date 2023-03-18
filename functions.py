import re
import secrets
import string


def generate_key():
    numbers = '0123456789'
    key = ''
    
    for i in range(10):
        key += secrets.choice(numbers)
    
    return key


def key_to_alphabet(key: str):
    if not key.isnumeric() or not len(key) == 10:
        raise ValueError('key was not 10 digits long, or was not numeric.')

    parts_order = {}
    alphabet = ''
    shift = ''
    invert = False

    for i in enumerate(key):
        if i[0] == 2 or i[0] == 3 or i[0] == 5 or i[0] == 7:
            parts_order[int(i[0])] = int(i[1])
        else:
            shift += i[1]

        if i[0] == 9 and (int(i[1]) % 2) == 0:
            invert = True

    shift = int(shift)

    parts_order = sorted(parts_order.items(), key=lambda x:x[1])
    for i in parts_order:
        if i[0] == 2:
            alphabet += string.ascii_lowercase
        elif i[0] == 3:
            alphabet += string.ascii_uppercase
        elif i[0] == 5:
            alphabet += string.digits
        elif i[0] == 7:
            alphabet += string.punctuation

    return alphabet, shift, invert


def encrypt(message, key):
    alphabet, shift, invert = key_to_alphabet(key)

    encrypted_message = ''

    for letter in message:
        if letter in alphabet:
            place = alphabet.find(letter)
            encrypted_message += alphabet[(place + shift) % len(alphabet)]
        elif letter == ' ':
            encrypted_message += '<?/'
        elif letter == '\n':
            encrypted_message += '^/,'

    if invert:
        return encrypted_message[::-1]
    else:
        return encrypted_message


def decrypt(message, key):
    alphabet, shift, invert = key_to_alphabet(key)

    decrypted_message = ''

    if invert:
        message = message[::-1]

    message = message.replace('<?/', ' ')
    message = message.replace('^/,', '\n')

    for letter in message:
        if letter in alphabet:
            place = alphabet.find(letter)
            decrypted_message += alphabet[(place - shift) % len(alphabet)]
        else:
            decrypted_message += letter

    return decrypted_message
