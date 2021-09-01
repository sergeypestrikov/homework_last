for i in range(1, 101):
    if 1 < i < 5 or 21 < i < 25 or 31 < i < 35 or 41 < i < 45 or 51 < i < 55 or 61 < i < 65 or 71 < i < 75 or 81 < i < 85 or 91 < i < 95:
        print(f'{i} процента')
    elif 5 <= i <= 20 or 25 <= i <= 30 or 35 <= i <= 40 or 45 <= i <= 50 or 55 <= i <= 60 or 65 <= i <= 70 or 75 <= i <= 80 or 85 <= i <= 90 or 95 <= i <= 100:
        print(f'{i} процентов')
    else:
        print(f'{i} процент')