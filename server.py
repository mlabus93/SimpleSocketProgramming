import socket

def Parse(data):
   prevCh = ' '
   tokens = ['']
   for ch in data:
      if ch == '.':
         if prevCh.isdigit():
            tokens[-1] += ch
         elif prevCh in '+-*/' or prevCh == ' ':
            tokens.append(ch)
      elif ch.isdigit():
         if prevCh.isdigit() or prevCh == '.':
            tokens[-1] += ch
         else:
            tokens.append(ch)
      elif ch in '+-*/':
         if prevCh.isdigit() or prevCh == '.' or prevCh == ' ':
            tokens.append(ch)
      prevCh = ch
   return tokens

def DoMathOp(data):
   if data[2] == '+':
      return float(data[1]) + float(data[3])
   elif data[2] == '-':
      return float(data[1]) - float(data[3])
   elif data[2] == '*':
      return float(data[1]) * float(data[3])
   else:
      if data[3] is not '0':
         return float(data[1]) / float(data[3])
      else:
         return 'Cannot divide by 0'


userPort = int(raw_input('Enter port number to use (over 1024): '))
while userPort <= 1024:
   userPort = int(raw_input('Enter port number greater than 1024: '))
HOST = ''
PORT = userPort
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( (HOST, PORT) )
s.listen(1)
print 'server is ready to receive on', PORT
conn, addr = s.accept()
print 'connected by', addr
while 1:
   data = conn.recv(1024)
   if not data:
      conn.close()
      conn, addr = s.accept()
      print 'connected by', addr
      continue
   if data == '0/0=':
      print data
      print 'Shutting down...'
      break
   print 'Received question:', data
   data = Parse(data)
   ans = DoMathOp(data)
   data = str(ans)
   dataStr = 'The answer is ' + data
   conn.send(dataStr)
conn.close()
