
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import binascii

# šifrovaná zpráva v hex
encrypted_msg_hex = "7da8ffed704d231c7d8e26a61bf2da342b7e22bf1652f032588b301fb05ace8194ac1a6e82958bfd27fc653de572d6418ab8e92ff2ff82f89ca036fdad87ab5846c9c58d43e1659764db80f9057b3f6bb51faf9e96fd87dfb60a5d74e54b4f0049fd920d013d034e3677ed8f2ecd06be22825db4d395e1418b4fa9f490dd60f3"
encrypted_msg = binascii.unhexlify(encrypted_msg_hex)


# nacteni rsa privátního klíče
with open("/Users/alexa/Desktop/GitHub/KBB-Breaking-RSA/private-key.pem", "rb") as f:
    private_key_data = f.read()

private_key = RSA.import_key(private_key_data)
cipher = PKCS1_OAEP.new(private_key)
decrypted_msg = cipher.decrypt(encrypted_msg)

print("Dešifrovaná zpráva: ", decrypted_msg.decode())