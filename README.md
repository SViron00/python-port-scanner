# Python Port Scanner 🔍

This is a simple TCP port scanner built using Python's `socket` module.  
It scans a target host and reports open ports in the specified range.

## How to Use

1. Make sure Python 3 is installed.
2. Run the script (either way):
   ```bash
   python port_scanner.py
   
   py port_scanner.py

3. Enter Targer IP, (e.g, 127.0.0.1, scanme.nmap.org), use scanme.nmap.org if your laptop doesn't have any ports.
    Example output:
    ```bash
    Scanning 127.0.0.1 from port 1 to 1024...
   
    [+] Port 22 is OPEN
    [+] Port 80 is OPEN
    
    Scan completed in: 0:00:01.234
