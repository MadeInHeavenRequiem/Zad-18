n = int(input('podaj ile będzie liczb '))
suma = 0
max_liczba = -1000000000000000000000
min_liczba = 1000000000000000000000
ile_mniejszych_od_3 = 0

for i in range(n):
    liczba = int(input('podaj następną liczbę '))
    print('Podałeś liczbę ' + str(liczba))
    suma = suma + liczba
    print(suma)
    if liczba > max_liczba:
        max_liczba = liczba
    if liczba < min_liczba:
        min_liczba = liczba
    if liczba < 3:
        ile_mniejszych_od_3 = ile_mniejszych_od_3 + 1

print('suma = {}'.format(suma))
print('średnia = {}'.format(suma / n))
print('max = {}'.format(max_liczba))
print('min = {}'.format(min_liczba))
print('mniejszych od 3 = {} liczb'.format(ile_mniejszych_od_3))