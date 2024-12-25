# Python Project 4
# Caesar Cipher

def encrypt(message, shiftkey):
    m = list(message)
    cipher = []
    c = ""
    for i in range(len(m)):
        if m[i] in alphabets:
            x = alphabets.index(m[i])
            e = (x + shiftkey) % 26
            cipher.append(alphabets[e])
        else:
            cipher.append(m[i])
    for i in cipher:
        c += i
    print(f"Encrypted result: {c}")

def decrypt(message, shiftkey):
    m = list(message)
    p = ""
    plain = []
    for i in range(len(m)):
        if m[i] in alphabets:
            x = alphabets.index(m[i])
            e = (x - shiftkey) % 26
            plain.append(alphabets[e])
        else:
            plain.append(m[i])
    for i in plain:
        p += i
    print(f"Decrypted result: {p}")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = False

while not c:
    a = input("Type 'encrypt' for encryption, and 'decrypt' for decryption: ").lower()
    if(a!='encrypt' or a!='decrypt'):
        print("Type 'encrypt' or 'decrypt' correctly\n ")
        a = input("Type 'encrypt' for encryption, and 'decrypt' for decryption: ").lower()
    b = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    
    if a == "encrypt":
        encrypt(b, shift)
    elif a == "decrypt":
        decrypt(b, shift)
    
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    c = choice != 'yes'

print("Goodbye")
