import math
import random

def make_monte_carlo_integral(P,x1,y1,x2,y2):
    buffer={'total_trails':0,'total_in':0}
    lowx=min(x1,x2)
    lowy=min(y1,y2)
    highx=max(x1,x2)
    highy=max(y1,y2)
    def simulator(*args):
        if len(args)==2 and args[0]=="run trials":
            buffer['total_trails']+=args[1]
            for i in range(args[1]):
                x=random.uniform(lowx, highx)
                y=random.uniform(lowy, highy)
                if P(x,y):
                    buffer['total_in']+=1
        elif args[0]=="get estimate":
            return buffer['total_in']/buffer['total_trails']*abs(x1-x2)*abs(y1-y2)
        elif args[0]=="trials":
            return buffer['total_trails']
    return simulator


def circle(x,y):
    return math.sqrt(x*x+y*y) < 1
    
circle_estimate = make_monte_carlo_integral(circle,-1,-1,1,1)
