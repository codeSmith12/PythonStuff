import socket
from _thread import *
import sys
from player import Player
import pickle

server = "192.168.1.14"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started.")

players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))]

def threadedClient(connection, player):
    print("Sending connection.")
    connection.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:

            data = pickle.loads(connection.recv(2048))
            players[player] = data
            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received:", data)
                print("Sending:", reply)
            connection.sendall(pickle.dumps(reply))
        except:
            print("Breaking because exception made. Error..")
            break

    print("Lost connection")
    connection.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threadedClient, (conn, currentPlayer))
    currentPlayer += 1
