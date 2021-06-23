import matplotlib.pyplot as plt

Country = ['USA','Canada','Germany','UK','France']
GDP_Per_Capita = [45,-42,52,49,47]

plt.bar(Country, GDP_Per_Capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()
