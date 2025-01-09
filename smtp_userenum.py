#!/usr/bin/python3

import socket
import sys
import threading

# GLOBALS
threads = []
max_threads = 10
exiting = False

def verify_username(username, target_ip):
    # Create a Socket
    global exiting
    if exiting: return
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the Server
    connect = s.connect((target_ip, 25))

    # Receive the banner
    banner = s.recv(1024)

    # VRFY a user
    user = username.encode()
    s.send(b'VRFY ' + user + b'\r\n')
    result = s.recv(1024)

    if b"250" in result:  # User exists
        print(username)
    elif b"252" in result:  # User exists
        print(username)
    elif b"450" in result:  # User exists
        print(username)
    elif b"503" in result
        if exiting: return
        print("[-] 503 SMTP error code. Need to authenticate")
        exiting = True
        sys.exit()

    # Close the socket
    s.close()

def join_threads():
    global threads
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    threads = []

def usage():
    print(f"Usage: {sys.argv[0]} <username or file> <target_ip>")
    sys.exit(0)

if len(sys.argv) < 3:
    usage()

target_ip = sys.argv[2]

# Check if the second argument is a file
if sys.argv[1].endswith('.txt'):
    usernames_file = sys.argv[1]
    try:
        with open(usernames_file) as file:
            usernames = file.read().splitlines()
    except IOError:
        print(f"Error: Failed to read usernames file '{usernames_file}'")
        usage()

    print("[!] Beginning Enumeration")
    print(f"[!] {len(usernames)} usernames to test")

    for username in usernames:
        thread = threading.Thread(target=verify_username, args=(username, target_ip))
        if exiting: break
        thread.start()
        threads.append(thread)

        count = len(threads)
        if count >= max_threads:
            join_threads()

else:
    username = sys.argv[1]
    verify_username(username, target_ip)
