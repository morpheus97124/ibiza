from math import log2,floor,prod

def euclid(a,b):
    if a==b:
        if a == 0:
            return None
        return b
    x = max(abs(a),abs(b))
    y = min(abs(a),abs(b))
    vk = y
    while vk > 0:
        vk = x%y
        x = y
        y = vk
    return x

def euclid_extended(a,b):
    if a==b:
        if a == 0:
            return None
        return (b,0,1)
    x = max(abs(a),abs(b))
    y = min(abs(a),abs(b))
    vk = y
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    num_of_steps = 1
    while vk > 0:
        vk = x%y
        qk = x//y
        x = y
        y = vk
        if(vk == 0):
                return (x,pow(-1,num_of_steps)*x1,pow(-1,num_of_steps+1)*y1)
        x_tmp = (x1*qk)+x0
        x0 = x1
        x1 = x_tmp
        y_tmp = (y1*qk)+y0
        y0 = x1
        y1 = y_tmp
        num_of_steps = num_of_steps + 1
        print("x = {} y = {}, vk = {}, qk = {} xx = {}, yy = {}".format(x,y,vk,qk,x1,y1))
    return (x,x0,y0)

def check_euclid_extended(a,b):
    a = max(abs(a),abs(b))
    b = min(abs(a),abs(b))
    t = euclid_extended(a,b)
    if t == None:
        return True
    sol = (a*t[1])+(b*t[2])
    print("t = {}, sol = {}, gcd = {}".format(t, sol, t[0]))
    return sol == t[0]

def is_congruent(a,b,mod):
    return (a%mod == b%mod)

def slow_modular_exponentiation(num,exp,mod):
    return (pow(num,exp)%mod)
    
def fast_modular_exponentiation(num,exp,mod):
    exp_cp = exp
    l_powers = []
    for i in range(0,floor(log2(exp))+1):
        if (exp_cp%2) != 0:
            l_powers.append(i)
        exp_cp = exp_cp // 2
    print(l_powers)
    l_nums = []
    for j in l_powers:
        l_nums.append((pow(num,pow(2,j))%mod))
    return (prod(l_nums)%mod)