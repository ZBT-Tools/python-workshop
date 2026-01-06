import numpy as np
my_vec = np.array([[1, 2, 3, 4]])
print(my_vec)
my_vec_t = my_vec.transpose() #np.transpose(my_vec)
print(my_vec_t)
print(my_vec_t.shape)
print(my_vec.shape)

my_mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(my_mat)
print(my_mat.shape) 

my_first_result = my_mat * my_vec
my_second_result = my_mat * my_vec_t
print(my_first_result)
print(my_second_result)