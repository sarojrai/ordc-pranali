# Generated by Django 3.2.2 on 2021-05-23 06:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(blank=True, max_length=255, null=True)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('province_code', models.CharField(blank=True, max_length=255, null=True)),
                ('country_code', models.CharField(blank=True, max_length=255, null=True)),
                ('country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('default', models.BooleanField(default=False)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('orders_count', models.IntegerField(default=0)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('total_spent', models.CharField(blank=True, max_length=255, null=True)),
                ('last_order_id', models.CharField(blank=True, max_length=255, null=True)),
                ('verified_email', models.BooleanField(default=False)),
                ('tax_exempt', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_blacklisted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('is_blacklisted', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('gross_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('discount', models.CharField(blank=True, max_length=255, null=True)),
                ('tax', models.CharField(blank=True, max_length=255, null=True)),
                ('payload_data', models.JSONField()),
                ('source_type', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('source_website', models.CharField(blank=True, max_length=1024, null=True)),
                ('client_id', models.CharField(blank=True, max_length=255, null=True)),
                ('source_status', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.CharField(default='SYSTEM', max_length=255)),
                ('updated_by', models.CharField(default='SYSTEM', max_length=255)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='billing_address', to='order_fulfiller.address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_customer', to='order_fulfiller.customer')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipping_address', to='order_fulfiller.address')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_customer', to='order_fulfiller.customer'),
        ),
    ]
