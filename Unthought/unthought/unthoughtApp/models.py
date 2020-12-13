from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=23)
    user_type = models.CharField(max_length=10)
    user_login_date = models.DateField(auto_now=True)

class Member(models.Model):
    user_name = models.CharField(max_length=50)
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)  
    Member_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=8)
    dob = models.DateField(auto_now=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    working_status = models.BooleanField(default=True)
    company_name = models.CharField(max_length=50)
    college_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    pri_specification_main = models.CharField(max_length=50)
    pri_specification_submain = models.CharField(max_length=50)
    sec_specification_main = models.CharField(max_length=50)
    sec_specification_submain = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    no_of_post = models.IntegerField(default=0)
    no_of_groups = models.IntegerField(default=0)  

class MemberDp(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    member_dp = models.ImageField(upload_to=None, height_field=None, width_field=None)

class Events(models.Model):
    event_name = models.CharField(max_length=50)
    mode = models.CharField(max_length=6)
    date  = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    venue = models.CharField(max_length=500)
    categories = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)

class EventsPics(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)     
    event_name = models.CharField(max_length=50)
    event_mode = models.CharField(max_length=7)
    event_dp = models.ImageField(upload_to=None, height_field=None, width_field=None)
    event_pic1 = models.ImageField(upload_to=None, height_field=None, width_field=None)
    event_pic2 = models.ImageField(upload_to=None, height_field=None, width_field=None)

class Post(models.Model):
    admin_id = models.ForeignKey(Member, on_delete=models.CASCADE)    
    admin_name = models.CharField(max_length=50)
    admin_designation = models.CharField(max_length=25)
    title_of_post = models.CharField(max_length=50)
    short_desc = models.CharField(max_length=50)
    long_desc = models.CharField(max_length=1500)
    requirement1 = models.CharField(max_length=50)
    requirement2 = models.CharField(max_length=50)
    requirement3 = models.CharField(max_length=50)
    requirement4 = models.CharField(max_length=50)
    goal_of_project = models.CharField(max_length=150)
    workdone = models.CharField(max_length=75)
    progress_status = models.IntegerField(default=0)
    no_of_links = models.IntegerField(default=0)
    no_of_saved = models.IntegerField(default=0)

class SavePostMember(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=50)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)

class LikedPostMember(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)  
    member_name = models.CharField(max_length=50)
    post_id = models.ForeignKey(Post,  on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)

class ProjectMember(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=10)

class PostPic(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_dp = models.ImageField(upload_to=None, height_field=None, width_field=None)
    post_pic1 = models.ImageField(upload_to=None, height_field=None, width_field=None)
    post_pic2 = models.ImageField(upload_to=None, height_field=None, width_field=None)    

