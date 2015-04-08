from datetime import *
import temp_list

# when it's Tue 19:58, change temp to 27
class Temperature(object):

    def __init__(self):
        self.temp = temp_list.temp

    def tem(self):
        now = datetime.now()
        day = now.strftime('%a')
        hour = now.hour
        minute = now.minute
        t = 'stay' # always start with default value
        if day in self.temp:
            # if self.temp.has_key(day):
            get = self.temp[day]
            for key, value in self.temp[day]:
                #if TimeDelta( -5 minutes ) < now.Time() - Time( key ) < TimeDelta( +5 minutes )
                #    t = value
                pass
            if get.has_key((hour, minute)):
                t = get[(hour, minute)]
            else:
                t = 'stay'
        else:
            t = 'stay'
        return t

if __name__ == "__main__":
    # this is where you do testing
    pass