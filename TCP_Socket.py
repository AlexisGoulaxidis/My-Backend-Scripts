import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	  s.bind(('127.0.0.1', 4444))
	  s.listen(10) #max connections
  
	  while True:
    
			conn, adrr = s.accept()
			data = conn.recv(1024) #max len
    
			if not data or data.decode() == 'close': break
			
			conn.send(data) #return accepted data
			
			#auto-close connection
    
    
