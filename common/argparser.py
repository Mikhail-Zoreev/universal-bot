import argparse


def init_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", type=str, action="store", help="Bot token")
    parser.add_argument("admin", type=int, action="store", help="Bot owner id")
    return parser
