import pytest


def test_case():
    print(111111)


class TestCase:
    def test_case_01(self):
        assert 1

    @pytest.mark.xfail()
    def test_case_02(self):
        assert 1

    @pytest.mark.xfail()
    def test_case_03(self):
        assert 0


if __name__ == "__main__":
    pytest.main(['2-pytest回顾.py','-v'])
