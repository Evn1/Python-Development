from Lab2.lab_python_oop.geometric_figure_class import Geometric_figure
from Lab2.lab_python_oop.color_class import Color
from Lab2.lab_python_oop.rectangle_class import Rectangle
from Lab2.lab_python_oop.quadrate_class import Quadrate
from Lab2.lab_python_oop.circle_class import Circle

def main():
    Rectangle1 = Rectangle(3, 4, "красный")
    print(Rectangle1)
    Quadrate1 = Quadrate(3, "green")
    print(Quadrate1)
    Circle1 = Circle(3,"желтый")
    print(Circle1)
if __name__ == "__main__":
    main()
