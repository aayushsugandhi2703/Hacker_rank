#this problem was about evaluating a polynomial at a given point
# the  polynomial is given in the form of its coefficients

#Some extra Notes about Polynomials:
#poly, rots, polyint, polyder, polyfit, polyval
# poly :Purpose: Construct a polynomial's coefficients from its roots.
#roots :  Find the roots of a polynomial with given coefficients.
# polyint :  Integrate a polynomial.
# polyder :  Differentiate a polynomial.
# polyfit :  Fit a polynomial to data using least squares.
# polyval :  Evaluate a polynomial at a given point.
import numpy
# for poly

roots = [1, 2, 3]
coeffs = numpy.poly(roots)  # returns coefficients of (x - 1)(x - 2)(x - 3)
print(coeffs)
# for roots
p = [1, -6, 11, -6]  # Coefficients of x^3 - 6x^2 + 11x - 6
r = numpy.roots(p)
print(r)  # Output: [3. 2. 1.]

# for polyval
N =list(map(float, input().split()))
X = float(input())
Z=numpy.polyval(N,X)
print(Z)