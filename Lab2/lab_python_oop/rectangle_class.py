from Lab2.lab_python_oop.geometric_figure_class import Geometric_figure
from Lab2.lab_python_oop.color_class import Color
class Rectangle(Geometric_figure):
    figure_type = "Прямоугольник"

    def __init__(self,width,heigth,color):
        self.width = width
        self.heigth = heigth
        self.fc = Color()
        self.fc.color = color


    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def Square(self):
        return self.width*self.heigth

    def __repr__(self):
        return("тип фигуры: {}\nширина: {}\nвысота: {}\nцвет:{}\nплощадь: {}\n\n".format
        (
            Rectangle.get_figure_type(),
            self.width,
            self.heigth,
            self.fc.color,
            self.Square()
        ))