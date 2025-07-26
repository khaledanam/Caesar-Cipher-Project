import json
import os
import base64
import random

CONFIG_FILE = "main_config.secure"
ENC_CONFIG_FILE = "enc_config.secure"

def encrypt_file(data, filename):
    encoded = base64.b64encode(json.dumps(data).encode())
    with open(filename, 'wb') as f:
        f.write(encoded)

def decrypt_file(filename):
    try:
        with open(filename, 'rb') as f:
            return json.loads(base64.b64decode(f.read()).decode())
    except Exception as e:
        print("❌ Failed to read:", filename)
        return None

# Caesar Cipher logic
def caesar_cipher(text, char_array, shift, encrypt=True):
    result = ""
    index_map = {c: i for i, c in enumerate(char_array)}
    array_len = len(char_array)

    for char in text:
        if char in index_map:
            idx = index_map[char]
            new_idx = (idx + shift) % array_len if encrypt else (idx - shift) % array_len
            result += char_array[new_idx]
        else:
            result += char
    return result

def setup():
    print("🔐 Initial Setup")
    array = input("Enter your custom character array:\n> ").strip()
    
    while True:
        try:
            shift = int(input("Enter your fixed shift key (number):\n> ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid integer for the shift key.")

    config_data = {
        'array': array,
        'fixed_shift': shift
    }

    encrypt_file(config_data, CONFIG_FILE)
    print("✅ Initial config saved with custom array and shift key.\n")
def encrypt_text():
    config = decrypt_file(CONFIG_FILE)
    if not config:
        return

    text = input("🔏 Enter text to encrypt:\n> ")
    words = text.split(" ")
    total_words = len(words)
    rand = random.randint(2, max(2, total_words - 1))
    shift = total_words // rand

    shuffled_indexes = list(range(total_words))
    random.shuffle(shuffled_indexes)
    shuffled_words = [words[i] for i in shuffled_indexes]
    shuffled_text = ' '.join(shuffled_words)

    encrypted_text = caesar_cipher(shuffled_text, config['array'], shift, encrypt=True)

    # Save enc config
    enc_config = {
        'random_number': rand,
        'total_words': total_words,
        'shift': shift,
        'shuffled_indexes': shuffled_indexes
    }
    encrypt_file(enc_config, ENC_CONFIG_FILE)

    print("\n✅ Encrypted Text:\n" + encrypted_text)
    print(f"ℹ️ Saved encryption config in {ENC_CONFIG_FILE}")

def decrypt_text():
    config = decrypt_file(CONFIG_FILE)
    enc_config = decrypt_file(ENC_CONFIG_FILE)
    if not config or not enc_config:
        return

    encrypted = input("🔓 Enter encrypted text:\n> ")
    decrypted_text = caesar_cipher(encrypted, config['array'], enc_config['shift'], encrypt=False)

    words = decrypted_text.split(" ")
    original_order = [''] * enc_config['total_words']

    for i, idx in enumerate(enc_config['shuffled_indexes']):
        original_order[idx] = words[i]

    restored_text = ' '.join(original_order)

    print("\n✅ Decrypted Text:\n" + restored_text)

def menu():
    while True:
        print("\n🔹 Caesar Cipher Tool (Text-Based Encryption)")
        print("1. Setup Initial Config")
        print("2. Encrypt Text")
        print("3. Decrypt Text")
        print("4. Exit")
        choice = input("Choose (1/2/3/4): ")
        if choice == '1':
            setup()
        elif choice == '2':
            encrypt_text()
        elif choice == '3':
            decrypt_text()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
