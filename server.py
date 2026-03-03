import socket
from crypto_utils import generate_rsa_keys, rsa_decrypt, aes_decrypt

# 1. Setup
print("[SERVER] Starting up...")
private_key, public_key = generate_rsa_keys()

# 2. Network connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345)) #
server.listen(1)
print("[SERVER] Waiting for Alice (Client) to connect...")

conn, addr = server.accept()
print(f"[SERVER] Connected to {addr}")

# 3. Secure Handshake
print("[SERVER] Sending Public RSA Key to Alice...")
conn.send(public_key) # Send RSA public key to client

encrypted_session_key = conn.recv(1024)
session_key = rsa_decrypt(private_key, encrypted_session_key) #
print(f"[SERVER] Handshake Complete. Session Key Received: {session_key.hex()}")

# 4. Secure Chat
while True:
    data = conn.recv(4096)
    if not data: break
    
    # We expect: nonce (16) + tag (16) + ciphertext
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    message = aes_decrypt(session_key, nonce, ciphertext, tag)
    print(f"[CLIENT SAYS]: {message}")

conn.close()