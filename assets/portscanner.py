import socket

def scan(target, ports):
    print('\n' + ' Starting scan for ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass

def start():
    targets = input("[*] Enter Targets to scan: ")
    ports = int(input("[*] Number of Ports to scan[blank = all]: "))
    if ports is None:
        ports = 65535
        
    try: 
        print("[*] Scanning multiple targets...")
        for ip_addr in targets.split(',', ' '):
            scan(ip_addr(' '), ports)
    except:
        scan(targets, ports)
