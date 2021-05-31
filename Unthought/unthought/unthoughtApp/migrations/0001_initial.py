# Generated by Django 3.0.5 on 2021-05-20 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('mode', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=500)),
                ('categories', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_name', models.CharField(max_length=50)),
                ('Member_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=8)),
                ('dob', models.DateField(auto_now=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('working_status', models.BooleanField(default=True)),
                ('company_name', models.CharField(max_length=50)),
                ('college_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('pri_specification_main', models.CharField(max_length=50)),
                ('pri_specification_submain', models.CharField(max_length=50)),
                ('sec_specification_main', models.CharField(max_length=50)),
                ('sec_specification_submain', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
                ('no_of_post', models.IntegerField(default=0)),
                ('no_of_groups', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_designation', models.CharField(max_length=25)),
                ('title_of_post', models.CharField(max_length=50)),
                ('short_desc', models.CharField(max_length=50)),
                ('long_desc', models.CharField(max_length=1500)),
                ('requirement1', models.CharField(max_length=50)),
                ('requirement2', models.CharField(max_length=50)),
                ('requirement3', models.CharField(max_length=50)),
                ('requirement4', models.CharField(max_length=50)),
                ('goal_of_project', models.CharField(max_length=150)),
                ('workdone', models.CharField(max_length=75)),
                ('progress_status', models.IntegerField(default=0)),
                ('no_of_links', models.IntegerField(default=0)),
                ('no_of_saved', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Member')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=23)),
                ('user_type', models.CharField(max_length=10)),
                ('user_login_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavePostMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('post_title', models.CharField(max_length=50)),
                ('saved', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Member')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=10)),
                ('pri_specification_submain', models.CharField(max_length=50)),
                ('progress_status', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Member')),
            ],
        ),
        migrations.CreateModel(
            name='PostPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_dp', models.ImageField(default='Images/None/No0img.jpg', upload_to='postPic/')),
                ('post_pic1', models.ImageField(default='Images/None/No0img.jpg', upload_to='postPic/')),
                ('post_pic2', models.ImageField(default='Images/None/No0img.jpg', upload_to='postPic/')),
                ('active', models.BooleanField(default=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='MemberDp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_dp', models.ImageField(default='Images/None/No0img.jpg', upload_to='memberDp/')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='User_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.User'),
        ),
        migrations.CreateModel(
            name='LikedPostMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('post_title', models.CharField(max_length=50)),
                ('liked', models.BooleanField(default=False)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Member')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='GroupText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=500)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Member')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='EventsPics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_mode', models.CharField(max_length=7)),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('categories', models.CharField(max_length=100)),
                ('event_dp', models.ImageField(default='Images/None/No0img.jpg', upload_to='eventPic/')),
                ('event_pic1', models.ImageField(default='Images/None/No0img.jpg', upload_to='eventPic/')),
                ('event_pic2', models.ImageField(default='Images/None/No0img.jpg', upload_to='eventPic/')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unthoughtApp.Events')),
            ],
        ),
    ]
