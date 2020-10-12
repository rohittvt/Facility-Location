import pandas as pd
import numpy as np
import math


    
    
def g(x,y,a,b):
    q=1/math.sqrt( (x-a)**2 + (y-b)**2 + 0.05 )
    return q

def sflp(a,b):
    x=[]
    
    x.append( sum(a )/ len(a))
    
    y=[]
    
    y.append( sum(b )/ len(b))
    
    # =============================================================================
    # 
    # x.append( sum (df.a[i] * g( x[-1],y[-1],df.a[i],df.b[i] ) for i in range (15) ) /  sum ( g( x[-1],y[-1],df.a[i],df.b[i] ) for i in range (15) ))
    # 
    # y.append( sum (df.b[i] * g( x[-1],y[-1],df.a[i],df.b[i] ) for i in range (15) ) /  sum ( g( x[-1],y[-1],df.a[i],df.b[i] ) for i in range (15) ))
    # 
    # =============================================================================
    
    for j in range (10000):
        x.append( sum (a[i] * g( x[-1],y[-1],a[i],b[i] ) for i in range (len(a)) ) /  sum ( g( x[-1],y[-1],a[i],b[i] ) for i in range (len(a)) ))
    
        y.append( sum (b[i] * g( x[-1],y[-1],a[i],b[i] ) for i in range (len(b)) ) /  sum ( g( x[-1],y[-1],a[i],b[i] ) for i in range (len(b)) ))
        
        if (math.sqrt( (x[-1]-x[-2])**2 + (y[-1]-y[-2])**2 )) <0.005:
            break 
        
    c=sum ( math.sqrt( (x[-1]-a[i])**2 + (y[-1]-b[i])**2 )  for i in range (len(a)))
    r=[x[-1], y[-1], c]
    return r


R=[]

for j in range (len(A)):
    m=[]
    n=[]    
    for i in range (len(A[j])):
        m.append( df.a[A[j][i]] )
        n.append( df.b[A[j][i]] )
    r=sflp( m  , n )
    R.append(r)
q=pd.DataFrame(R)
q.to_excel(r"C:\Users\ROHIT GUPTA\Desktop\Dops\4\ResultsSFLP.xlsx")
        
    
    
    