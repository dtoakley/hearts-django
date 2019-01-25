from django.apps import apps
from django.test.runner import DiscoverRunner


class PytestTestRunner(DiscoverRunner):
    """Runs pytest to discover and run tests."""

    def __init__(self, verbosity=1, failfast=False, keepdb=False, **kwargs):
        self.verbosity = verbosity
        self.failfast = failfast
        self.keepdb = keepdb
        self._enable_unmanaged_models()

    def run_tests(self, test_labels):
        import pytest

        argv = []
        if self.verbosity == 0:
            argv.append('--quiet')
        if self.verbosity == 2:
            argv.append('--verbose')
        if self.verbosity == 3:
            argv.append('-vv')
        if self.failfast:
            argv.append('--exitfirst')
        if self.keepdb:
            argv.append('--reuse-db')

        argv.extend(test_labels)
        return pytest.main(argv)

    @staticmethod
    def _enable_unmanaged_models():
        unmanaged_models = [m for m in apps.get_models() if not m._meta.managed]
        for m in unmanaged_models:
            m._meta.managed = True
