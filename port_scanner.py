import socket

from datetime import datetime

target = input("Enter IP address scan: ").strip()

start_port = 1
end_port =  1024

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))  
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()


end_time = datetime.now()
print(f"\nScan completed in: {end_time - start_time}")