import string
import secrets


def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    while True:
        ask = input('length?: ')
        if not ask.isdigit():
            print('  a positive integer')
            continue

        length = int(ask)

        if length <= 0:
            print('Password length must be an integer')
            continue

        password = generatePassword(length)
        print('Generated password:', password)
        break

main()
