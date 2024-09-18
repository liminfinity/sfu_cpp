from app.lib.file import File
from app.lib.args import args
from app.lib.figure_action import FigureAction
from app.lib.filter import filter_figures
from colorama import Fore, Style


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
        print(Fore.LIGHTGREEN_EX + 'Фигуры:' + Style.RESET_ALL)
        for idx, figure in enumerate(figures):
            print(f'{idx + 1}. {figure}')

    def __count_figures(self):
        figures = filter_figures(self.file.read())
        figuresCnt = str(len(figures))
        print(f'Количество фигур: {Fore.LIGHTGREEN_EX + figuresCnt + Style.RESET_ALL}')