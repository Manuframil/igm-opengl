# N y P significan Negativo y positivo
N = -0.25
P = 0.25

# Representacion de los 3 vertices v1,2 y 3
v1 = [P,P,P]
v2 = [P,P,N]
v3 = [N,P,P]

# Algoritmo para el cálculo de la normal
U = [v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]]
V = [v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]]

x = U[1] * V[2] - U[2] * V[1]
y = U[2] * V[0] - U[0] * V[2]
z = U[0] * V[1] - U[1] * V[0]

# Impresión
x, y, z