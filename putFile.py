import socket

def putFile():
# Initialize Socket Instance
    sock = socket.socket()
    print ("Socket created successfully.")
    
    # Defining port and host
    port = 8800
    host = '5.230.70.234'
    ##host = 'localhost'
    
    # Connect socket to the host and port
    sock.connect((host, port))
    print('Connection Established.')
    # Send a greeting to the server
    sock.send('Hallo  '.encode())
    
    # file read
    file = open('cfile.txt', 'rb')
    line = file.read(1024)
    # file send
    while(line):
        sock.send(line)
        line = file.read(1024)
    
    print('File has been received successfully.')
    
    file.close()
    sock.close()
    print('Connection Closed.')
    