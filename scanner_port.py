import socket


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lower_port, upper_port):
        for port in range(lower_port, upper_port + 1):
            if self.is_open(port):
                self.add_port(port)
                print('Port is open: {}'.format(port))
            else:
                print('Port is closed: {}'.format(port))

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def write(self, filepath):
        open_port = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(open_port))


def main():
    print("Enter IP address in format xxx.xxx.xxx.xxx: ")
    ip = input()
    print("Enter start port from 1: ")
    start_port = int(input())
    print("Enter end port up to 65535: ")
    end_port = int(input())
    scanner = Scanner(ip)
    scanner.scan(start_port, end_port)
    scanner.write('./open_ports')


if __name__ == '__main__':
    main()
