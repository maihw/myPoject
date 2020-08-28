#只需要建立 URL 和 Python 回调函数简单的映射关系。
from django.urls import path
from . import views
urlpatterns = [
    path('book/<int:year>', views.year_archive),
]

#urls.py 指出了什么样的 URL 调用什么视图。 在这个例子中 
#books/xxxxx 将会调用 year_archive() 这个函数。也就是说，
#在进入这个链接时，会返回视图函数的结果。