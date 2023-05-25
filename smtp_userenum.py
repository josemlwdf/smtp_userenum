#!/usr/bin/python3

import socket
import sys
import threading

def verify_username(username, target_ip):
    # Create a Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the Server
    connect = s.connect((target_ip, 25))

    # Receive the banner
    banner = s.recv(1024)
    print(banner)

    # VRFY a user
    user = username.encode()
    s.send(b'VRFY ' + user + b'\r\n')
    result = s.recv(1024)

    if b"250" in result:  # User exists
        print(username)

    # Close the socket
    s.close()

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <username or file> <target_ip>")
    sys.exit(0)

target_ip = sys.argv[2]

# Check if the second argument is a file
if sys.argv[1].endswith('.txt'):
    usernames_file = sys.argv[1]
    try:
        with open(usernames_file) as file:
            usernames = file.read().splitlines()
    except IOError:
        print(f"Error: Failed to read usernames file '{usernames_file}'")
        sys.exit(0)

    threads = []
    for username in usernames:
        thread = threading.Thread(target=verify_username, args=(username, target_ip))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

else:
    username = sys.argv[1]
    verify_username(username, target_ip)
