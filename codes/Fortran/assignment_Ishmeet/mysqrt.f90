program mysqrt
   implicit none
   real(kind=8)::y,z
   real(kind=8),external::sqrt2
   y=2.0
   z=sqrt2(y)
   print *,z
   
	    
end program mysqrt
real(kind=8) function sqrt2(x)
   implicit none
   
   real(kind=8) ,intent(in)::x
   
   real(kind=8):: s
   integer, parameter ::kmax=100
   integer::i
   
   s=1.0
   
   
   do i=1,kmax
		
		s = 0.5 * (s + (x/s))
		sqrt2=s
   enddo
end function sqrt2
