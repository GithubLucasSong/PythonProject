import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")
import django
django.setup()
from app01 import models

#################基于对象的查询############
# 正向查询
# book_obj = models.Book.objects.get(pk=1)
# print(book_obj.publisher)     # 关联的出版社对象
# print(book_obj.publisher_id)  # 关联的出版社的id

# 反向查询
# pub_obj = models.Publisher.objects.get(pk=1)
# 没有指定related_name  类名小写_set
# print(pub_obj)
# print(pub_obj.book_set,type(pub_obj.book_set))  #类名小写_set  关系管理对象
# print(pub_obj.book_set.all())
# 指定related_name = 'books'  没有类名小写_set的写法

#################基于字段的查询###########
# ret = models.Book.objects.filter(publisher__name='新华出版社')

# 不指定related_name='boos'  类名小写
# ret = models.Publisher.objects.filter(book__name='床上学python')

# 指定related_name='books'  不指定related_query_name
# ret = models.Publisher.objects.filter(books__name='床上学python')

# 指定related_query_name='book'
# ret = models.Publisher.objects.filter(book__name='床上学python')



