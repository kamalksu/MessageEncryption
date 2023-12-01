from Crypto.Cipher import AES
import hashlib
import hmac

class Server(object):
    def myPublicKeyForDH(self):
          return 3
    def decrypt(ciphertext, nonce, key):
          #.textToEncryptByte = bytes(textToEncrypt, 'utf-8')
          cipher = AES.new(key, AES.MODE_EAX, nonce)
          
          plainText = cipher.decrypt(ciphertext, key)    
          return plainText 
             
    def hmac_compare_digest(textToEncrypt, key, hmac_digester_old):
          textToEncryptByte = bytes(textToEncrypt, 'utf-8')
          hash = hashlib.sha256
          hmac_digest = hmac.new(key,textToEncryptByte,hash)
          hmac_digester_new =  hmac_digest.hexdigest()
          return hmac.compare_digest(hmac_digester_new,hmac_digester_old)


        
