# Generated by Django 3.1.5 on 2021-05-25 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20210525_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referred',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='app.trader'),
        ),
    ]
