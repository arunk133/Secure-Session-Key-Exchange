import socket

def start_eavesdropping():
    # Eve sets up a 'proxy' or simply listens on the same port
    print("[EVE] Monitoring network traffic on port 12345...")
    
    # In a real demo, you'd use a library like Scapy, 
    # but for this project, we will simulate what Eve sees.
    print("[EVE] Intercepting data packets...")
    print("-" * 50)
    
    # This is a simulation of the raw buffer data
    print("[EVE] Packet Captured: 0x4f23a1... (Encrypted RSA Key)")
    print("[EVE] Packet Captured: 0xa8b92c... (Encrypted Session Key)")
    print("[EVE] Packet Captured: 0x7e... (AES Encrypted Message)")
    print("-" * 50)
    print("[EVE] RESULT: Data is unreadable gibberish. Eavesdropping failed.")

if __name__ == "__main__":
    start_eavesdropping()