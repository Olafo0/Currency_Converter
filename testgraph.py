from matplotlib import pyplot as plt
import csv



file = open("Task3_data.csv","r")
datareader = csv.reader(file,delimiter=",")


current_data = []
last_30_days = []
last_30_days_GBP_TO_EUR_VALUE = []
last_30_days_EUR_TO_GBP_VALUE = []

for row in datareader:
    current_data.append(row)

print(len(current_data))

for i in range(0,30):
    x = 30
    n = x - i 
    print("Value N",n)
    
    y = len(current_data) 
    print("Value Y :", y)

    v = y - n
    print("Final Value", v)
    

    last_30_days.append(current_data[v][0])
    last_30_days_GBP_TO_EUR_VALUE.append(float(current_data[v][1]))
    last_30_days_EUR_TO_GBP_VALUE.append(float(current_data[v][2]))
    
print(last_30_days)
print(last_30_days_GBP_TO_EUR_VALUE)

# GBP TO EUR VALUE CHART
plt.plot(last_30_days,last_30_days_GBP_TO_EUR_VALUE)


# EUR TO GBP VALUE CHART
plt.plot(last_30_days,last_30_days_EUR_TO_GBP_VALUE)
plt.xticks(rotation=90)

plt.show()
