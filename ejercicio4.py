#biseccion - divide el intervalo en dos 
def biseccion(f, a, b, t=1e-6):
  if f(a) * f(b) > 0:
    print("La función no cambia de signo en el intervalo dado")
    return None
  c = (a + b) / 2
  while abs(f(c)) > t=1e-6:
    if f(c) * f(a) > 0:
      a = c
    else:
      b = c
    c = (a + b) / 2
  return c
#secante - se usa la tangente para la raiz 
def secante(f, x0, x1, t=1e-6):
  while abs(f(x1)) > t:
    x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
  return x1
#Newton-Raphson - se usa la derivada la de funcion para encontrar la raiz
def newton_raphson(f, df, x, t=1e-6):
  while abs(f(x)) > t:
    x = x - f(x) / df(x)
  return x

#comparación
from math import sin

def f(x):
  return x**3 + x + 16

def df(x):
  return 3*x**2 + 1

#aproximación para la derivada
def dfaprox(x, h=1e-6):
  return (sin(x+h) - sin(x)) / h

a, b = -3, 0
x_biseccion = biseccion(f, a, b)
x_secante = secante(f, a, b)
x_newton_raphson = newton_raphson(f, df_approx, a)

#muestro las soluciones y comparacioon 
print("bisección:", x_biseccion)
print("secante:", x_secante)
print("Newton-Raphson:", x_newton_raphson)

print("Diferencia en decimales entre bisección y secante:", abs(x_biseccion - x_secante))
print("Diferencia en decimales entre bisección y Newton-Raphson:", abs(x_biseccion - x_newton_raphson))
print("Diferencia en decimales entre secante y Newton-Raphson:", abs(x_secante - x_newton_raphson))
