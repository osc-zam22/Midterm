from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt plaintext using 3DES (Triple DES)
def des3_encrypt(key, plaintext):
    """
    Encrypts a plaintext string using 3DES encryption.
    :param key: A 16-byte or 24-byte key
    :param plaintext: The plaintext string to encrypt
    :return: The ciphertext and initialization vector (IV)
    """
    # Create a cipher object using the key and a random IV
    cipher = DES3.new(key, DES3.MODE_CBC)
    iv = cipher.iv
    # Pad the plaintext to ensure it's a multiple of 8 bytes
    padded_plaintext = pad(plaintext.encode("utf-8"), DES3.block_size)
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Return the ciphertext and IV
    return ciphertext, iv

# Function to decrypt ciphertext using 3DES
def des3_decrypt(key, ciphertext, iv):
    """
    Decrypts a ciphertext string using 3DES encryption.
    :param key: A 16-byte or 24-byte key
    :param ciphertext: The encrypted ciphertext
    :param iv: The initialization vector (IV) used during encryption
    :return: The decrypted plaintext string
    """
    # Create a cipher object using the key and the provided IV
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)
    # Unpad the plaintext to its original form
    plaintext = unpad(padded_plaintext, DES3.block_size).decode("utf-8")

    return plaintext

# Main method to demonstrate the functionality
if __name__ == "__main__":
    # Generate a random 16-byte or 24-byte key for 3DES
    key = DES3.adjust_key_parity(get_random_bytes(16))

    # Demonstration for 3DES encryption and decryption
    plaintext = 'Hello, 3DES encryption'

    print(f"Original Text: {plaintext}")
 
    ciphertext, iv = des3_encrypt(key, plaintext)
    print(f"Ciphertext (3DES) = {ciphertext.hex()}")

    decrypted_text = des3_decrypt(key, ciphertext, iv)
    print(f"Decrypted Text (3DES): {decrypted_text}")
