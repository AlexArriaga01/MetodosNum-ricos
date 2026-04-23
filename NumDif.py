def DifCen(x,h,f):
    t_i=x
    h=0.25
    ti=[t_i,t_i+h,t_i+2*h,t_i-2*h,t_i-h]
    return (1/(12*h))*(-f(ti[2])+8*f(ti[1])-8*f(ti[-1])+f(ti[-2]))

def DifAtr(x,h,f):
    t_i=x
    h=0.25
    ti=[t_i,t_i+h,t_i+2*h]
    return (4*f(ti[1])-3*f(ti[0])-f(ti[2]))/(2*h)