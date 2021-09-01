duration = int(input('Введите, пожалуйста, секунды: '))

h = str(duration // 3600)
m = str((duration // 60) % 60)
s = str(duration % 60)

print('Получается: ' + h + ' час ' + m + ' мин ' + s + ' сек ')