print ''
print ''
print ''
print ''
print 'Taking u all to the era of 70s'
print '|*****************************|'
print '*'
print '*'
print '*'
print '*'
print '*'
print 'Moon Techs'
print 'Welcomes you to the Future'
print '*'
print '*'
print '*'
print '*'
print '*'
print '*'
print '|*****************************|'
print ''
print ''
print 'Featuring the Moon Calculator'
print ''
print 'A:Addition'
print 'B:Subtraction'
print 'C:Multiplication'
print 'D:Division'
print 'E:Square of'
print 'F:Power of'
ch=raw_input("Enter your choice:")
if ch=='A':
    n1=int(raw_input('Enter a number:'))
    n2=int(raw_input('Enter another number:'))
    sum=n1+n2
    print 'The sum is:',sum

if ch=='B':
    n1 = int(raw_input('Enter a number:'))
    n2 = int(raw_input('Enter another number:'))
    sum = n1 - n2
    print 'The difference is:', sum

if ch=='C':
    n1 = int(raw_input('Enter a number:'))
    n2 = int(raw_input('Enter another number:'))
    sum = n1 * n2
    print 'The multiplication is:', sum

if ch=='D':
    n1 = int(raw_input('Enter a number:'))
    n2 = int(raw_input('Enter another number:'))
    sum = n1 / n2
    print 'The division is:', sum

if ch=='F':
    n1 = int(raw_input('Enter a number:'))
    n2 = int(raw_input('Enter its powerr:'))
    sum = pow(n1,n2)
    print 'The resultant is:', sum

if ch=='E':
    n1 = int(raw_input('Enter a number:'))
    sum = n1*n1
    print 'The Square is:', sum


