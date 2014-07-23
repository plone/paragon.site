# -*- coding: UTF-8 -*-
from Acquisition import aq_inner
from plone.app.layout.viewlets import ViewletBase
from plone import api


class SubmitLinkViewlet(ViewletBase):

    def available(self):
        context = aq_inner(self.context)
        if api.user.is_anonymous() and api.content.get_state(context) == 'private':
            return True
