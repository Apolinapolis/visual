import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

#Заголовок диаграммы и метки осей
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('square of value', fontsize=14)

# Размер шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])

plt.show()