from Crypto.Cipher import AES
from secrets import token_bytes
import hashlib
import hmac

class Client(object):
    hmac_key = token_bytes(16)

    def myPublicKeyForDH(self):
          return 4
    
    def encrypt(self, textToEncrypt, key):
          textToEncryptByte = bytes(textToEncrypt, 'utf-8')
          cipher = AES.new(key, AES.MODE_EAX)
          nonce = cipher.nonce
          ciphertext, tag = cipher.encrypt_and_digest(textToEncryptByte)     
          return ciphertext, nonce, tag

    def hmac_digester(textToEncrypt, key):
          textToEncryptByte = bytes(textToEncrypt, 'utf-8')
          hash = hashlib.sha256
          hmac_digest = hmac.new(key,textToEncryptByte,hash)
          hmac_hexdigest =  hmac_digest.hexdigest()
          return hmac_hexdigest


          