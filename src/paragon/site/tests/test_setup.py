# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from paragon.site.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of paragon.site into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if paragon.site is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('paragon.site'))

    def test_uninstall(self):
        """Test if paragon.site is cleanly uninstalled."""
        self.installer.uninstallProducts(['paragon.site'])
        self.assertFalse(self.installer.isProductInstalled('paragon.site'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IParagonSiteLayer is registered."""
        from paragon.site.interfaces import IParagonSiteLayer
        from plone.browserlayer import utils
        self.failUnless(IParagonSiteLayer in utils.registered_layers())
