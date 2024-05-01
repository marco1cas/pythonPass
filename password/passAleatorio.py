import random
import string


def generate_password(
    length=12,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_symbols=True,
):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("no characters")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    while True:
        try:
            length = int(input("Lenght: "))
            if length <= 0:
                print("only numbers")
                continue
            break
        except ValueError:
            print("invalid number")

    include_symbols = (
        input("symbols? (yes/no):  ").strip().lower()
    )
    while include_symbols not in ("yes", "no"):
        print(" yes or no! >:(")
        include_symbols = (
            input("symbols? (yes/no): ").strip().lower()
        )

    try:
        password = generate_password(
            length=length,
            include_symbols=include_symbols == "si",
        )
        print(f"generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
