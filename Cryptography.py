class Crypto:
    alphabet = [" ", 'a', 'A', 'b', 'B', 'c', 'C',"ç","Ç", 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G',"ğ","Ğ", 'h', 'H', 'i', 'I',"i","İ", 'j', 'J',
                    'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O',"ö","Ö", 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S',"ş","Ş", 't', 'T', 'u',
                    'U',"ü","Ü", 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                    "#", "%", "!","-","+","}","[","]","_","@","{","<",">",".",",",":","?","(",")","*","+","^","=",";","£","$","¨","~","|"]
    def encrypt(secretText):
        alphabet=Crypto.alphabet
        """ encrypt """
        newSecretText = ""
        for indeX in secretText:
            if indeX in alphabet :
                indeks = alphabet.index(indeX)
                newSecretText += alphabet[indeks + 3]
        return newSecretText

        """ decrypt """
    def decrypt(newSecretText):
        alphabet = Crypto.alphabet
        oldSecretText = ""
        for indeX in newSecretText :
            if indeX in alphabet:
                indeks=alphabet.index(indeX)
                oldSecretText += alphabet[indeks - 3]
        return oldSecretText
