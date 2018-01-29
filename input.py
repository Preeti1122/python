Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nos=input("Enter Number :")
Enter Number :2
>>> nos
'2'
>>> nos=int(input("Enter Number :"))
Enter Number :2
>>> nos
2
>>> nos=string(input("Enter Number :"))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    nos=string(input("Enter Number :"))
NameError: name 'string' is not defined
>>> nos=str(input("Enter Number :"))
Enter Number :2
>>> nos
'2'
>>> type(nos)
<class 'str'>
>>> clr
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> cl
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cl
NameError: name 'cl' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> os.system('cls')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.system('cls')
NameError: name 'os' is not defined
>>> import os
>>> os.system('cls')
0
>>> import os
>>> os.system('clear')
1
>>> print("Your no. is",nos)
Your no. is 2
>>> name=input("Enter Name : ")
Enter Name : Priti
>>> reg=input("Enter Reg no.")
Enter Reg no.11609607
>>> reg=int(input("Enter Reg no.: "))
Enter Reg no.: 11609607
>>> course=input("Enter the course : ")
Enter the course : MCA
>>> print("The Student name is ",name,"Reg. no is",reg,"in course",course)
The Student name is  Priti Reg. no is 11609607 in course MCA
>>> 
>>> no1=int(input("Enter no 1 :"))
Enter no 1 :5
>>> no2=int(input("Enter no 2 :"))
Enter no 2 :5
>>> sum=no1+no2
>>> sum
10
>>> print("The addition of two is :",sum)
The addition of two is : 10
>>> name=input("Enter Name : ")
Enter Name : Priti
>>> reg=int(input("Enter Reg no.: "))
Enter Reg no.: 11609607
>>> print("The name is",name,"and the Reg no. is",reg)
The name is Priti and the Reg no. is 11609607
>>> word="hello"
>>> revere=word[::-1]
>>> reverse=word[::-1]
>>> reverse
'olleh'
>>> if word==reverse:
	print("Both are same.")
	else:
		
SyntaxError: invalid syntax
>>> if word==reverse:
	print("Both are same.")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if word==reverse:
	print("Both are same.")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if word==reverse:
	print("Both are same.")
	else:
		
SyntaxError: invalid syntax
>>> if word==reverse:
	print("Both are same.")
		else
		
SyntaxError: unexpected indent
>>> if word==reverse:
	print("Both are same.")
		else:
			
SyntaxError: unexpected indent
>>> 
