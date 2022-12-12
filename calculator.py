def math_exp(att):
    x = []
    for i in range(len(att)):
        if att[i] in ("*", "/", "-", "+", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ","):
            x.append(att[i])
        else:
            continue
    u = "".join(map(str,x))
    
    return u
    

def calc(ev):
    print(eval(ev))

z = input()
pre_result = math_exp(z)
result = calc(pre_result)
