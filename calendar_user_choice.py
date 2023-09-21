from datetime import datetime,timedelta
def get_day_string(m):
    if m == 0:
        return "Monday"
    elif m==1:
        return "Tuesday"
    elif m==2:
        return "Wednesday"
    elif m == 3:
        return "Thursday"
    elif m==4:
        return "Friday"
    elif m==5:
        return "Saturday"
    elif m==6:
        return "Sunday"

def get_cal_nmonth(year_input,month_input,num_of_month):
    day = datetime(year_input,month_input,1)
    month_txt = []
    month_nmonth = month_input
    day_value = [[],[],[],[],[],[],[]]
    index_of_next_month = 7
    for nmonth in range(num_of_month):
        day_list = datetime(year_input,month_nmonth,1)
        month_txt.append(day_list.strftime("%B"))
        #fill whitepsace for the day before first day of the month
        for whitespace in range(0, day_list.weekday()):
            day_value[whitespace].append(' ')
        while day_list.month == month_nmonth and day_list.year == year_input :
            this_weekday = day_value[day_list.weekday()]
            this_weekday.append(str(day_list.day))
            day_list = day_list + timedelta(days=1)
        month_nmonth = day_list.month
        #fill each day with space so the next month print will start at the same index
        for a in range(len(day_value)):
            if len(day_value[a]) < index_of_next_month:
                b = len(day_value[a])
                while b < index_of_next_month:
                    day_value[a].append(' ')
                    b = b+1
        index_of_next_month = index_of_next_month + 7
    return day_value,month_txt

def display(y,m,n,sw):
    p1,p2 = get_cal_nmonth(y,m,n)
    z = ''
    x = z.ljust(10)
    for s in range(len(p2)):
        x = x+'       '+p2[s]
    print(x)
    if sw == 1 :
        print(get_day_string(6).ljust(10), ' '.join(p1[6]))
        for y in range(len(p1)-1):
            print(get_day_string(y).ljust(10), ' '.join(p1[y]))
    else:
        for y in range(len(p1)):
            print(get_day_string(y).ljust(10), ' '.join(p1[y]))


year_input = int(input("input desired year:"))
day_input = int(input("input start day of week \n(0 - Mon\n1 - Sun):"))
month_input = int(input("input many months to display in a single row(1,2,3):"))
if month_input > 3 :
    print('number of months must smaller than 3')
elif month_input < 1:
    print('number of months must larger than 0')
else:
    i = 1
    while i < 13:
        display(year_input, i, month_input,day_input)
        i = i+month_input

