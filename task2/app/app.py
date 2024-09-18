from app.lib.file import File
from app.lib.args import args
from app.lib.figure_action import FigureAction
from app.lib.filter import filter_figures

class App:
    def __init__(self):
        self.file = File(args.file)
        self.oper = args.oper

    def run(self):
        match self.oper:
            case FigureAction.PRINT:
                self.__print_figures()
            case FigureAction.COUNT:
                self.__count_figures()
            case _:
                print('Неизвестная команда')

    def __print_figures(self):
        figures = filter_figures(self.file.read())
        print('Фигуры:')
        for idx, figure in enumerate(figures):
            print(f'{idx + 1}. {figure}')

    def __count_figures(self):
        figures = filter_figures(self.file.read())
        print(len(figures))