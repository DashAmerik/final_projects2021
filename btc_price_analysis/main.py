import csv,time
import matplotlib.pyplot as plt
name_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
data = [[-32.13475233438765, -14.383791096625586, 0.6999365812365695, -27.572600531691926, -7.71130921354633, 29.96066070255682], [17.24374631006568, 18.50466600506838, 21.528496223867798, 1.5687787703702853, 11.392368531422397, -7.9907989741760135], [-3.955831023783918, -4.838357128649627, -9.17341754706342, -32.84997799711122, 6.529919031637567, -25.129940397448042], [-3.307633911820599, 7.572219561085042, 25.77003704829799, 31.950172169728642, 30.335063399477498, 34.505580025803475], [-2.4366438451600647, 18.48493487757776, 69.57723273063533, -18.994817654446827, 60.24367182984756, 9.089082907512056], [14.263371764574407, 26.779910891589758, 8.412685383581273, -14.621304231451159, 26.1646528255351], [8.090145216008853, -7.112701416785466, 15.355049945921973, 21.347910803840442, -6.588008723365077], [-19.189564657384548, -7.865809873580451, 63.80698835839432, -9.415062315654522, -4.433449510499667], [2.5206731097648674, 5.940265895783173, -7.721572838011319, -5.951189549310743, -13.879982681311123], [-12.674900754594287, 33.11892495990681, 14.926813876977443, 49.00542939059877, -4.565665846290289, 10.842102887567487], [11.633546049907794, 19.782545677329797, 6.324207275682266, 58.88288980389269, -36.41691276402279, -17.667649393047324], [-15.34861984417761, 14.083469309343402, 29.180097992909204, 38.8072964302603, -7.001277465656666, -4.992554818756111]]


def extract():
	lastday_row = [0,0,0,0,0,0] # row of the last day of the month
	prev_row = [0,0,0,0,0,0] #row of a first day of the month previus to the one after the last of the month
	start_printing = 0
	months = [[],[],[],[],[],[],[],[],[],[],[],[]]
	with open('BTC-USD.csv','r') as file:
		reader = csv.reader(file)
		for row in reader:

			#if '-01' in reader[row][0]:
			time.sleep(0.1)
			if '01' == (row[0][8:]):
				if prev_row[1] == 0:
					pass
				else:
				#    print("open of" ,prev_row[0],":", prev_row[1])
				#    print("close of" ,lastday_row[0],":", lastday_row[4])
					calc = float(lastday_row[4]) -float(prev_row[1])
					percentage = (calc /float(prev_row[1])) *100
				#    print("percentage change: ",percentage*100)
					date = prev_row[0].split("-")
					months[int(date[1])-1].append(percentage)

			#    print(row)
				prev_row = row
				print(months)
			lastday_row = row
	return months

def percentage_analysis(months):
	total = 0
	neg = 0
	neg_month = ''
	pos = 0
	pos_month = ''
	percentages = []
	for i in range(len(months)):
		total = sum(months[i])
		total = total / len(months[i])
		print(name_month[i], total)
		percentages.append(total)

		if total < neg:
			neg = total
			neg_month = name_month[i]
		if total > pos:
			pos = total
			pos_month = name_month[i]
	print('\n')
	print('The most profitabl month for bitcoin is:',pos_month,'with an average percentage increase of:', pos)
	print('The most unprofitabl month for bitcoin is:',neg_month,'with an average percentage decrease of:', neg)
	return(percentages)



data2 = extract()
percentages = percentage_analysis(data2)

plt.bar(name_month, percentages)
plt.title('Average BTC Months ROI')
plt.xlabel('Months')
plt.ylabel('Percentage increase')
plt.show()
