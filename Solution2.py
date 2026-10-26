total_second = 9875
Hour = total_second // 3600
Minute = (total_second % 3600) // 60
Second = total_second % 60

print(Hour, Minute, Second)

print("Check_Total_second:", (Hour * 3600) + (Minute * 60) + Second == total_second)

