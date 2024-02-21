def my_cubrt(x):
   
   if x<0:
     return -(my_cubrt(abs(x)))
   elif x==0:
     return 0
   else :
     s=1.0
     kmax=100
     tol=1.0e-10
     for k in range(kmax):

     
         s=(2*s+(x/(s**2)))/3.0

         s0=s
         s=(2*s+(x/(s**2)))/3.0
         
         if abs((s0-s)/x)<tol:
             break

     return s    

