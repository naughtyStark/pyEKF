import sys
sys.path.append('..')

from sympy import *
from helpers import *

# Parameters
q = toVec(symbols('q_0:4'))
R_VEL = Symbol('R_VEL')
dt = Symbol('dt')
gravity = Symbol('gravity')
gravityNED = toVec(0.,0.,gravity)

# Observations
velNEDMeas = toVec(symbols('vnmeas vemeas vdmeas'))

# Inputs
nControlInputs = 6
u = toVec(symbols('u_0:%u' % (nControlInputs,)))
dAngMeas = u[0:3,0]
dVelMeas = u[3:6,0]
w_u = toVec(symbols('w_u_0:%u' % (nControlInputs,)))
dAngNoise = w_u[0:3,0]
dVelNoise = w_u[3:6,0]

# States
nStates = 6
x = Matrix(nStates,1,symbols('x_0:%u' % (nStates,)))
rotVec = x[0:3,0]
velNED = x[3:6,0]

# Covariance matrix
P = Matrix(nStates,nStates,symbols('P_0:%u_0:%u' % (nStates,nStates)))
