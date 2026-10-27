import socket
ports_to_scan = [21, 22, 80, 443, 8080]
server_ip = "127.0.0.1"
print(f"--- Starting Server Port Scan on {server_ip} ---")
for port in ports_to_scan:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1.0)

	result = sock.connect_ex((server_ip, port))

	if result == 0:
		print(f"Port {port}: OPEN (Service Running!)")
	else:
		print(f"Port {port}: CLOSED")
	sock.close()
