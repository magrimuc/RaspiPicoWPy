import socket

def putFile():
    # Initialize Socket Instance
    sock = socket.socket()
    print ("Socket created successfully.")

    # Defining port and host
    port = 8800
    host = 'mgrillo.de'

    # Connect socket to the host and port
    sock.connect((host, port))
    print('Connection Established.')
    # Send a greeting to the server
    # sock.send('A message from the client'.encode())

    # Write File in binary
    file = open('server-file.txt', 'rb')
    line = file.read(1024)
    # Keep sending data to the client
    while(line):
        sock.send(line)
        line = file.read(1024)

    print('File has been sent successfully.')

    file.close()
    sock.close()
    print('Connection Closed.')














