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
    set_up_content(site)


def set_up_content(site):
    """Create and configure some initial content"""
    if 'addons' in site:
        return
    addons = api.content.create(
        container=site,
        type='addons_folder',
        id='addons',
        title='Addons')

def delete_default_content(portal):
    all_content = portal.portal_catalog()
    if all_content:
        expected = [
            'front-page',
            'news',
            'aggregator',
            'events',
            'aggregator',
            'Members'
        ]
        if not [i.id for i in all_content] == expected:
            return
        to_delete = ['news', 'events', 'Members']
        for i in to_delete:
            obj = portal[i]
            modification_date = obj.modification_date.utcdatetime()
            creation_date = obj.creation_date.utcdatetime()
            delta = modification_date - creation_date
            if delta >= timedelta(seconds=2):
                return
        portal.manage_delObjects(to_delete)
