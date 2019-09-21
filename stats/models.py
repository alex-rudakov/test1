from django.db import models


from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    """
    Currency
    """

    name = models.CharField(verbose_name=_(
        'Name'), null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")


class Rate(models.Model):
    """
    Rate
    """

    currency = models.ForeignKey("stats.Currency", verbose_name=_(
        'Currency'), null=True, blank=True, related_name='rates', on_delete=models.PROTECT)
    date = models.DateField(verbose_name=_('Date'), null=True, blank=True)
    rate = models.DecimalField(verbose_name=_(
        'Rate'), null=True, blank=True, max_digits=20, decimal_places=8)
    volume = models.DecimalField(verbose_name=_(
        'Volume'), null=True, blank=True, max_digits=20, decimal_places=8)

    class Meta:
        verbose_name = _("Rate")

        indexes = [
            models.Index(fields=['-date', 'currency'], name='stats_index'),
        ]
