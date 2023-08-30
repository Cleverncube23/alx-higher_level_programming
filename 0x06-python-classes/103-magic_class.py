#!/usr/bin/python3
	"""Define a class MagicClass that matches specific bytecode provided."""

import math


class MagicClass:
    """Represent a geometric shape called MagicClass."""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance.

        Args:
            radius (float or int): The radius of the MagicClass instance.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the MagicClass instance.

        Returns:
            float: The area of the MagicClass instance.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculate and return the circumference of the MagicClass instance.

        Returns:
            float: The circumference of the MagicClass instance.
        """
        return (2 * math.pi * self.__radius)

