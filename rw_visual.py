import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые графики строятся, пока программа остается активной
while True:

    # Постороение случайного блуждания
    rw = RandomWalk()
    rw.fill_walk()

    #Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, s=15)
    plt.show()

    keep_running = input("Хотите ли вы продолжить? (да/нет): ")
    if keep_running == 'нет':
        break