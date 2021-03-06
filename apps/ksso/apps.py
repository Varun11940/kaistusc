"""
KAIST 단일인증서비스 앱.
"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class KssoConfig(AppConfig):
    """
    KAIST 단일인증서비스 커스텀 앱 설정.
    """

    name = 'apps.ksso'
    verbose_name = _("KAIST 단일인증서비스")
