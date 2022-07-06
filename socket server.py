import random
import socket

port = 8000

s = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)

s.bind(('127.0.0.1', port))

s.listen(1)
c, addr = s.accept()

print("CONNECTION FROM:", str(addr))

bank={
    'who':['Mr Bean','police','sahar','doctor','ranande','ammat','azhdar','Amirali','babat','nanva','raghsande'],
    'when':['ghabl az milad','dirooz','100 sal pish','1 sanie ghabl'],
    'where':['takhte khab','taxi','darya','mashin','hoz','resturan'],
    'what':['shena mikardan','avaz mikhondondan','khabide bodan','miraghsidan','dava mikardan']
}


# c.send(b"HELLO, Welcome to my game you want to be player 1 or 2???")

# player = c.recv(1024).decode()

player=random.choice(['1','2'])
c.send(player.encode())

if player=='1':
    who=random.choice(bank['who'])
    what=random.choice(bank['what'])
    p=c.recv(1024)
    when,where,wwho=p.decode().split('@')
    result=when+' '+who+' ba '+wwho+' dar '+where+' '+what
    c.send(result.encode())

else:
    when=random.choice(bank['when'])
    where=random.choice(bank['where'])
    wwho=random.choice(bank['who'])
    p=c.recv(1024)
    who,what,who=p.decode().split('@')
    result=when+' '+who+' ba '+wwho+' dar '+where+' '+what
    c.send(result.encode())
    

c.close()
