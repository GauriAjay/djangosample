# Generated by Django 4.0.3 on 2022-04-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
