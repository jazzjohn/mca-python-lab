# Create class Time with private attributes hour,minute,seconds. Overload '+' operator to sum two times

class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        second = self.__second + other.__second
        minute = self.__minute + other.__minute
        hour = self.__hour + other.__hour
        if second > 60:
            minute += int(second / 60)
            second = second % 60
        if minute > 60:
            hour += int(minute / 60)
            minute = minute % 60
        time = "{0} Hours:{1} minutes:{2} seconds".format(hour,minute,second)
        return time


t1 = Time(7, 55, 35)
t2 = Time(4, 51, 51)
print("Sum of time:", t1 + t2)
