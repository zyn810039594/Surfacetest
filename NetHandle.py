import socket
import binascii



class NetTransmit:
    defaultNetsocket = None
    DefaultData=b'\xe8\xaf\xad\xe8\xa8\x80\xe4\xb8\xad\xe6\x96\x87\xe7\xbd\x91\xe5\xb2\x81\xe4\xba\x86'
    def Net_Init(HOST='127.0.0.1',PORT = 9000):
        ADDRESS = (HOST, PORT)
        defaultNetsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        defaultNetsocket.connect(ADDRESS)
        return defaultNetsocket

    def Net_Send(Data=DefaultData, NetSocket=defaultNetsocket):
        if NetSocket:
            NetSocket.send(Data)

    def Net_Receive(DataLength=1024,NetSocket=defaultNetsocket):
        if NetSocket:
            Data=NetSocket.recv(DataLength)
            return Data

    def Net_DeInit(NetSocket=defaultNetsocket):
        if NetSocket:
            NetSocket.close()







