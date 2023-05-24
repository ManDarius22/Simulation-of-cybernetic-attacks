from cryptography.fernet import Fernet
import os
import glob

with open("key.key", "rb") as kf:
    key = kf.read()
fernet = Fernet(key)
director = 'D:\Scoala\SSI\Dictionary\cript'
files = glob.glob(f'{director}\\**\\*.*', recursive=True)


for file in files:
    try:
        with open(file,"rb") as tf:
            tf_bytes = tf.read()
    except:
        pass
    try:
        tf_bytes_dec= fernet.decrypt(tf_bytes)
    except Exception as e:
        print("Error in decryption process: ", file, "is", e)
        pass
    with open(file,"wb") as tf:
        tf.write(tf_bytes_dec)
        
