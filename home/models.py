# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    userid = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Service_Provider(models.Model):

    #__Service_Provider_FIELDS__
    providerid = models.IntegerField(null=True, blank=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    username = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)

    #__Service_Provider_FIELDS__END

    class Meta:
        verbose_name        = _("Service_Provider")
        verbose_name_plural = _("Service_Provider")


class Class_Listing(models.Model):

    #__Class_Listing_FIELDS__
    class_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    schedule = models.DateTimeField(blank=True, null=True, default=timezone.now)
    location = models.TextField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    providerid = models.ForeignKey(service_provider, on_delete=models.CASCADE)

    #__Class_Listing_FIELDS__END

    class Meta:
        verbose_name        = _("Class_Listing")
        verbose_name_plural = _("Class_Listing")


class Payment(models.Model):

    #__Payment_FIELDS__
    amount = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    providerid = models.ForeignKey(service_provider, on_delete=models.CASCADE)

    #__Payment_FIELDS__END

    class Meta:
        verbose_name        = _("Payment")
        verbose_name_plural = _("Payment")


class Virtual(models.Model):

    #__Virtual_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    link = models.TextField(max_length=255, null=True, blank=True)
    classid = models.ForeignKey(class_listing, on_delete=models.CASCADE)
    paymentid = models.ForeignKey(payment, on_delete=models.CASCADE)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)

    #__Virtual_FIELDS__END

    class Meta:
        verbose_name        = _("Virtual")
        verbose_name_plural = _("Virtual")



#__MODELS__END
