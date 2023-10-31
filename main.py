lista = [1, 1, 1, 1]
akcja = 1
score1 = 0
score2 = 0
x = (score1 - score2)
y = (score2 - score1)
for i in lista:
    print('Akcja nr {}'.format(akcja))
    print('druzyna1 {} :'.format(score1), '{} druzyna2 '.format(score2))
    odpowiedz = int(input('Ktora z druzyn wygrala akcje? '))
    if odpowiedz == 1:
        score1 = score1 + 1
    elif odpowiedz == 2:
        score2 = score2 + 1
    akcja = akcja + 1
    lista.append(1)
    if score1 >= 21 or score2 >= 21:
        if score1 >= 21 and score1 - score2 >= 2:
            print('druzyna1 {} :'.format(score1), '{} druzyna2 '.format(score2))
            print('Druzyna1 wygrala')
            break
        elif score2 >= 21 and score2 - score1 >= 2:
            print('druzyna1 {} :'.format(score1), '{} druzyna2 '.format(score2))
            print('Druzyna2 wygrala')
            break
        else:
            print('Dodatkowe rundy')
