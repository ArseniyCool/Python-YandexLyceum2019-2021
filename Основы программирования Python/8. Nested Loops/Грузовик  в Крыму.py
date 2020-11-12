# Грузовику с посылкой нужно доставить груз из пункта Казани в пункт Крым.
# В Крыму,как гористой местности, имеется много дорог, каждая из которых
# проходит через несколько туннелей.

# Программа выводит оптимальный путь и максимальную высоту,
# которую может иметь грузовик, чтобы проехать сквозь туннель и не застрять.
number_of_roads = int(input('Сколько имеется дорог:'))
chosen_road = 0
chosen_height = 0
min_height = 0
for road_counter in range(1, number_of_roads + 1):
    size_of_road = int(input('Через сколько туннелей проходит путь:'))
    if 0 == chosen_road:
        chosen_road = road_counter
    min_height = 0
    for tunnel_counter in range(size_of_road):
        tunnel_height = int(input('H туннеля:'))
        if 0 == min_height:
            min_height = tunnel_height
        if min_height > tunnel_height:
            min_height = tunnel_height
    if 0 == chosen_height:
        chosen_height = min_height
        continue
    if chosen_height < min_height:
        chosen_height = min_height
        chosen_road = road_counter
print(chosen_road, chosen_height)
