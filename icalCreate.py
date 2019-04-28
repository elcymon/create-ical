import pandas as pd
from datetime import datetime,timedelta
from icalendar import Calendar, Event
import re
calData = pd.read_csv('rccgSchedule.csv')
#print(calData)
year = 2019
def splitData(x):
    return list(map(int,re.split('/|-',x)))
def toDate(x):
    xSplit = splitData(x)
    return datetime(year,xSplit[1],xSplit[0])
#get dates of events
calData['StartDate'] = calData['StartDate'].apply(toDate)
calData['EndDate'] = calData['EndDate'].apply(toDate) + timedelta(hours=23,minutes=59)
##get times of events
#timeSplit = calData['Time'].apply(splitData)
cal = Calendar()
for i, row in calData.iterrows():
    event = Event()
    
    event.add('summary',row['Event'])
    event.add('dtstart',row['StartDate'])
    event.add('dtend',row['EndDate'])
    event.add('description',row['Event'])
#    event.add('location',row['Venue'])
    cal.add_component(event)
with open('schedule.ics','wb') as f:
    f.write(cal.to_ical())
    
    