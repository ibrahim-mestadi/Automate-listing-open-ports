import socket  
  
maxPort = 65535 # range of the number of the ports that we will scan 

ip = socket.gethostbyname (socket.gethostname())  #getting ip-address of host
  
for port in range(maxPort):      #check for all available ports, change it depends on where you are executing the script
  
    try:
   
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # creating a new socket
  
        serv.bind((ip,port))     # binding the socket with address
             
    except:
  
        print('This Port is Open :',port) #print open port number
  
    serv.close() #closing the connection
    
    
   
