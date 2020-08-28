#设计模型 Model
#Django 无需数据库就可以使用，
#通过对象关系映射器（Object-relational mapping），
#仅使用 Python 代码就可以描述数据结构。
from django.db import models
class book(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField()


#models.py 文件主要用一个 Python 类来描述数据表。
#称为模型(model) 。 运用这个类，你可以通过简单的 
#Python 代码来创建、检索、更新、删除 数据库中的记录
#而无需写一条又一条的 SQL 语句。