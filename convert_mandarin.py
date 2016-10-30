trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    num = int(us_num)
    if num in range(10):
        return trans[us_num]
    elif num == 10:
        return trans['10']
    elif num > 10 and num <20:
        return trans['10'] + ' ' + trans[us_num[1]]
    elif us_num[1] == '0':
        return trans[us_num[0]] + ' ' +trans['10']
    else:
        return trans[us_num[0]] + ' ' +trans['10'] + ' '+ trans[us_num[1]]

