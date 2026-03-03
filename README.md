# Secure Session Key Exchange & Hybrid Encryption Demonstrator

## 1. Project Overview
This project is a functional implementation of a **Hybrid Cryptosystem**, designed to provide a secure communication channel between two network entities (Alice and Bob). It solves the "Key Distribution Problem" by combining the strengths of Asymmetric and Symmetric cryptography.



The system demonstrates the three pillars of Cybersecurity:
* **Confidentiality:** Ensuring data is unreadable to unauthorized parties.
* **Integrity:** Detecting if data has been modified during transit.
* **Key Exchange:** Securely sharing a secret session key over an insecure medium.

---

## 2. Core Components
The project consists of five primary scripts:
* `crypto_utils.py`: The cryptographic engine containing the logic for **RSA-2048** and **AES-128 EAX** mode.
* `server.py` (Bob): The receiver that generates the RSA key pair and listens for connections.
* `client.py` (Alice): The sender that initiates the handshake and generates the secret AES session key.
* `eve_sniffer.py`: A simulation script proving that intercepted data is unreadable (Confidentiality).
* `tamper_demo.py`: A script demonstrating that any bit-level modification of the ciphertext is detected (Integrity).

---

## 3. Technical Specifications
* **Asymmetric Algorithm:** RSA-2048 with PKCS1_OAEP padding.
* **Symmetric Algorithm:** AES-128 in EAX (Authenticated Encryption) mode.
* **Integrity Check:** 16-byte Message Authentication Code (MAC) tag.
* **Network Protocol:** TCP/IP Sockets (Port 12345).



---

## 4. How to Run the Demonstration

### Prerequisites
* Python 3.12+ (Anaconda recommended)
* `pycryptodome` library installed

### Step-by-Step Execution
1.  **Initialize the Environment:**
    ```bash
    conda activate secure_crypto
    ```

2.  **Start the Server (Bob):**
    Open an Anaconda Prompt and run:
    ```bash
    python server.py
    ```

3.  **Start the Client (Alice):**
    Open a second Anaconda Prompt and run:
    ```bash
    python client.py
    ```

4.  **Test Confidentiality (Eve):**
    Open a third terminal and run the sniffer simulation:
    ```bash
    python eve_sniffer.py
    ```

5.  **Test Integrity (Tampering):**
    Run the tamper demo to see the MAC verification fail:
    ```bash
    python tamper_demo.py
    ```

---

## 5. Security Analysis
By utilizing **AES-EAX**, this project provides **Authenticated Encryption**. Unlike standard encryption which only hides the message, EAX mode ensures that if a single bit of the ciphertext is changed (as shown in the `tamper_demo.py`), the receiver's system will throw a `ValueError` and reject the message. This prevents "Man-in-the-Middle" attacks.

---


