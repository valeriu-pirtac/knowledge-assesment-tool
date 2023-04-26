from argparse import ArgumentParser


def build_app_args():
    """application cli arguments"""

    parser = ArgumentParser(prog="kat", description="Python Knowledge Assessment Tool")
    parser.add_argument(
        "--generate",
        "-g",
        dest="gen_enabled",
        action="store_true",
        help="generate list of exercises",
    )

    return parser.parse_args()
