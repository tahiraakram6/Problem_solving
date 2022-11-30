############# CAESAR-CIPHER PROGRAM ###########

def ceaser_cipher(word,shift):
    result = ""
 
    for i in range(len(word)):
        char = word[i]
        
        if (char == " "):
            result += chr(ord(char))
       
        elif (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
    
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
 
    return result
 
while(True):
    word =input("Enter the message:")
    shift = int(input("Enter the shift code:"))
    print ("Text  : " + word)
    print ("Shift : " + str(shift))
    print ("Cipher: " + ceaser_cipher(word,shift))