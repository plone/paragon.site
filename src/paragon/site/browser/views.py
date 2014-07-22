# -*- coding: UTF-8 -*-
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class AddonView(BrowserView):

    template = ViewPageTemplateFile('addonview.pt')

    def __call__(self):
        return self.template()


class AddonList(BrowserView):

    template = ViewPageTemplateFile('addonlist.pt')

    def items(self):
        results = []
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog.unrestrictedSearchResults(portal_type='addon')
        for brain in brains:
            results.append(dict(
                title = brain.Title,
                state = brain.review_state
                ))
        return results
