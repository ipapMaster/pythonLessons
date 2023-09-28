import sys
import argparse

parser = argparse.ArgumentParser(
    description='Конвертирует числа в десятичную систему счисления')
parser.add_argument('integers', metavar='Набор целых чисел', nargs='+',
                    type=str, help='Числа для конвертации')
parser.add_argument('--base', default=2, type=int,
                    help='Основание системы счисления')
parser.add_argument('--log', default=sys.stdout,
                    type=argparse.FileType('w'),
                    help='Файл с результатами')

args = parser.parse_args()
s = ' '.join(map(lambda x: str(int(x, args.base)), args.integers))

args.log.write(s + '\n')
args.log.close()
