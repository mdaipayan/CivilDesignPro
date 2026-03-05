import numpy as np

def assemble_global_stiffness(nodes, members):

    dof = 6 * len(nodes)
    K = np.zeros((dof, dof))

    for m in members:

        n1, n2, E, A, I, L = m

        k_local = np.array([
            [A*E/L, 0, 0, -A*E/L, 0, 0],
            [0, 12*E*I/L**3, 6*E*I/L**2, 0, -12*E*I/L**3, 6*E*I/L**2],
            [0, 6*E*I/L**2, 4*E*I/L, 0, -6*E*I/L**2, 2*E*I/L],
            [-A*E/L,0,0,A*E/L,0,0],
            [0,-12*E*I/L**3,-6*E*I/L**2,0,12*E*I/L**3,-6*E*I/L**2],
            [0,6*E*I/L**2,2*E*I/L,0,-6*E*I/L**2,4*E*I/L]
        ])

        dof_map = [6*n1,6*n1+1,6*n1+2,6*n2,6*n2+1,6*n2+2]

        for i in range(6):
            for j in range(6):
                K[dof_map[i], dof_map[j]] += k_local[i,j]

    return K
