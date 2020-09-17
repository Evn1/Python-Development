from Lab2.lab_python_oop.rectangle_class import Rectangle
class Quadrate(Rectangle):
    figure_type = "квадрат"
    def __init__(self,side,color):
        self.side = side
        super().__init__(side, side,color)

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __repr__(self):
        return("тип фигуры: {}\nдлина: {}\nцвет:{}\nплощадь: {}\n\n".format
        (
            Quadrate.get_figure_type(),
            self.width,
            self.fc.color,
            self.Square()
        ))