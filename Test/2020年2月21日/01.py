null
数据库中字段是否可以为空
db_column
数据库中字段的列名
default
数据库中字段的默认值
primary_key
数据库中字段是否为主键
db_index
数据库中字段是否可以建立索引
unique
数据库中字段是否可以建立唯一索引
unique_for_date
数据库中字段【日期】部分是否可以建立唯一索引
unique_for_month
数据库中字段【月】部分是否可以建立唯一索引
unique_for_year
数据库中字段【年】部分是否可以建立唯一索引

verbose_name
Admin中显示的字段名称
blank
Admin中是否允许用户输入为空
editable
Admin中是否可以编辑
help_text
Admin中该字段的提示信息
choices
Admin中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作
如：gf = models.IntegerField(choices=[(0, '何穗'), (1, '大表姐'), ], default=1)

error_messages
自定义错误信息（字典类型），从而定制想要显示的错误信息；
字典健：null, blank, invalid, invalid_choice, unique, and unique_for_date
如：{'null': "不能为空.", 'invalid': '格式错误'}

validators
自定义错误验证（列表类型），从而定制想要的验证规则
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator, URLValidator, DecimalValidator, \
    MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator

如：
test = models.CharField(
    max_length=32,
    error_messages={
        'c1': '优先错信息1',
        'c2': '优先错信息2',
        'c3': '优先错信息3',
    },
    validators=[
        RegexValidator(regex='root_\d+', message='错误了', code='c1'),
        RegexValidator(regex='root_112233\d+', message='又错误了', code='c2'),
        EmailValidator(message='又错误了', code='c3'), ]
)
