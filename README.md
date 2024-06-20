## File Transfer

This project allows you to send and receive files over a local network using TCP sockets in Python. 

### Functionality:

* **send.py:**
    * Opens a file specified by `file_path`.
    * Connects to a receiver on a specified IP address and port number.
    * Sends the entire file content to the receiver.
    * Prints a confirmation message upon successful transfer.
* **receive.py:**
    * Listens for incoming connections on a specified port.
    * Accepts a connection from a sender.
    * Checks if a file named "received.json" exists, creates an empty one if not. 
    * Receives data from the sender in chunks and appends it to "received.json".
    * Prints a confirmation message upon receiving the data.


### Usage:

1. **Edit `send.py`:**
    * Replace `file_path` with the path to the file you want to send.
    * Replace `HOST` with the IP address of the receiver machine. 
2. **Edit `receive.py` (Optional):**
    * You can modify the `PORT` number in both scripts if needed to avoid conflicts.
3. **Run the scripts:**
    * Start the **receiver** script (`receive.py`) on the machine that will receive the file.
    * Run the **sender** script (`send.py`) on the machine that has the file to send. 

**Note:** Both machines need to be on the same local network for this to work.


### Security Considerations:

This is a basic file transfer example and doesn't implement any security features. Be cautious when using it on untrusted networks.


### Additional Notes:

* The buffer size in `receive.py` is set to 1024 bytes. You might need to adjust this based on the size of the files you are transferring.
* The receive script currently assumes the received data is JSON. You can modify it to handle different file formats.


I hope this helps!