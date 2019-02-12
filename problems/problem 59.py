print("Starting")

def decrypt(message,key):
    newMessage = []
    for i in range(0,len(message)):
        newMessage.append(message[i] ^ key[i%3])
    return newMessage

def containsSubList(sub,big):
    for i in range(0,len(big)- len(sub)+1):
        if big[i] == sub[0]:
            found = True
            for k in range(1,len(sub)):
                if big[i+k] != sub[k]:
                    found = False
                    break
            if found:
                return True
    return False

def toLetters(message):
    newMessage = ""
    for i in message:
        newMessage += chr(i)
    return newMessage

file = open("cipher1.txt")
message = []
for line in file:
    line = line.strip()
    tokens = line.split(',')
    for i in tokens:
        message.append(int(i))

the = [32, 116, 104, 101, 32]
it =  [32, 105, 116]
# " the " -> 32 116 104 101 32
# " it" -> 32 105 116
# "a" -> 97
# "z" -> 122
      
goodMessage = []
for i in range(97,123):
    key = [i,0,0]
    print(i)
    for j in range(97,123):
        key[1] = j
        for k in range(97,123):
            key[2] = k
            newMessage = decrypt(message,key)
            if containsSubList(the,newMessage):
                goodMessage = newMessage
                print(toLetters(goodMessage))
                print(sum(goodMessage))

input("Done")

            

