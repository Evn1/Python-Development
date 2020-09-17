from Lab2.lab_python_oop.geometric_figure_class import Geometric_figure
from Lab2.lab_python_oop.quadrate_class import Quadrate
from Lab2.lab_python_oop.color_class import Color
from math import pi

class Circle(Quadrate):
    figure_type = "круг"
    def __init__(self,r,color):
        self.r = r
        super().__init__(r, color)

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def Square(self):
        return pi*self.r*self.r

    def __repr__(self):
        return("тип фигуры: {}\nрадиус: {}\nцвет: {}\nплощадь: {}\n\n".format
        (
            Circle.get_figure_type(),
            self.r,
            self.fc.color,
            self.Square()
        ))