from concurrent.futures import process


ones = ('Zero', 'One', 'Two', 'Three', 'Four',
        'Five', 'Six', 'Seven', 'Eight', 'Nine')
twos = ('Ten','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
        'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
        'Seventy', 'Eighty', 'Ninety', 'Hundred')
suf = ('', 'Thousand', 'Million', 'Billion')


def method(number, index, ln):
    if number == '0':
        return 'Zero'

    length = len(number)

    if(length > 3):
        return False

    number = number.zfill(3)
    words = ''

    hnum = int(number[0])
    tnum = int(number[1])
    onum = int(number[2])

    words += '' if number[0] == '0'else ones[hnum]
    words += 'Hundred' if not words == ''else''

    if index == 0 and ln > 3:
        words += 'and'
    elif words == '':
        words += ''
    elif index == 0 and tnum == 0 and onum == 0:
        words += ''
    elif index == 0:
        words += 'and'
    else:
        words += ''

    if(tnum > 1):
        words += tens[tnum-2]
        words += ''
        words += ones[onum]

    elif(tnum == 1):
        words += twos[(int(tnum + onum) % 10)-1]
    elif(tnum == 0):
        words += ones[onum]
    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ''
    if(not len(words) == 0):
        words += suf[index]

    return words


def getWords(number):
    length = len(str(number))

    if length > 12:
        return "This script only supports 12 digit numbers."

    count = length // 3 if length % 3 == 0 else length // 3+1
    copy = count
    words = []

    for i in range(length - 1, -1, -3):
        words.append(
            method(str(number)[0 if i - 2 < 0 else i - 2: i + 1], copy - count, length))
        count -= 1
    final = ''
    for s in reversed(words):
        temp = s + ''
        final += temp
    return final


number = int(input('Enter any number:'))
print('%d in word is %s' % (number, getWords(number)))
