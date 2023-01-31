import sys

from math_tools.functions import quadratic_function

# way of accesing to functions in files in other directories
print(sys.path)
sys.path.append('/home/ewa/PycharmProjects/Podstawy_Pythona/03_Dzien_2/03_Moduly_i_importowanie')

print(quadratic_function(2, 2, 3, 4))