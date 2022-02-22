import socket
from _thread import *
import sys
from player import Player
import pickle
from game import Game

server = "192.168.1.14"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started.")

connected = set()
games = {}
idCount = 0


def threadedClient(connection, player, gameId):
    global idCount
    connection.send(str.encode(str(p)))
    reply = ""

    while True:
        try:
            data = connection.recv(4096*4).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetLocked()
                    elif data != "get":
                        game.play(p, data)
                    # reply = game
                    conn.sendall(pickle.dumps(game))

            else:
                break
        except:
            print("Error in threadedClient")
            break

    try:
        print("Lost connection, closing gameId =", gameId, "by player id =", player)
        del games[gameId]
    except:
        print("Failed to delete game.")
        pass
    idCount -= 1
    connection.close()
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2 #integer divide

    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating new game...")
    else:
        games[gameId].ready = True
        p = 1



    start_new_thread(threadedClient, (conn, p, gameId))
