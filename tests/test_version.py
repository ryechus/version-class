import pytest

from util.version import Version

@pytest.mark.parametrize('version1, version2, outcome', [
    ('5.1', '5.1.2', True),
    ('5.1.', '5.1.2', True),
    ('5.10', '5.9.9', False),
    ('5.1', '5.0.9', False),
    ('5.1', '5.1', False)
])
def test_versions_less_than(version1, version2, outcome):
    assert (Version(version1) < Version(version2)) == outcome


@pytest.mark.parametrize('version1, version2, outcome', [
    ('5.1', '5.1.2', True),
    ('5.1.', '5.1.2', True),
    ('5.10', '5.9.9', False),
    ('5.1', '5.0.9', False),
    ('5.1', '5.1', True)
])
def test_versions_less_than_equal(version1, version2, outcome):
    assert (Version(version1) <= Version(version2)) == outcome


@pytest.mark.parametrize('version1, version2, outcome', [
    ('5.1', '5.1.2', False),
    ('5.1.', '5.1.2', False),
    ('5.10', '5.9.9', True),
    ('5.1', '5.0.9', True),
    ('5.1', '5.1', False)
])
def test_versions_greater_than(version1, version2, outcome):
    assert (Version(version1) > Version(version2)) == outcome


@pytest.mark.parametrize('version1, version2, outcome', [
    ('5.1', '5.1.2', False),
    ('5.1.', '5.1.2', False),
    ('5.10', '5.9.9', True),
    ('5.1', '5.0.9', True),
    ('5.1', '5.1', True)
])
def test_versions_greater_than_equal(version1, version2, outcome):
    assert (Version(version1) >= Version(version2)) == outcome
