# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)

import matplotlib.pyplot as plt
import numpy as np
random_array = np.random.rand(5) # массив из 5 случайных чисел
print(random_array)
plt.scatter(random_array, random_array)
plt.title("Диаграмма рассеяния")
plt.xlabel("Ось х")
plt.ylabel("Ось y")

plt.show()

