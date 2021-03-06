import errno
import gettext
import os
import sys
from os.path import dirname

from jinja2 import Environment, FileSystemLoader

from ..i18n import N_, locale_dir, translation as default_translation

_top_path = dirname(dirname(dirname(os.path.realpath(__file__))))
inx_path = os.path.join(_top_path, "inx")
template_path = os.path.join(_top_path, "templates")

current_translation = default_translation
current_locale = "en_US"


def build_environment():
    env = Environment(
        loader=FileSystemLoader(template_path),
        autoescape=True,
        extensions=['jinja2.ext.i18n']
    )

    env.install_gettext_translations(current_translation)
    env.globals["locale"] = current_locale

    if "BUILD" in os.environ:
        # building a ZIP release, with inkstitch packaged as a binary
        if sys.platform == "win32":
            env.globals["command_tag"] = '<command reldir="extensions">inkstitch/bin/inkstitch.exe</command>'
        else:
            env.globals["command_tag"] = '<command reldir="extensions">inkstitch/bin/inkstitch</command>'
    else:
        # user is running inkstitch.py directly as a developer
        env.globals["command_tag"] = '<command reldir="extensions" interpreter="python">inkstitch.py</command>'

    return env


def write_inx_file(name, contents):
    inx_locale_dir = os.path.join(inx_path, current_locale)

    try:
        os.makedirs(inx_locale_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    inx_file_name = "inkstitch_%s.inx" % name
    with open(os.path.join(inx_locale_dir, inx_file_name), 'w') as inx_file:
        print >> inx_file, contents.encode("utf-8")


def iterate_inx_locales():
    global current_translation, current_locale

    locales = sorted(os.listdir(locale_dir))
    for locale in locales:
        translation = gettext.translation("inkstitch", locale_dir, languages=[locale], fallback=True)

        # L10N If you translate this string, that will tell Ink/Stitch to
        # generate menu items for this language in Inkscape's "Extensions"
        # menu.
        magic_string = N_("Generate INX files")
        translated_magic_string = translation.ugettext(magic_string)

        if translated_magic_string != magic_string or locale == "en_US":
            current_translation = translation
            current_locale = locale
            yield locale
