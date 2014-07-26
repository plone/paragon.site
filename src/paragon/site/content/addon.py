# -*- coding: utf-8 -*-
from paragon.site import _
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.formwidget.multifile import MultiFileFieldWidget
from plone.indexer import indexer
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

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

certification_vocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'true',
                title=_(u'Yes')),
     SimpleTerm(value=u'false',
                title=_(u'No')),
     SimpleTerm(value=u'does_not_apply',
                title=_(u'Does not apply')),
     SimpleTerm(value=u'todo',
                title=_(u"I don't know")),
     ]
)


class IAddon(model.Schema):
    """ A Plone product
    """

    fieldset(
        'urls',
        label=u'URLs',
        fields=[
            'pypi_link',
            'github_link',
            'homepage'
        ]
    )

    fieldset(
        'experience',
        label=u'User experience quality',
        fields=[
            'updated_last_plone_version',
            'enduser_documentation',
            'used_in_production',
            'maintained',
            'install_uninstall_profile',
            'i18n',
            'proper_screenshots',
        ]
    )

    fieldset(
        'codequality',
        label=u'Code quality',
        fields=[
            'dexterity_ready',
            'code_structure',
            'internal_documentation',
            'tested',
        ]
    )

    fieldset(
        'review',
        label=u'Review',
        fields=['notes', 'verdict']
    )

    title = schema.TextLine(
        title=_(u'package_name', default=u'Addon'),
        description=_(
            u'as_used_in_buildout',
            default=u'The name of the addon as used in buildout (e.g. Products.PloneFormGen)'),
        required=True,
    )

    name = schema.TextLine(
        title=_(u'submitter_name', default=u'Your Name'),
        required=False,
    )

    email = schema.TextLine(
        title=_(u'submitter_email', default=u'Your email'),
        description=_(u'In case the jury has a question'),
        required=False,
    )

    summary = RichText(
        title=_(u'Short summary'),
        description=_(u'The summary of the features of the product.'),
        required=True,
    )

    screenshot_1 = NamedBlobImage(
        title=_(u"Screenshot 1"),
        description=u"",
        required=False,
    )

    screenshot_2 = NamedBlobImage(
        title=_(u"Screenshot 2"),
        description=u"",
        required=False,
    )

    screenshot_3 = NamedBlobImage(
        title=_(u"Screenshot 3"),
        description=u"",
        required=False,
    )

    directives.widget(categories=CheckBoxFieldWidget)
    categories = schema.List(
        title=_(u'Categories'),
        value_type=schema.Choice(
            vocabulary=product_categories),
        required=False,
    )

    # form.widget(captcha=ReCaptchaFieldWidget)
    # captcha = schema.TextLine(
    #     title=u"ReCaptcha",
    #     description=u"",
    #     required=False,
    # )

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

    # directives.widget(pypi_page=RadioFieldWidget)
    # pypi_page = schema.Choice(
    #     title=_(u'Has a curated PyPi page (README.rst/README.md)'),
    #     vocabulary=certification_vocabulary,
    #     default=u"todo",
    #     required=True,
    # )

    # directives.widget(public_repo=RadioFieldWidget)
    # public_repo = schema.Choice(
    #     title=_(u'Has a public and open to contributions repo (GitHub/BitBucket, etc)'),
    #     vocabulary=certification_vocabulary,
    #     default=u"todo",
    #     required=True,
    # )

    directives.widget(updated_last_plone_version=RadioFieldWidget)
    updated_last_plone_version = schema.Choice(
        title=_(u'Works on latest Plone version'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=True,
    )

    directives.widget(used_in_production=RadioFieldWidget)
    used_in_production = schema.Choice(
        title=_(u'Widely used in production'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=True,
    )

    directives.widget(install_uninstall_profile=RadioFieldWidget)
    install_uninstall_profile = schema.Choice(
        title=_(u'Uninstall profile, installs and uninstalls cleanly'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=True,
    )

    directives.widget(maintained=RadioFieldWidget)
    maintained = schema.Choice(
        title=_(u'Existed and maintained for at least 6 months'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=True,
    )

    directives.widget(enduser_documentation=RadioFieldWidget)
    enduser_documentation = schema.Choice(

        title=_(u'End-user documentation'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=True,
    )

    directives.widget(i18n=RadioFieldWidget)
    i18n = schema.Choice(
        title=_(u'Internationalizion ready'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=True,
    )

    directives.widget(proper_screenshots=RadioFieldWidget)
    proper_screenshots = schema.Choice(
        title=_(u'Has proper screenshots'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=False,
    )

    directives.widget(dexterity_ready=RadioFieldWidget)
    dexterity_ready = schema.Choice(
        title=_(u'Dexterity ready'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=False,
    )

    directives.widget(code_structure=RadioFieldWidget)
    code_structure = schema.Choice(
        title=_(u'Code structure follows best practice'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=False,
    )

    directives.widget(internal_documentation=RadioFieldWidget)
    internal_documentation = schema.Choice(
        title=_(u'Internal documentation (how to extend, interfaces, etc.)'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=False,
    )
    directives.widget(tested=RadioFieldWidget)
    tested = schema.Choice(
        title=_(u'Fair test coverage'),
        vocabulary=certification_vocabulary,
        default=u"todo",
        required=False,
    )

    directives.read_permission(notes="paragon.site.ReviewAddon")
    directives.write_permission(notes="paragon.site.ReviewAddon")
    notes = RichText(
        title=_(u'Notes'),
        description=_(u'Notes about the review and the vedict.'),
        required=False,
    )

    directives.read_permission(verdict="paragon.site.ReviewAddon")
    directives.write_permission(verdict="paragon.site.ReviewAddon")
    verdict = RichText(
        title=_(u'Verdict'),
        description=_(u'Notes about the verdict.'),
        required=False,
    )

# from plone.autoform.interfaces import ORDER_KEY
# from paragon.site.content.addon import IAddon
# IAddon.setTaggedValue(ORDER_KEY, [('IBasic.description', 'before', 'ILeadImage.image')])


@indexer(IAddon)
def addon_categories(context):
    """Create a catalogue indexer, registered as an adapter, which can
    populate the ``context.categories`` value and index it.
    """
    return context.categories
