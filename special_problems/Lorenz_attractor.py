# Libraries needed
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# differential equations used in attractor
def Lorenz(state, sigma=10, rho=28, beta = 8/3):
    x,y,z = state
    dx_dt = sigma*(y-x)
    dy_dt = x*(rho-z)-y
    dz_dt = x*y - beta*z
    return np.array([dx_dt, dy_dt, dz_dt])


# RK4 method 
def rk4(state,dt = 0.001):
    k1 = Lorenz(state)
    k2 = Lorenz(state+0.5*dt*k1)
    k3 = Lorenz(state + 0.5*dt*k2)
    k4 = Lorenz(state + dt*k3)
    return state + (dt/6)*(k1+k4+2*k2+2*k3)

# initial conditions
state = np.array([1,1,1])
state1 = np.array([1.0001,1,1])

# time steps
dt = 0.001
steps = 100000
x_traj,y_traj,z_traj = [state[0]],[state[1]],[state[2]]
x_traj1,y_traj1,z_traj1 = [state1[0]],[state1[1]],[state1[2]]
x,y,z=state[0],state[1],state[2]
x1,y1,z1=state1[0],state1[1],state1[2]
for i in range(steps):
    # updating initial conditions
    x,y,z = rk4(state = state ,dt = dt)
    x1,y1,z1 = rk4(state = state1,dt = dt)
    state = np.array([x,y,z])
    state1 = np.array([x1,y1,z1])

    # append trajactories
    x_traj.append(x)
    y_traj.append(y)
    z_traj.append(z)
    x_traj1.append(x1)
    y_traj1.append(y1)
    z_traj1.append(z1)

# plotting
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_traj, y_traj, z_traj, linewidth=0.5)
ax.plot(x_traj1, y_traj1, z_traj1, linestyle='dashed', linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
