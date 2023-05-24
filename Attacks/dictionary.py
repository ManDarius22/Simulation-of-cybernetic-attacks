from tqdm import tqdm
import pyzipper

isFound = False
file="2.jpg"


def printName(zipFile):
    with pyzipper.AESZipFile(zipFile) as f:
        for name in f.namelist():
            print(name)

def attack(zipFile,wordList):
    total = len(list(open(wordList,"rb")))
    print("Total password to test:- ", total)
    print("\n")
    with pyzipper.AESZipFile(zipFile)as f:
        with open(wordList,"rb") as wordList:
            for word in tqdm(wordList, total=total,unit="word"):
                password = word.decode(errors="ignore").strip()
                try:
                    f.extract("3.jpg",pwd=password.encode('UTF-8'))
                except:
                    continue
                else:
                    isFound = True
                    break
            if isFound:
                print("\n[*] Password Found:- ",word.decode().strip())
            else:
                print("\n[!] Password not found!")




attack("test.zip","rockyou.txt")


