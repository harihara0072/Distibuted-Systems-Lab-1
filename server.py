
#Name: Hari Hara Kummi Nakshatrala
#import all the packages
import socket
from threading import Thread
from tkinter import *
import time
import datetime

#global variables declaration
host = ''
port = 80
#global declaration of http format messages
post = "POST /"
http = "HTTP/1.1 \n"
host_name = "Host:" + str(host) +"\n"
user_agent = "User-Agent: Python/3.6 + \n"
content_type = "text/html \n"

#creating socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket and the port
skt.bind((host, port))
skt.listen(5)

#tk inter window

display = Tk()
display.title("Server")
display.geometry("500x500")
#message boxes in the tkinter
message = Message(display, text="")
message.pack()
#message box initailaisation
#thread method
def client_thread(client, c_ip, c_skt):
    # requesting client for the username
    get_username_str = "GET /Username HTTP/1.1 \n Host: 127.0.0.1 " + "\n UserAgent: Python/3.6"
    print(get_username_str)
    message["text"] = message["text"] + get_username_str
    client.send(bytes(get_username_str, 'utf-8'))

    #receiving the username header
    username_header_bytes=client.recv(1024)
    username_header = username_header_bytes.decode('utf-8')
    #send the messages to the client
    message["text"] = message["text"] + username_header + "\n"
    #print("Username header:")
    print(username_header)
    username_bytes = client.recv(1024)
    username = username_bytes.decode('utf-8')
    #decode the messages from the client to the server
    print(username)
    print("Connected to client: " + username)
#create a infinete while loop to keep the connection live to accept any client request
    while True:
        #receiving the random number header
        #print("while")
        rand_number_header_bytes = client.recv(1024)
        #print(rand_number_header_bytes)
        rand_number_header = rand_number_header_bytes.decode('utf-8')
        message["text"] = message["text"] + rand_number_header + "\n"
        print("this is received" + rand_number_header)
        #random number split in the messages
        rand_after_post = rand_number_header.split('POST /')[1]
        random_number = rand_after_post.split('HTTP/1.1')[0]
#if we get quit message from the client close the gui
        if random_number == "quit":
            client.close()
            break

        else:
            #sleeping for the random time
            print("Server is waiting for " + random_number)
            message["text"] = message["text"] + "Server waiting " + random_number + " sec for client " + username + "\n"
            time.sleep(int(random_number))
            print("waited for " + random_number)
            #sending response to the client
            str1 = "Server waited for " + random_number + " sec "
            #append all the messages to the response header in the gui window
            response_header = post + str1 + http + host_name + user_agent + content_type + "Content-length: " + str(len(bytes(str1, 'utf-8'))) + "\n"
            print(response_header)
            message["text"] = message["text"] + response_header + "\n"
            client.send(bytes(response_header,'utf-8'))
#create a thread to handle multiple client requests
def create_thread():
    client, (client_ip, client_socket) = skt.accept()
    #append the messages while creating a thread
    message["text"] = message["text"] + "Server connected to client: " + str(client_socket)
    t = Thread(target=client_thread, args=(client, client_ip, client_socket))
    t.start()


#main method
def main():
    print("waiting for connection")
    create_thread()
    #createa a thread
    display.after(200, create_thread)
    display.mainloop()
#display messgaes in the gui window of tkinter

if __name__ == '__main__':
    main()

#main loop to instantiate the main function
