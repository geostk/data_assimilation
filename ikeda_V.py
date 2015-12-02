import numpy as np

def ikeda(state,steps):
    
    """This is the vectorized iterative map for the Ikeda model"""
    # Define the system parameters
    u = .92
    [particles, state_dim] = size(state)    

    # create storage for the trajectories
    traj = np.zeros([particles,state_dim,steps])

    # unpack the state variables
    X = state[:,0]
    Y = state[:,1]

    for i in range(steps):
        T = 0.4 - 6.0*(1 + X**2 + Y**2)**(-1)
        X1 = 1 + u*(X*np.cos(T) - Y*np.sin(T))
        Y1 = u*(X*np.sin(T) + Y*np.cos(T))
        traj[:,0,i] = X1
        traj[:,1,i] = Y1
	X = X1
	Y = Y1
    
    return traj
