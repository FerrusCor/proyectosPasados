program Energia_3D_iter
implicit none
!Programa creado para calcular el valor de energía respecto a una caja de 2x2x2
!La referencia 2x2x2 puede ser facilmente cambiada en la linea n° 37.
!---------------------
real*8 :: a,b,c,E,EXT,INT1,INT2,INT3
real*8 :: E111_simetrico,razon
real*8,parameter ::h=6.62608E-34 !J s
real*8,parameter ::m=9.10939E-31!Kg
integer          ::nx=1,ny=1,nz=1
integer          ::limite=4,calculado=0 !Modulacion de cuantos valores quiero obtener
!---------------------------
OPEN(UNIT=9,FILE="intento_2_4_1.bat",ACTION="WRITE") !Eligo como se llama el archivo de respaldo
WRITE (*,*) "nota:Escribiendo datos en FILE. Usando como referencia E111 en caja 2x2x2"
WRITE (*,*) "Este programa procesa el valor de energía de una caja 3D"
WRITE (*,*) "Ingresa el valor del largo de la caja:"
READ  (*,*) a
WRITE (*,*) "Ingresa el valor del ancho de la caja:"
READ  (*,*) b
WRITE (*,*) "Ingresa el valor de la altura de la caja:"
READ  (*,*) c
IF (a == b .and. b == c) THEN
  WRITE(9,*) "Es una caja simetrica de",a**3,"U.A"
  WRITE(*,*) "Es una caja simetrica de",a**3,"U.A"
ELSEIF (a == b .and. b /= c)THEN
  WRITE(9,*) "Es una caja Asimetrica de",a*b*c,"U.A"
  WRITE(*,*) "Es una caja Asimetrica de",a*b*c,"U.A"
ELSEIF (a /= b .and. b/=c .and. a /=c)THEN
  WRITE(9,*) "Es una caja completamente Asimetrica de",a*b*c,"U.A"
  WRITE(*,*) "Es una caja completamente Asimetrica de",a*b*c,"U.A"
ENDIF
DO WHILE (nx <=limite .and. ny<=limite .and. nz<=limite)
 EXT = ((h**(2)) /(8*m))
 INT1=(nx/a)**2
 INT2=(ny/b)**2
 INT3=(nz/c)**2
 E111_simetrico= EXT*(0.75)
 WRITE (*,*) E111_simetrico
 E = EXT*(INT1+INT2+INT3)
 calculado=calculado + 1
 razon = E/E111_simetrico
 WRITE (*,*) "El valor de energia es:",E,"E",nx,ny,nz
 WRITE (*,*) razon,"veces E111."
 WRITE (9,*) "E",nx,ny,nz, "=" ,razon,"E111"
 IF (nx == ny .and. ny == nz)THEN !211
   nx = nx + 1
 ELSEIF (nx-1 == ny .and. nx-1==nz)THEN
   nx = nx - 1
   ny = ny + 1 !121
 ELSEIF (ny-1 == nx .and. ny - 1 == nz)THEN
   ny = ny - 1
   nz = nz + 1!112
 ELSEIF (nz-1 == nx .and. nz-1 ==ny) THEN
   ny = ny + 1!122
 ELSEIF (ny == nz .and. ny - 1 == nx .and. nz - 1 == nx)THEN
   nx = nx + 1
   ny = ny - 1!212
 ELSEIF (nx == nz .and. nx-1 == ny) THEN
   ny = ny + 1
   nz = nz - 1!221
 ELSEIF (nx == ny .and. nx - 1 ==nz)THEN
   nz = nz + 1
 ENDIF
ENDDO
WRITE (*,*)calculado
CLOSE(9)
ENDPROGRAM Energia_3D_iter