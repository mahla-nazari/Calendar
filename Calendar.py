from calendar import month

whith open('calendar.txt' ,'a') as e:
    for i in range(1,13):
        e.write(month(2022,i))
        e.write("\n")