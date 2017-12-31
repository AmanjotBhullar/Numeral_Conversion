#hindu-arabic to roman numeral
def ro(N):
    Nstring = '000' + str(N)
    roman_num = ''

    romans = [['', 'M', 'MM', 'MMM', '', '', '', '', '', ''],
             ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
             ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
             ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]
    
    for i in range(1,5):
        roman_num = roman_num + romans[i-1][int(Nstring[len(Nstring) - (5-i)])]
    print(roman_num)

#roman numeral to hindu-arabic (only valid for 1 to 3999)
def hin_ara(roman_num):
    roms = {'M':1000, 'D': 500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    N = 0
    i = 0
    while i<len(roman_num)-1:
        if int(roms[roman_num[i]]) >= int(roms[roman_num[i+1]]):
            N = N + int(roms[roman_num[i]])
        else:
            N = N - int(roms[roman_num[i]])
        i=i+1
    N = N + int(roms[roman_num[i]])
    print(N)
    
#For example, 1979 = MCMLXXIX and v.v
ro(1979)
hin_ara('MCMLXXIX')