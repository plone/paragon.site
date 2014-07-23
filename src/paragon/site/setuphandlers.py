# -*- coding: UTF-8 -*-
from plone.app.controlpanel.security import ISecuritySchema
from plone import api
from Products.CMFPlone.interfaces.constrains import ISelectableConstrainTypes
from plone.app.dexterity.behaviors import constrains
from datetime import timedelta

import logging

PROFILE_ID = 'profile-paragon.site:default'
logger = logging.getLogger('paragon.site')


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('paragon.site_various.txt') is None:
        return

    site = api.portal.get()
    delete_default_content(site)
    setup_content(site)
    setup_groups(site)


def setup_content(site):
    """Create and configure some initial content"""
    if 'addons' in site:
        reinstall = True
        addons = site['addons']
    else:
        addons = api.content.create(
            container=site,
            type='addons_folder',
            id='addons',
            title='Addons')
    addons.setLayout("@@addontable")
    site.setLayout("@@addonlist")
    addons.exclude_from_nav = True
    addons.reindexObject()


def delete_default_content(portal):
    to_delete = ['news', 'events', 'Members', 'front-page']
    portal.manage_delObjects(to_delete)


def setup_groups(site):
    api.group.create(
        groupname="Jury",
        title="Jury",
        description="Members of the jury",
        roles=["Jury"])