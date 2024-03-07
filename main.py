#code block 1 import libraries
import pandas as pd 
import matplotlib.pyplot as plt

#code block 2 loads data
data = pd.read_csv('data.csv')

#code block 3 set up the plot
plt.figure(figsize=(8,5))
plt.gca().set_aspect('equal', adjustable="box")
plt.axis('off')

#code block 4 create bar chart
bars = data.shape[0]
barWidth = 800  /bars
barHeight = 500 

#code block 5 the for loop iterates through each row of the DataFrame
for i in range(bars):
    x = i * barWidth
    y = 0
    d = data.iloc[i, 1] #integer based data
    if d > 0:
      col = plt.cm.Reds(d) #if data is greater than 0 turn it red
    else: 
      col = plt.cm.Blues(-d) #if data is a negative value, turn it blue
plt.bar(x, barHeight, width=barWidth, bottom=y, color=col)

plt.show()
