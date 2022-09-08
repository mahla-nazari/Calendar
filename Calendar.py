from calender import month

whith open('calender.txt' ,'a') as e:
    for i in range(1,13):
        e.write(month(2022,i))
        e.write("\n")