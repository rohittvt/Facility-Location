import pandas as pd
import numpy as np
df=pd.read_csv(r"datacsv.csv")
#df=df[df.index<5]
a=df.a
b=df.b
d=0 
z=1
A=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

def convexhull(d,f):
    global z
    e=f
    if(f > 1):
        for q in range(len(A[d])-1):
            for r in range(q+1,len(A[d])):
                
                a1=df.a[A[d][q]]
                a2=df.a[A[d][r]]  
                b1=df.b[A[d][q]]  
                b2=df.b[A[d][r]]
                m=(b2-b1)/(a2-a1)
                B=[]
                C=[]
                D=[]
                E=[]
               # A.append([])
               # A.append([])
                for x in range(len(A[d])):
                    w=(df.b[A[d][x]]-b1)-m*(df.a[A[d][x]]-a1)
                    if(w<0):
                        B.append(A[d][x])
                    if(w>=0):
                        C.append(A[d][x])
                    if(w<=0):
                        D.append(A[d][x])
                    if(w>0):
                        E.append(A[d][x])
                
                if B not in A:
                    A.append(B)
                    d1=z
                    z=z+1
                    
                    if (len(B)>1):
                        f=f-1
                        convexhull(d1,f)
                        f=e
                if C not in A:
                    A.append(C)
                    d2=z
                    z=z+1
                    
                    if (len(C)>1):
                        f=f-1
                        convexhull(d2,f)
                        f=e
                if D not in A:
                    A.append(D)
                    d1=z
                    z=z+1
                    
                    if (len(D)>1):
                        f=f-1
                        convexhull(d1,f)
                        f=e
                if E not in A:
                    A.append(E)
                    d1=z
                    z=z+1
                    
                    if (len(E)>1):
                        f=f-1
                        convexhull(d1,f)
                        f=e
           
                
convexhull(d,4)

A.remove([])
A.remove(A[0])


H=np.zeros((15,len(A)))
H=pd.DataFrame(H)

for i in range(len(A)):
    H.loc[A[i],i]=1
H.to_excel("Convexhull.xlsx")

    
                
                
                
                
                
                
                
                
                
#if (check(df.a[x],df.b[x],df.a[q],df.b[q],df.a[r],df.b[r]>=0):
                   
                    
                
            