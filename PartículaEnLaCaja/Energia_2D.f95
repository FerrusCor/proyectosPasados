program Energia_2D
implicit none
!---------------------
real*8 :: a,b,E,EXT,INT1,INT2
real*8,parameter ::h=6.62607E-34 !J s
real*8,parameter ::m=9.10939E-31!Kg
integer          ::nx,ny
!---------------------------
WRITE (*,*) "Este programa procesa el valor de energía de una caja 2D"
WRITE (*,*) "Ingresa el valor del largo de la caja:"
READ  (*,*) a
WRITE (*,*) "Ingresa el valor del ancho de la caja:"
READ  (*,*) b
WRITE (*,*) "Ingresa el valor de nx:"
READ  (*,*) nx
WRITE (*,*) "Ingresa el valor de ny:"
READ  (*,*) ny
EXT = ((h**(2)) /(8*m))
INT1=(nx/a)**2
INT2=(ny/b)**2
E = EXT*(INT1+INT2)
WRITE (*,*) "El valor de energía es:",E
ENDPROGRAM Energia_2D
