import sympy as sp
sp.init_printing()

# f = sp.exp(-a*t) + sp.exp(-3*a*t)

def L(f):
  return sp.laplace_transform(f,t,s, noconds=True)

def invL(F):
  return sp.inverse_laplace_transform(F,s,t)

t,s = sp.symbols('t,s')
a = sp.symbols('a', real=True, positive=True)

# CASE: Question 1
# a.
y = t**2
print(L(y))

# b.
y = sp.exp(-a*t) + sp.exp(-3*a*t)
# print(L(y))

# c.
y = sp.exp(2*t)*sp.sin(2*t)
# print(L(y))

#d.
y = sp.exp(3*t) + sp.cos(6*t) - (sp.exp(-3*t)*sp.cos(6*t))
# print(L(y))

# e. 
# r = sp.symbols('r')
def r(t):
  return t * sp.Heaviside(t)

y = sp.Heaviside(t-2) + 2*sp.Heaviside(t-3) - 2*r(t-2)
# print(L(y))

# CASE: Question 2
f = sp.Heaviside(t) * sp.Heaviside(3 - t)
g = sp.Heaviside(t) - sp.Heaviside(t - 3)

# b.
# print(L(f))
# print(L(g))
# print(L(f) == L(g))

# CASE: Question 3
f = t-1
F = sp.integrate(f*sp.exp(-s*t), (t, 1, 2))
# print(F)

# CASE: Question 4
# a.
F = 1/s
# print(invL(F))

# b.
F = (10/(s**2 + 25))+(4/(s-3))
# print(invL(F))

# c.
F = (sp.exp(-3*s)*(2*s + 7))/(s**2 + 16)
print(invL(F))

# d.
F = (s**2 + 5*s - 3)/((s**2 + 16)*(s-2))
# print(invL(F))

# CASE: Question 5
f = r(t-2)*sp.Heaviside(3-t) + sp.Heaviside(t-3) - sp.Heaviside(t-4)
# print(L(f))

# CASE: Question 6
y = sp.Function('y')(t)
y_ = sp.Derivative(y,t)     #  y_ == y'
y__ = sp.Derivative(y_,t)   # y__ == y''

# a.
f = y_ + 2*y - 4*t
# print(L(f))

# b.
f = y__ + 3*y_ + 2*y - 6*sp.exp(-t)
# print(L(f))

# c.
g = sp.Function('g')(t)
f = y_ + 4*y - g
# print(L(f))


# CASE: Question 7
f1 = t
f2 = s-t
F1 = sp.integrate(f1*f2, (t, 0, s))
F2 = invL(L(f1)*L(f1))
print(F1)
print(F2)