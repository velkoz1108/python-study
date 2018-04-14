from django.db import models

# Create your models here.
from django.utils import timezone


class Test(models.Model):
    name = models.CharField(max_length=20)
    picUrl = models.CharField(max_length=200)
    creator = models.CharField(max_length=20)
    modifier = models.CharField(max_length=20)

    # DateTimeField、DateField和TimeField三种类型
    # createdate = models.DateTimeField('保存日期', default=timezone.now())
    # modifydate = models.DateTimeField('最后修改日期', auto_now=True)


# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField(default=0)
#     email = models.EmailField()
#
#     def __unicode__(self):
#         return self.name
#
#
# class Tag(models.Model):
#     contact = models.ForeignKey(Contact)
#     name = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.name
