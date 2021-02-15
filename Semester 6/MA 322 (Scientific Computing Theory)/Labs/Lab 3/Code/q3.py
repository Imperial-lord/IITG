# Question 3 Lab 03
# AB Satyaprakash (180123062)

# imports ----------------------------------------------------------------------
import sympy as sp
# ------------------------------------------------------------------------------
# functions --------------------------------------------------------------------


def f(x):
    # Use the result obtained in line 28
    return -5*(x**3)+(8*(x**2))+(x**4)


# ------------------------------------------------------------------------------
print('Given Δ_4(P(0))=24, Δ_3(P(0))=6, Δ_2(P(0))=0 and ΔP(x)=P(x+1)-P(x).')
print('Using the 3rd relation, i.e., Δ_2(P(0))=0,')
print('We can write this as P(x) = P(0) + ∆P(0)·x + x(x−1)(x−2) + x(x−1)(x−2)(x−3).')
print('To obtain Δ_2(P(10)) we will use Δ_2(P(x)) at x = 10, which will remove the constant and linear term.')

x = sp.Symbol('x')
px = x*(x-1)*(x-2)+x*(x-1)*(x-2)*(x-3)
px = sp.expand(px)

print('This makes Δ_2(P(x)) = Δ_2([{}]).'.format(px))
print('Again using the fact that second differences will remove the const and linear term,')
print('We get Δ_2([-5*(x**3)+(8*(x**2))+(x**4)]) at x=10.')
print('Finally use: ∆_2([f(x)]) = f(x+2)− 2f(x+1)+ f(x).')


ans_x = sp.expand(f(x+2) - 2*f(x+1) + f(x))
# substituing the value of x = 10 to evaluate the expression at 10!
ans_10 = ans_x.subs(x, 10)
print('Thus, the value of ∆_2(P(10)) =', ans_10)

# Question 3 ends --------------------------------------------------------------
