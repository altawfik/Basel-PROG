# Password-Generator.py
import secrets
import string
import argparse

def generate_password(length=20):
    if length < 4:
        raise ValueError("Die Länge muss mindestens 4 sein, um jede Kategorie sicherzustellen.")

    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"

    password_chars = [
        secrets.choice(lowers),
        secrets.choice(uppers),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_chars = lowers + uppers + digits + symbols
    remaining = length - len(password_chars)
    for _ in range(remaining):
        password_chars.append(secrets.choice(all_chars))

    # sicherer Shuffle
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

def main():
    parser = argparse.ArgumentParser(
        description="Passwort-Generator — erzeugt sichere Passwörter mit Standardlänge 20."
    )
    parser.add_argument("-n", "--number", type=int, default=1,
                        help="Anzahl der zu erzeugenden Passwörter (Standard: 1).")
    parser.add_argument("-l", "--length", type=int, default=20,
                        help="Länge jedes Passworts (Standard: 20).")
    parser.add_argument("-o", "--outfile", type=str, help="Datei zum Speichern (optional)")
    args = parser.parse_args()

    results = []
    for i in range(args.number):
        pwd = generate_password(length=args.length)
        results.append(pwd)
        print(pwd)

    if args.outfile:
        with open(args.outfile, "w", encoding="utf-8") as f:
            for p in results:
                f.write(p + "\n")
        print(f"\nSaved {len(results)} passwords to {args.outfile}")

if __name__ == "__main__":
    main()
