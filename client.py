import socket
from Crypto.Random import get_random_bytes
from crypto_utils import rsa_encrypt, aes_encrypt

# 1. Setup & Connection
print("[CLIENT] Connecting to Bob (Server)...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345)) #

# 2. Secure Handshake
# Receive the RSA Public Key from Bob
public_key = client.recv(2048)
print("[CLIENT] Public Key received from Server.")

# Generate a random 16-byte (128-bit) AES Session Key
session_key = get_random_bytes(16) #
print(f"[CLIENT] Generated Secret Session Key: {session_key.hex()}")

# Encrypt the Session Key with Bob's Public Key so ONLY Bob can read it
encrypted_session_key = rsa_encrypt(public_key, session_key) #
client.send(encrypted_session_key)
print("[CLIENT] Encrypted Session Key sent. Handshake complete.")

# 3. Secure Chat
print("\n--- You can now chat securely ---")
while True:
    msg = input("Enter message: ")
    if msg.lower() == 'exit': break
    
    # Encrypt the message using the shared Session Key
    nonce, ciphertext, tag = aes_encrypt(session_key, msg) #
    
    # Send as one package: nonce + tag + ciphertext
    client.send(nonce + tag + ciphertext)

client.close()