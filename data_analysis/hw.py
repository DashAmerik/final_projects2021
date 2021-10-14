import matplotlib.pyplot as plt
import matplotlib.dates as dates


date = ["2020-04-01","2020-05-01","2020-06-01","2020-07-01","2020-08-01"]
cases = [100,200,111,123,209]

months=[1,2,3,4,5]
unemployed_perc = [4,2,1,5,3]

x_values = date
y_values = cases

second_x_values = months
second_y_values = unemployed_perc


fig = plt.figure()
ax=fig.add_subplot(111)
ax2=fig.add_subplot(111, frame_on=False)

ax.plot(x_values, y_values, color="black")
#ax.set_xlabel("Date", color="black")
#ax.set_ylabel("New cases", color="black")
#ax.tick_params(axis='x', colors="black")
#ax.tick_params(axis='y', colors="black")


ax2.plot(second_x_values, second_y_values, color="red")
ax2.xaxis.tick_top()
ax2.yaxis.tick_right()
#ax2.set_xlabel('Months', color="red")
#ax2.set_ylabel('Unemployed percentage', color="red")
#ax2.xaxis.set_label_position('top')
#ax2.yaxis.set_label_position('right')
#ax2.tick_params(axis='x', colors="red")
#ax2.tick_params(axis='y', colors="red")

years = dates.MonthLocator()
ax.xaxis.set_major_locator(years)


plt.xticks(rotation = 45)
plt.show()
