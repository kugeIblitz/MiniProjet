from django.db import models

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION(Infos générales)

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



# SKILLS SECTION(Compétences)

class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    def __str__(self):
        return self.skill_name


# EXPERIENCE SECTION

class Experience(models.Model):
    exp_name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000,default=' ')

    def __str__(self):
        return self.exp_name


class Exp_cat(models.Model):
    exp = models.ForeignKey(Experience,
                                on_delete=models.CASCADE)
  


# CERTIFICATES SECTION

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    number=models.CharField(max_length=10,default='0')

    def __str__(self):
        return f'Id {self.id}'