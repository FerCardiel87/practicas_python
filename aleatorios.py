# import random
#
# print(random.randrange(11))
# print("---"*5)
# print(random.randrange(1,12,4))
# print("****"*5)
# print(random.random())
# print("----"*5)
# print(random.uniform(1,10))
# print(random.randint(10,20))
#
from datetime import datetime

formato = "%H:%M:%S"
fecha = (datetime.now())
hora = fecha.time()

print(hora)