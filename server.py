###################################################################
#References:
#https://docs.python.org/2/library/socket.html
#https://stackoverflow.com/questions/21153262/sending-html-through-python-socket-server
#http://blog.wachowicz.eu/?p=256
#https://www.thoughtco.com/building-a-simple-web-server-2813571
#https://elearn.uta.edu/bbcswebdav/pid-7205400-dt-content-rid-132005341_2/courses/2185-COMPUTER-NETWORKS-54684-003/Programming%20Assignment%201_reference_Python.pdf
#https://stackoverflow.com/questions/32168871/tkinter-with-multiple-threads
#https://stackoverflow.com/questions/42222425/python-sockets-multiple-messages-on-same-connection
#https://www.programcreek.com/python/example/105552/tkinter.Message
#https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
#https://scorython.wordpress.com/2016/06/27/multithreading-with-tkinter/
#https://docs.python.org/3/tutorial/classes.html
#https://stackoverflow.com/questions/46788776/update-tkinter-widget-from-main-thread-after-worker-thread-completes
#https://stackoverflow.com/questions/3567238/threaded-tkinter-script-crashes-when-creating-the-second-toplevel-widget
#https://stackoverflow.com/questions/10556479/running-a-tkinter-form-in-a-separate-thread/10556698#10556698
#https://bugs.python.org/issue11077
#https://github.com/dojafoja/GUI-python-server/blob/master/server.py
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
#https://www.geeksforgeeks.org/python-gui-tkinter/
#https://stackoverflow.com/questions/9342757/tkinter-executing-functions-over-time
#https://stackoverflow.com/questions/9776718/how-do-i-stop-tkinter-after-function
#https://stackoverflow.com/questions/49432915/how-to-break-out-of-an-infinite-loop-with-a-tkinter-button
#https://stackoverflow.com/questions/49742217/python-socket-threading-tkinter-how-to-know-the-message-sender
###################################################################

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