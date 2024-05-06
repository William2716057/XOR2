def XORcipher(text, key):
    if isinstance(text, str):
        text = text.encode()
        
    if len(key) < len(text):
        key = key * (len(text) // len(key) + 1)
        key = key[:len(text)]
        
    return bytes([x ^ y for x, y in zip(text, key)]) 
original = "message to be XORed"

key = b'secret'

encrypted = XORcipher(original, key)
print(encrypted)

decrypted = XORcipher(encrypted, key)
print(decrypted)
print(decrypted.decode())