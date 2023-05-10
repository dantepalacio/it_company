from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


status_choices = [
    ('pending', _('pending')),
    ('reviewed', _('reviewed'))
]

class Contact(models.Model):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(_("email"))
    message = models.TextField(_("message"))

    status = models.CharField(_("status"), max_length=10, choices=status_choices, default=_('pending'))

    class Meta:
        #перенести в другое приложение
        # app_label = _('application')

        verbose_name = _('сontact')
        verbose_name_plural = _('сontacts')

    def __str__(self):
        return self.first_name

class TechsupportAnswer(models.Model):
    answer = models.TextField()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)


class Services(models.Model):
    name = models.CharField(_("title"), max_length=255)
    price = models.PositiveIntegerField(_("price"), null=False, blank=True)
    
    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

class Projects(models.Model):
    name = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to='project_image')
    area = models.CharField(_("area"), max_length=50)
    client = models.CharField(_("client"), max_length=50)
    
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

class News(models.Model):
    title = models.CharField(_("title"), max_length=50)
    info = models.TextField(_("description"), max_length=5000)
    data = models.DateTimeField(_("data"), auto_now_add=True)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')

class AboutCompany(models.Model):
    text = models.TextField(_("description"))

    class Meta:
        verbose_name = _('about company')
        verbose_name_plural = _('about company')

class Communication(models.Model): 
    phone_validator = RegexValidator(
        regex = r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$',
        message = _("Номер телефона должен быть в формате: '+7-7XX-XXX-XX-XX'.")
    )
    city_validator = RegexValidator(
        regex = r'^\+7-\d{4}-\d{2}-\d{2}-\d{2}$',
        message = _("Номер телефона должен быть в формате: '+7-7212-XX-XX-XX'.")
    )
    
    email = models.EmailField(_("email"))
    adress = models.CharField(_("adress"), max_length=255)
    phone = models.CharField(_("phone"), validators=[phone_validator], max_length=15, null=True)
    city_phone = models.CharField(_("city phone"), validators=[city_validator], max_length=15, null=True,)
    location = models.CharField(_("location"), max_length=55)

    class Meta:
        verbose_name = _('communication')
        verbose_name_plural = _('communication')    