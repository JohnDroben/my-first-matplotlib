# Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
#
# # Параметры нормального распределения
# mean = 0 # Среднее значение
# std_dev = 1 # Стандартное отклонение
# num_samples = 1000 # Количество образцов
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=10)
plt.title("Параметры нормального распределения")
plt.xlabel("Ось х")
plt.ylabel("Ось y")
plt.show()


