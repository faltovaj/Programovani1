spoluzaci = [('Jan', 'Votava'), ('Mirek', 'Frost'), ('Eva', 'Strakova')]
spoluzaci.append(('Jan', 'Ebr'))

# Inicialy
for p1, p2 in spoluzaci:
    print(f'{p1[0]}.{p2[0]}')

# Je mezi spoluzaky Jan?
print('Jmenuje je nejaky spoluzak Jan? ',
      any([p1=='Jan' for p1, p2 in spoluzaci]))
