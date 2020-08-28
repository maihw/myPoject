from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

#模型是 django.db.models.Model 类的子类。每个模型有一些类变量，
#它们都表示模型里的一个数据库字段。

#每个字段都是 Field 类的实例。比如字符字段是 CharField，日期字段被表示为 
#DateTImeField。这将告诉 Django 每个字段要处理的数据类型。

#定义某些 Field 类实例需要参数。如上面的 max_length=100 中的 max_length。
#这个参数的用处不止于用来定义数据结构，也用于验证数据。

#通过前面的代码，Django 可以：

#为这个应用创建数据库 schema（生成 CREATE TABLE 语句）。
#创建可以与 Book 对象进行交互的 Python 数据库 API。