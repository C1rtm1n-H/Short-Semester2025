import numpy as np
from scipy.optimize import minimize

def svm(X, y):
    '''
    SVM Support vector machine.

    INPUT:  X: training sample features, P-by-N matrix.
            y: training sample labels, 1-by-N row vector.

    OUTPUT: w: learned perceptron parameters, (P+1)-by-1 column vector.
            num: number of support vectors

    '''
    P, N = X.shape
    w = np.zeros((P + 1, 1))
    num = 0

    # YOUR CODE HERE
    # Please implement SVM with scipy.optimize. You should be able to implement
    # it within 20 lines of code. The optimization should converge wtih any method
    # that support constrain.
    #TODO
    # begin answer
    y_col = y.flatten()
    K = X.T @ X
    def objective(alpha):
        return 0.5 * np.sum(np.outer(alpha, alpha) * np.outer(y_col, y_col) * K) - np.sum(alpha)
    def eq_constraint(alpha):
        return np.dot(alpha, y_col)
    
    alpha_0 = np.zeros(N)
    bounds = [(0, None) for _ in range(N)]
    constraints = {'type': 'eq', 'fun': eq_constraint}
    result = minimize(objective, alpha_0, bounds=bounds, constraints=constraints)
    alpha = result.x
    w_flat = np.sum((alpha * y_col)[:, np.newaxis] * X.T, axis=0)
    sv_indices = np.where(alpha > 1e-6)[0]
    num = len(sv_indices)

    if num > 0:
        b = np.mean(y_col[sv_indices] - X[:, sv_indices].T @ w_flat)
        w = np.insert(w_flat, 0, b).reshape(-1, 1)
    # end answer
    return w, num

