import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head(5))

case = int(input("Введите вариант (1 - get_dummies или 2 - без get_dummies):"))
if case == 1:
    data = pd.get_dummies(data['whoAmI'], drop_first=True)
elif case == 2:
    data = data.rename(columns={"whoAmI": "robot"})
    data = data.replace({'robot': True, 'human': False})

print(data.head(5))
