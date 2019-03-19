
#Name: Hari Hara Kummi Nakashatrala
import socket
import random
import time
from tkinter import *

#server host and port number
host = '127.0.0.1'
port = 80
#socket properties defined with inbuilt methods
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#creating TK inter
display = Tk()
display.title("Client")
display.geometry("300x300")
#create a text box to display the messages
tempp = Message(display, text="")


#declaring the global variables
post = "POST /"
http = "HTTP/1.1 \n"
#mentioned about all the HTTP formats in the requests between client and server
#HTTP formats decsribed here as per the problem statement
host_name = "Host:" + str(host) +"\n"
user_agent = "User-Agent: Python/3.6 + \n"
content_type = "text/html \n"

#function to generate random numbers between 5 to 15 and send to server
def random_generator(mess):
    try:
        #sending random nunber post to the server
        random_number = random.randint(5, 15)
        random_number_str = str(random_number)
        random_number_header = post + random_number_str + http + host_name + user_agent + content_type + str(len(bytes(random_number_str, 'utf-8')))
        print(random_number_header + "\n")
        skt.send(bytes(random_number_header, 'utf-8'))
        #mess["text"] = mess["text"] + random_number_str +"\n"

        #waiting for the response from the server
        server_response_bytes = skt.recv(1024)
        #after a while we get the response from client send the response message to the client
        server_response = server_response_bytes.decode('utf-8')
        print(server_response)
        response_after_post = server_response.split('POST /')[1]
        response = response_after_post.split('HTTP/1.1')[0]
        #print the responses in the tkinter window
        print(response)
        mess["text"] = mess["text"] + response + "\n"
        val = int(random_number_str) * 100
        #evaluvate the random numbers and stop the processes based on it
        temp = "true"
        display.after(val, random_generator, mess)
    except:
        print("disconnected from the server")

#this function helps to close the client window in the tkinter gui
def close_connection():
    q = "quit"
    #send all the quitting ,essage to the server
    quit_mess = post + q + http + host_name + user_agent + content_type + str(len(bytes(q, 'utf-8')))
    print(quit_mess)
    #send the close messages to the server
    skt.send(bytes(quit_mess, 'utf-8'))
    skt.close()
    display.quit()


#client connecting to server
try:
    skt.connect((host, port))

except:
    print("Unable to connect to the server on given port")

#message box in the server
message = Message(display, text="Connected to the server")
message.pack()
#appends username to the client server
username_header_bytes = skt.recv(1024)
username_header = username_header_bytes.decode('utf-8')
print(username_header)
after_rec = username_header.split('GET /')[1]
username_request = after_rec.split('HTTP/1.1')[0]
if username_request == "Username ":
    #Sending username header to the server
    my_name = str(skt.getsockname()[1])
    my_name_bytes = bytes(my_name, 'utf-8')
    username_sending_header = "HTTP/1.1 200 OK \n Content-type: text/html \n Content-length: " + str(len(my_name_bytes)) + "\n "
    print(username_sending_header)
    skt.send(bytes(username_sending_header, 'utf-8'))
    #sending username to server
    skt.send(bytes(my_name, 'utf-8'))
#initialise buttons in the window
button = Button(display, text="exit", command=close_connection)
button.pack()
teeeemp = "true"
random_generator(message)
display.mainloop()





