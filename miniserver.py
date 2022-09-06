
class Server:
    ipo = 0

    def __new__(cls, *args, **kwargs):
        cls.ipo += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = self.ipo
        self.buffer = []

    def send_data(self, data):
        self.router.buffer += [data]

    def get_data(self):
        output = []
        for i in range(len(self.buffer)):
            output.append(self.buffer.pop())
        return output

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.servers = {}
        self.buffer = []

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        del self.servers[server.ip]

    def send_data(self):
        for pocket in self.buffer:
            if pocket.ip in self.servers:
                self.servers[pocket.ip].buffer += [pocket]
        self.buffer.clear()


class Data:
    def __init__(self, msg, dist):
        self.data = msg
        self.ip = dist
