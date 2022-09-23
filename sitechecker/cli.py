import argparse

def read_user_cli_args():
    """ Cria uma aplicação de linha de comando, recebendo os argumentos da linha de comando"""
    parser = argparse.ArgumentParser(
        prog="sitechecker",description="Teste a disponibilidade de uma URL"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLS",
        nargs="+",
        type=str,
        default=[],
        help="Insira um ou mais URLs"
    )
    return parser.parse_args()