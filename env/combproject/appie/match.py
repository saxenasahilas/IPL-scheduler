import calendar
import datetime
from calendar import monthrange
from .models import schedule

def Match(yy,mm,dd):
    a = ['Team A Vs Team B', 'Team C Vs Team D', 'Team E Vs Team F', 'Team A Vs Team H', 'Team F Vs Team G',
         'Team B Vs Team C', 'Team D Vs Team E', 'Team F Vs Team G', 'Team A Vs Team C', 'Team B Vs Team D',
         'Team C Vs Team E', 'Team D Vs Team F', 'Team E Vs Team G', 'Team F Vs Team H', 'Team A Vs Team D',
         'Team B Vs Team E', 'Team C Vs Team F', 'Team D Vs Team G', 'Team E Vs Team H', 'Team A Vs Team E',
         'Team B Vs Team F', 'Team C Vs Team G', 'Team D Vs Team H', 'Team A Vs Team F', 'Team B Vs Team G',
         'Team C Vs Team H', 'Team A Vs Team G', 'Team B Vs Team H', 'Team A Vs Team B', 'Team C Vs Team D',
         'Team E Vs Team F', 'Team A Vs Team H', 'Team F Vs Team G', 'Team B Vs Team C', 'Team D Vs Team E',
         'Team F Vs Team G', 'Team A Vs Team C', 'Team B Vs Team D', 'Team C Vs Team E', 'Team D Vs Team F',
         'Team E Vs Team G', 'Team F Vs Team H', 'Team A Vs Team D', 'Team B Vs Team E', 'Team C Vs Team F',
         'Team D Vs Team G', 'Team E Vs Team H', 'Team A Vs Team E', 'Team B Vs Team F', 'Team C Vs Team G',
         'Team D Vs Team H', 'Team A Vs Team F', 'Team B Vs Team G', 'Team C Vs Team H', 'Team A Vs Team G',
         'Team B Vs Team H']
    b = ['Bangalore Vs Delhi', 'Pune Vs Chenai', 'Kolkata Vs Hydrabad', 'Bangalore Vs Patna', 'Hydrabad Vs Kochi',
         'Delhi Vs Pune', 'Chenai Vs Kolkata', 'Hydrabad Vs Kochi', 'Bangalore Vs Pune', 'Delhi Vs Chenai',
         'Pune Vs Kolkata', 'Chenai Vs Hydrabad', 'Kolkata Vs Kochi', 'Hydrabad Vs Patna', 'Bangalore Vs Chenai',
         'Delhi Vs Kolkata', 'Pune Vs Hydrabad', 'Chenai Vs Kochi', 'Kolkata Vs Patna', 'Bangalore Vs Kolkata',
         'Delhi Vs Hydrabad', 'Pune Vs Kochi', 'Chenai Vs Patna', 'Bangalore Vs Hydrabad', 'Delhi Vs Kochi',
         'Pune Vs Patna', 'Bangalore Vs Kochi', 'Delhi Vs Patna', 'Bangalore Vs Delhi', 'Pune Vs Chenai',
         'Kolkata Vs Hydrabad', 'Bangalore Vs Patna', 'Hydrabad Vs Kochi', 'Delhi Vs Pune', 'Chenai Vs Kolkata',
         'Hydrabad Vs Kochi', 'Bangalore Vs Pune', 'Delhi Vs Chenai', 'Pune Vs Kolkata', 'Chenai Vs Hydrabad',
         'Kolkata Vs Kochi', 'Hydrabad Vs Patna', 'Bangalore Vs Chenai', 'Delhi Vs Kolkata', 'Pune Vs Hydrabad',
         'Chenai Vs Kochi', 'Kolkata Vs Patna', 'Bangalore Vs Kolkata', 'Delhi Vs Hydrabad', 'Pune Vs Kochi',
         'Chenai Vs Patna', 'Bangalore Vs Hydrabad', 'Delhi Vs Kochi', 'Pune Vs Patna', 'Bangalore Vs Kochi',
         'Delhi Vs Patna']
    c = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    #yy, mm, dd = int(input()), int(input()), int(input())
    d = [calendar.weekday(yy, mm, dd)]
    i = int(d[0])
    j = 0
    days = int(monthrange(yy, mm)[1])
    date = datetime.datetime(yy, mm, dd, 0, 0, 0)
    start = 1
    p = 1
    while (j < 56):
        l = j
        flag = 0

        if (i == 5 or i == 6):
            if (start):
                date = str(date).split()
                date[0]
            else:
                date = datetime.datetime(yy, mm, dd, 0, 0, 0) + datetime.timedelta(days=p)
                date = str(date).split()
                date[0]
            s=schedule(date=date[0],matches=(a[l] + "and" + a[l + 1]),city=(b[l] + "and" + b[l + 1]))
            s.save()
            flag = 1
        else:
            if (start):
                date = str(date).split()
                date[0]
            else:
                date = datetime.datetime(yy, mm, dd, 0, 0, 0) + datetime.timedelta(days=p)
                date = str(date).split()
                date[0]
            s=schedule(date=date[0],matches=a[l],city=b[l])
            s.save()
        start = 0

        if (flag):
            j += 2
        else:
            j += 1
        if (i == 6):
            i = 0
        else:
            i += 1
        p += 1