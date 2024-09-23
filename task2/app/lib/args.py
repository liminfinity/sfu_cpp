from argparse import ArgumentParser
from app.lib.figure_action import FigureAction

parser = ArgumentParser(description='CLI для управления фигурами')

parser.add_argument('-f', '--file', metavar='filename', type=str, required=True, help='Имя файла с фигурами')

parser.add_argument('-o', '--oper', metavar='command', type=FigureAction, default=FigureAction.PRINT, help='Операция над фигурами')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()