from Crypto.Cipher import AES
import hashlib
import hmac

class Server(object):
    def myPublicKeyForDH(self):
          return 3
    
    def decrypt(self, ciphertext, nonce, key):   
          cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
          plaintext = cipher.decrypt(ciphertext)
          return plaintext
       
    def hmac_compare_digest(textToEncrypt, key, hmac_digester_old):
          textToEncryptByte = bytes(textToEncrypt, 'utf-8')
          hash = hashlib.sha256
          hmac_digest = hmac.new(key,textToEncryptByte,hash)
          hmac_digester_new =  hmac_digest.hexdigest()
          return hmac.compare_digest(hmac_digester_new,hmac_digester_old)


        
