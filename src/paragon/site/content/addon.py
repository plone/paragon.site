# -*- coding: utf-8 -*-
from five import grok
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.app.dexterity import PloneMessageFactory as _PMF
from plone.app.textfield import RichText
from plone.directives import form
from plone.formwidget.multifile import MultiFileFieldWidget
from plone.indexer import indexer
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model

from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from paragon.site import _

my_vocab = SimpleVocabulary(
    [SimpleTerm(value=True,
                title=_(u'Yes')),
     SimpleTerm(value=False,
                title=_(u'No')),
     SimpleTerm(value=u'does_not_apply',
                title=_(u'Does not apply')),]
)

product_categories = SimpleVocabulary(
    [SimpleTerm(value=u'auth_and_user',
                title=_(u'Authentication and user management')),
     SimpleTerm(value=u'communication',
                title=_(u'Communication')),
     SimpleTerm(value=u'calendaring',
                title=_(u'Calendaring')),
     SimpleTerm(value=u'collaboration',
                title=_(u'Collaboration')),
     SimpleTerm(value=u'databases_and_external_storage',
                title=_(u'Databases and external tools')),
     SimpleTerm(value=u'ecommerce',
                title=_(u'E-commerce')),
     SimpleTerm(value=u'forms_and_surveys',
                title=_(u'Forms, surveys and polls')),
     SimpleTerm(value=u'geo',
                title=_(u'Geospatial')),
     SimpleTerm(value=u'i18n',
                title=_(u'Internationalization')),
     SimpleTerm(value=u'layout_and_presentation',
                title=_(u'Layout and presentation')),
     SimpleTerm(value=u'media',
                title=_(u'Media (photo/video/audio')),
     SimpleTerm(value=u'project_management',
                title=_(u'Project management')),
     SimpleTerm(value=u'search_and_navigation',
                title=_(u'Search and navigation')),
     SimpleTerm(value=u'social_media',
                title=_(u'Social media')),
     SimpleTerm(value=u'theming',
                title=_(u'Theming and look and feel')),
     SimpleTerm(value=u'upload',
                title=_(u'Uploads')),
     SimpleTerm(value=u'weblogs',
                title=_(u'Weblogs')),
     SimpleTerm(value=u'workflow',
                title=_(u'Workflow')),
     SimpleTerm(value=u'widgets',
                title=_(u'Widgets')),
     SimpleTerm(value=u'other',
                title=_(u'Other'))]
)

certification_options = SimpleVocabulary(
    [SimpleTerm(value=True,
                title=_(u'Yes')),
     SimpleTerm(value=False,
                title=_(u'No')),
     SimpleTerm(value=u'does_not_apply',
                title=_(u'Does not apply')),
     ]
)


certification_checklist = [
    'pypi_page',
    'updated_last_plone_version',
    'dexterity_ready',
    'proper_screenshots',
    'used_in_production',
    'install_uninstall_profile',
    'code_structure',
    'maintained',
    'internal_documentation',
    'enduser_documentation',
    'tested',
    'i18n',
]

labels = [
    _(u'Has a curated PyPi page (README.rst/README.md)'),
    _(u'Has a public and open to contributions repo (GitHub/BitBucket, etc)'),
    _(u'Works on latest Plone version'),
    _(u'Dexterity ready'),
    _(u'Has proper screenshots'),
    _(u'Widely used in production'),
    _(u'Uninstall profile, installs and uninstalls cleanly'),
    _(u'Code structure follows best practice'),
    _(u'Existed and maintained for at least 6 months'),
    _(u'Internal documentation (documentation, interfaces, etc.)'),
    _(u'End-user documentation'),
    _(u'Fair test coverage'),
    _(u'Internationalized'),
]

my_fields = ['huhu', 'baba']

class IAddon(model.Schema):
    """ A Plone product
    """

    form.fieldset(
        'URLs',
        label=u'URLs',
        fields=['pypi_link', 'github_link', 'homepage']
    )

    # form.fieldset(
        # 'quality',
        # label=u'Quality review',
        # fields=['certification', ]
    # )

    title = schema.TextLine(
        title=_PMF(u'label_title', default=u'Title'),
        required=True,
    )

    summary = RichText(
        title=_(u'Short summary'),
        description=_(u'The summary of the features of the product.'),
        required=True,
    )

    form.widget(screenshots=MultiFileFieldWidget)
    screenshots = schema.List(
        title=u'Screenshots',
        description=_(u'Upload some screenshots showing the main product '
                      u'functionality and features.'),
        value_type=NamedBlobImage(),
        required=False,
    )

    categories = schema.List(
        title=_(u'Categories'),
        value_type=schema.Choice(
            vocabulary=product_categories),
        required=False,
    )

    pypi_link = schema.TextLine(
        title=_(u'Pypi URL'),
        description=_(u'The PyPi egg URL for the releases of this product.'),
        required=True
    )

    github_link = schema.TextLine(
        title=_(u'GitHub URL'),
        description=_(u'Link to repository (GitHub or similar) for this product.'),
        required=True
    )

    homepage = schema.TextLine(
        title=_(u'Homepage URL'),
        description=_(u'The home page URL for this product, if any.'),
        required=False
    )

    # form.widget(certification=CheckBoxFieldWidget)
    # certification = schema.Set(
    #     title=_(u'Certification checklist'),
    #     description=_(u'This is the feature checklist of add-on developing. Once the product accomplish all of them, you can send it for review and earn the certified add-on badge.'),
    #     value_type=schema.Choice(
    #         vocabulary=certification_checklist),
    #     required=False
    # )

    for i in certification_checklist:
        i = schema.Choice(
            title=u'uhuh',
            vocabulary=my_vocab,
        )


@indexer(IAddon)
def addon_categories(context):
    """Create a catalogue indexer, registered as an adapter, which can
    populate the ``context.categories`` value and index it.
    """
    return context.categories
grok.global_adapter(addon_categories, name='addon_categories')
