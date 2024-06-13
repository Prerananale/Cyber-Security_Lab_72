from Crypto.Cipher import AES 
key = b'Pg@gfh#prerana12'
cipher = AES.new(key,AES.MODE_EAX)
data= "Welcome to sanjivani".encode()
nonce = cipher.nonce
ciphertext=cipher.encrypt(data)
print("ciphertext",ciphertext)
cipher=AES.new(key,AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print ("plaintext: ", plaintext.decode())