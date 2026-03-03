from crypto_utils import aes_encrypt, aes_decrypt
from Crypto.Random import get_random_bytes

def run_tamper_test():
    # 1. Setup a valid session
    session_key = get_random_bytes(16)
    original_message = "Transfer $100 to Alice"
    print(f"Original Message: {original_message}")

    # 2. Alice encrypts the message
    nonce, ciphertext, tag = aes_encrypt(session_key, original_message)
    print(f"Original Ciphertext (Hex): {ciphertext.hex()[:20]}...")

    # 3. MALEVOLENT ACTOR (TAMPERING)
    # Let's change one byte of the ciphertext to try and change the data
    tampered_ciphertext = bytearray(ciphertext)
    tampered_ciphertext[0] ^= 0x01  # Flip a single bit
    print(f"Tampered Ciphertext (Hex): {tampered_ciphertext.hex()[:20]}...")

    # 4. Bob tries to decrypt
    print("\n[SERVER] Bob is attempting to decrypt the tampered message...")
    try:
        decrypted_message = aes_decrypt(session_key, nonce, tampered_ciphertext, tag)
        print(f"Decrypted: {decrypted_message}")
    except ValueError:
        print("[ALERT] INTEGRITY ERROR: The message was tampered with! The MAC check failed.")
        print("[SERVER] Message discarded. Connection terminated.")

if __name__ == "__main__":
    run_tamper_test()