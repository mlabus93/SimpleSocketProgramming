import socket

def GetInput():
   equation = raw_input("Enter math problem: ")
   return equation

def ParseCh(input):
   prevCh = ''
   tokens = ['']
   for ch in input:
      if ch == '.':
         if prevCh.isdigit():
            tokens[-1] += ch
         elif prevCh in '+-*/' or prevCh == ' ' or not prevCh:
            tokens.append(ch)
      elif ch.isdigit():
         if prevCh.isdigit() or prevCh == '.':
            tokens[-1] += ch
         else:
            tokens.append(ch)
      elif ch in '+-*/':
         if prevCh.isdigit() or prevCh == '.' or prevCh == ' ':
            tokens.append(ch)
         else:
            return 'fault'
      elif ch == ' ':
         prevCh = ch
         continue
      elif ch == '=':
         if prevCh.isdigit() or prevCh == ' ':
            continue
         else:
            return 'fault'
      else:
         return 'fault'
      prevCh = ch
   return tokens

def Minify(tokens):
   minInput = tokens[1] + tokens[2] + tokens[3]
   return str(minInput)

userHost = str(raw_input('Enter host name of server: '))
HOST = userHost
userPort = int(raw_input('Enter port number used on server (eustis2): '))
PORT = userPort

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
   s.connect((HOST, PORT))
except socket.gaierror:
   print 'Connection failed. Check host name.'
   raise SystemExit
except socket.error:
   print 'Connection refused. Check port number.'
   raise SystemExit
while True:
   input = GetInput()
   if input == '0/0=':
      s.send(input)
      print 'Exiting app...'
      s.close()
      break
   data = ParseCh(input)
   if data == 'fault':
      print 'Input error. Re-type the math question again.'
      continue
   data = Minify(data)
   s.send(data)
   data = s.recv(1024)
   print 'Received from server: ', data
s.close()
