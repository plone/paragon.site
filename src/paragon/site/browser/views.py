# -*- coding: UTF-8 -*-
from AccessControl.SecurityManagement import getSecurityManager
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class AddonView(BrowserView):

    template = ViewPageTemplateFile('addonview.pt')

    def __call__(self):
        return self.template()


class SubmitAddon(BrowserView):

    def __call__(self):
        api.content.transition(self.context, 'submit')
        api.portal.show_message(
            message="Thank you for submitting the addon '%s'" % self.context.title,
            request=self.request,
            type='info')
        portal_url = api.portal.get().absolute_url()
        self.request.response.redirect(portal_url)


class AddonList(BrowserView):

    template = ViewPageTemplateFile('addonlist.pt')

    def items(self):
        results = []
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog.unrestrictedSearchResults(
            portal_type='addon',
            sort_on='sortable_title',
            review_state='pending',
        )
        for brain in brains:
            results.append(dict(
                title = brain.Title,
                state = brain.review_state,
                pypi_link = brain.pypi_link,
                ))
        return results

    def can_review(self):
        security = getSecurityManager()
        if security.checkPermission('paragon.site: Review Addon', self.context):
            return True


class AddonTable(BrowserView):
    """
    """

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
                pypi_link=brain.pypi_link,
                github_link=obj.github_link,
                state=brain.review_state,
                categories=', '.join(obj.categories),
                submitter=obj.name,
                ))
        return results
