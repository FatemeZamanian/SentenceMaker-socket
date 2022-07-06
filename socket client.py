import socket

host = 'local host'
port = 8000

s = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)

s.connect(('127.0.0.1', port))

# msg = s.recv(1024)

# print('Received:' + msg.decode())

# ans=input()
# s.send(ans.encode())


p=s.recv(1024)
ans=p.decode()

if ans=='1':
  when=input('Tell me When?')
  where=input('Tell me Where?')
  wwho=input('Tell me Who?')
  res=when+'@'+where+'@'+wwho
  s.send(res.encode())
  final=s.recv(1024).decode()
  print(final)

    
else:
  wwho=input('Tell me with Who?')
  what=input('Tell me what they were doing?')
  res=wwho+'@'+what
  s.send(res.encode())
  final=s.recv(1024).decode()
  print(final)


s.close()
