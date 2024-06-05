
import numpy as np

# Функция для суммирования функционального ряда
def functional_series_sum(k, x):
    return np.sin(k * x) / (2 * k ** 2 + 6 + k ** 2)

# Суммирование ряда до точности 10^-6 для заданного x
x = 1  # Пример значения для x, вы можете изменить это по необходимости
functional_series_sum_value = 0
k = 1
while True:
    term = functional_series_sum(k, x)
    functional_series_sum_value += term
    if abs(term) < 1e-6:
        break
    k += 1

print(f"Значение суммы функционального ряда = {functional_series_sum_value:.10f} для x = {x}, Количество членов = {k}")
