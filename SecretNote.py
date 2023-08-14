import tkinter
from tkinter import messagebox
from PIL import ImageTk , Image
import Cryptography

# -------------- INTERFACE --------------- #

""" window setting  """
window = tkinter.Tk()
window.geometry("750x750")
window.title("Secret Note")

""" image """
image=ImageTk.PhotoImage(Image.open("logo.png"))
label = tkinter.Label(window, image = image)
label.pack()

""" Title Label"""
FONT=("Arial",15,"bold")
titleLabel=tkinter.Label(text="Enter your title",font=FONT)
titleLabel.config(pady=30)
titleLabel.pack()

""" Title entry """
titleEntry=tkinter.Entry(width=100)
titleEntry.pack()

""" Secret Label """
secretLabel=tkinter.Label(text="Enter your secret",font=FONT)
secretLabel.config(pady=30)
secretLabel.pack()

""" Secret Text"""
secretText=tkinter.Text(width=75,height=10)
secretText.pack()

""" Master Label """
masterKey=tkinter.Label(text="Enter master key")
masterKey.config(font=FONT,pady=30)
masterKey.pack()

""" Master Entry"""
masterEntry=tkinter.Entry(font=FONT,width=50)
masterEntry.pack()


# -------------- EVENTS --------------- #

# ---------- ENCRYPT ----------- #

""" Save & Crypte button and save """
def clickToSaveEncrypt():
    titleText=titleEntry.get()
    secret_text=secretText.get("1.0",tkinter.END)
    cryptedText=Cryptography.Crypto.encrypt(secret_text)

    """ Oluşturulan dosyaya başlığı ve kriptolanmış içeriği yazdırır """
    master_text=masterEntry.get()
    master_text_cryptoded=Cryptography.Crypto.encrypt(master_text)

    if len(master_text) == 0 or len(titleText) == 0 or len(secret_text) -1  == 0:
        messagebox.showerror(title="Uyarı!", message="Bütün bilgileri doğru girdiğinizden emin olunuz !")
    else:
        messagebox.showinfo(title="Tebrikler", message="Dosyalarınız Başarıyla Kaydedildi!")

        with open ("requirement.txt","a") as file:
            file.write(titleText)
            file.write("\n")
            file.write(master_text_cryptoded)
            file.write(cryptedText)
            file.write("\n")

        titleEntry.delete(0,tkinter.END)
        masterEntry.delete(0,tkinter.END)
        secretText.delete("1.0",tkinter.END)

# ---------- DECRPYT ----------- #

def clickToDecrypt():
    master_text=masterEntry.get()
    secret_text = secretText.get("1.0", tkinter.END)
    masterTextLen=len(master_text)
    is_masterKey=""
    for i in range(masterTextLen):
        is_masterKey += Cryptography.Crypto.decrypt(secret_text[i])


    """ MASTER KEY CHECK  """
    if master_text == is_masterKey:
        secret_text=secretText.get("1.0",tkinter.END)
        decryptText=Cryptography.Crypto.decrypt(secret_text)
        decryptText2=""

        for x in range(len(decryptText)- len(is_masterKey)):
            decryptText2 += decryptText[masterTextLen+x]

        secretText.delete("1.0",tkinter.END)
        secretText.insert(tkinter.END,decryptText2)
    else:
        messagebox.showerror(title="Uyarı!",message="Bütün bilgileri doğru girdiğinizden emin olunuz !")


""" Save & Encrypt Button """
saveEncryptButton=tkinter.Button(text="Save & Encrypt",command=clickToSaveEncrypt,pady=10,width=15)
saveEncryptButton.pack()

""" Decrypt Button """
decryptButton=tkinter.Button(text="Decrypt",command=clickToDecrypt,pady=10,width=15)
decryptButton.pack()

window.mainloop()