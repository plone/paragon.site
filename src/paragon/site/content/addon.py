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
                title=_(u'Find out')),
     ]
)


class IAddon(model.Schema):
    """ A Plone product
    """

    fieldset(
        'URLs',
        label=u'URLs',
        fields=['pypi_link', 'github_link', 'homepage']
    )

    fieldset(
        'quality',
        label=u'Quality review',
        fields=[
            'pypi_page',
            'public_repo',
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
    )

    title = schema.TextLine(
        title=_(u'package_name', default=u'Name of the Addon'),
        description=_(
            u'as_used_in_buildout',
            default=u'The name you have to add to a buildout (e.g. Products.PloneFormGen)'),
        required=True,
    )

    summary = RichText(
        title=_(u'Short summary'),
        description=_(u'The summary of the features of the product.'),
        required=True,
    )

    directives.widget(screenshots=MultiFileFieldWidget)
    screenshots = schema.List(
        title=u'Screenshots',
        description=_(u'Upload some screenshots showing the main product '
                      u'functionality and features.'),
        value_type=NamedBlobImage(),
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

    directives.widget(pypi_page=RadioFieldWidget)
    pypi_page = schema.Choice(
        title=_(u'Has a curated PyPi page (README.rst/README.md)'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(public_repo=RadioFieldWidget)
    public_repo = schema.Choice(
        title=_(u'Has a public and open to contributions repo (GitHub/BitBucket, etc)'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(updated_last_plone_version=RadioFieldWidget)
    updated_last_plone_version = schema.Choice(
        title=_(u'Works on latest Plone version'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(dexterity_ready=RadioFieldWidget)
    dexterity_ready = schema.Choice(
        title=_(u'Dexterity ready'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(proper_screenshots=RadioFieldWidget)
    proper_screenshots = schema.Choice(
        title=_(u'Has proper screenshots'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(used_in_production=RadioFieldWidget)
    used_in_production = schema.Choice(
        title=_(u'Widely used in production'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(install_uninstall_profile=RadioFieldWidget)
    install_uninstall_profile = schema.Choice(
        title=_(u'Uninstall profile, installs and uninstalls cleanly'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(code_structure=RadioFieldWidget)
    code_structure = schema.Choice(
        title=_(u'Code structure follows best practice'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(maintained=RadioFieldWidget)
    maintained = schema.Choice(
        title=_(u'Existed and maintained for at least 6 months'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(internal_documentation=RadioFieldWidget)
    internal_documentation = schema.Choice(
        title=_(u'Internal documentation (documentation, interfaces, etc.)'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(enduser_documentation=RadioFieldWidget)
    enduser_documentation = schema.Choice(
        title=_(u'End-user documentation'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(tested=RadioFieldWidget)
    tested = schema.Choice(
        title=_(u'Fair test coverage'),
        vocabulary=certification_vocabulary,
        required=True,
    )

    directives.widget(i18n=RadioFieldWidget)
    i18n = schema.Choice(
        title=_(u'Internationalized'),
        vocabulary=certification_vocabulary,
        required=True,
    )


@indexer(IAddon)
def addon_categories(context):
    """Create a catalogue indexer, registered as an adapter, which can
    populate the ``context.categories`` value and index it.
    """
    return context.categories
