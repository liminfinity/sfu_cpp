from argparse import ArgumentParser
from app.lib.figure_action import FigureAction

parser = ArgumentParser(description='CLI для управления фигурами')

parser.add_argument('-f', '--file', metavar='filename', type=str, default='input.txt', help='Имя файла с фигурами')

parser.add_argument('-o', '--oper', metavar='command', type=FigureAction, default=FigureAction.PRINT, help='Операция над фигурами')

args = parser.parse_args()