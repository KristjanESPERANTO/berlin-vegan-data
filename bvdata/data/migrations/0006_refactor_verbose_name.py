# Generated by Django 2.0.2 on 2018-03-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_gastrosubmit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastro',
            name='bar',
            field=models.BooleanField(default=False, verbose_name='Bar'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='breakfast',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Breakfast'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='brunch',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Brunch'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='catering',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Catering'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='childChair',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='High chair'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='city',
            field=models.CharField(default='Berlin', max_length=20, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='cityCode',
            field=models.CharField(max_length=5, verbose_name='Postal code'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment in German'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='commentEnglish',
            field=models.TextField(blank=True, null=True, verbose_name='Comment in English'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='commentOpen',
            field=models.TextField(blank=True, null=True, verbose_name='Comment opening hours'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='delivery',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Delivery service'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='district',
            field=models.CharField(choices=[('CHARLOTTENBURG', 'Charlottenburg'), ('FRIEDRICHSHAIN', 'Friedrichshain'), ('HELLERSDORF', 'Hellersdorf'), ('HOHENSCHÖNHAUSEN', 'Hohenschönhausen'), ('KREUZBERG', 'Kreuzberg'), ('KÖPENICK', 'Köpenick'), ('LICHTENBERG', 'Lichtenberg'), ('MARZAHN', 'Marzahn'), ('MITTE', 'Mitte'), ('NEUKÖLLN', 'Neukölln'), ('PANKOW', 'Pankow'), ('PRENZLAUER BERG', 'Prenzlauer Berg'), ('REINICKENDORF', 'Reinickendorf'), ('SCHÖNEBERG', 'Schöneberg'), ('SPANDAU', 'Spandau'), ('STEGLITZ', 'Steglitz'), ('TEMPELHOF', 'Tempelhof'), ('TIERGARTEN', 'Tiergarten'), ('TREPTOW', 'Treptow'), ('WEDDING', 'Wedding'), ('WEISSENSEE', 'Weißensee'), ('WILMERSDORF', 'Wilmersdorf'), ('ZEHLENDORF', 'Zehlendorf')], max_length=30, null=True, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='dog',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Dogs allowed'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='eiscafe',
            field=models.BooleanField(default=False, verbose_name='Ice cream parlor'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='glutenFree',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Gluten-free options'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='handicappedAccessible',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Wheelchair accessible'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='handicappedAccessibleWc',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Wheelchair accessible toilet'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='imbiss',
            field=models.BooleanField(default=False, verbose_name='Snack bar'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name of location'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='organic',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Organic'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='publicTransport',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Public transport'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='restaurant',
            field=models.BooleanField(default=False, verbose_name='Restaurant'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='seatsIndoor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Seats indoor'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='seatsOutdoor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Seats outdoor'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Street / No'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='telephone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='vegan',
            field=models.IntegerField(choices=[(2, 'Ominvore (vegan labeled)'), (4, 'Vegetarian (vegan labeled)'), (5, 'Vegan')], verbose_name='Vegan friendly'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='gastro',
            name='wlan',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Wi-Fi'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='bar',
            field=models.BooleanField(default=False, verbose_name='Bar'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='breakfast',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Breakfast'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='brunch',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Brunch'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='catering',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Catering'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='childChair',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='High chair'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='city',
            field=models.CharField(default='Berlin', max_length=20, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='cityCode',
            field=models.CharField(max_length=5, verbose_name='Postal code'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment in German'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='commentEnglish',
            field=models.TextField(blank=True, null=True, verbose_name='Comment in English'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='commentOpen',
            field=models.TextField(blank=True, null=True, verbose_name='Comment opening hours'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='delivery',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Delivery service'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='district',
            field=models.CharField(choices=[('CHARLOTTENBURG', 'Charlottenburg'), ('FRIEDRICHSHAIN', 'Friedrichshain'), ('HELLERSDORF', 'Hellersdorf'), ('HOHENSCHÖNHAUSEN', 'Hohenschönhausen'), ('KREUZBERG', 'Kreuzberg'), ('KÖPENICK', 'Köpenick'), ('LICHTENBERG', 'Lichtenberg'), ('MARZAHN', 'Marzahn'), ('MITTE', 'Mitte'), ('NEUKÖLLN', 'Neukölln'), ('PANKOW', 'Pankow'), ('PRENZLAUER BERG', 'Prenzlauer Berg'), ('REINICKENDORF', 'Reinickendorf'), ('SCHÖNEBERG', 'Schöneberg'), ('SPANDAU', 'Spandau'), ('STEGLITZ', 'Steglitz'), ('TEMPELHOF', 'Tempelhof'), ('TIERGARTEN', 'Tiergarten'), ('TREPTOW', 'Treptow'), ('WEDDING', 'Wedding'), ('WEISSENSEE', 'Weißensee'), ('WILMERSDORF', 'Wilmersdorf'), ('ZEHLENDORF', 'Zehlendorf')], max_length=30, null=True, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='dog',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Dogs allowed'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='eiscafe',
            field=models.BooleanField(default=False, verbose_name='Ice cream parlor'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='glutenFree',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Gluten-free options'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='handicappedAccessible',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Wheelchair accessible'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='handicappedAccessibleWc',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Wheelchair accessible toilet'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='imbiss',
            field=models.BooleanField(default=False, verbose_name='Snack bar'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name of location'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='organic',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Organic'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='publicTransport',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Public transport'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='restaurant',
            field=models.BooleanField(default=False, verbose_name='Restaurant'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='seatsIndoor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Seats indoor'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='seatsOutdoor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Seats outdoor'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Street / No'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='submit_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Submitter e-mail'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='telephone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='vegan',
            field=models.IntegerField(choices=[(2, 'Ominvore (vegan labeled)'), (4, 'Vegetarian (vegan labeled)'), (5, 'Vegan')], verbose_name='Vegan friendly'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='gastrosubmit',
            name='wlan',
            field=models.NullBooleanField(choices=[(None, 'unknown'), (True, 'yes'), (False, 'no')], verbose_name='Wi-Fi'),
        ),
    ]
