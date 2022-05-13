import socket
import time
import threading
import datetime

WAIT_SECONDS = 30

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

def keepalive():
    dateData="{\"ApiCommands\": 6,\"KeepAliveDate\":\" "+ '{0}'.format(datetime.datetime.strptime(time.ctime(), "%c")    ) +"\"}" + chr(11)
    #print(dateData)
    clientSocket.send(dateData.encode())
    threading.Timer(WAIT_SECONDS, keepalive).start()

def matriksIqTest():

    try:
        clientSocket.connect(("127.0.0.1", 18890))
        data = "{\"ApiCommands\": 0}" + chr(11)
        keepalive()
        clientSocket.send(data.encode())

        while True:
            try:
                dataFromServer = clientSocket.recv(1024)
                print(dataFromServer.decode())
            except BlockingIOError:
                print("BlockingIOError")
            except ConnectionResetError:
                print("ConnectionResetError")
            except socket.timeout as e:
                print(e)
    except:
        print("An exception occurred")






