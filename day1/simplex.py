import numpy as np

def simplex_method(c, A, b):
    # Add slack variables
    m, n = A.shape
    A_slack = np.hstack((A, np.eye(m)))
    c_slack = np.hstack((c, np.zeros(m)))
    
    # Initialize tableau
    tableau = np.vstack((
        np.hstack((A_slack, b.reshape(-1, 1))),
        np.hstack((c_slack, [0]))
    ))
    
    basic_vars = list(range(n, n + m))
    iterations = 0
    
    while True:
        print(f"\nIteration {iterations}:")
        print("Tableau:")
        print(tableau)
        print("Basic variables:", basic_vars)
        
        # Check optimality
        if all(tableau[-1, :-1] >= 0):
            print("\nOptimal solution found!")
            break
        
        # Choose entering variable
        entering = np.argmin(tableau[-1, :-1])
        print(f"Entering variable: x{entering + 1}")
        
        # Choose leaving variable
        ratios = tableau[:-1, -1] / tableau[:-1, entering]
        ratios[tableau[:-1, entering] <= 0] = np.inf
        leaving = np.argmin(ratios)
        print(f"Leaving variable: x{basic_vars[leaving] + 1}")
        
        # Pivot
        pivot = tableau[leaving, entering]
        tableau[leaving] /= pivot
        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i] -= tableau[i, entering] * tableau[leaving]
        
        # Update basic variables
        basic_vars[leaving] = entering
        
        iterations += 1
    
    # Extract solution
    solution = np.zeros(n + m)
    for i, var in enumerate(basic_vars):
        solution[var] = tableau[i, -1]
    
    return solution[:n], tableau[-1, -1]

# Example usage
c = np.array([1.5,2,5])
A = np.array([[1,3], [1, 1]])
b = np.array([3,2])

print("Objective function: Maximize 3x1 + 5x2")
print("Constraints:")
print("x1 <= 4")
print("2x2 <= 12")
print("3x1 + 2x2 <= 18")
print("x1, x2 >= 0")

solution, optimal_value = simplex_method(c, A, b)

print("\nFinal solution:")
print(f"x1 = {solution[0]:.2f}")
print(f"x2 = {solution[1]:.2f}")
print(f"Optimal value: {-optimal_value:.2f}")