import select
import socketserver
import threading
from queue import Queue


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """A threaded tcp request handler
    """

    def handle(self):

        """ The handle function.

            Reads data from the client as long as the server is not requested to close.
            Sends the read data back to the client and stores it in a queue.
        """
        while self.server.instance.keep_alive:
            ready_read, ready_write, exceptional = select.select([self.request], [], [], 1)

            for sock in ready_read:
                if sock == self.request:
                    recv_msg = sock.recv(self.server.instance.receive_bytes)
                    if recv_msg is not None:
                        self.request.sendall(recv_msg)
                        self.server.instance._add(recv_msg)


class EchoServer:
    socketserver.TCPServer.allow_reuse_address = True
    """A threaded tcp server

    Attributes
    ----------
    ip : str
        The ip address of the tcp server.
    port : int
        The port of the tcp server.
    bytes_to_receive : int, default 4096
        Reads the number bytes from the socket. Returns fewer bytes than bytes_to_receive if fewer are available.
    """
    def __init__(self, ip, port, receive_bytes=4096):
        self.server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server.socket.setblocking(False)
        self.server.instance = self
        self.keep_alive = False
        self.receive_bytes = receive_bytes
        self._last_received = Queue(maxsize=1)

    @property
    def last_received(self):
        """bytes: Returns the last received message."""
        return self._last_received.get()

    def start_server(self):
        """ Starts the tcp server.
        """
        self.keep_alive = True
        self.server_thread.start()

    def stop_server(self):
        """ Stops the tcp server.
        """
        self.keep_alive = False
        self.server.shutdown()
        self.server.server_close()

    def _add(self, message):
        if not self._last_received.full():
            self._last_received.put(message)
        else:
            self._last_received.get_nowait()
            self._last_received.put(message)
