import random
import string


def randompasswordgen():
    list1 = ['1','2','3','4','5','6','7','8','9','0','!','#','$','%','&','(','*','+','-','.','/',':',';','<',
            '=','>','?','@','[','/',']','^','_','`','{','|','}','~',
            '.',"a",'b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    print('enter the length of the password :')
    a = int(input('> '))
    random.shuffle(list1)
    password = []
    for x in range(1,a+1):
        jeb_ = random.choice(list1)
        password.append(jeb_)

    the_real_password = "".join(password)
    print(the_real_password)
    return password

randompasswordgen()
