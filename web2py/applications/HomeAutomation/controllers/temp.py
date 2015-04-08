from datetime import *

temp={'Tue':{(19,58):27}}
#when it's Tue 19:58, change temp to 27 
def tem(temp):
	now=datetime.now()
	day=now.strftime( '%a' )
	hour=now.hour
	minute=now.minute
	if temp.has_key(day):
		get=temp[day]
		if get.has_key((hour,minute)):
			t=get[(hour,minute)]
		else:
			t='stay'
	else:
		t='stay'
	return t