"""App entry point."""
import unittest
import argparse

from api import create_app


def run(app):
    app.run(host='0.0.0.0', port=3000)


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('./api/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


def parse_args():
    parser = argparse.ArgumentParser(description='API Rest')
    parser.add_argument("mode", help="Run Mode [dev | prod | test]")
    args = parser.parse_args()
    return args


def main(args):
    mode = args.mode
    app = create_app(mode)
    if mode == "test":
        test()
    else:
        run(app)


if __name__ == '__main__':
    main(parse_args())
