from abc import ABC
from Lab4.patterns.web_element import ConcreateMediator, ConcreteWebElementBuilder
from Lab4.patterns.director import WebDirector

if __name__ == "__main__":
    builder = ConcreteWebElementBuilder()
    director = WebDirector(builder)

    director.make_button()
    button = builder.product

    director.make_label()
    label = builder.product

    mediator = ConcreateMediator(button, label)

    button.makeAction()