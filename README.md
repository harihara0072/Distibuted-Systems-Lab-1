# Distibuted-Systems-Lab-1

<b>Language used </b>:
Python 3.7

<b>Libraries used</b>:
Tkinter,
Threading,
Socket


<b>Server.py</b>
1. Created a socket in the server by giving the host name and port number
2. Server will be continuously listening for the clients
3. Once a client is connected then the server sends a HTTP GET request to the client asking for the username
4. Once we get the response from the client then it will create a new thread.
5. The server will receive the random integer from the client
6. Server will then wait for that time and responds to the client saying that it has waited for that time.
7. Sever will keep on doing this until client stops sending the number.

<b>Client.py:</b>
1. The client will connect to the server socket by using server hostname and port number.
2. Then the client will receive the HTTP GET request for the username and client will respond to it.
3. Then a random integer between 5 and 15 will be generated and send it to client using HTTP POST method.
4. The client will wait for the server to respond and once it receives the response then it will generate and send a new random number to server until the user quits the program using the quit button in the gui.

<b>Code running structure:</b>
python server.py

python client.py(3 times)
