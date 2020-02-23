获取值：
 文本输人框：$('#username').val();
单选radio框：$('.a1:checked').val();
checked
代表被选中的

多选checkout框：$('.a2:checked').val()
是不行的;
需要循环取值，如下：
 var d = $(':checkbox:checked');
for (var i = 0; i < d.length; i++) {
    console.log(d.eq(i).val());
}

单选select框：$('#city').val()；
 多选select框：$('#lover').val();

设置值：
 文本输入框：$('#username').val('一串文字');

单选radio框：$('.a1').val([2]);
#注意内容必须是列表，写的是value属性对应的值

多选checkout框：$('.a2').val(['2', '3'])

单选select框：$('#city').val('1')；

 多选select框：$('#lover').val(['2', '3'])