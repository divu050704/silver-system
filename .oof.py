import os
import subprocess
ch = 'Y'
def zero():
	exit()
def zero1():
	print(282)
def one():
	
	os.system('python3 boot.py')
def two():
	
	os.system('python3 do.py')
def three():
	
	os.system('python3 ping.py')
def four():
	
	os.system('python3 wifi.py')
def five():
	
	os.system('python3 install.py')
def six():
	
	os.system('python3 app.py')
def seven():
	
	os.system('python3 remove.py')
def eight():
	
	os.system('python3 dir.py')
def nine():
	
	os.system('python3 file.py')
if ch == 'n':
	exit()
while ch == 'Y':
	print('0.\t Exit')
	print('0.1\t See number of lines in programs')
	print('1.\t See boot time')
	print('2.\t Do a system upgrade')
	print('3.\t Ping any website')
	print('4.\t Search devices connected to wifi')
	print('5.\t Install a new application')
	print('6.\t Run an application')
	print('7.\t Remove an application')
	print('8.\t Change your working directory')
	print('9.\t Want to see files in a particular folder')
	y = float(input('Enter you choice:\t'))		 
	if y == 0 :
		zero()
	if y == 0.1:
		zero1()
	if y==1:
		one()
	if y==2:
		two()
	if y==3:
		three()
	if y==4:
		four()
	if y == 5:
		five()
	if y == 6:
		six()
	if y == 7:
		seven()
	if y == 8:
		eight()
	if y == 9:
		nine()
	ch = input('\nDo you want to continue main program(Y/n):\t')
