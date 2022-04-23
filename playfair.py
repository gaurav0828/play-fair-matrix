l=[]
#Generation of play fair matrix
def playfairmatrix():
    global l
    ip = (input("Enter the key for playfair matrix :- ").upper()).replace('J','I') + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    s = ''
    for i in ip:
        if (i not in s) and (ord(i) >= 65 and ord(i) <= 90):
            s+=i
    p = 0
    while(p <= 20):
        m=[]
        for i in range(0,5):
            m.append(s[i+p])
        l.append(m)
        p+=5
    print("Playfair Matrix :- ")
    for i in l:
        print(i)



def checkval(a):
    x=-1
    for i in l:
        x+=1
        y=-1
        for j in i:
            y+=1
            if j == a:
                return x,y
        
def incrval(v,y):
    if(v<4):
        v+=1
    else:
        v=0
    if(y<4):
        y+=1
    else:
        y=0
    return v,y


#Plain text to Cypher text
def encryption():
    ip = (input("Enter the message for encryprion : - ").upper()).replace('J','I')
    op = ""
    s = []
    for i in ip:
        if (ord(i) >= 65 and ord(i) <= 90):
            s.append(i)
    ec = ""
    for i in s:
        ec += i
    print("Modified string :- ",ec)   
    i=0
    while(i < len(s)):
        if(i == len(s)-1):
            s.append('Z')
        if(s[i] == s[i+1]):
            s.insert(i+1,'X')
        u,v = checkval(s[i])
        x,y = checkval(s[i+1])
        
        #other code than the repetation of char
        if(x==u):
            v,y = incrval(v,y)
            op += l[u][v]
            op += l[x][y]
        elif(v==y):
            u,x = incrval(u,x)
            op += l[u][v]
            op += l[x][y]
        else:
            x,u = u,x
            op += l[x][y]
            op += l[u][v]
        i+=2
    print("Encoded ouptup :- ",op)
    return op

def decrval(v,y):
    if(v>0):
        v-=1
    else:
        v=4
    if(y>0):
        y-=1
    else:
        y=4
    return v,y


def decryption(ip):
    pass
    i = 0
    op=[]
    while(i < len(ip)):
        u,v = checkval(ip[i])
        x,y = checkval(ip[i+1])
        if(x==u):
            v,y = decrval(v,y)
            op.append(l[u][v])
            op.append(l[x][y])
        elif(v==y):
            u,x = decrval(u,x)
            op.append(l[u][v])
            op.append(l[x][y])       
        else:
            x,u = u,x
            op.append(l[x][y])
            op.append(l[u][v])
        if(len(op) >= 4):
            if op[-2] == op[-4] and op[-3] == 'X' :
                op.remove('X')
        i+=2
    if op[-1]=='Z' :
        op.pop()
    msg=""
    for i in op:
        msg = msg + i
    print("Decoded string : - ",msg)
#Calling the function
playfairmatrix()
op = encryption()
decryption(op)