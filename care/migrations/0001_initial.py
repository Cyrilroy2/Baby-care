# Generated by Django 5.0.4 on 2024-06-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.CharField(max_length=150)),
                ('p_id', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='baby_enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('pid', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='baby_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='babysitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('d_id', models.CharField(max_length=150)),
                ('p_id', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('basicpay', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=150)),
                ('feedback', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='nutrition_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('n_id', models.CharField(max_length=150)),
                ('p_id', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('basicpay', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='nutritionists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='parent_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=150)),
                ('basicpay', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('cvv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('typee', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='sitter_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('bs_id', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('date_frm', models.CharField(max_length=150)),
                ('date_to', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('p_id', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='vacinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=150)),
                ('vaccine', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('p_id', models.CharField(max_length=150)),
            ],
        ),
    ]
