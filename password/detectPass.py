def detect(password):
    
    if len(password) < 8:
        return False
  
    num_mayusculas = sum(1 for char in password if char.isupper())
    num_minusculas = sum(1 for char in password if char.islower())
    num_digitos = sum(1 for char in password if char.isdigit())
    num_simbolos = sum(1 for char in password if not char.isalnum())
    
    if num_mayusculas < 1 or num_minusculas < 1 or num_digitos < 1 or num_simbolos < 1:
        return False
    
    return True

def seraBuena(password):
    if detect(password):
        return "good"
    else:
        return "bad"

def main():
    password = input("Dime tu contraseña: ")
    clasificacion = seraBuena(password)
    print(f"contraseña: {clasificacion}")

if __name__ == "__main__":
    main()
