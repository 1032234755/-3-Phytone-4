
import numpy as np

# ������� ��� ������������ ��������������� ����
def functional_series_sum(k, x):
    return np.sin(k * x) / (2 * k ** 2 + 6 + k ** 2)

# ������������ ���� �� �������� 10^-6 ��� ��������� x
x = 1  # ������ �������� ��� x, �� ������ �������� ��� �� �������������
functional_series_sum_value = 0
k = 1
while True:
    term = functional_series_sum(k, x)
    functional_series_sum_value += term
    if abs(term) < 1e-6:
        break
    k += 1

print(f"�������� ����� ��������������� ���� = {functional_series_sum_value:.10f} ��� x = {x}, ���������� ������ = {k}")
