import math

def r2(r):
    P = 1.2/(1-0.15)
    ans = math.exp((8 + 0.5663+((0.4516 * r)/((P-0.5662)*r-P))-3*math.log(3))/3)
    return ans


def ram_ram(r):
    ans = 1/(3*(1-r*0.1))
    return ans


def myu(ram,r):
    Q = 1.2/(1-0.15)
    ans = (0.4516*Q*ram)/math.pow(((Q-0.5662)*r)-Q,2)
    return ans

def new_r(c,ram,r):
    ans = (1-1/(3*c+ram*r))/0.15
    return ans

def finalcal(r, new_r, r2, ram_ram, myu):
    ans = r + 0.5 * ((new_r(ram_ram(r2(r)),myu(ram_ram(r2(r)),r),r))-r)
    return ans

for i in range(3):
    if(i==0):
        r = 2
    rrr = finalcal(r, new_r, r2, ram_ram, myu)
    r = rrr

    print("r1:  "+str(r))
    print("r2:  "+str(r2(r)))
