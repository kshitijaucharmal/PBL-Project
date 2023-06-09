print("Matplotlib")
# line plot
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8]
y = [0,1,2,3,4,5,6,7,8]

plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.plot(x,y)
plt.show()