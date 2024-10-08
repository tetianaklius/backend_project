# Generated by Django 5.1 on 2024-09-03 09:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDealershipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
            options={
                'db_table': 'car_dealerships',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CarAdminModel',
            fields=[
                ('profilemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.profilemodel')),
                ('staff_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cd_admin_profile', to='users.profilestaffmodel')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='dealerships.cardealershipmodel')),
            ],
            options={
                'db_table': 'cd_admins',
                'ordering': ['id'],
            },
            bases=('users.profilemodel',),
        ),
        migrations.CreateModel(
            name='CarManagerModel',
            fields=[
                ('profilemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.profilemodel')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='dealerships.cardealershipmodel')),
                ('staff_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cd_manager_profile', to='users.profilestaffmodel')),
            ],
            options={
                'db_table': 'cd_managers',
                'ordering': ['id'],
            },
            bases=('users.profilemodel',),
        ),
        migrations.CreateModel(
            name='CarMechanicModel',
            fields=[
                ('profilemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.profilemodel')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanics', to='dealerships.cardealershipmodel')),
                ('staff_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cd_mechanic_profile', to='users.profilestaffmodel')),
            ],
            options={
                'db_table': 'cd_mechanics',
                'ordering': ['id'],
            },
            bases=('users.profilemodel',),
        ),
        migrations.CreateModel(
            name='CarSellerModel',
            fields=[
                ('profilemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.profilemodel')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='dealerships.cardealershipmodel')),
                ('staff_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cd_seller_profile', to='users.profilestaffmodel')),
            ],
            options={
                'db_table': 'cd_sellers',
                'ordering': ['id'],
            },
            bases=('users.profilemodel',),
        ),
    ]
