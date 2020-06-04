import re
from itertools import zip_longest, repeat
from operator import gt, ge, lt, le, eq, ne


class Version:
    def __init__(self, version, subversions=4, *args, **kwargs):
        if not isinstance(subversions, int) or subversions > 6 or subversions < 1:
            raise ValueError('kwarg subversions must be an integer between 1 and 6')

        VERSION_REGEX = re.compile(f'^((\\d+\\.?){{1,{subversions}}})$')
        if not VERSION_REGEX.match(version):
            repeats = '.'.join(list(repeat('X', subversions)))
            raise ValueError(f'Version string {version} doesn\'t follow the {repeats} format')

        if version[-1] == '.':
            version = version[:-1]

        self._version = version
        self._version_parts = list(map(int, version.split('.')))

    def __repr__(self):
        return f'Version({self._version})'

    @classmethod
    def _inequality_comparator(cls, version1, version2, op):
        outcomes = {
            lt: (True, False),
            le: (True, True),
            gt: (True, False),
            ge: (True, True)
        }
        zipped_versions = zip_longest(version1, version2, fillvalue=0)
        for p1, p2 in zipped_versions:
            if p1 == p2:
                continue
            elif op(p1, p2):
                return outcomes[op][0]
            else:
                return not outcomes[op][0]
        return outcomes[op][1]

    def __eq__(self, other):
        return self._version_parts == other._version_parts

    def __ne__(self, other):
        return self._version_parts != other._version_parts

    def __lt__(self, other):
        return self._inequality_comparator(self._version_parts, other._version_parts, lt)

    def __le__(self, other):
        return self._inequality_comparator(self._version_parts, other._version_parts, le)

    def __gt__(self, other):
        return self._inequality_comparator(self._version_parts, other._version_parts, gt)

    def __ge__(self, other):
        return self._inequality_comparator(self._version_parts, other._version_parts, ge)
