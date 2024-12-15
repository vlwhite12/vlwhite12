from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrpyt_message(key, message):
    cipher_suite = Fernet(key)
    encrpyted_message = cipher_suite.encrypt(message.encode())
    return encrpyted_message

def decrypt_message(key, encrpyted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrpyted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    key = generate_key()
    message = input("Enter a message to encrypt: ")

    encrpyted_message = encrpyt_message(key, message)
    print(f"Encrypted Message: {encrpyted_message}")

    decrypted_message = decrypt_message(key, encrpyted_message)
    print(f"Decrypted Message: {decrypted_message}")
