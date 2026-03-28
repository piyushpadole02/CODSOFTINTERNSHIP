
import string
import secrets

def ask_yes_no(prompt, default="y"):
    valid = {"y": True, "n": False}
    while True:
        resp = input(f"{prompt} [{'Y/n' if default=='y' else 'y/N'}]: ").strip().lower()
        if resp == "" and default:
            return valid[default]
        if resp in valid:
            return valid[resp]
        print("Please enter 'y' or 'n'.")

def get_length():
    while True:
        s = input("Enter desired password length (e.g. 12): ").strip()
        if not s:
            print("Please enter a number.")
            continue
        if not s.isdigit():
            print("Please enter a positive integer.")
            continue
        length = int(s)
        if length <= 0:
            print("Length must be greater than 0.")
            continue
        return length

def build_charset(include_lower, include_upper, include_digits, include_symbols, avoid_ambiguous):
    charset = ""
    if include_lower:
        charset += string.ascii_lowercase
    if include_upper:
        charset += string.ascii_uppercase
    if include_digits:
        charset += string.digits
    if include_symbols:
        # use common punctuation characters; exclude space
        charset += string.punctuation
    if avoid_ambiguous:
        ambiguous = "Il1O0"
        charset = "".join(ch for ch in charset if ch not in ambiguous)
    return charset

def generate_password(length, charset):
    if not charset:
        raise ValueError("Character set is empty. Choose at least one character type.")
    return "".join(secrets.choice(charset) for _ in range(length))

def main():
    print("Password Generator (Python 3)")

    length = get_length()

    print("\nChoose which character types to include in the password:")
    include_lower = ask_yes_no("Include lowercase letters? (a-z)", default="y")
    include_upper = ask_yes_no("Include uppercase letters? (A-Z)", default="y")
    include_digits = ask_yes_no("Include digits? (0-9)", default="y")
    include_symbols = ask_yes_no("Include symbols/punctuation? (e.g. !@#$%)", default="n")
    avoid_ambiguous = ask_yes_no("Avoid ambiguous characters like I, l, 1, O, 0?", default="n")

    charset = build_charset(include_lower, include_upper, include_digits, include_symbols, avoid_ambiguous)

    try:
        password = generate_password(length, charset)
    except ValueError as e:
        print("Error:", e)
        print("Please run again and select at least one character type.")
        return

    print("\nGenerated password:")
    print(password)

if __name__ == "__main__":
    main()