class ClientError(Exception):
    pass


class ClientSocketError(ClientError):
    pass


class ClientProtocolError(ClientError):
    pass


class ClientTimeoutError(ClientError):
    pass
