from datetime import *
import temp_list

#when it's Tue 19:58, change temp to 27 
class temperature(object):
	def __init__(self):
		self.temp=temp_list.temp
	def tem(self):
		now=datetime.now()
		day=now.strftime( '%a' )
		hour=now.hour
		minute=now.minute
		if self.temp.has_key(day):
			get=self.temp[day]
			if get.has_key((hour,minute)):
				t=get[(hour,minute)]
			else:
				t='stay'
		else:
			t='stay'
		return t