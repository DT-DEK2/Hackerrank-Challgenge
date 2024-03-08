# https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true 

#121 = 11*11
#12321 = 111*111
#1234321 = 1111*1111
n = input()
for i in range(1, int(n)+1):# More than 2 lines will result in 0 score. Do not leave a blank line
    print(int('1'*i)**2)

