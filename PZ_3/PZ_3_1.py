# Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у) лежит в первой или третьей
# координатной четверти»

x, y = float(input('Введите x: ')), float(input('Введите y: '))
if x > 0 and y > 0:
    print('Точка лежит в 1й координатной четверти')
elif x < 0 and y < 0:
    print('Точка лежит в 3й четверти')
else:
    print('Точка не лежит ни в 1й, ни в 3й четверти!')
print('\nПрограмма завершена!')
