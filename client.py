

#Justin Swain
#09/30/2021

from socket import *


serverName="localhost" #IP address of host
serverPort=12000 #port used to identify server process
clientSocket=socket(AF_INET,SOCK_STREAM) #create socket using ip address and Stream
clientSocket.connect((serverName,serverPort)) # requests a connection to the server socket
loggedIn = False



#Register user, sends info to server
def register():
    action = "register"
    messageBytes=str.encode(action)
    clientSocket.send(messageBytes)
    userName = input("Please enter a username\n")
    messageBytes=str.encode(userName) #converting message to bytes
    clientSocket.send(messageBytes) #send to server
    password = input("Please enter a password\n")
    messageBytes = str.encode(password)
    clientSocket.send(messageBytes)
    message = clientSocket.recv(1024)
    message = message.decode()
    print(message)
    

def login():
    action = "login"
    messageBytes=str.encode(action)
    clientSocket.send(messageBytes)
    userName = input("Please enter a username\n")
    messageBytes=str.encode(userName) #converting message to bytes
    clientSocket.send(messageBytes) #send to server
    password = input("Please enter a password\n")
    messageBytes = str.encode(password)
    clientSocket.send(messageBytes)
    message = clientSocket.recv(1024)
    messageFromServer = message.decode()
    print(messageFromServer)

def main():

    userInput = ""
    while(userInput != "quit"):
        print("Welcome to Aristocrat's ticket purchasing service")
        print("Please enter a number for the following choices:")
        print("1. Register")
        print("2. Login")
        print("3. view events")
        print("4. purchase tickets")
        userInput = input("")
        if userInput == "quit":
            print("goodbye")
        else:
            try:
                userInput = int(userInput)
            except ValueError:
                print("You must enter a number!")
                print()
                
            else:
                if(userInput == 1):
                    register()
                
                elif(userInput == 2):
                    login()


main()
