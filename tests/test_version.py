import os
import unittest

import pystac as ps
from tests.utils import TestCases


class VersionTest(unittest.TestCase):
    def test_override_stac_version_with_environ(self):
        version = os.environ.get('PYSTAC_STAC_VERSION_OVERRIDE')

        try:
            override_version = '1.0.0-gamma.2'
            os.environ['PYSTAC_STAC_VERSION_OVERRIDE'] = override_version
            cat = TestCases.test_case_1()
            d = cat.to_dict()
            self.assertEqual(d['stac_version'], override_version)
        finally:
            if version is None:
                del os.environ['PYSTAC_STAC_VERSION_OVERRIDE']
            else:
                os.environ['PYSTAC_STAC_VERSION_OVERRIDE'] = version

    def test_override_stac_version_with_call(self):
        version = ps.get_stac_version()
        try:
            override_version = '1.0.0-delta.2'
            ps.set_stac_version(override_version)
            cat = TestCases.test_case_1()
            d = cat.to_dict()
            self.assertEqual(d['stac_version'], override_version)
        finally:
            ps.set_stac_version(version)
