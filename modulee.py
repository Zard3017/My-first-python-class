import math
import statistics
import datetime
import modules
modules.hello(" Brad")
modules.hello("Fidel")
print(math.sqrt(36))
print(math.e)
dataset=[3,6,6,8,32,7,9,7,5]
x=statistics.mean(dataset)
y=statistics.median(dataset)
g=statistics.mode(dataset)
print("The mean is",x)
print("The median is",y)
print("The mode is",g)
taimu=datetime.datetime.now()
print(taimu)