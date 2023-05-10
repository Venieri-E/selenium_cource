import pytest


@pytest.mark.xfail(strict=False)
def test_xfail_strict():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
