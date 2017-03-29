s = open('script1', 'w')

for i in range(1, 250, 35):
    s.write('sphere\n')
    s.write('250 250 0 ' + str(i) + '\n')

s.write('display')
    
