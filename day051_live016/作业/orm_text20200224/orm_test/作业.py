import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_text20200224.settings")
import django
django.setup()
from app01 import models

# 1. 查找所有书名里包含金老板的书
ret = models.Book.objects.filter(title__contains='金老板')
print(ret)

# 2. 查找出版日期是2018年的书
ret = models.Book.objects.filter(publish_date__year='2018')
print(ret)
# 3. 查找出版日期是2017年的书名
ret = models.Book.objects.filter(publish_date__year='2017').values('title')
print(ret)
# 4. 查找价格大于10元的书
ret = models.Book.objects.filter(price__gt='10')
print(ret)
# 5. 查找价格大于10元的书名和价格
ret = models.Book.objects.filter(price__gt='10').values_list('title','price')
print(ret)
# 6. 查找memo字段是空的书
ret = models.Book.objects.filter(memo__isnull=True)
print(ret)
#
# 7. 查找在北京的出版社
ret = models.Publisher.objects.filter(city='北京')
print(ret)
# 8. 查找名字以沙河开头的出版社
ret = models.Publisher.objects.filter(name__startswith='沙河')
print(ret)
#
# 9. 查找“沙河出版社”出版的所有书籍
#基于对象
pub_obj = models.Publisher.objects.filter(name='沙河出版社')
pub_obj[0].book_set.all()
print(pub_obj[0].book_set.all(),pub_obj[1].book_set.all())
#基于字段
ret = models.Book.objects.filter(publisher__name='沙河出版社')
print(ret)

# 10. 查找每个出版社出版价格最高的书籍价格(不做)
# 11. 查找每个出版社的名字以及出的书籍数量(不做)
#
# 12. 查找作者名字里面带“小”字的作者
ret = models.Author.objects.filter(name__contains='小')
print(ret)
# 13. 查找年龄大于30岁的作者
ret = models.Author.objects.filter(age__gt=30)
print(ret)
# 14. 查找手机号是155开头的作者
ret = models.Author.objects.filter(phone__startswith='155')
print(ret)
# 15. 查找手机号是155开头的作者的姓名和年龄
ret = models.Author.objects.filter(phone__startswith='155').values_list('name','age')
print(ret)
#
# 16. 查找每个作者写的价格最高的书籍价格(不做)
# 17. 查找每个作者的姓名以及出的书籍数量(不做)
#
# 18. 查找书名是“跟金老板学开车”的书的出版社
ret = models.Publisher.objects.filter(book__title='跟金老板学开车')
print(ret)
# 19. 查找书名是“跟金老板学开车”的书的出版社所在的城市
ret = models.Publisher.objects.filter(book__title='跟金老板学开车').values('city')
print(ret)
# 20. 查找书名是“跟金老板学开车”的书的出版社的名称
ret = models.Book.objects.filter(title='跟金老板学开车').values('publisher__name')
print(ret)
# 21. 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
print(models.Book.objects.get(title='跟金老板学开车').publisher.book_set.exclude(title='跟金老板学开车').values_list('title','price'))
#
# 22. 查找书名是“跟金老板学开车”的书的所有作者
print(models.Book.objects.get(title='跟金老板学开车').author.all())
# 23. 查找书名是“跟金老板学开车”的书的作者的年龄
print(models.Book.objects.get(title='跟金老板学开车').author.all().values_list('name','age'))
# 24. 查找书名是“跟金老板学开车”的书的作者的手机号码
print(models.Book.objects.get(title='跟金老板学开车').author.all().values_list('name','phone'))
# 25. 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱
print(models.Book.objects.get(title='跟金老板学开车').author.all().values_list('name','book__title','book__price'))