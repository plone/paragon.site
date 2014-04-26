from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class AddonView(BrowserView):

    template = ViewPageTemplateFile('addonview.pt')

    def __call__(self):
        return self.template()
