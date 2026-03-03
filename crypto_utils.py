from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_rsa_keys():
    """Generates a Private and Public RSA key pair."""
    key = RSA.generate(2048) #
    return key.export_key(), key.publickey().export_key()

def rsa_encrypt(public_key, data):
    """Encrypts small data (like a session key) using RSA Public Key."""
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key) #
    return cipher_rsa.encrypt(data)

def rsa_decrypt(private_key, encrypted_data):
    """Decrypts data using RSA Private Key."""
    key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    return cipher_rsa.decrypt(encrypted_data)

def aes_encrypt(session_key, plain_text):
    """Encrypts data using the Shared Session Key (AES)."""
    cipher_aes = AES.new(session_key, AES.MODE_EAX) #
    ciphertext, tag = cipher_aes.encrypt_and_digest(plain_text.encode())
    return cipher_aes.nonce, ciphertext, tag

def aes_decrypt(session_key, nonce, ciphertext, tag):
    """Decrypts data using the Shared Session Key (AES)."""
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return data.decode()