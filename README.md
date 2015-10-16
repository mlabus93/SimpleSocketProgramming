# SimpleSocketProgramming
Socket program to do basic math operations (mult, div, add, sub) between 2 numbers.

INSTRUCTIONS:  
1.	Connect to 2 different servers, or use your own computer as client side.  
2.	Place server.py code on one server.  
3.	Place client.py code on other server acting as client.  
4.	On designated server run:  
	$ python server.py  
5.	When prompted enter a port (it will not allow a port below 1024)  
6.	If it runs, you should see “server is ready to receive on <port you specified>”  
7.	On client, run command:  
	$ python client.py  
8.	It will prompt you to enter the server name where your server.py code is running.  
9.	Then, it will prompt you to enter the port number you used on for the server.  
10.	If you get an error CONN REFUSED, most likely, the server isn’t up or the port isn’t matched.  
11.	If successful, you should see a prompt telling you to enter a math problem.  
12.	To end the application, type "0/0=" as a math problem. This will also shut the server down.  

The input format is a number (float) followed by an operand that can be ‘+’, ‘-‘, ‘*’, ‘/’ followed by another number (float).  
Examples: (white space does not matter)  
	4.3 * 7  
	2.1 - 1  
	39. /3.0  
	56 + 11.135  
NOTE: other input can be placed after the 2nd operand, but it will not be used or sent to the server.  
Examples:  
	45-2 =  
	35 * 2 ignoredValues123


