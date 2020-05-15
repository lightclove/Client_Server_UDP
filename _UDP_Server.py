# from
# https://docs.python.org/3/library/socketserver.html#module-socketserver
import socket

# IP = "127.0.0.1"
# PORT = 20001
# RESPONSE = "RESPONSE FROM SERVER:"
# serve(IP='192.168.13.117',PORT=20001,CLIENT_IP='127.0.0.1',CLIENT_PORT=20001,RESPONSE="\"SERVER's response\"")
# serve(IP='127.0.0.1',PORT=20001,CLIENT_IP='127.0.0.1',CLIENT_PORT=20001,RESPONSE="\"SERVER's response\"")

import socketserver


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)

    # Listen for incoming datagrams and sending response

    @staticmethod
    def serve(IP, PORT, CLIENT_IP, CLIENT_PORT, RESPONSE):
        # Create a datagram socket
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        UDPServerSocket.bind((IP, PORT))
        print("UDP server up and listening on ip: " + str(IP) + " and port: " + str(PORT))
        while (True):
            bytesAddressPair = UDPServerSocket.recvfrom(1024)
            if not bytesAddressPair:
                break
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]
            print(RESPONSE)
            print(CLIENT_IP)
            # print(clientIP)
            bytesToSend = str.encode(RESPONSE)
            print('Getting message from client: \"' + str(message) + '\"')
            # Sending a reply to client
            UDPServerSocket.sendto(bytesToSend, address)
            print('Sending response message:\"' + RESPONSE + '\" to client\'s to port: ' + str(
                CLIENT_PORT) + ' and ip address: ' + str(CLIENT_IP))
        UDPServerSocket.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
