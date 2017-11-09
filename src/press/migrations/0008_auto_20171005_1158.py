# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0007_auto_20171004_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='press',
            name='preprint_publication',
            field=models.TextField(blank=True, default='<p>Dear {{ article.owner.full_name }},</p><p>Your preprint has been published on {{ request.press.name }}. It is now available on our <a href="{{ request.press_base_url }}{% url \'preprints_article\' article.pk %}">website</a>.</p><p>Regards,</p><p>{{ request.press.name }} Team</p>', null=True),
        ),
        migrations.AddField(
            model_name='press',
            name='preprint_submission',
            field=models.TextField(blank=True, default='<p>Dear {{ article.owner.full_name }},</p><p>Thank you for your preprint submission. Our Preprint Editor has been notified and will review it before making a decision.</p><p>Regards,</p><p>{{ request.press.name }} Team</p>', null=True),
        ),
    ]