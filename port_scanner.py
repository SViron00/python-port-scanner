import socket
from datetime import datetime

common_ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3",
    143: "IMAP", 443: "HTTPS", 465: "SMTPS", 587: "SMTP",
    993: "IMAPS", 995: "POP3S", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 8080: "HTTP-Proxy"
}

target = input("Enter IP address to scan: ").strip()

start_port = 1
end_port = 1024

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

open_ports = 0
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        service = common_ports.get(port, "Unknown")
        print(f"[+] Port {port} is OPEN - Service: {service}")
        open_ports += 1
    s.close()

end_time = datetime.now()
scan_time = end_time - start_time

print(f"\nScan completed in: {scan_time}")
print(f"Found {open_ports} open port(s)")