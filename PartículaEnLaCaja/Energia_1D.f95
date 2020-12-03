program Energia_1D
implicit none
!---------------------
real*8 :: a,E,NUM,DEN
real*8,parameter ::h=6.62607E-34 !J s
real*8,parameter ::m=9.10939E-31!Kg
integer        ::nx
!---------------------------
WRITE (*,*) "Este programa procesa el valor de energía de una caja 1D"
WRITE (*,*) "Ingresa el valor del largo de la caja:"
READ  (*,*) a
WRITE (*,*) "Ingresa el valor de n:"
READ  (*,*) nx
NUM = ((h**(2)) * (nx**(2)))
DEN = 8*m*(a**(2))
E = NUM/DEN
WRITE (*,*) "El valor de energía es:",E
ENDPROGRAM Energia_1D