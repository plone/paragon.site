# -*- coding: UTF-8 -*-
""" Export recommended addons as JSON.
"""
from DateTime import DateTime
from Products.CMFCore.interfaces import IFolderish
from Products.Five.browser import BrowserView
from paragon.site.content.addon import IAddon
from plone import api
from plone.app.textfield.interfaces import IRichTextValue
from zope.schema import getFieldsInOrder

import base64
import json
import os


class AddonJSONList(BrowserView):
    """Exports addons as JSON.
    Returns downloadable JSON from the data.
    """

    def __call__(self):
        """ export all addons as json
        """
        data = self.export()
        pretty = json.dumps(data, sort_keys=True, indent=4)
        self.request.response.setHeader("Content-type", "application/json")
        return pretty

    def export(self):
        results = []
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog(
            portal_type='addon',
            review_state='published'
            )
        for brain in brains:
            obj = brain.getObject()
            data = self.grabDexterityData(obj)
            results.append(data)
        return results

    def grabDexterityData(self, obj):
        """
        Export Dexterity schema data as dictionary object.

        Binary fields are encoded as BASE64.
        """
        data = {}
        for name, field in getFieldsInOrder(IAddon):
            value = getattr(obj, name)
            if IRichTextValue.providedBy(value):
                value = value.output
            if name == "screenshots":
                # handle images
                for index, i in enumerate(value, start=1):
                    shotname = "screenshot_%s" % index
                    raw = getattr(i, "data", None)
                    if raw:
                        data[shotname] = base64.b64encode(raw)
            else:
                data[name] = value
        return data
