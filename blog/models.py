from django.db import models
from django.templatetags.static import static

class Tag(models.Model):
    title=models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title=models.CharField(max_length=50)
    descreption=models.TextField()
    heading=models.CharField(max_length=50)
    thumbnai=models.ImageField(upload_to='blogs/',blank=True)
    body=models.TextField()
    slug=models.SlugField(unique=True)
    tags=models.ManyToManyField(Tag,related_name='blogs')

    def get_thumbnai(self):
        print(static('images/defult_images/defult_blog.png'))
        return self.thumbnai.url if self.thumbnai else static('images/defult_images/defult_blog.png')

    def __str__(self):
        return self.title

def get_blog_used_image_path(blog_used,filename:str):
    return f"blog_image/{blog_used.blog.slug}/{filename}"
 
class BlogUsedImages(models.Model):
    blog = models.ForeignKey(Blog,related_name='images',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=get_blog_used_image_path)