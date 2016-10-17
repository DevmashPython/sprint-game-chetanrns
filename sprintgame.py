import time
import msvcrt
finish=10
count=0
print "Press 'D' to move right"
print "Press 'S' to move down"

print "press enter key to get started!"

raw_input()
s_time=time.time()
def move_right():
	count=0
	while(1):
		key=msvcrt.getch()
		if key=='d':
			count=count+1
			print "d",
			if count==finish:
				print "Move down"
				move_down()
				break
		else:
			print "GAME OVER"
			break
			
				
	return
def move_down():
	count=0
	while(1):
		key=msvcrt.getch()
		if key=='s':
			count=count+1
			print "\t\t\ts"
			if count==finish:
				print "\t\t\tMove right",
				breakn
		else:
			print "GAME OVER"
			break
				
	return
	
move_right()
count=0
while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print "d",
		if count==finish:
			print "\nyou've successfully completed the game"
			break
	else:
		print "GAME OVER"
		break
f_time=time.time()-s_time

print "time taken:"+str(f_time)

	
'''
specify the controls properly.
'''
	
	
	
	
	
	
	
	
	
	
