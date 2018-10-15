x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

x = 5
print('Before 5')
if x ==5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5 ')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

x = 42
if x> 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

x = 4
if x>2:
    print('Bigger')
else:
    print('Smaller')
print('All done')


x = 0
if x < 2:
    print('small')
elif x<10:
    print('Medium')
else:
    print('Larger')
print('All done')
        
astr='Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done',istr)
