- Exploit known plaintext to recover the encryption key  
- Decrypt the flag and submit it to complete the challenge  

It’s designed for **learning, sharing techniques, and showcasing cybersecurity skills**.

---

## 🛠 Challenge Context

- The target is a TryHackMe room called `W1seGuy`.  
- The room sends an encrypted flag via a service running on a remote machine.  
- To solve it, you must reverse-engineer the encryption scheme and extract the correct key.  

---

## 🔹 Key Concepts

### XOR Encryption

XOR (exclusive OR) is a bitwise operation that’s reversible. In this challenge:


Ciphertext XOR Plaintext = Key


Knowing part of the plaintext (like `THM{`) allows recovery of the encryption key — a classic **known-plaintext attack**.

### Hex Encoding

The server sends ciphertext as hex. Converting it to raw bytes is the first step toward analysis.

---

## 🧩 Walkthrough Steps

### 1️⃣ Connect to the Server

Use Netcat to connect:

```bash
nc <MACHINE_IP> 1337

The server sends a hex-encoded ciphertext.

2️⃣ Decode Hex & Extract Ciphertext

Convert the hex string to raw bytes. This is the encrypted flag to analyze.

3️⃣ Exploit Known Plaintext
Flags start with THM{.
XOR the known prefix against the ciphertext to partially recover the key.

4️⃣ Automate Decryption

Use a Python script to brute-force remaining key characters and decrypt the flag:

# Example snippet
from itertools import product

# partial_key known from THM{
# generate remaining key guesses

🎯 Outcome

✅ Decrypted the first flag
✅ Submitted the correct key to the server
✅ Received the final flag
