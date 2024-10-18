import numpy as np
def furness_method(Tij, Oi, Dj, max_error=0.05):
    """
    Parameters:
    Tij (numpy array): Trip distribution matrix
    Oi (numpy array): Origin trip vector
    Dj (numpy array): Destination trip vector
    max_error (float): Convergence criteria

    Returns:
    Tij (numpy array): Adjusted trip distribution matrix
    """
     # Initialize iteration counter
    iter = 0

    # Begin iteration process
    while True:
        # Row adjustment
        row_totals = Tij.sum(axis=1)
        Tij = (Tij.T* (Oi / row_totals)).T

        # Column adjustment
        col_totals = Tij.sum(axis=0)
        Tij = Tij * (Dj / col_totals)

        # New row and column sums
        oi_new = Tij.sum(axis=1)
        dj_new = Tij.sum(axis=0)

        # Check convergence
        if np.allclose(oi_new, Oi, atol=max_error) and np.allclose(dj_new, Dj, atol=max_error):
            break

        # Update values for next iteration
        Oi = oi_new
        Dj = dj_new

    return Tij

Tij = np.array([[10, 40, 90, 150], [50, 5, 120, 100], [80, 120, 20, 200], [140,180,210,5]])
Oi = np.array([341, 300, 466, 596])
Dj = np.array([320, 390,490, 503])
Tij_adjusted = furness_method(Tij, Oi, Dj)
Tij_adjusted = np.round(Tij_adjusted)
print(Tij_adjusted,Oi.sum())
