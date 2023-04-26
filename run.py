import sys

import kat.cli.cli_args as cli


def main():
    """main function"""

    if len(sys.argv) == 1:
        sys.argv.append("-h")

    args = cli.build_app_args()

    if args.gen_enabled:
        print("==> Generate list of exercises")


if __name__ == "__main__":
    main()
