# scripts/decrypt.py
# W1seGuy TryHackMe - XOR decryption walkthrough

ciphertext_hex = "REPLACE_WITH_HEX_FROM_CHALLENGE"
ciphertext = bytes.fromhex(ciphertext_hex)

known_plaintext = b"THM{"  # TryHackMe flags start with THM{

partial_key = bytes([c ^ p for c, p in zip(ciphertext, known_plaintext)])
print("Partial key (hex):", partial_key.hex())

decrypted = bytes([c ^ partial_key[i % len(partial_key)] for i, c in enumerate(ciphertext)])
print("Decrypted output:", decrypted.decode(errors="ignore"))

with open("../outputs/flag.txt", "w") as f:
    f.write(decrypted.decode(errors="ignore"))
