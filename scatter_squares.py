import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(2,4, s=200)

#Заголовок диаграммы и метки осей
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('square of value', fontsize=14)

# Размер шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()