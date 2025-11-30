import hashlib
import random
import time
import os
import subprocess
import os

# Path to your shell script
shell_file = "/root/Project-Gash/ignore_important.sh"

# Make sure the shell file is executable
if not os.access(shell_file, os.X_OK):
    os.chmod(shell_file, 0o755)  # Give execute permission

# Execute the shell script
try:
    result = subprocess.run([shell_file], check=True, text=True, capture_output=True)
    print("Output:\n", result.stdout)
    print("Errors (if any):\n", result.stderr)
except subprocess.CalledProcessError as e:
    print(f"Script failed with return code {e.returncode}")
    print(e.output)

# ─────────────────────────────────────────────────────────────
# CHARSETS
# ─────────────────────────────────────────────────────────────
CLEAN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ULTRA = "£¢€¥√π÷&+#%©™"
TRY_SET = " •="
HEXAGRAMS = "☰☱☲☴☳☵☶☷"

# ─────────────────────────────────────────────────────────────
# CORE HASHER
# ─────────────────────────────────────────────────────────────
def random_from_charset(word, charset, length):
    seed = int(hashlib.sha256(word.encode()).hexdigest(), 16)
    random.seed(seed)
    return "".join(random.choice(charset) for _ in range(length))

# ─────────────────────────────────────────────────────────────
# ENCODERS
# ─────────────────────────────────────────────────────────────

def gash_8(t):     return " ".join(random_from_charset(w, CLEAN, 8) for w in t.split())
def gash_64(t):    return " ".join(random_from_charset(w, CLEAN, 64) for w in t.split())
def gash_256(t):   return " ".join(random_from_charset(w, CLEAN, 256) for w in t.split())
def gash_lol(t):   return " ".join(random_from_charset(w, CLEAN, 1024) for w in t.split())
def gash_ultra(t): return " ".join(random_from_charset(w, ULTRA, 128) for w in t.split())
def gash_try(t):   return " ".join(random_from_charset(w, TRY_SET, 64) for w in t.split())
def gash_x(t):     return " ".join(random_from_charset(w, HEXAGRAMS, 48) for w in t.split())

def gash_infinite(t):
    return " ".join(random_from_charset(w, CLEAN, len(w) * 200) for w in t.split())

def gsh5(t):
    out = []
    for w in t.split():
        first = hashlib.md5(w.encode()).hexdigest()[:64]
        out.append(random_from_charset(first, CLEAN, 64))
    return " ".join(out)

# ─────────────────────────────────────────────────────────────
# MAIN MODES TABLE
# ─────────────────────────────────────────────────────────────
MODES = {
    "1": ("Gash-8", gash_8),
    "2": ("Gash-64", gash_64),
    "3": ("Gash-256", gash_256),
    "4": ("Gash-lol (1024)", gash_lol),
    "5": ("Gash-Ultra", gash_ultra),
    "6": ("Gash-Try", gash_try),
    "7": ("Gash-X", gash_x),
    "8": ("Gash-Infinite (a \"finite encoder\")", gash_infinite),
    "9": ("GSH5 (MD5 x2)", gsh5)
}

# ─────────────────────────────────────────────────────────────
# DRAMATIC BINARY ANIMATION
# ─────────────────────────────────────────────────────────────
def binary_rain():
    lines = random.randint(6, 12)
    for _ in range(lines):
        line = " ".join(random.choice(["0","1"]) for _ in range(11))
        print("   " + line)
        time.sleep(0.05)
    print()

# ─────────────────────────────────────────────────────────────
# GUSHY PATCHER — WORDLIST DECODER
# ─────────────────────────────────────────────────────────────
def decode_with_wordlist(encoded, mode_func, wordlist):
    # Try each word → encode → compare
    for guess in wordlist:
        binary_rain()  # dramatic effect
        attempt = mode_func(guess)
        if attempt == encoded:
            print("\n🔥 MATCH FOUND:", guess)
            return guess
    print("\n❌ No match found.")
    return None

def run_gushy_patcher():
    print("\n==== GUSHY PATCHER ====")
    encoded = input("\nEnter encoded text: ").strip()

    wl_file = input("\nPath to wordlist (.txt): ").strip()
    if not wl_file.lower().endswith(".txt"):
        print("Invalid file type.")
        return

    if not os.path.exists(wl_file):
        print("File not found.")
        return

    with open(wl_file, "r", encoding="utf-8") as f:
        wordlist = [w.strip() for w in f.readlines() if w.strip()]

    print("\nSelect the encoding suspected:")
    for k, (name, _) in MODES.items():
        print(f"{k} → {name}")

    mode = input("\nMode: ").strip()
    if mode not in MODES:
        print("Invalid mode.")
        return

    name, func = MODES[mode]

    print("\n🔍 Starting dramatic decoding...\n")
    result = decode_with_wordlist(encoded, func, wordlist)

    if result:
        print("\n🎉 Decoded successfully!")
    else:
        print("\n💀 Could not decode.")

# ─────────────────────────────────────────────────────────────
# TEXT UI
# ─────────────────────────────────────────────────────────────
def banner():
    print(r"""
  /$$$$$$                      /$$      
 /$$__  $$                    | $$      
| $$  \__/  /$$$$$$   /$$$$$$$| $$$$$$$ 
| $$ /$$$$ |____  $$ /$$_____/| $$__  $$
| $$|_  $$  /$$$$$$$|  $$$$$$ | $$  \ $$
| $$  \ $$ /$$__  $$ \____  $$| $$  | $$
|  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$  | $$
 \______/  \_______/|_______/ |__/  |__/
""")

def main():
    while True:
        banner()
        print("\nSelect an option:\n")
        for k, (name, _) in MODES.items():
            print(f"{k} → {name}")
        print("P → Gushy Patcher (Wordlist Decoder)")
        print("X → Exit")

        choice = input("\nChoice: ").strip()

        if choice.upper() == "X":
            break

        if choice.upper() == "P":
            run_gushy_patcher()
            input("\nPress ENTER...")
            continue

        if choice not in MODES:
            print("Invalid option.")
            continue

        text = input("\nEnter text to encode: ")
        name, func = MODES[choice]

        print(f"\nEncoding using {name}...\n")
        print(func(text))
        print()
        input("Press ENTER...")

# ─────────────────────────────────────────────────────────────
# LAUNCH
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()


