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


class AddonTable(BrowserView):

    template = ViewPageTemplateFile('addontable.pt')

    def items(self):
        results = []
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='addon')
        for brain in brains:
            obj = brain.getObject()
            results.append(dict(
                title=brain.Title,
                url=brain.getURL(),
                pypi_link=obj.pypi_link,
                github_link=obj.github_link,
                state=brain.review_state,
                categories=', '.join(obj.categories),
                ))
        return results
