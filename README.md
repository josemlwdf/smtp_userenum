# smtp_userenum

## Script Description

The provided script is a Python program designed to verify the existence of a given username on a target email server using the VRFY command. The script utilizes sockets to establish a connection with the target server, send commands, and receive responses.

The script can be run from the command line and accepts two arguments: the username or a file containing a list of usernames, and the target IP address of the email server. If a single username is provided as the first argument, the script will attempt to verify that specific username. If a file with a ".txt" extension is provided as the first argument, the script will read the file and verify each username listed within it.

The script creates a separate thread for each username verification to allow for concurrent processing, enhancing efficiency. It utilizes the threading module to manage the threads and ensure they complete before the script exits.

## Usage

To use the script, execute it from the command line using the following format:

    python smtp_userenum.py <username or file> <target_ip>

``Replace script.py with the name of the script file.

The first argument, <username or file>, should be either a single username or a text file containing a list of usernames to be verified. If a file is used, it should have a ".txt" extension.``

The second argument, <target_ip>, should be the IP address of the target email server.

Ensure that you have the necessary permissions to execute the script and that Python is installed on your system.

## Example Usages

Verify a single username:

    python smtp_userenum.py john.doe@example.com 192.168.0.1

Verify multiple usernames from a file:

    python smtp_userenum.py usernames.txt 192.168.0.1


## Important Note

It's worth noting that the VRFY command may not be supported by all email servers due to security and privacy concerns. The script should be used responsibly and only on servers where you have proper authorization.
