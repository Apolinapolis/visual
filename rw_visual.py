import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые графики строятся, пока программа остается активной
while True:

    # Постороение случайного блуждания
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    
    # Выделение первого и последнего точек
    ax.scatter(0, 0, c='green', s=100, edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               s=100, edgecolors='none')
    
    # Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Хотите ли вы продолжить? (y/n): ")
    if keep_running == 'n':
        break