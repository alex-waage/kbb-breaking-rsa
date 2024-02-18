from Crypto.PublicKey import RSA

# import RSA klíče
with open('/Users/alexa/Desktop/GitHub/KBB-Breaking-RSA/public-key.pub', 'r') as file:
    key = RSA.importKey(file.read())

# print n & e
print("n: ", key.n, "e: ", key.e)
