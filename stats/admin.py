# generated: c3d3b752e00731952055e3f179448e1a


from django.contrib import admin
from django import forms
from stats.models import Currency, Rate
from django.contrib.admin import ModelAdmin


class CurrencyModelForm(forms.ModelForm):
    class Meta:
        model = Currency
        exclude = ()
        widgets = {

        }


class CurrencyAdmin(ModelAdmin):
    """
    #currency
    Currency Admin
    """

    form = CurrencyModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name']
        }),)

    list_display = ['name']


admin.site.register(Currency, CurrencyAdmin)


class RateModelForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude = ()
        widgets = {

        }


class RateAdmin(ModelAdmin):
    """
    #rate
    Rate Admin
    """

    form = RateModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['currency', 'date', 'rate', 'volume']
        }),)

    list_display = ['currency', 'date', 'rate', 'volume']


admin.site.register(Rate, RateAdmin)
