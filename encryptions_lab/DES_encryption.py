from Crypto.Cipher import DES
from Crypto.Util.Padding import pad , unpad
from Crypto.Random import get_random_bytes

# Function to encrypt plaintext using DES
def des_encrypt(key , plaintext):
    """
    Encrypts a plaintext string using DES encryption.
    :param key: A 8-byte key
    :param plaintext: The plaintext string to encrypt
    :return: The ciphertext and initialization vector (IV)
    """
    # Create a cipher object using the key and a random IV
    cipher = DES.new(key , DES.MODE_CBC)
    iv = cipher.iv
    # Pad the plaintext to ensure it's a multiple of 8 bytes
    padded_plainText = pad(plaintext.encode("utf-8"), DES.block_size)
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plainText)

    # Return the ciphertext and IV
    return ciphertext , iv

# Function to decrypt ciphertext using DES
def des_decrypt(key, ciphertext , iv):
    """
    Decrypts a ciphertext string using DES encryption.
    :param key: A 8-byte key
    :param ciphertext: The encrypted ciphertext
    :param iv: The initialization vector (IV) used during encryption
    :return: The decrypted plaintext string
    """
    # Create a cipher object using the key and the provided IV
    cipher = DES.new(key , DES.MODE_CBC , iv = iv)
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)
    # Unpad the plaintext to its original form
    plaintext = unpad(padded_plaintext , DES.block_size).decode("utf-8")

    return plaintext



# Main method to demonstrate the functionality
if __name__ == "__main__":
    # Generate a random 8-byte key for DES
    key = get_random_bytes(8)

    # demonstration for DES encryption and decryption

    plaintext = 'Hello, DES encryption'

    print(f"original text : {plaintext}")
 
    ciphertext, iv2 = des_encrypt(key , plaintext)

    print(f"CipherText (DES) = {ciphertext}")

    
    decrypted_text = des_decrypt(key , ciphertext , iv2)

   
    print(f"decrypted text DES : {decrypted_text}")
