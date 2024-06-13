import hashlib
message = str(input("Enter message:: "))
result1 = hashlib.md5(b'message')
message_digest = result1.hexdigest()
print("The MD5 message digest for given message is:: ", message_digest)
result2 = hashlib.sha1(b'message')
sha1 = result2.hexdigest()
print("The SHA1 message digest for given message is:: ", sha1)
