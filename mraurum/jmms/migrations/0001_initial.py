# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 17:43
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jmms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cutting_phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_sent', models.FloatField(default=0.0, verbose_name='Weight Sent')),
                ('receive_weight', models.FloatField(default=0.0, verbose_name='Receive Weight')),
                ('cutting_cost', models.PositiveIntegerField(verbose_name='Cutting Cost')),
                ('other_cost', models.PositiveIntegerField(verbose_name='Other Cost')),
                ('sent_date', models.DateField(verbose_name='Sent Date')),
                ('receive_date', models.DateField(verbose_name='Receive Date')),
            ],
        ),
        migrations.CreateModel(
            name='Design_Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_name', models.CharField(max_length=255, verbose_name='Design Name')),
                ('design_description', models.TextField(max_length=1000, verbose_name='Design Description')),
                ('added_date', models.DateField(blank=True, null=True, verbose_name='Added Date')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Design photo')),
            ],
        ),
        migrations.CreateModel(
            name='Embedding_phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_sent', models.FloatField(default=0.0, verbose_name='Weight Sent')),
                ('receive_weight', models.FloatField(default=0.0, verbose_name='Receive Weight')),
                ('jewel_price', models.PositiveIntegerField(verbose_name='Jewel Price')),
                ('jewel_quantity', models.PositiveIntegerField(verbose_name='Jewel Quantity')),
                ('jewel_weight', models.FloatField(default=0.0, verbose_name='Jewel Weight')),
                ('jewel_size', models.PositiveIntegerField(verbose_name='Jewel Size')),
                ('embedding_cost', models.PositiveIntegerField(verbose_name='embedding Cost')),
                ('other_cost', models.PositiveIntegerField(verbose_name='Other Cost')),
                ('sent_date', models.DateField(verbose_name='Sent Date')),
                ('receive_date', models.DateField(verbose_name='Receive Date')),
            ],
        ),
        migrations.CreateModel(
            name='Hallmark_Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_receive_date', models.DateField(verbose_name='Order Receive Date')),
                ('order_send_date', models.DateField(blank=True, null=True, verbose_name='Order Send Date')),
                ('verifying_cost', models.PositiveIntegerField(verbose_name='Verifying Cost')),
                ('other_cost', models.PositiveIntegerField(verbose_name='Other Cost')),
                ('weight_sent', models.FloatField(default=0.0, verbose_name='Weight Sent')),
                ('receive_weight', models.FloatField(default=0.0, verbose_name='Receive Weight')),
                ('status', models.TextField(blank=True, max_length=10, null=True, verbose_name='Status')),
                ('remark', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Remark')),
            ],
        ),
        migrations.CreateModel(
            name='Jewel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewel_name', models.CharField(max_length=255, verbose_name='Jewel Name')),
            ],
        ),
        migrations.CreateModel(
            name='Jewellery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Design_Catalog', verbose_name='Jewellery Design')),
            ],
        ),
        migrations.CreateModel(
            name='Jewellery_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewellery_name', models.CharField(max_length=255, verbose_name='Jewellery Name')),
            ],
        ),
        migrations.CreateModel(
            name='Material_Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Purchase Price')),
                ('purchase_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Purchase Weight')),
                ('purchase_date', models.DateTimeField(blank=True, null=True, verbose_name='Purchase Date')),
            ],
        ),
        migrations.CreateModel(
            name='Polishing_phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_sent', models.FloatField(default=0.0, verbose_name='Weight Sent')),
                ('receive_weight', models.FloatField(default=0.0, verbose_name='Receive Weight')),
                ('polishing_cost', models.PositiveIntegerField(verbose_name='polishing Cost')),
                ('other_cost', models.PositiveIntegerField(verbose_name='Other Cost')),
                ('sent_date', models.DateField(verbose_name='Sent Date')),
                ('receive_date', models.DateField(verbose_name='Receive Date')),
                ('jewellery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Jewellery', verbose_name='Jewellery')),
            ],
        ),
        migrations.CreateModel(
            name='Raw_Material_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=255, verbose_name='Material Name')),
                ('material_purity', models.PositiveIntegerField(verbose_name='Material Purity')),
                ('material_current_price', models.FloatField(verbose_name='Current Price')),
                ('material_unit', models.FloatField(verbose_name='Material Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_receive_date', models.DateField(verbose_name='Order Receive Date')),
                ('order_send_date', models.DateField(blank=True, null=True, verbose_name='Order Send Date')),
                ('payment_received', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Amount of payment received')),
                ('jewellery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Jewellery', verbose_name='Jewellery')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_address', models.TextField(max_length=1000, verbose_name='Address')),
                ('contact_details_1', models.CharField(max_length=13, verbose_name='Phone Number 1')),
                ('contact_details_2', models.CharField(max_length=13, null=True, verbose_name='Phone Number 2')),
                ('email', models.CharField(max_length=255, verbose_name='EMail ID')),
                ('rating', jmms.models.IntegerRangeField(default=5, help_text='Rating of the User')),
                ('name', models.OneToOneField(max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Name')),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Seller Name'),
        ),
        migrations.AddField(
            model_name='polishing_phase',
            name='polisher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Polisher Name'),
        ),
        migrations.AddField(
            model_name='material_purchase',
            name='material_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Raw_Material_Type', verbose_name='Material Type'),
        ),
        migrations.AddField(
            model_name='material_purchase',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Suplier'),
        ),
        migrations.AddField(
            model_name='jewellery_type',
            name='material_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Raw_Material_Type', verbose_name='Material Type'),
        ),
        migrations.AddField(
            model_name='jewellery',
            name='raw_material_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Raw_Material_Type', verbose_name='Raw Material'),
        ),
        migrations.AddField(
            model_name='hallmark_verification',
            name='jewellery_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Jewellery', verbose_name='Jewellery'),
        ),
        migrations.AddField(
            model_name='embedding_phase',
            name='embedder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Embedder Name'),
        ),
        migrations.AddField(
            model_name='embedding_phase',
            name='jewel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Jewel', verbose_name='Jewel'),
        ),
        migrations.AddField(
            model_name='embedding_phase',
            name='jewellery_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Jewellery', verbose_name='Jewellery'),
        ),
        migrations.AddField(
            model_name='design_catalog',
            name='jewellery_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Jewellery_type', verbose_name='Jewellery Type'),
        ),
        migrations.AddField(
            model_name='cutting_phase',
            name='cutter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cutter Name'),
        ),
        migrations.AddField(
            model_name='cutting_phase',
            name='jewellery_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmms.Jewellery', verbose_name='Jewellery'),
        ),
        migrations.AlterUniqueTogether(
            name='seller',
            unique_together=set([('seller_id', 'jewellery_id', 'order_send_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='polishing_phase',
            unique_together=set([('jewellery_id', 'polisher_id', 'sent_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='hallmark_verification',
            unique_together=set([('jewellery_id', 'order_send_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='embedding_phase',
            unique_together=set([('jewellery_id', 'embedder_id', 'sent_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='cutting_phase',
            unique_together=set([('jewellery_id', 'cutter_id', 'sent_date')]),
        ),
    ]
