from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('telugu_name', models.CharField(blank=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(blank=True, max_length=500)),
                ('farmer_id', models.IntegerField()),
            ],
        ),
    ]
