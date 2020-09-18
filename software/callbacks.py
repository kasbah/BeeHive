#import uosc
from uosc import server

def main():
    running = True
    server.run_server('192.168.42.255', 9001, handler=server.handle_osc)
    while running:



        
