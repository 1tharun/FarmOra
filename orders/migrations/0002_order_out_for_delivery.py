from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[
                    ('pending', 'Pending'),
                    ('accepted', 'Accepted'),
                    ('rejected', 'Rejected'),
                    ('out_for_delivery', 'Out for Delivery'),
                    ('delivered', 'Delivered'),
                ],
                default='pending',
                max_length=20,
            ),
        ),
    ]
