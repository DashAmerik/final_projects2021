from datetime import datetime

datetime_str = '19/09/18'
#print(type(datetime_str))

now = datetime.now()


datetime_object = datetime.strptime(datetime_str, '%d/%m/%y')

#print(type(datetime_object))
print(datetime_object)

print(now)

print(now==datetime_object) #>< == !=
