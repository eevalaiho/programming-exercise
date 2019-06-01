import mock
#import pytest


def test_init():
    from src import hello

    with mock.patch.object(hello, "main", return_value="Hello Eeva"):
        with mock.patch.object(hello, "__name__", "__main__"):
            hello.main("Eeva")


if __name__ == '__main__':
    test_init()


