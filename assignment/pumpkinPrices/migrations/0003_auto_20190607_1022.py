# Generated by Django 2.2.1 on 2019-06-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumpkinPrices', '0002_auto_20190604_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumpkin',
            name='variety',
            field=models.CharField(choices=[('HOWDEN_TYPE', 'HOWDEN_TYPE'), ('PIE_TYPE', 'PIE_TYPE'), ('MINIATURE', 'MINIATURE'), ('HOWDEN_WHITE_TYPE', 'HOWDEN_WHITE_TYPE'), ('CINDERELLA', 'CINDERELLA'), ('FAIRY_TALE', 'FAIRY_TALE'), ('BIG_MACK_TYPE', 'BIG_MACK_TYPE'), ('MIXED_HEIRLOOM_VARIETIES', 'MIXED_HEIRLOOM_VARIETIES'), ('BLUE_TYPE', 'BLUE_TYPE'), ('KNUCKLE_HEAD', 'KNUCKLE_HEAD')], default='HOWDEN_TYPE', max_length=100),
        ),
    ]