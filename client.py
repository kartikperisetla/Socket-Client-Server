'''
Created on 08-Mar-2014

@author: kartik perisetla
'''
from socket import *
import time

# a class that wraps attributes and methods to manage a client
class client(object):
    #attribute to hold host name to which the client will connect
    host=None
    #attribute to hold port to which the client will connect
    port=None
    #creating socket instance
    s=socket(AF_INET,SOkCK_STREAM,0)
    
    def __init__(self, host,port):
        #setting host and port 
        self.host= host #gethostname()        
        self.port=port                
        self.run()
        
    def connect(self):
        print "\nconnecting..."
        #connect to server host and port 
        self.s.connect((self.host,self.port))
                
    def request(self):
        i=0
        #keep a counter with i and send it to server and print the received response
        while True:
            i=i+1
            self.s.send(str(i))
            data=self.s.recv(1024)            
            print "\ngot response:",data
            time.sleep(2)

            
    def run(self):
        self.connect()
        self.request()
 
#created a client instance that connects to server at 127.0.0.1 and 1234 port       
c=client("127.0.0.1",1234)
        
    
        