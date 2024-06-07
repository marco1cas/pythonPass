def detect(password):
    if len(password) < 8:
        return "La contraseña es demasiado corta"

    num_uppercase = sum(1 for char in password if char.isupper())
    num_lowercase = sum(1 for char in password if char.islower())
    num_digits = sum(1 for char in password if char.isdigit())
    num_symbols = sum(1 for char in password if not char.isalnum())

    if num_uppercase < 1:
        return "Faltan letras mayúsculas"
    if num_lowercase < 1:
        return "Faltan letras minúsculas"
    if num_digits < 1:
        return "Faltan dígitos"
    if num_symbols < 1:
        return "Faltan caracteres especiales"

    return "Your password is so good"

def isGood(password):
    result = detect(password)
    if result == "Your password is so good":
        return "muy buena"
    elif len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "medio vulnerable"
    else:
        return "vulnerable"

def askthem():
    password = input('your password: ')
    clasificacion = isGood(password)
    print(f"password: {clasificacion}")

askthem()

