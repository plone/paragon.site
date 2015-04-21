# -*- coding: UTF-8 -*-
from Products.CMFPlone.interfaces.constrains import ISelectableConstrainTypes
from datetime import timedelta
from plone import api
from plone.app.controlpanel.security import ISecuritySchema
from plone.app.dexterity.behaviors import constrains
from plone.app.textfield.value import RichTextValue

import logging
import pkg_resources

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
    setup_site(site)


def setup_site(site):
    """Create and configure some initial content"""
    if 'paragon' not in site:
        frontpage = api.content.create(
            container=site,
            type='Document',
            id='paragon',
            title='The hunt is on...')
        frontpage_text = pkg_resources.resource_string(
            __name__, "frontpage.html")
        frontpage.text = RichTextValue(
            frontpage_text,
            'text/html',
            'text/x-html-safe'
        )
    else:
        frontpage = site['paragon']
    frontpage.setLayout("@@addonlist")
    site.setDefaultPage('paragon')

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
    addons.exclude_from_nav = True
    addons.reindexObject()

    api.group.create(
        groupname="Jury",
        title="Jury",
        description="Members of the jury",
        roles=["Jury"])
    api.portal.set_registry_record(
        "plone.app.discussion.interfaces.IDiscussionSettings.globally_enabled",
        True)
    api.portal.set_registry_record(
        "plone.app.discussion.interfaces.IDiscussionSettings.user_notification_enabled",
        True)
    api.group.grant_roles(
        groupname='Jury',
        roles=["Reader", "Reviewer", "Contributor", "Editor"],
        obj=addons)


def delete_default_content(portal):
    to_delete = ['news', 'events', 'Members', 'front-page']
    portal.manage_delObjects(to_delete)
