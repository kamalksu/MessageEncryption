from flask import Flask, render_template, request, url_for, flash, redirect
from Crypto.Cipher import AES
from dh import DiffieHellman
from client import Client
from server import Server

app = Flask(__name__)

@app.route('/',  methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        textToEncrypt = request.form['textToEncrypt']
        
        # get shared key from Diffie Hollman 
        key = DiffieHellman().getSimulatedKey()
        
        # encrypt message in client 
        ciphertext, nonce, tag =  Client().encrypt(textToEncrypt, key)
        
        # decrypt message in server 
        plainText = Server().decrypt(ciphertext, nonce, key)

        # hmac message authentication. 
        hmac_digest = Client.hmac_digester(textToEncrypt, key)
        hmac_auth = Server.hmac_compare_digest(textToEncrypt, key, hmac_digest)

        
        return render_template('server.html', ciphertext=ciphertext,  plainText=plainText.decode(), key = key, hmac_auth=hmac_auth )
    return render_template('index.html')

