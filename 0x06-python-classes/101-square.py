#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square shape."""

    def __init__(self, side_length=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            side_length (int): The length of a side of the square.
            position (tuple): The position of the square.
        """
        self.side_length = side_length
        self.position = position

    @property
    def side_length(self):
        """Retrieve the length of a side of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        elif value < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__side_length * self.__side_length

    def my_print(self):
        """Print the square with the '#' character."""
        if self.__side_length == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__side_length):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__side_length)]
            print("")

    def __str__(self):
        """Define the string representation of a Square."""
        if self.__side_length != 0:
            [print("") for _ in range(self.__position[1])]
        for _ in range(self.__side_length):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__side_length)]
            if _ != self.__side_length - 1:
                print("")
        return ("")
