from socket import *
import random

serverName="localhost"
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
messageFromClientBytes = ""
print("Server is ready to recieve")

def register(userName,password): #Write to user info to file
    try:
        file = open("userDB.txt","a")
        points = str(generatePoints())
        info = userName+" "+password
        file.write(info+" "+points+"\n")
        file.close()
        return True
    except FileNotFoundError:
        print("File could not be found")
        return False

    
def generatePoints(): #generate points for user
    return random.randrange(25,100)

def login(userName,password):
    
    with open("userDB.txt","r") as file:
        for line in file:
            line = line.split() #check line size
            print(line)
            if(line[0] == userName and line[1] == password):
                return True
        return False   

def main():
    while True:
        connectionSocket,clientAddress=serverSocket.accept()#accept connection
        messageFromClientBytes = ""
        while messageFromClientBytes != "quit" :
            messageFromClientBytes=connectionSocket.recv(1024)#recieve action to be completed
            messageFromClientBytes = messageFromClientBytes.decode()
            print(messageFromClientBytes)
            if messageFromClientBytes == "register":
                userName =connectionSocket.recv(1024)#recieve message
                userName = userName.decode()
                password=connectionSocket.recv(1024)#recieve message
                password = password.decode()
                registered = register(userName,password)
                if(registered):
                    message = "Registration successful"
                    messageBytes = str.encode(message)
                    connectionSocket.send(messageBytes)
                else:
                    message = "Registration unsuccessful"
                    messageBytes = str.encode(message)
                    connectionSocket.send(messageBytes)
            elif messageFromClientBytes == "login":
                userName =connectionSocket.recv(1024)#recieve message
                userName = userName.decode()
                password=connectionSocket.recv(1024)#recieve message
                password = password.decode()
                print(userName)
                print(password)
                loggedIn = login(userName,password)
                if loggedIn:
                    message = "sucessful login!"
                    messageBytes=str.encode(message)
                    connectionSocket.send(messageBytes)
                else:
                    message = "unsucessful login!"
                    messageBytes=str.encode(message)
                    connectionSocket.send(messageBytes)
                

        connectionSocket.close()
        break

main()
