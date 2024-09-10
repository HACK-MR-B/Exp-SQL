# Exp-SQL

This tool helps check database errors by trying to access specific paths present in a wordlist file on a specific server using the HTTP protocol. The tool sends GET requests to the server and checks for responses that contain the status code 200 (OK Libraries used:

os: Used to handle system files, such as opening files and reading paths.
requests: Used to send HTTP requests to the server to check for valid endpoints.
sys: Used to interact with standard inputs and outputs, such as typing to the console.
time: It is used to delay execution and track the time during the execution of operations.
Threading: Used to create and perform multiple tasks at the same time, such as displaying animated messages without stopping the primary execution of the tool.
prompt_toolkit: A library used to provide an interactive user interface with support for auto-completion of file paths using PathCompleter.
colorama: Used to add colors to text on the command line to make the output clearer and more attractive.

How to use the tool:

When you run the tool, an animated welcome message will appear with the phrase “HACK Mr : B” displayed in red.
The user is required to enter the IP address of the target server.
Next, the user is asked to enter the path to the wordlist file (which contains a list of paths to scan).
Once the input is provided, the tool scans each path in the wordlist file and sends an HTTP request to check if the endpoint exists or not.
Valid paths (that get a 200 OK response) are displayed on the command line

    sudo python3 Exp-SQL.py

    Please enter the IP address ==>> 192.168.100.5

    Please enter the path to your wordlist file ==>> /usr/share/wordlists/dirb/common.txt

    HACK Mr : B

The tool will start searching for valid paths and display the results:

     Found valid endpoints (200 OK):
     http://192.168.100.5/admin
     http://192.168.100.5/login

I wish you happy hacking
