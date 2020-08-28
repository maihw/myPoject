#在模型被定义之后，我们便可以在视图中引用模型。通常，
#视图根据参数检索数据，加载一个模板，并使用检索到的数据呈现模板
from django.shortcuts import render
from .models import Person

def book_archive(request, year):
    book_list = Person.objects.filter(birth_year = year)
    context = {'year': year,'book_list':book_list}
    return render(request, 'books/year_archive.html', context)

#views.py 文件包含了页面的业务逻辑。book_archive() 
#函数叫做视图。这里还用到了 year_archive.html 模板。