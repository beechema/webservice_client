import argparse
import socket
import json
import sys
from datetime import datetime

def get_time(data):
    try:
        timeDict = json.loads(data.decode())
        if 'currentTime' in timeDict:
            try:
                datetime.strptime(timeDict['currentTime'], '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                return 'Invalid format or not a timestamp'
            return timeDict['currentTime']
        else:
            return 'No currentTime key'
    except:
        return 'Failed to decode json'

def main():
    parser = argparse.ArgumentParser(description='Connect to a time service and get json time string')
    parser.add_argument('--port', '-p', type=int, default=59000, help='Port to connect to')
    parser.add_argument('--ip', '-i', type=str, default='localhost', help='The IP or hostname to connect to')
    args = parser.parse_args()
    
    host = ''
    try:
        host = socket.gethostbyname(args.ip)
    except socket.error:
        print(host + ' is not a valid IP or recognized hostname!')
        sys.exit(0)
    
    if (args.port > 65535 or args.port < 1023):
        print('Please use a port 1024-65535')
        sys.exit(0)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(30)
    
    addr = (host, args.port)
    try:
        sock.connect(addr)
    except socket.error as e:
        print(e)
        exit(0)
    
    data = sock.recv(512)
    sock.close()
    print(get_time(data))

if __name__ == '__main__':
    main()
