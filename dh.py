from secrets import token_bytes
import hashlib
from client import Client
from server import Server

class DiffieHellman(object):
    def getSimulatedKey(self):
        g = 5
        p = 23
        
        a = Client().myPublicKeyForDH()
        b = Server().myPublicKeyForDH()

        A = pow(g, a) % p
        B = pow(g, b) % p

        S1 = pow(B, a) % p
        S2 = pow(A, b) % p

        key = hashlib.sha256(str(S1).encode()).digest()[:16]
        return key

