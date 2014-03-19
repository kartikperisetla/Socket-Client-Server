'''
Created on 08-Mar-2014

@author: kartik perisetla
'''
from socket import *
from datetime import datetime

# a class that wraps attributes and methods to manage a server
class server(object):
    #attribute to hold host name to which the server will bind
    host=None
    #attribute to hold port to which the server will bind
    port=None
    #creating socket instance
    s=socket(AF_INET,SOCK_STREAM,0)
    

    def __init__(self, host,port):
        #setting host and port 
        self.host=host  #gethostname()        
        self.port=port        
        #binding the server to host and port passed as param within a tuple
        self.s.bind((self.host,self.port))
        self.run()
        
    def listen(self):
        #start listening for requests
        self.s.listen(10)        
        print "\nStarted listening"
        
    def serve(self):
        #creates a never server
        while True:
            print "\nback to listening..."
            try:
                #accept connections from client
                c,addr=self.s.accept()
                while True:          
                    #get current datetime
                    tstmp=str(datetime.now())  
                    print "\nGot req from:",addr," at :",tstmp                 
                    #receive the data from client
                    data=c.recv(1024)
                    #output the data received in terminal
                    print "\n\tdata:",data

                    val=int(data)*int(data)
                    #send the double of data received to client
                    c.send("res="+str(val))                   
                    
                c.close()
            except Exception as e:
                #in case of exception, print that and go back to listening mode
                print e
                pass
            
    def run(self):
        self.listen()
        self.serve()

#created a server instance that listens at 127.0.0.1 and 1234 port
s=server("127.0.0.1",1234)

        
    
