import matplotlib.pyplot as plt
import numpy as np

# x = np.array([1,2,3,4,5])
# y = np.array([5,4,3,2,1])

# # plt.plot(x,y, marker='o', c="g", ms =10, mec='r', mfc='b')
# # plt.plot(x,x, '+:r')  

# # plt.plot(x)
# # plt.plot(y)

# plt.plot(x,y,'o')
# plt.show()

#Multiple plots of xs and ys
# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
# plt.title("Multiple plots",fontdict = font1)
# plt.xlabel("x axis", fontdict=font2)
# plt.ylabel("y axis", fontdict=font2)

# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.show()

#Scatter plots

#day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes, alpha=0.5)
# plt.show()

#Color map

# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.rand(100)
# sizes = 1000 * np.random.rand(100)

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.title("Scatter plot")
# plt.xlabel("x axis")
# plt.ylabel("y axis")    
# plt.colorbar()
# plt.show()

#bar chat

# x = ["APPLES", "BANANAS","ORANGES"]
# y = [400, 350, 500]
# plt.bar(x, y, color='orange', width=0.2)
# plt.show()


# x = np.random.normal(170, 10, 250)
# plt.hist(x, bins=5, color='r')
# plt.show()


# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels= mylabels)
# plt.show() 


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["green", "blue", "orange", "red"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, colors=mycolors, shadow=True)
plt.legend(title = "Four Fruits:")
plt.show() 
