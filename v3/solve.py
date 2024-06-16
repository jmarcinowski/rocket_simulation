import copy
from scipy.optimize import minimize
from simulate_gains import simulate_gains
from model_rocket import model_rocket


initial_guess = [-0.4, -0.3]
a = [0, 0]

def func_wrapper(lst):
    rocket_copy = copy.deepcopy(model_rocket)
    value = float(simulate_gains({"P": lst[0], "D":lst[1]}, rocket_copy).to("deg").magnitude)
    print(f"Tried input {lst} output was: {value}")
    return value



result = minimize(func_wrapper, initial_guess, method='L-BFGS-B')

# # # Extract optimal PD values
optimal_pd_values = result.x
print(optimal_pd_values)
print(result)