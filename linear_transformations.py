import math


import numpy as np


class LinearTransformation(object):
    """Linear transformations of tuples. Uses Numpy to handle matrix dot product. 
    Handles scaling, rotation, and translation."""
    # Linear Transformations Definitions
    # a function is a linear transformation if T: R^n -> R^m if it satisfies:
    # 1. T(u + v) = T(u) + T(v)
    # 2. T(ru) = rT(u)
    # for all vectors u, v in R^n for all scalars r

    # scale, rotate, then translate

    def __init__(self, matrix_size):
        if matrix_size != 3 and matrix_size != 4:
            raise ValueError("Matrix size must be either (3): 3x3 or (4): 4x4.")
        if matrix_size == 3:
            raise NotImplementedError("3x3 matrix is not implemented, yet!")
        self.matrix_size = matrix_size
        self.cosine = 0
        self.sine = 0

#------------------------------------------------------------------------------ Properties

    @property
    def cosine(self):
        return self._cosine

    @cosine.setter
    def cosine(self, theta):
        self._cosine = math.cos(theta)

    @property
    def sine(self):
        return self._sine

    @sine.setter
    def sine(self, theta):
        self._sine = math.sin(theta)

#------------------------------------------------------------------------------ Transformations

    def scale_xyz(self, scale_factor_xyz, point):
        """
        @params self, scaling factor of xyz (tuple) or s(float), tuple of 'self.matrix' size
        @return tuple
        """
        if isinstance(scale_factor_xyz, float) or isinstance(scale_factor_xyz, int):
            # if true scale xyz by scale factor
            scale_factor_x = scale_factor_y = scale_factor_z = scale_factor_xyz
        else:
            # tuple unzipping
            scale_factor_x, scale_factor_y, scale_factor_z = (scale_factor_xyz)
        self._check_size(point, self.scale_xyz) # function name
        std_matrix_repr = np.array([[scale_factor_x, 0, 0, 0],
                                    [0, scale_factor_y, 0, 0],
                                    [0, 0, scale_factor_z, 0],
                                    [0, 0, 0, 1]])
        vector_repr = np.array(point)
        return tuple(np.dot(std_matrix_repr, vector_repr))

    def rotation_about_x(self, theta_x, point):
        """
        @params self, radians, tuple of 'self.matrix' size
        @return tuple
        """
        self._check_size(point, self.rotation_about_x) # function name
        self.cosine = theta_x
        self.sine = theta_x
        std_matrix_repr = np.array([[1, 0, 0, 0],
                          [0, self.cosine, -self.sine, 0],
                          [0, self.sine, self.cosine, 0],
                          [0, 0, 0, 1]])
        vector_repr = np.array(point)
        return tuple(np.dot(std_matrix_repr, vector_repr))

    def rotation_about_y(self, theta_y, point):
        """
        @params self, radians, tuple of 'self.matrix' size
        @return tuple
        """
        self._check_size(point, self.rotation_about_y) # function name
        self.cosine = theta_y
        self.sine = theta_y
        std_matrix_repr = np.array([[self.cosine, 0, self.sine, 0],
                          [0, 1, 0, 0],
                          [-self.sine, 0, self.cosine, 0],
                          [0, 0, 0, 1]])
        vector_repr = np.array(point)
        return tuple(np.dot(std_matrix_repr, vector_repr))

    def rotation_about_z(self, theta_z, point):
        """
        @params self, radians, tuple of 'self.matrix' size
        @return tuple
        """
        self._check_size(point, self.rotation_about_z) # function name
        self.cosine = theta_z
        self.sine = theta_z
        std_matrix_repr = np.array([[self.cosine, -self.sine, 0, 0],
                          [self.sine, self.cosine, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        vector_repr = np.array(point)
        return tuple(np.dot(std_matrix_repr, vector_repr))

    def translate_xyz(self, translation_xyz, point):
        """
        @params self, translation xyz, tuple of 'self.matrix' size
        @return tuple
        """
        self._check_size(point, self.translate_xyz) # function name
        translation_x, translation_y, translation_z = (translation_xyz) # tuple unzipping
        std_matrix_repr = np.array([[1, 0, 0, translation_x],
                                    [0, 1, 0, translation_y],
                                    [0, 0, 1, translation_z],
                                    [0, 0, 0, 1]])
        vector_repr = np.array(point)
        return tuple(np.dot(std_matrix_repr, vector_repr))

#------------------------------------------------------------------------------ Debug

    def _check_size(self, point, function_name):
        if len(point) != self.matrix_size:
            help(function_name)
            raise ValueError(f"Size of point: {point} != matrix size: {self.matrix_size}.")

lt = LinearTransformation(4)

print(lt.scale_xyz(2, (1, 2, 3, 1)))