a = 100.3526
aErr = 10.1436

print('mereni = ', a, 'chyba = ', aErr)

#fstring
print(f'mereni = {a}, chyba = {aErr}')
print(f'mereni = {a:0.2f}, chyba = {aErr:0.2f}')

#format
print('mereni = {}, chyba = {}'.format(a, aErr))
print('mereni = {0}, chyba = {1}'.format(a, aErr))   # odkaz pres indexy
print('mereni = {:0.2f}, chyba = {:0.2f}'.format(a, aErr))
