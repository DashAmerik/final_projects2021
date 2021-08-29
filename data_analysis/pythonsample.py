import csv
date = ['4/12/20','6/12/20','3/1/20','1/10/20','6/4/20']
price = ['1234.5','2345.6','3456.7','4567.8','5678.9']
# open the file in the write mode
with open(r'C:\Users\DAmer\OneDrive\Документы\GitHub\final_projects2021\data_analysis\cleanedsample.csv', 'w' ,newline = '') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for i in range(len(date)):
        data = [date[i],price[i]]
        writer.writerow(data)


    '''    
    for row in price:
        if i > 0:
            writer.writerow(row)
        i+=1
'''
