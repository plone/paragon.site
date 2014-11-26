=============
paragon.site
=============

ct and config for paragon.plone.org

Installing with the Universal Installer:
----------------------------------------

- Download the Universal Installer, as usual (wget https://launchpad.net/plone/4.3/4.3.3/+download/Plone-4.3.3-UnifiedInstaller.tgz)
- tar -zxvf Plone-4.3.3-UnifiedInstaller.tgz
- cd Plone-4.3.3-UnifiedInstaller
- ./install.sh with your usual preferred option (do ./install.sh --help for options)

Then, copy all files from the doc/ directory here into your buildout, overwriting the buildout.cfg that the universal installer generated.

Change secret.cfg as required. 

Run bin/buildout, and you should be on your merry way.
