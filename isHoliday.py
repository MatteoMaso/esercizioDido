import urllib.request
import vobject
import datetime

holidays = {}

def initHolidays(yy: int):

    if str(yy) not in holidays:
        holidays[str(yy)] = []
        url = "https://giorni-festivi.eu/ical/italia/"+str(yy)+"/"

        try:
            response = urllib.request.urlopen(url)
            cal = vobject.readOne((response.read()).decode("utf-8"))
            for ev in cal.vevent_list:
                holidays[str(yy)].append(datetime.datetime(ev.dtstart.value.year, ev.dtstart.value.month, ev.dtstart.value.day))
        except:
            print("Error in initialization days")


# Specificare il giorno, mese ed anno in formato numerico
# return true if is holyday, false otherwise
def isHoliday(dd: int, mm: int, yy: int):

    if  1 <= int(dd) <= 31 and 1 <= int(mm) <= 12 and 1960 <= int(yy) <= 2100:  # params check
        initHolidays(yy)

        dayToCheck = datetime.datetime(int(yy), int(mm), int(dd))

        if dayToCheck in holidays[str(yy)] or dayToCheck.weekday() in [5,6]:
            print("holiday")
        else:
            print("Work")
    else:
        print("Error input parameter: "+str(dd)+"-"+str(mm)+"-"+str(yy))

# Test
isHoliday("01", "01", "22034")
isHoliday(2, 1, "2020")
isHoliday("02", "01", "2020")
isHoliday("01", "01", "2020")

isHoliday("1", "02", "2020")
isHoliday("2", "02", "2020")
isHoliday("3", "02", "2018")
isHoliday("04", "02", "2020")
