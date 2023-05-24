import random
import pyautogui
import string


chars ="abcdefghijklmnopqrstuvwxyz0123456789"
#chars = string.printable toate caracterele posibile dar necesita mai mult timp
chars_list= list(chars)

password = pyautogui.password("Introduceti o parola: ")

quess_password=""
i=0

while(quess_password != password):
    quess_password = random.choices(chars_list, k=len(password))
    print("##########"+ str(quess_password)+"##########")
    i=i+1

    if(quess_password == list(password)):
        print("Password is: "+ "".join(quess_password))
        print("Numar incercari: ",i)
        break
