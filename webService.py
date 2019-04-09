import argparse
import socket
import sys
import json
import datetime

def get_time_str():
    date = datetime.datetime
    now = date.now().replace(microsecond=0)
    return json.dumps({"currentTime": now.isoformat()}).encode()

def main():
    parser = argparse.ArgumentParser(description='Start up a web service to give the time')
    parser.add_argument('--port', '-p', type=int, default = 59000, help='Port to run service on')
    parser.add_argument('--ip', '-i', type=str, default='localhost', help='IP to run service on')
    args = parser.parse_args()
    
    host = ''
    try:
        host = socket.gethostbyname(args.ip)
    except socket.error:
        print(host + ' is not a valid IP or recognized hostname!')
        sys.exit(0)
    
    if (args.port > 65535 or args.port < 1024):
        print('Please use a port 1024-65535')
        sys.exit(0)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    addr = (host, args.port)
    try:
        sock.bind(addr)
    except socket.error as e:
        print(e)
        sys.exit(0)
    sock.listen(1)
    
    try:
        while True:
            client, client_addr = sock.accept()
            time_str = get_time_str()
            client.sendall(time_str)
    except KeyboardInterrupt:
        print('Quitting...')
    finally:
        sock.close()

if __name__ == '__main__':
    main()
