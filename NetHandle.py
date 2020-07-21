import socket

NetSocket = socket.socket()


class NetTransmit():
    DefaultData = b'\xff\xee\xff\xff\xff\xff\xff\xff\xff\xff\xff\xef\xfe'

    def Init(self,HOST:str='127.0.0.1', PORT:int=9000):
        Address=(HOST, PORT)
        NetSocket.connect(Address)

    def Send(self,Data:bytes=DefaultData):
        NetSocket.send(Data)

    def Receive(self,DataLength:int=1024):
        Data = NetSocket.recv(DataLength)
        return Data

    def DeInit(self):
        NetSocket.shutdown(2)
        NetSocket.close()
