from django.db import models
from django.utils.translation import ugettext as _

class Tasks(models.Model):
    user = models.CharField(verbose_name=_("Kullanıcı"), max_length=100)
    assignee = models.CharField(verbose_name=_("Atayan Kişi"), max_length=100)
    task_name = models.CharField(verbose_name=_("Görev İsmi"), max_length=100)
    email = models.CharField(verbose_name=_("Email"), max_length=255, default="weveyej837@healteas.com")
    priority = models.CharField(verbose_name=_("Öncelik"), max_length=100, choices=(("Acil", 1),("Önemli", 2),("Az Önemli", 3)))
    status = models.CharField(verbose_name=_("Durum"), max_length=100, choices=(("Bekleniyor", 1),("İşleme Alındı", 2),("Revize Verildi", 3)))
    due_date = models.DateTimeField(auto_now_add=False, verbose_name=_("Termin Tarihi"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Veriliş Tarihi"))

    def __str__(self) -> str:
        return f"{self.task_name}"

    class Meta:
        verbose_name = _('Görevler')
        verbose_name_plural = _('Görevler')
