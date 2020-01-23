# Python学习笔记

## 第一章 计算机基础

### 1.1 硬件

计算机基本的硬件由：cpu / 内存 / 主板 /硬盘 / 网卡 / 显卡 等组成，只有硬件但硬件之间无法进行交流和通信

### 1.2 操作系统

操作系统用于协调和控制硬件之间进行工作，常见的操作系统有那些：

- windows
- linux
  - centos [公司线上一般用]
- mac

### 1.3  解释器或编译器

编程语言的开发者写的一个工具，将用户写的代码转换成010101交给操作系统去执行。

#### 1.3.1 解释型和编译型语言

解释型语言类似于：实时编译，代表：Python / PHP / Ruby / Perl

编译型语言类似于: 写完之后，整体再进行编译， 代表： C / C++ / Java / Go.....

### 1.4 软件（应用程序）

软件又称为应用程序，就是我们在电脑上使用的工具，类似于：记事本 / 图片查看器 / 游戏

### 1.5 进制

对于计算机而言无论是文件存储 / 网络传输输入本质上都是：二进制（1010101101），如： 电脑上存储视频/图片/文件都是二进制；QQ/微信聊天发送的表情/文字/语音/视频 也全部都是二进制。

进制：

- 二进制，计算机内部
- 8进制
- 10进制，人来进行使用一般情况下计算机可以获取10进制，然后在内部会自动转换成二进制并操作。
- 16进制，一般用于表示二进制（用更短的内容表示更多的数据），一般是：\x 开头。

| 二进制 | 八进制 | 十进制 | 十六进制 |
| ------ | ------ | ------ | -------- |
| 0      | 0      | 0      | 0        |
| 1      | 1      | 1      | 1        |
| 10     | 2      | 2      | 2        |
| 11     | 3      | 3      | 3        |
| 100    | 4      | 4      | 4        |
| 101    | 5      | 5      | 5        |
| 110    | 6      | 6      | 6        |
| 111    | 7      | 7      | 7        |
| 1000   | 10     | 8      | 8        |
| 1001   | 11     | 9      | 9        |
| 1010   | 12     | 10     | A        |
| 1011   | 13     | 11     | B        |
| 1100   | 14     | 12     | C        |
| 1101   | 15     | 13     | D        |
| 1110   | 16     | 14     | E        |
| 1111   | 17     | 15     | F        |





## 第二章 Python入门

### 2.1 环境的安装

- 解释器： py2/ py3 （环境变量）
- 开发工具：pycharm

### 2.2 编码

#### 2.2.1 编码基础

- ascii (八位表示一个字符)
- unicode （4个字节，32位表示一个字符）
- utf-8 （用尽量少的字节表示，中文占3个字节）
- gbk
- gb2312

#### 2.2.2 python编码相关

对于python默认解释器编码：

- py2：ascii
- py3：utf-8

如果想要修改默认编码，则可以使用：

```python
# -*- coding:utf-8 -*-
```

注意：对于操作文件时，要按照：以什么编码写入，就要用什么编码去打开。

###   2.3 变量

问：为什么要有变量?

为某个值创建一个‘外号’，以后在使用的时候通过此外号就可以直接调用。

## 第三章 数据类型

### 3.1  整型（int）

#### 3.1.1 整型的长度

py2中有：int/long

py3中有：int（int/long）

#### 3.1.2 整除

py2和py3中整除是不一样的。

### 3.2 布尔（bool）

布尔值就是用于表示真假。True和False

其他类型转换成布尔值：

- str
- ....

对于：None /  ‘’ / 0 .....>false

### 3.3 字符串（str）

字符串是写代码中最常见的，python内存中的字符串是按照：unicode 编码存储，对于字符串是不可变的。

字符串自己有很多方法，如：

1.大写

````py
v = 'ALEX'
v1 = v.upper()
print(v1)
v2 = v.isupper() # 判断是否全部是大写
print(v2)
````



2.小写

```py
v = 'ALEX'
v1 = v.lower()
print(v1)
v2 = v.islower() # 判断是否全部是大写
print(v2)
```



3.判断是否是数字

```py
v = '1'
# v = '二'
# v = '②'
v1 = v.isdigit()    # '1'->True; '二' -> False '②'-> True
v2 = v.isdecimal()  # '1'->True; '二' -> False '②'-> False
v3 = v.isnumeric()  # '1'->True; '二' -> True  '②'-> True     能识别的字符最全
print(v1,v2,v3)

##############应用############
v = ['alex','eric','tony']
for i in v:
    print(i)
num = input('请输入序号：')
if num.isdecimal():
    num = int(num)
    print(v[num])
else:
    print('你输入的不是字符串')
```

4.去两侧的空白 \t \n 字符

```py
v1 = ' alex '
print(v1.strip())

v2 = 'alex \t'
print(v2.strip())

v3 = 'alex \n'
print(v3.strip())

v4 = ' aalexa'
print(v4.strip('a'))


```

5 .替换 replace

6.开头/结尾

7.编码，把字符串转换成二进制

8.format / format_map

```py
v = '我是{0}，谢谢{1}'.format('alex',19)
print(v)

v = '我是{x1}，谢谢{x2}'.format_map({'x1':'alex','x2':19})
print(v)
```



9.join 连字符

10.split 切割

### 3.4 列表

### 3.5  元组

### 3.6 集合

集合在python中也是一个数据类型,我们只用它自带的特性,其余的操作很少使用

集合在Pyhton中的关键字是set,也是以{}的形式展示 只不过集合是一个没有值得字典,为什么这么说呢??

因为集合中的元素要求是不可变的并且还是唯一的,我们就利用它是唯一来做去重

```python
lst = [1,3,4,112,23,1,3,1,41,12,3,1]
print(set(lst))  # 这样就没有重复的元素出现了,我们在将集合抓换成列表
list(set(lst)) # 这样就把没有重复的集合转成列表了
print(list(set(lst)))
```

集合是无序,可变的数据类型,说到可变我们就知道集合是能够增加和删除等操作的,我们来看看怎么操作

#### set集合增删改查

增加

```python
s = {"刘嘉玲", '关之琳', "王祖贤"}
s.add("郑裕玲")
print(s)
s.add("郑裕玲") # 重复的内容不会被添加到set集合中
print(s)
s = {"刘嘉玲", '关之琳', "王祖贤"}
s.update("麻花藤") # 迭代更新
print(s)
s.update(["张曼⽟", "李若彤","李若彤"])
print(s)
```

删除　　

```python
s = {"刘嘉玲", '关之琳', "王祖贤","张曼⽟", "李若彤"}
item = s.pop() # 随机弹出⼀个.
print(s)
print(item)
s.remove("关之琳") # 直接删除元素
# s.remove("⻢⻁疼") # 不存在这个元素. 删除会报错
print(s)
s.clear() # 清空set集合.需要注意的是set集合如果是空的. 打印出来是set() 因为要和
dict区分的.
print(s) # set()
```

修改

```python
# set集合中的数据没有索引. 也没有办法去定位⼀个元素. 所以没有办法进⾏直接修改.
# 我们可以采⽤先删除后添加的⽅式来完成修改操作
s = {"刘嘉玲", '关之琳', "王祖贤","张曼⽟", "李若彤"}
# 把刘嘉玲改成赵本⼭
s.remove("刘嘉玲")
s.add("赵本⼭")
print(s)
```

查询　　

```python
# set是⼀个可迭代对象. 所以可以进⾏for循环
for el in s:
 print(el)
```

常⽤操作　　

```python
s1 = {"刘能", "赵四", "⽪⻓⼭"}
s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
# 交集
# 两个集合中的共有元素
print(s1 & s2) # {'⽪⻓⼭'}
print(s1.intersection(s2)) # {'⽪⻓⼭'}
# 并集
print(s1 | s2) # {'刘科⻓', '冯乡⻓', '赵四', '⽪⻓⼭', '刘能'}
print(s1.union(s2)) # {'刘科⻓', '冯乡⻓', '赵四', '⽪⻓⼭', '刘能'}
# 差集
print(s1 - s2) # {'赵四', '刘能'} 得到第⼀个中单独存在的
print(s1.difference(s2)) # {'赵四', '刘能'}
# 反交集
print(s1 ^ s2) # 两个集合中单独存在的数据 {'冯乡⻓', '刘能', '刘科⻓', '赵四'}
print(s1.symmetric_difference(s2)) # {'冯乡⻓', '刘能', '刘科⻓', '赵四'}
s1 = {"刘能", "赵四"}
s2 = {"刘能", "赵四", "⽪⻓⼭"}
# ⼦集
print(s1 < s2) # set1是set2的⼦集吗? True
print(s1.issubset(s2))
# 超集
print(s1 > s2) # set1是set2的超集吗? False
print(s1.issuperset(s2))
```

set集合本⾝是可以发⽣改变的. 是不可hash的. 我们可以使⽤frozenset来保存数据. frozenset是不可变的. 也就是⼀个可哈希的数据类型

```python
s = frozenset(["赵本⼭", "刘能", "⽪⻓⼭", "长桂"])
dic = {s:'123'} # 可以正常使⽤了
print(dic)
```

这个不是很常⽤. 了解⼀下就可以了

### 3.7 字典

### 3.8 公共功能

- 求长度    len()
- 索引        [number]
- 切片        [number,nuimber]
- 步长        [number,nuimber,number]
- for循环

### 3.9 嵌套











## 第四章 文件操作

### 4.1 文件的基本操作'

```py
obj = open('路径',mode = '模式',encoding = '编码')
obj.write()
obj.read()
obj.close()

```

### 4.2 打开模式

- r / w / a
- r+ / w+ / a+
- rb / wb / ab 
- r+b / w+b / a+b

### 4.3 操作

- read()  全部读到内存

- read(1) 

  - 1表示一个字符

    ```python
    obj = open('a.txt',mode = 'r',encoding = 'utf-8')
    data = obj.read(1) # 一个字符
    obj.close()
    print(data)
    ```

  - 1表示一个字节

    ```python
    obj = open('a.txt',mode = 'rb')
    data = obj.read(1) # 一个字节
    obj.close()
    print(data)
    ```

  - write(字符串)
  
    ```python
    obj = open('a.txt',mode = 'w',encoding = 'utf-8')
    obj.write('中文')
    obj.close()
    
    ```
  
  - write(二进制)
  
    ```python
    obj = open('a.txt',mode = 'wb')
    v = '中文'.encode('utf-8')
    obj.write(v)
    obj.close
    ```
  
  - seek(光标字节位置),无论模式是否带B，都是按照字节进行处理。
  
    ```python
    obj = open('a.txt',mode = 'r',encoding = 'utf-8')
    obj.seek(3) # 跳转到指定字节
    data = obj.read()
    obj.close()
    print(data)
    ```
  
  - tell() 获取当前光标所在的字节位置
  
    ```python
    obj = open('a.txt',mode = 'rb')
    obj.seek(3) # 跳转到指定字节位置
    obj.read()
    data = obj.tell()
    print(data)
    obj.close
    ```
  
  - flush() 强制将内存中的数据写入硬盘
  
    ```python
    v = open('a.txt',mode = 'a',encoding = 'utf-8')
    while True:
        val = input('请输入:')
        v.write(val)
        v.flush()
    v.close()
    
    ```

### 4.4 关闭文件

手动关闭文件

```python
v = open('a.txt',mode = 'a',encoding = 'utf-8')
v.close()
```

自动关闭文件

```python
with open('a.txt',mode = 'a',encoding = 'utf-8') as v:
    data = v.raad()
    # 缩进中的代码执行完毕后，自动关闭文件
 
```

### 4.5 文件的修改

```python
with open('a.txt',mode = 'r',encoding = 'utf-8') as f1:
    data = f1.read()
new_data =data.replace('被替换的字符串'，'替换成的字符串')
with open('a.txt',mode='w',encoding = 'utf-8') as f1:
    data = f1.write(new_data)
    
```

大文件修改

```python
f1 = open('a.txt',mode = 'r',encoding = 'utf-8') #初始大文件
f2 = open('b.txt',mode = 'w',encoding = 'utf-8') #另外打开一个空白文件
for line in f1:
    new_line = line.replace('被替换的字符串'，'替换成的字符串')
    f2.write(new_line)
f1.close()
f2.close()
```

```python
with open('a.txt',mode = 'r',encoding = 'utf-8') as f1,open('b.txt',mode = 'w',encoding = 'utf-8') as f2:
    for line in f1:
        new_line = line.replace('被替换的字符串'，'替换成的字符串')
        f2.write(new_line)
```





## 第五章 函数

### #三元运算（三目运算）

```python
v = 前面 if 条件（条件为真前面 条件为假后边） else 后面
```

```python
# 让用户输入值，如果值是整数，则转换为整数，否则赋值为None
data = input('请输入')
value = int(data) if data.isdecimal() else None
```

注意：先做成来，再思考如何简化。

### 函数

函数之前的代码统称为面向过程编程 缺点：可读性差 可重用性差。

```python
# 面向过程编程
user_input = input('请输入角色：')
if user_input == '管理员':
    pass # 给管理员发邮件 ：10行代码
elif user_input == '业务员':
    pass # 给管理员发邮件 ：10行代码
elif user_input == '老板':
    pass # 给管理员发邮件 ：10行代码
```

发送邮件：

```python
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('hello word','plain','utf-8')
msg['From'] = formataddr(['python','732336318@qq.com'])
msg['To'] = formataddr(['导演','2731650266@qq.com'])
msg['Subject'] = '亲爱的导演'
server = smtplib.SMTP('smtp.qq.com', 25)
server.login('732336318@qq.com','brawjlffjubnbecc')
server.sendmail('732336318@qq.com',['2731650266@qq.com',],msg.as_string())
server.quit()
```

函数式编程

```python
def send_email():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('hello word','plain','utf-8')
    msg['From'] = formataddr(['python','732336318@qq.com'])
    msg['To'] = formataddr(['导演','2731650266@qq.com'])
    msg['Subject'] = '亲爱的导演'
    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login('732336318@qq.com','brawjlffjubnbecc')
    server.sendmail('732336318@qq.com',['2731650266@qq.com',],msg.as_string())
    server.quit()

user_input = input('请输入角色：')
if user_input == '管理员':
    send_email():
elif user_input == '业务员':
    end_email():
elif user_input == '老板':
    send_email():
```

对于函数式编程：

- 本质：将N行代码拿到别处并给他起个名字，以后通过名字就可以找到这段代码并执行。
- 场景：
  - 代码重复执行
  - 代码量特别多超过了一屏，可以选择通过函数进行代码的分割。

###  5.1 函数的基本结构

```python
def 函数名():
    #函数的内容
    pass

#函数的执行
函数名（）

```

```python
def get_list_first_data():
    v = [11,22,33,44]
    print(v[0])
    pass
get_list_first_data()

```

### 5.2  函数的参数

```python
def get_list_first_data(aaa): # 此时的aaa叫形式参数
    v = [11,22,33,44]
    print(v[aaa])
    pass
get_list_first_data(0)    # 调用函数时传递的叫实际参数
get_list_first_data(1)
get_list_first_data(2)
get_list_first_data(3)
```

### 5.3 函数的返回值

```python
def func(arg):
    # .....
    return 9 # 返回值为9
```



## 第六章 模块



## 第七章 面向对象



## 进程和多线程

### 多进程

- 程序:是一个指令的集合
- 进程：正在执行的程序；或者说：当你运行一个进程，你就启动了一个进程 
  - 编写完成的代码，没有运行时，称为程序，正在运行的代码，称为进程
  - 程序是死的（静态的），进程是活的（动态的）
- 操作系统轮流让各个任务交替执行，由于CPU的执行速度太快了，我们感觉所有任务就像在同时执行
- 多进程中，每个进程中的所有数据（包括全局变量）都各拥有一份，互不影响。
- 程序开始运行时，首先会创建一个主进程
- 在主进程（父进程）下，我们可以创建新的进程（子进程），子进程依赖于主进程，如果主进程结束，程序会退出。

#### multiprocessing



- python提供了飞航好用的多进程包multiprocessing，借助这个包，可以轻松完成从单进程到并发执行的转换

- multiprocessing模块提供了一个Process类来创建一个进程对象

  ```python
  from multiprocessing import Process
  def run(name):
      print('子进程正在运行，name= %s'%(name))
  if __name__ == '__main__':
      print('父进程启动')
      p = Process(target = run,args = ('test',))
      #target表示调用对象，args表示调用对象的位置参数元组
      #注意：元组中只有一个元素时结尾要加逗号
      print('子进程将要执行')
      p.start()
      print(p.name)
      p.join()
      print('子进程结束')
  ```

- ``` python
  if __name__ == '__main__':说明
  '''
  一个python的文件有两种使用的方法，第一是直接作为程序执行，第二是import到其他python程序中被调用（模块重用）执行。
  因此 if __name__ == '__main__':的作用就是控制这两种情况执行代码的过程，__name__是内置变量，用于表示当前模块的名字
  在 if __name__ == '__main__': 下的代码只有在文件作为程序直接执行才会被执行，而import到其他程序中是不会被中的
  在windows上，子进程会自动import启动它的这个文件，而在import的时候是会执行这些语句的。
  如果不加 if __name__ == '__main__': 的话就会无限递归创建子进程
  所以必须把创建子进程的部分用 if判断保护起来
  import的时候__name__不是__main__,就不会递归运行了
  
  
  '''
  ```

- Process(target,name,args)
- 参数介绍
  - target表示调用对象，即子进程要执行的任务
  - args表示调用对象的位置参数元组，args = （1，）
  - name为子进程的名称

- Process类常用用法：
  - p.start():启动进程，并调用该子进程中的p.run()
  - p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法
  - p.terminate(): 强行终止进程p，不会进行任何清理操作
  - p.is_alive():如果p仍然运行，返回True，用在判断进程是否还在运行
  - p.join([timeout]):主进程等待p终止，timeout是可选的超时时间

- Process类常用属性：

  - name:当前进程实例别名，默认为Process-N，N为从1开始递增的整数
  - pid：当前进程实例的PID值

- 全局变量在多个进程中不共享：进程之间的数据是独立的，默认情况下互不影响

  ```python
  from multiprocessing import Process
  num = 1
  def run1():
      global num
      num += 5
      print('子进程1运行中，num = %d'%(num))
  def run2():
      global num
      num += 10
      print('子进程2运行中，num = %d'%(num))
  if __name__ == '__main__':
      print('父进程启动')
      p1 = Process(target= run1)
      p2 = Process(target= run2)
      print('子进程将要执行')
      p1.start()
      p2.start()
      p1.join()
      p2.join()
      print('子进程结束')
  ```

- 创建新的进程还可以使用类的方式，可以自定义一个类，继承Process类，每次实例化这个类的时候，就等同于实例化一个进程对象

  ```python
  import multiprocessing
  import time
  class ClockProcess(multiprocessing.Process):
      def run(self):
          n = 5
          while n > 0:
              print(n)
              time.sleep(1)
              n -= 1
  if __name__ == '__main__':
      p = ClockProcess()
      p.start()
      p.join()
  ```

#### 进程池

- 进程池:用来创建多个进程

- 当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程，但如果是上百个甚至是上千个目标，手动去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool

- 初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行

  ```python
  from multiprocessing import Pool
  import random,time
  def work(num):
      print(random.random()*num)
      time.sleep(3)
  if __name__ == '__main__':
      po = Pool(3) #定义一个进程池，最大进程数为3，默认大小为CPU核数
      for i in range(10):
          po.apply_async(work,(i,)) # apply_async选择要调用的目标，每次循环会用空出来的子进程去调用目标
      po.close() # 进程池关闭之后不会再接受新的请求
      po.join() # 等待po中所有子进程结束，必须放在close后面
  # 在多进程中，主进程一般用来等待，真正的任务都在子进程中执行
  ```

  

- multiprocessing.Pool常用函数解析：

  - apply_async(func[,args[,kwds]]): 使用非阻塞方式调用func（并行执行，阻塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
  - apply(func[,arg[,kwds]]) ：使用阻塞方式调用func
  - close(): 关闭Pool，使其不再接受新的任务;
  - join(): 主进程阻塞，等待子进程的退出，必须在close或terminate之后使用

### 进程间通信 -Queue

- 多进程之间，默认是不共享数据的

- 通过Queue（队列Q）可以实现进程间的数据传递

- Q本身是一个消息队列

- 如何添加消息（入队操作）:

  ```python
  from multiprocessing import Queue
  q = Queue(3)
  q.put('消息1')
  q.put('消息2')
  q.put('消息3')
  print(q.full())
  ```

- 可以使用multiprocessing模块的Queue实现多进程之间的数据传递

- 初始化Queue（）对象时（例如：q = Queue()）,括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接收的消息数量没有上限

- Queue.qsize(): 返回当前队列包含的消息数量

- Queue.empty(): 如果队列为空，返回True，反之False

- Queue.full(): 如果队列满了，返回True，反之False

- Queue.get([block,[,timeout]): 获取队列中的一条消息，然后将其从队列中移除，block默认值为True

  - 如果block使⽤默认值， 且没有设置timeout（单位秒） ， 消息列队如果为
     空， 此时程序将被阻塞（停在读取状态） ， 直到从消息列队读到消息为⽌，
     如果设置了timeout， 则会等待timeout秒， 若还没读取到任何消息， 则抛
     出"Queue.Empty"异常 
  - 如果block值为False， 消息列队如果为空， 则会⽴刻抛
     出“Queue.Empty”异常

- •Queue.get_nowait()： 相当Queue.get(False)

- Queue.put(item,[block[, timeout]])： 将item消息写⼊队列， block默认值
   为True

  - 如果block使⽤默认值， 且没有设置timeout（单位秒） ， 消息列队如果已
     经没有空间可写⼊， 此时程序将被阻塞（停在写⼊状态） ， 直到从消息列队
     腾出空间为⽌， 如果设置了True和timeout， 则会等待timeout秒， 若还没空间， 则抛
     出"Queue.Full"异常
  - 如果block值为False， 消息列队如果没有空间可写⼊， 则会⽴刻抛
     出"Queue.Full"异常

  Queue.put_nowait(item)： 相当Queue.put(item, False)； 

- ```python
  from multiprocessing import Queue,Process
  import time
  
  def write(q):
      for value in ['a','b','c']:
          print('开始写入：',value)
          q.put(value)
          time.sleep(1)
  
  
  def read(q):
      while True:
          if not q.empty():
              print('读取到的是：',q.get())
              time.sleep(1)
          else:
              break
  
  if __name__  == '__main__':
      q = Queue()
      pw = Process(target=write,args=(q,))
      pr = Process(target=read, args=(q,))
      pw.start()
      pw.join() #等待接收完毕
      pr.start()
      pr.join()
      print('接收完毕')
  ```

- 进程池创建的进程之间通信：如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue(),而不是multiprocessing.Queue()

- 否则会得到一条如下的错误信息：

  ```python
  RuntimeError: Queue objects should only be shared between processes
   through inheritance.
  ```

- ```python
  from multiprocessing import Manager,Pool
  import time
  
  
  def write(q):
      for i in 'welcome':
          print('开始写入',i)
          q.put(i)
  
  def reader(q):
      time.sleep(3)
      for i in range(q.qsize()):
          print('得到消息',q.get())
  
  if __name__ == '__main__':
      print('主进程启动')
      q = Manager().Queue()
      po = Pool()
      po.apply_async(write, (q,))
      po.apply_async(reader, (q,))
      po.close()
      po.join()
  ```

### 多线程

- 是操作系统能够进行运算调度的最小单位
- 他包含在进程中
- 是进程中的实际运作单位
- 进程是线程的容器
- 线程：实现多任务的另一种方式
- 一个进程中，也经常需要同时做多件事，就需要同时运行多个’子任务‘，这些子任务，就是线程
- 线程又被称为轻量级进程(lightweight process),是更小的执行单元
  - 一个进程可拥有多个并行的(concurrent)线程，当中每一个线程，共享当前进程的资源
  - 一个进程中的线程共享相同的内存单元/内存地址空间➡可以访问相同的变量和对象，而且它们从同一堆中分配对象➡通信、数据交换、同步操作
  - 由于线程的通信是在同一地址空间上进行的，所以不需要额外的通信机制，这就使得通信更简单而且信息传递的速度也更快

#### 进程和线程的区别

- 进程是系统进行资源分配和调度的一个独立单位

- 进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大的提高了程序的运行效率

- 一个程序至少有一个进程，一个进程至少有一个线程

- 线程是进程的一个实体，是CPU调度和分配的基本单位，它是比进程更小的能独立运行的基本单位

- 线程自己基本上不拥有系统资源，只拥有一点在运行中必不可少的资源，但是它可与同属一个进程的其他线程共享进程所拥有的全部资源

- 线程的划分尺度小于进程（资源比进程少）,使得多进程程序的并发性高

- 线程不能独立执行，必须依存在进程中

- 线程和进程在使用上各有优缺点:线程执行开销小，但不利于资源的管理和保护；而进程正相反

- 一般来讲：我们把进程用来分配资源，线程用来具体执行（CPU调度）

  ![image-20200102211619891](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20200102211619891.png)

- python的thread模块是比较底层的模块，在各个操作系统中表现形式不同（低级模块）

- python的threading模块是对thread做了一些包装的，可以更加方便的被使用（高级模块）

- thread有一些缺点，在threading得到了弥补，所以我们直接学习threading

  ```python
  import threading
  if __name__ == '__main__':
      #任何进程默认会启动一个线程，这个线程称为主线程，主线程可以启动新的子线程
      #current_thread():范围当前线程的实例
      #.name：当前线程的名称
      print('主线程%s启动'%(threading.current_thread().name))
  ```

  ```python
  import threading,time
  
  def saySorry():
      print('子线程程%s启动'%(threading.current_thread().name))
      time.sleep(1)
      print('亲爱的，我错了，我能吃饭了吗？')
  
  if __name__ == '__main__':
      print('主进程%s启动'%(threading.current_thread().name))
      for i in range(5):
          t = threading.Thread(target=saySorry)
          t.start()
  ```

#### 查看当前线程数量

```python
import threading
import time

def sing():
    for i in range(3):
        print('正在唱歌。。。%d'%i)
        time.sleep(1)

def dangce():
    for i in range(2):
        print('正在跳舞。。。%d'%i)
        time.sleep(1)

if __name__ == '__main__':
    print('开始：%s'%time.time())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dangce)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        # threading.unumerate(): 返回当前运行中的Thread对象列表
        print('当前线程数为：%d'%length)
        if length <= 1:
            break
        time.sleep(1)
```

- 创建多线程的两种方式：

  - 第一：通过 threading.Thread 直接在线程中运行函数；
  - 第二：通过继承 threading.Thread 类来创建线程
    
  - 这种方法只需要重载 threading.Thread 类的 run 方法，然后调用 start()开启线程就可以了
    
  - ```python
    import threading
    class MyThread(threading.Thread):
        def run(self):
            for i in range(5):
                print(i)
    if __name__ == "__main__":
        t1 = MyThread()
        t2 = MyThread()
        t1.start()
        t2.start()
    
    ```

- ```python
  import threading
  import time
  class MyThread(threading.Thread):
      def run(self):
          for i in range(3):
              time.sleep(1)
              msq = "I`m" + self.name + "@" + str(i)
              #name属性中保存了当前线程的名字
              print(msq)
  if __name__ == "__main__":
      t = MyThread()
      t.start()
  
  ```

#### 线程的五种状态

- 1、新状态：线程对象已经创建，还没有在其上调用start()方法。
- 2、可运行状态：当线程有资格运行，但调度程序还没有把它选定为运行线程时线程所处的状态。当start()方法调用时，线程首先进入可运行状态。在线程运行之后或者从阻塞、等待或睡眠状态回来后，也返回到可运行状态。
- 3、运行状态：线程调度程序从可运行池中选择一个线程作为当前线程时线程所处的状态。这也是线程进入运行状态的唯一一种方式。
- 4、等待/阻塞/睡眠状态：这是线程有资格运行时它所处的状态。实际上这个三状态组合为一种，其共同点是：线程仍旧是活的（可运行的），但是当前没有条件运行。但是如果某件事件出现，他可能返回到可运行状态。
- 5、死亡态：当线程的run()方法完成时就认为它死去。这个线程对象也许是活的，但是，它已经不是一个单独执行的线程。线程一旦死亡，就不能复生。如果在一个死去的线程上调用start()方法，会抛出java.lang.IllegalThreadStateException异常。

#### 线程共享全局变量

- 在⼀个进程内的所有线程共享全局变量， 多线程之间的数据共享（这点要⽐多进程要好）

- 缺点就是， 可能造成多个线程同时修改一个变量（即线程⾮安全），可能造成混乱

- ```python
  import threading
  import time
  
  num = 100
  def work1():
      global num
      for i in range(3):
          num += 1
      print("---in work1,num is %d" %num)
  def work2():
      global num
      print("---in work2,num is %d" %num)
      print("---线程创建之前 num is %d" %num)
  t1 = threading.Thread(target=work1)
  t1.start()
  time.sleep(1)
  #延时一会保证线程1中的任务做完
  t2 = threading.Thread(target=work2)
  t2.start()
  ```

- ```python
  import threading,time
  def work1(nums):
      nums.append(44)
      print('-----in work1-----' ,nums)
  def work2(nums):
      time.sleep(1)
      #延时一会保证另一线程执行
      print('-----in work2-----', nums)
  
  g_nums = [11,22,33]
  t1 = threading.Thread(target=work1,args=(g_nums,))
  t1.start()
  t2 = threading.Thread(target=work2,args=(g_nums,))
  t2.start()
  ```

#### 执行10000000次的bug

- ```python
  import threading
  num = 0
  def test1():
      global num
      for i in range(100):#一百万错误
  	    num += 1
  def test2():
      global num
      for i in range(100):#一百万错误
  	    num += 1
  p1 = threading.Thread(target=test1)
  p1.start()
  p2 = threading.Thread(target=test2)
  p2.start()
  print("---num = %d---" %num)
  ```

### 线程同步

- 当多个线程⼏乎同时修改某⼀个共享数据的时候， 需要进⾏同步控制 
- 线程同步能够保证多个线程安全访问竞争资源， 最简单的同步机制是引⼊互
   斥锁 
- 互斥锁保证了每次只有⼀个线程进⾏写⼊操作，从⽽保证了多线程情况下数据的正确性（原子性）
- 互斥锁为资源引入一个状态：锁定/非锁定。某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
- threading模块中定义了Lock类， 可以⽅便的处理锁定 



## 网络编程

### 网络基础

#### ip地址



- 如何在网络中唯一标识一台计算机？-----------ip地址

- 同一台计算机上的多个程序如何共同网络而不冲突？-----网络端口

- 不同的计算机通信怎么才能互相理解？ -------使用相同的协议

- IP地址：用来在网络中标记一台电脑的一串数字，比如192.168.1.1（c类）；在同一网络上是唯一的（用来标记唯一的一台电脑）

- 每一个IP地址包括两部分：网络地址和主机地址

- 主机号0，255两个数不能使用（网络号，广播地址）

  ![image-20191231115510702](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20191231115510702.png)

- A类IP地址由1字节的网络地址和3字节的主机地址组成，网络地址的最高位必须是’0‘，地址范围1.0.0.1—126.255.255.254 可用的A类网络有126个，每个网络能容纳1677214个主机
- B类IP地址由2个字节的⽹络地址和2个字节的主机地址组成， ⽹络地址的最⾼位必须是“10”，地址范围128.1.0.1-191.255.255.254 可⽤的B类⽹络有16384个， 每个⽹络能容纳65534主机
- C类IP地址由3字节的⽹络地址和1字节的主机地址组成， ⽹络地址的最⾼位必须是“110”范围192.0.1.1-223.255.255.254  C类⽹络可达2097152个， 每个⽹络能容纳254个主机
- D类IP地址第⼀个字节以“1110”开始， 它是⼀个专⻔保留的地址。它并不指向特定的⽹络， ⽬前这⼀类地址被⽤在多点⼴播（一对多） 中多点⼴播地址⽤来⼀次寻址⼀组计算机 地址范围224.0.0.1-239.255.255.254
- E类IP地址以“1111”开始， 为将来使⽤保留 E类地址保留， 仅作实验和开发用
- 私有IP:本地局域网上的IP,专门为组织机构内部使用
- 在这么多网络IP中，国际规定有一部分IP地址是用于我们的局域网使用，属于私网IP,不在公网中使用，它们的范围是：
  - 10.0.0.0~10.255.255.255
  - 172.16.0.0~172.31.255.255
  - 192.168.0.0~192.168.255.255
  - 私有IP：局域网通信，内部访问，不能在外网公用。私有IP禁止出现在internet中，来自于私有IP的流量全部都会阻止并丢掉
  - 公有IP：全球访问
- IP地址 127.0.0.1 用于回路测试
  - 测试当前计算机的网络通信协议
  - 如：127.0.0.1可以代表本机IP地址，用 http://127.0.0.1 就可以测试本机配置的web服务器
  - 常用来ping：127.0.0.1来看本地ip/tcp正不正常，如能ping通即可正常使用
- 子网掩码：是我们测量两个IP是否属于同一个网段的工具
  - 子网掩码不能单独存在，他必须结合IP地址一起使用
  - 子网掩码只有一个作用，就是将某个IP地址划分为网络地址和主机地址两部分
  - 子网掩码的设定必须遵循一定的规则：
    - 与IP地址相同，子网掩码的长度也是32位
    - 左边是网络位，用二进制数字’1‘表示
    - 右边是主机位，用二进制数字’2‘表示
  - 假设IP地址位’192.168.1.1‘ 子网掩码为’255.255.255.0'  其中‘1’有24个，代表于此相对应的IP地址左边24位是网络号；‘0’有8个，代表与此相对应的IP地址右边是主机号

#### 端口号

- 端口号：用来标记区分进程

- 一台拥有IP地址的主机可以提供许多服务，比如HTTP（万维网服务）、FTP(文件传输)、SMTP(电子邮件) 等，这些服务完全可以通过一个IP地址来实现。那么主机是怎样区分不同的网络服务呢

- 显然不能只靠IP地址，因为IP地址与网络服务的关系是一对多的关系。实际上是通过‘ip地址+端口号‘来区分不同的服务的。

  ![image-20191231121448458](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20191231121448458.png)

- 端口号是一个数字，只有整数，范围是从0到65535 （分为知名和动态两种）

- 知名端口是众所周知的端口号（用来做固定事情），范围从0到1023

  - 80端口分配给HTTP服务（网站）
  - 21端口分配给FTP服务（文件下载）
  - 可以理解为，一些常用的功能使用的号码是固定的

- 动态端口的范围是从1024到65535

  之所以称为动态端口 ，是因为它一般不固定分配某种服务，而是动态分配。动态分配是指当一个系统进程或应用程序进程需要网络通信时，它向主机申请一个端口，主机从可用端口号中分配一个供它使用

#### 协议



- 协议：约定好的规范

- 早期的计算机网络，都是由各厂商自己规定一套协议，IBM、Apple和Microsoft都有各自的网络协议，互不兼容（语言、方言、阿帕网）

  为了能把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。

  因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP/IP/协议，所以，大家把互联网的协议总称TCP/IP协议 （大家都遵循的最基本网络通信协议）

- 是完成进程之间通信的规范

- 根据TCP/IP协议簇功能的不同，将他们分为了几种层次（TCP/IP协议簇层次划分）（重点记住）

  - 写代码按四层划分
    - 网络接口层（链路层）
    - 网络层
    - 传输层
    - 应用层
  - 理论上是由七层组曾
    - 物理层
    - 数据链路层
    - 网络层
    - 传输层
    - 会话层
    - 表示层
    - 应用层

  ![image-20191231152654362](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20191231152654362.png)

- 在早期，不同的公司都推出了属于自己的私有网络协议，相互之间不能兼容

- 于是，ISO（国际标准化组织）站出来：干脆这样，我给大家制定一个通用的网络通信协议，该协议是国际标准

- 于是ISO博览众家之长，制定了’一堆‘详细的，复杂的，繁琐的，精确的网络通信协议

- 不过这堆协议太复杂了，为了理清思路，便于学习，将他们分为了7类（也就是分了7层），不同层代表不同的供能，并把这些协议归到相应的层里面去

- 国际标准出来了，接下来就是要软件/硬件厂商去实现了。但实际上各厂商并没有完整实现7层协议，因为7层协议栈追求全能、完善、导致它太过复杂，实现起来太难了

- 于是，实际使用时，按4层划分（5层划分非官方）

- ![image-20191231153402691](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20191231153402691.png)

- OSI七层协议，是英文Open System Interconnect的缩写，中文翻译开放系统互联

- TCP/IP定义了电子设备如何接入因特网，以及数据如何在它们之间传输的标准

- 4层的层级结构中，每一层都呼叫它的下一层所提供的网络来完成自己的需求

- 其中的应用层关注的是应用程序的细节，而不是数据在网络中的传输活动

  其他三层主要处理所有的通信细节，对应用程序一无所知：

  - 应用层：应用程序间沟通的层，不同的文件系统有不同的文件命名原则和不同的文本行表示方法等，不同的系统之间传输文件还有各种不兼容问题，这些都将由应用层来处理
  - 传输层：在此层中，它提供了节点间的数据传送服务，如传输控制协议（TCP）、用户数据报协议（UDP）等，这一层负责传送数据，并且确定数据已被送达并接收
  - 网络层：负责提供基本的数据包传送功能，让每一块数据包都能够到达目的主机。网络层接收由更低层发来的数据包，并把该数据包发送到更高层，相反，IP层也把从TCP或UDP层接收来的数据包传送到更低层
  - 网络接口层：对实际的网络媒体的管理，定义如何使用实际网络来传送数据（处理机械的、电气的和过程的接口）

### Socket编程

#### 简介

- Socket：通过网络完成进程间通信的方式（区别于一台计算机之间进程通信）

- Socket的英文愿义是’插孔’。通常也称作‘套接字’

  ![image-20191231154310722](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20191231154310722.png)

- Socket本质是编程接口（API）：Socket是对TCP/IP协议的封装，Socket只是个编程接口不是协议，通过Socket我们才能使用TCP/IP协议簇（程序员层面）

- TCP/IP也要提供可供程序员做网络开发所用的接口，这就是Socket编程接口：HTTP是轿车，提供了封装或者显示数据的具体形式；Socket是发动机，提供了网络通信的能力

- 最重要的是，Socket是面向客户/服务器模型而设计的，针对客户和服务器程序提供不同的Socket系统调用

- 套接字之间的连接过程可分为三个步骤：服务器监听，客户端请求，连接确认

- 创建Socket：

  ```python
  import socket
  #导入套接字模块
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #s此时是一个socket对象，拥有发送和接收网络数据的功能
  
  ```

  - 该函数带有两个参数（参数必须写）

    - AF_INET（ipv4协议⽤于 Internet 进程间通信）

    - 套接字类型， 可以是 SOCK_STREAM（流式套接字， ⽤于
       TCP 协议） 或者 SOCK_DGRAM（数据报套接字， ⽤于 UDP 协
       议） 

      - TCP慢但是稳定不会丢数据

      - UDP快但是可能会丢数据（黑客攻击）

  - 确定了IP地址端口号（ipv4协议），TCP或UDP协议之后，计算机之间可以进行通信

#### UDP和TCP

- UDP --- User Data Protocol，用户数据报协议，是⼀个⽆连接的简单的⾯向数据报的传输层协议。 UDP不提供可靠性， 它只是把应⽤程序传给IP层的数据报发送出去， 但是并不能保证它们能到达⽬的地。 由于UDP在传输数据报前不⽤在客户和服务器之间建⽴⼀个连接， 且没有超时重发等机制，故而传输速度很快

- UDP⼀般⽤于多点通信和实时的数据业务， ⽐如：

  - 语⾳⼴播
     视频
     QQ
     TFTP(简单⽂件传送）

  - 可以理解为写信

- TCP（Transmission Control Protocol，传输控制协议）是面向连接的协议，也就是说，在收发数据前，必须和对方建立可靠的连接

- 一个TCP连接必须要经过三次“对话”才能建立起来，其中的过程非常复杂，只简单的描述下这三次对话的简单过程：

  - 主机A向主机B发出连接请求数据包：“我想给你发数据，可以吗？”，这是第一次对话

  - 主机B向主机A发送同意连接和要求同步（同步就是两台主机一个在发送，一个在接收，协调工作）的数据包：“可以，你什么时候发？”，这是第二次对话

  - 主机A再发出一个数据包确认主机B的要求同步：“我现在就发，你接着吧！”，这是第三次对话

  - 三次“对话”的目的是使数据包的发送和接收同步，经过三次“对话”之后，主机A才向主机B正式发送数据
  - 可以理解为打电话，先建立通道

- TCP与UDP的区别：
  - 基于连接与无连接
  - 对系统资源的要求（TCP较多，UDP少）
  - UDP程序结构较为简单
  - 流模式与数据报模式
  - TCP保证数据正确性，UDP可能丢包，TCP保证数据顺序，UDP不保证

##### UDP编程

- 发送数据：为看到效果先安装‘网络调试助手’

  ```python
  from socket import *
  s = socket(AF_INET, SOCK_DGRAM) #创建套接字
  addr = ('192.168.1.17', 8080) #准备接收方地址
  data = input("请输入：")
  s.sendto(data.encode(),addr)
  #发送数据时，python3需要将字符串转成byte
  #encode(‘utf-8’)# 用utf-8对数据进行编码，获得bytes类型对象
  #decode（）反过来
  s.close()
  ```

- 发送数据给飞秋

  飞秋使用 2425端口

  发送普通数据，飞秋不会响应，必须发送特殊格式的内容

  1:123123:吴彦祖:吴彦祖-pc:32:haha
   飞秋有自己的应用层协议

  - 1表示版本

  - 后边的数字发送的时间，随便写

  - 32代表发送消息

  - 飞秋炸弹：循环不延时发消息（可能会造成卡死）

    注意：IP和端口在网络通信中缺一不可，用到的协议也要匹配，例如飞秋用的是udp协议，使用TCP协议发数据是无效的

    udp理解为写信（只有收件人地址），TCP理解为打电话（先拨号建立通路，需要通路稳定）

- 接收数据

  ```python
  from socket import *
  s = socket(AF_INET, SOCK_DGRAM) #创建套接字
  s.bind(('', 8788))
  addr = ('192.168.1.17', 8080) #准备接收方地址
  data = input("请输入：")
  s.sendto(data.encode(),addr)
  #等待接收数据
  redata = s.recvfrom(1024)
  #1024表示本次接收的最大字节数
  print(redata)
  s.close()
  ```

  

- 绑定信息：

  如果信息没有绑定，每发送一次信息，系统会随机分配一个端口

  ![image-20191231212602235](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20191231212602235.png)

- 还要避免同一台计算机上的不同进程端口号相同的问题

  ![image-20191231212643038](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20191231212643038.png)

  

- 绑定信息：让一个进程可以使用固定的端口

- 一般情况下，发送方不绑定端口，接收方会绑定

  ```python
  from socket import *
  s = socket(AF_INET, SOCK_DGRAM) #创建套接字
  s.bind(('', 8788))   #绑定一个端口，ip地址和端⼝号，ip⼀般不⽤写
  addr = ('192.168.1.17', 8080)   #准备接收方地址
  data = input("请输入：")
  s.sendto(data.encode(),addr)
  redata = s.recvfrom(1024) #1024表示本次接收的最⼤字节数
  print(redata)
  s.close()
  ```

- echo服务器：echo服务是一种非常有用的用于调试和检验的工具，这个协议的作用也十分简单，接收到什么原封发回

  ```python
  from socket import *
  #创建套接字
  udpSocket = socket(AF_INET,SOCK_DGRAM)
  #绑定本地信息，不使用随机分配的端口
  binAddr = ('',7088)
  udpSocket.bind(binAddr)
  num = 0
  while True:
      #接收对方发送的数据
      recvData = udpSocket.recvfrom(1024)
      print(recvData)
      #将接收到的数据发回给对方
      udpSocket.sendto(recvData[0],recvData[1])
      num += 1
      print('已将接收到的第%d个数据返回给对方,'%num)
  udpSocket.close()
  ```

- 聊天室

  ```python
  from socket import *
  import time
  #1创建套接字
  udpSocket = socket(AF_INET, SOCK_DGRAM)
  bindAddr = ("",7088)
  udpSocket.bind(bindAddr)#绑定
  while True:
      #接收对方发送的数据
      recvData = udpSocket.recvfrom(1024)
      print('【%s】 %s.%s' %(time.ctime(),recvData[1],recvData[0].decode("GB2312")))
      a = input("请输入：")
      udpSocket.sendto(a.encode('GB2312'),('192.168.1.17',8080))
  #5关闭套接字
  udpSocket.close()
  ```

- udp网络通信过程：（类似于发快递）

  - 应用层编写数据（你好），然后向下层传递
  - 传输层在数据前面加上端口号（包括发送端口和目的端口）
  - 网络层继续在前面加上IP地址（包括原IP和目的IP）
  - 链路层再在前面加上MAC地址（MAC:硬件地址，用于定义网络设备的位置）

  此时数据变成了：MAC地址 IP地址 端口号 数据内容

  之后通过网络传输给另一台计算机的链路层开始逐步解析判断

- 练习：使用多线程完成一个全双工的聊天程序
  - 全双工（Full Duplex）是通讯传输的一个术语。通信允许数据在两个方向上同时传输（电话）
  - 单工只是允许甲方向乙方传送信息，而乙方不能向甲方传送（收音机）
  - 半双工：甲方发消息时乙方只能收不能发（对讲机）

#### 字符集

- ASCII

  英文字符集 1个字节

- ISO8859-1

  西欧字符集 1个字节

- BIG5

  台湾的大五码，表示繁体汉字 2个字节

- GB2312

  大陆使用最早、最广的简体中文字符集 2个字节

- GBK

  GB2312的扩展，可以表示繁体中文 2个字节

- GB18030

  最新GBK的扩展，可以表示汉字、维吾尔文、藏文等中华民族字符 2个字节

- Unicode

  国际通用字符集 2个字节

#### TFTP客户端

- TFTP（Trivial File Transfer Protocol,简单⽂件传输协议）是TCP/IP协议簇中的⼀个⽤来在客户端与服务器之间进⾏简单⽂件传输的协议
  - 使用TFTP这个协议，就可以实现简单文件的下载
- 特点：
  - 简单
  - 占⽤资源小
  - 适合传递小文件
  - 适合在局域网进行传递
  - 端口号为69
  - 基于UDP实现



## 数据库

### 数据库的相关概念

#### 数据



- 数据：是描述事物的一种符号
  - 数据就是数值，是指对客观事件（客观事物）进行观察的结果
  - 是对客观事物的性质，状态以及相互关系等进行记载的符号或这些符号的组合
  - 它是可以进行记录并可以借鉴别的符号，是对客观事物的逻辑归纳
- 表现形式多样：文本、图形、音视频（都是二进制）
  - 数据有很多种，最简单的就是数字
  - 数据也可以是文字、图像、声音等
  - 

#### 数据库（DataBase/DB）

- 数据库（DataBase，简称DB）:存放数据的仓库（文件夹）
  - 数据按照一定的格式存放在计算机中，可为用户共享
  - 方便存储、快速查找

- 数据库管理系统（DataBase Management System 简称DBMS）
  - 科学的组织和存储数据
  - 是一种操纵和管理数据库的大型软件，用于建立、使用和维护数据库
  - 它对数据库进行统一的管理和控制，以保证那个数据库的安全性和完整性
  - 用户通过DBMS访问数据库中的数据，数据库管理员也通过DBMS进行数据库的维护工作
  - 有oracle、MySQL、SQL Server等等
    - mysql主要用于大型门户，例如搜狗、新浪等，它主要的优势就是开放源代码，因为开放源代码这个数据库是免费的，他现在是甲骨文公司的产品。（官网下载，有些大公司会做二次封装用自己的）
    - oracle主要用于银行、铁路、飞机场等。该数据库功能强大（规避很多风险），软件费用高。也是甲骨文公司的产品
    - sql server是微软公司的产品，主要应用于大中型企业，如联想、方正等（使用较少）

- 数据库应用程序（DBAS）
  - 在数据库管理系统的基础上，使用数据库管理系统的语法，直接面对最终稿用户的应用程序
  - 图书管理系统、人事管理系统等等
- 数据库管理员（DBA）
  
  - 数据库管理系统的操作者
- 最终用户
  
- 数据库应用程序的使用者
  
- 数据库系统（DBS）

  - 数据库 + 数据库管理系统 + 数据库应用程序 + 数据库管理员 + 最终用户

    ![image-20200106202742869](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20200106202742869.png)

#### 数据库的好处

- 程序稳定性：任意一台服务器所在的机器崩溃了都不会影响数据和另外的服务（备份）
- 数据一致性：所有的数据都存储在一起，所有的程序操作的数据都是统一的，就不会出现数据不一致的现象
- 并发:数据库可以良好的支持并发，所有的程序操作数据库都是通过网络，而数据库本身支持并发的网络操作，不需要我们自己写socket
- 效率：使用数据库对数据进行增删改查的效率要高出我们自己处理文件很多

#### 总结

- 数据库服务器：一台计算机运行数据库管理软件
- 数据库管理软件：管理-数据库
- 数据库：即文件夹，用来组织文件/表
- 表：即文件，用来存放多行内容/多条记录

### MySQL

- MySQL:是一个应用广泛、免费、开源的关系型数据库管理系统
  - 关系型数据库需要有表结构
    - 关系型数据库最典型的数据结构是表，由二维表及其之间的联系所组成的一个数据组织
  - 优点：
    - 易于维护：都是使用表结构，格式一致
    - 使用方便：SQL语言通用，可用于复杂查询
    - 复杂操作：支持SQL、可用于一个表以及多个表之间非常复杂的查询
  - 缺点：
    - 读写性能比较差，尤其是海量数据的高效率读写
    - 固定的表结构，灵活度稍欠
    - 高并发读写需求，传统关系型数据库来说，硬盘I/O是一个很大的瓶颈

### MySQL操作

- 登录管理员用户：

  ```mysql
  mysql -uroot -p 
  ```

- 远程登录MySQL服务器：

  ```mysql
  mysql -uroot -p123 -h+ip地址
  ```

- 查看当前用户：

  ```mysql
  select user();
  ```

- 退出：

  ```mysql
  exit;
  ```

- 给当前账户设置密码（必须以管理员登录）：

  ```mysql
  set password = password('123')
  ```

- 创建一个其他用户：

  ```mysql
  mysql> create user 'shang'@'192.168.10.%'   IDENTIFIED BY '123'; #指定网段密码
  mysql> create user 'shang'@'192.168.10.5'  # 指示某机器可以连接
  mysql> create user 'shang'@'%'   #指示所有机器都可以连接
  
  ```

- 给一个用户授权：

  ```mysql
  grant 权限类型 on 数据库名称.*(或表名) to 'shang'@'%';
  
  - all 所有权限
  - select 查
  - select，insert 查和写
  
  mysql> flush privileges;    # 刷新使授权立即生效（万一没有立即生效）
  
  
  ```

- 创建账号并授权

  ```mysql
  grant all on 数据库名称 .* to 'alex'@'%' identified by '123'
  
  ```

  

### SQL

- SQL:结构化查询语言，是一种特殊的编程语言（4代）
  - 是用于访问和处理数据库的标准化的计算机语言
  - 用于存取数据以及查询、更新、管理关系数据库系统
  - 1986年10月，美国国家标准协会（AESC）对SQL进行规范后，以此作为关系式数据库管理系统的标准语言
  - 不过各种通行的数据库系统在其实实践过程中都对SQL规范做了某些编改和扩充。所以实际上不同数据库系统之间的SQL不能完全相互通用
  - 针对不同的数据库，如hivesq, mysql, sqlserver, oracle等，sql语法会有所不同，但是总体上大同小异
- SQL的作用：使我们有能力访问数据库，需要在数据库上执行的大部分工作都由 SQL 语句完成
  - SQL 面向数据库执行查询
  - SQL 可从数据库取回数据
  - SQL 可在数据库中插入新的记录
  - SQL 可更新数据库中的数据
  - SQL 可从数据库删除记录
  - SQL 可创建新数据库
  - SQL 可在数据库中创建新表
  - SQL 可在数据库中创建存储过程
  - SQL 可在数据库中创建视图
  - SQL 可以设置表、存储过程和视图的权限

- SQL语言的5个部分（重要性从高到低）：

  - 数据查询语言（DQL:Data Query Language）：select
    
  - 其语句，也称为“数据检索语句”，用以从表中获得数据，确定数据怎样在应用程序给出
    
  - 数据操作语言（DML：Data Manipulation Language）：inster,updata,delete
    
  - 其语句包括动词INSERT，UPDATE和DELETE。它们分别用于添加，修改和删除表中的行。也称为动作查询语言
    
  - 数据定义语言（DDL）：create,alter,drop
    
  - 在数据库中创建新表或删除表；为表加入索引等
    
  - 数据控制语言（DCL）：grant,revoke
    
  - 它的语句确定单个用户和用户组对数据库对象的访问
    
  - 事务处理语言（TPL）：
    
  - 它的语句能确保被DML语句影响的表的所有行及时得以更新
    
  - 前三个部分必须掌握，后两个部分可以现用现查

  - 同时注意：**SQL** **对大小写不敏感**

    

- 数据库操作（DDL）:

  - 创建数据库：
    - CREATE DATABASE 数据库名称；
      - CREATE DATABASE test101 CHARSET=utf8;
  - 删除数据库：
    - DROP DATABASE 数据库名称；
  - 切换数据库：
    - USE 数据库名称 ;

  - 显示所有数据库：
    - USE 数据库名称;

  - 查看当前选择的数据库
    - 

  -  -- 代表注释

- 表的概念：

  - 在操作数据时，多部份数据应以表的形式存储

  - 例如一个学生管理系统：在一个数据库中将信息分类；学生信息、成绩、考勤记录、教师信息等 分别存放在不同的表中

  - 创建表：

    ```mysql
    CREATE TABLE t_person(    
    id INT PRIMARY KEY,         int代表数据类型
    NAME VARCHAR(32)         字段名 数据类型
    )
    
    ```

    数据类型（常用）：

    数字：int , decimal（小数）

    字符串：varchar，char

    日期：datatime（日期加时分秒）

- char与varchar:
  - char与varchar后面接的数据大小为存储的字符数，而不是字节数（MySQL4.1之后）
  - char定义的是固定长度，长度范围为0-255，存储时，如果字符数没有达到定义的位数，会在后面用空格补全存入数据库中
  - varchar是变长长度，长度范围为0-65535，存储时，如果字符没有达到定义的位数，也不会在后面补空格

- 显示所有的表：

  - SHOW TABLES;

- 修改表（列）：

  - ALTER TABLE t_person ADD age INT;

  - 格式：

    - alter table 表名 add（增加列）列名 类型
      - ALTER TABLE t_person ADD age INT;

    - change（修改列名和数据类型）
      - ALTER TABLE t_person CHANGE age age_num VARCHAR(10);

    - drop（删除列）
      - ALTER TABLE t_person DROP ageNum;

    - modify（修改列的数据类型）
      - ALTER TABLE t_person MODIFY age VARCHAR(10);

- 查看表结构：

  DESC t_person;

- 删除表： 

  DROP TABLE t_person;

- 更改表名称：

  RENAME TABLE t_person TO t_user;

- 查看表的创建语句：

  SHOW CREATE TABLE t_person;

- 在表中放数据：
  - 查询表的信息（后面详细讲）
    - SELECT * FROM t_person;
    - select代表查询 * 代表查询表中所有信息 from 在哪查
  - 增加数据
    - INSERT INTO t_person VALUES('刘备'，'蜀国')；
    - 注意：在表中增加的数据，必须与表中的列对应
    - 另一种写法：INSERT INTO t_person(NAME,country) VALUES('曹操','魏国')
    - 当列数比较多时，可以用上面的方法指定列名选择性增加，顺序必须一一对应
    - 连续添加：INSERT INTO t_person VALUE('孙权','吴国'),('小乔','吴国')；
    - 后面的括号可以有任意个

- 修改数据：

  - UPDATE t_person SET NAME = '大乔' WHERE country = '蜀国'

    - update代表更新后面表中的值，把name改变为‘大乔’

    - where代表从contry = ‘蜀国’的更新

    - 更好的方式是我们在表中添加一个列叫做‘id’，每一行都有不同的id，之后通过id去修改相应的数据

  - 删除数据：

    - DELETE FROM t_person WHERE id = 1
    - 如果不加where,   DELETE FROM t_person;会删除所有表中的内容

- 数据的备份与恢复：
  - 数据库中的数据是非常宝贵的，尤其是已经上线的项目
  - 在维护和操作时，一定要先备份一份，之后再去操作数据库

- 数据库可能会遭遇各种各样的不测从而导致数据丢失，大概分为以下几种：
  - 硬件故障
  - 软件故障
  - 自然灾害
  - 黑客攻击
  - 误操作（占比最大）

- 数据备份

  - 1，在MySQL的bin目录中打开命令窗口（bin目录中才有复制的命令）

  - 2，输入：

    ```mysql
    mysqldump –uroot –p test101 > C :\t1.sql  （如果有警告可以忽略）
    ```

- 数据恢复

  - 连接MySQL，创建数据库

  - 在MySQL的bin目录中打开命令窗口

  - 输入：

    ```mysql
    mysql –uroot –p 数据库名 < d:\t1.sql
    
    ```

    

### 数据类型

#### 整数

- MySQL支持所有标准SQL数值数据类型：

  - 关键字INT是INTEGER的同义词，m表示该数据类型指定的显示宽度，指定能够显示的数值中数字的个数。比如说，定义：year int(4),声明一个只显示4位数字宽度表示年的字段

  - 显示宽度和数据类型的取值范围是无关的（int unsigned）

    ![image-20200109111333805](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20200109111333805.png)

#### 小数

- 关键字DEC是DECIMAL的同义词

- MySQL中使用浮点数和定点数来表示小数。它们都可以用（m，n）来表示，其中m称为精度，表示总共的位数；n称为标度，是表示小数的位数（四舍五入）

  ![image-20200109111640820](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20200109111640820.png)

#### 日期

- date 20190101（格式要求严格，差一位都不行）

- 如果定义了timestamp 不能为空置，默认为当前时间（不常用）

- 插入值时 values （now（））代表当前时间

  ![image-20200109111954576](C:\Users\MrAme\AppData\Roaming\Typora\typora-user-images\image-20200109111954576.png)

  ```mysql
  create table t_5(
      dt datetime not null
      default current_timestamp
  on update current_timestamp)
  ```

#### 字符串

- char(18) 最多255个字符
  - 定长储存，浪费空间，范围小，节省时间
  - 不足时位数补空格（查询时不显示空格 ）
- varchar(18) 最多7=65535个字符
  - 变长存储，节省空间，范围大，存取速度慢
- char适合：身份证号/手机号/QQ号用户名密码等经常做查询的
- varchar适合：评论，朋友圈，微博等查询频率不高的

#### 枚举/集合

- enum 单选行为（枚举）
  - 例如建表时定义字段
    - 性别enum（‘男’，‘女’）
- set 多选行为（集合）
  - 例如建表时定义字段
    - 爱好 set（‘游泳’，‘篮球’，‘下棋’，‘音乐’，‘旅游’）
    - insert时会自动去重和去掉不存在的

### 主键

- 表中每一行都应该具有可以标识自己的一列（或一组列）
- 而这个承担标识作用的列称为主键。
  - 如果没有主键，数据的管理将会十分混乱。比如会存在多条一摸一样的记录，删除和修改特定行十分困难
- 任何列都可以作为主键，主要它满足以下条件：
  - 任何两行都不具有相同的主键值（唯一）
  - 每个行都必须具有一个主键值（不能为空）
  - 主键列的值不允许进行修改和更新

#### 设置主键

```mysql
-- 创建数据库
CREATE DATABASE test2;
-- 显示数据库列表
SHOW DATABASES;
--使用数据库
USE test2; 
-- 创建表之后设置主键：
CREATE TABLE t1(
   id INT NOT NULL,
   NAME CHAR(20)
);
ALTER TABLE t1 ADD PRIMARY KEY (id);

```

```mysql
-- 创建时就带有主键的
CREATE TABLE t2(
   id int primary key,
   name char(20)
); 



```

```mysql
-- 自动更新的主键
CREATE TABLE t_user(
id INT PRIMARY KEY AUTO_INCREMENT,
-- id  你自己起的字段名字。
-- int  数据类型，整型。
-- primary key 定义这个字段为主键。
-- auto_increment 定义这个字段为自动增长，即如果INSERT时不赋值，则自动加1
uname VARCHAR(32) )；
-- 添加信息
INSERT INTO t_user(uname) VALUES('吕布')
-- 查看
SELECT * FROM t_user;

```

### select查询



```mysql
select查询： 
CREATE TABLE t_user(
id INT PRIMARY KEY AUTO_INCREMENT,
uname VARCHAR(32),
age INT,
country VARCHAR(10)
);
INSERT INTO t_user(uname) VALUES('吕布')
...
-- 查询一个表中的所有数据(所有列)
SELECT * FROM t_user;
-- 查询某一列
SELECT uname FROM t_user;

-- 查询某几列
SELECT uname,country,age FROM t_user;
修改select后面字段的顺序可以修改显示结果的顺序

-- 查询某几列，并且所有人年龄增加50（使用算数表达式）
SELECT uname,country,age+50 FROM t_user;

-- 修改列名的显示（起别名）注意不要用关键字，as可以省略
SELECT age+50 AS '年龄' FROM t_user;

-- 查询时去除重复项（国家会重复）
SELECT DISTINCT country FROM t_user;

distinct：作用范围是后面所有字段的组合（可以有多个字段）
SELECT DISTINCT country，uname FROM t_user;
-- 查询每个国家都有谁，注意：distinct后面的字段用逗号分隔，逗号两边不能有空格


```

### 排序

- SELECT DISTINCT country,uname FROM t_user ORDER BY country;

- 按国家排序

  

- SELECT DISTINCT country,uname,age FROM t_user ORDER BY country,age;

- 按国家和年龄排序（默认从低到高）

  

- SELECT DISTINCT country,uname,age FROM t_user ORDER BY country,age DESC;

- 排列顺序从高到低

  

- SELECT DISTINCT country,uname,age FROM t_user ORDER BY country,age ASC;

- 排列顺序从低到高（默认）

### 按条件查询

#### 限制查询条件

- 查出所有年龄超过20岁的人
  - SELECT uname,age FROM t_user WHERE age>20;
- 查出某个国家所有年龄超过20的人
  - SELECT uname,age FROM t_user WHERE age>20 AND country='魏国';

- 查出年龄为21或者67的人
  - SELECT uname FROM t_user WHERE age=21 OR age=67;

#### 设置查询条件

- like
  - WHERE 子句中可以使用等号 **=** 来设定获取数据的条件， country='魏国’
  - 但是有时候我们需要获取含有某个字符的所有记录，这时我们就需要在 WHERE 子句中使用 LIKE 子句
  - SELECT uname,age FROM t_user WHERE age>20 AND uname LIKE ‘吕%';
  - SELECT uname,age FROM t_user WHERE age>20 AND uname LIKE ‘%乔';
  - SQL LIKE 子句中使用百分号 **%**字符来表示任意字符，如果没有使用百分号 **%**, LIKE 子句与等号 **=** 的效果是一样的



### 分页

- 在查询时可以只检索前几条或者中间某几行数据（数据量很大时，几百万条）

- SELECT * FROM t_user LIMIT 0,3;

- limit 后面的第一个数字设置从哪里开始检索（偏移量，从0开始）

- limit 后面的第二个数字是设置显示多少条
- 问题：查询第11-15条怎么写

### 聚合函数和内置函数

#### 聚合函数：



- 为了快速得到统计数据（多条数据的统计结果），提供了5个聚合函数

- count():查询表中某项数据一共包含了多少条（统计数据）

  ```mysql
  --查询表中共包含多少条数据（会检索所有列）
  SELECT COUNT(*) FROM t_user ;
  --查询表中一共有多少个人（只会检索一列）
  SELECT COUNT(uname) FROM t_user ;
  
  推荐使用第二种写法，可以提高效率
  ```

```mysql
max(列)：求此列的最大值
SELECT MAX(age) FROM t_user ;

min(列)：求此列的最小值
SELECT MIN(age) FROM t_user ;

sum(列)：求此列的和
SELECT SUM(age) FROM t_user ;

avg(列)：求此列的平均值
SELECT AVG(age) FROM t_user ;

查出总人数、最大年龄、最小年龄、年龄的总和、平均年龄
SELECT COUNT(uname),MAX(age),MIN(age),SUM(age),AVG(age) FROM t_user ;
```



#### 内置函数（了解即可）

- 字符串函数：

  ```mysql
  ascii（str）查看字符的ASCII码值,str是空时返回0
  SELECT ASCII('a')
  
  char(数字)查看ASCII码值对应的字符
  SELECT CHAR(97)
  
  concat（str1,str2,...）拼接字符串
  SELECT CONCAT(12,34,'ab')
  SELECT uname,CONCAT(age,'岁') FROM t_user;
  
  length（str）字符串中包含的字符个数
  SELECT LENGTH('abc')
  ```

  

- 截取字符串：

  ```mysql
  left（str，len）截取字符串左端的len个字符
  SELECT LEFT('qwertyui',3)
  
  right（str,len）截取字符串右端的len个字符
  SELECT RIGHT('qwertyui',3)
  
  substring(str,pos,len) 指定位置截取：截取字符串str的位置pos起的len个字符（从1开始）
  SELECT SUBSTRING('qwertyuio',2,3)
  
  SELECT SUBSTRING(uname,1,1) FROM t_user; 
  截取所有人物的姓
  
  SELECT DISTINCT SUBSTRING(uname,1,1) FROM t_user;
  同时去除重复项
  ```

  

- 去除空格：

  ```mysql
  ltrim（str）：返回删除了左空格的字符串
  SELECT LTRIM('  abc  ')
  
  rtrim（str）：返回删除了右空格的字符串
  SELECT RTRIM('   abc   ')
  
  trim（方向 remstr from str）：返回从某侧删除remstr后的字符串str
  方向词包括both（两侧）、leading（左）、trailing（右）
  SELECT TRIM(‘  abc  ’)  --删除两侧空格
  SELECT TRIM(BOTH ‘x’ FROM ‘xxxabcxxx’) --删除两侧特定字符
  SELECT TRIM(LEADING 'x' FROM 'xxxabcxxx')
  SELECT TRIM(TRAILING 'x' FROM 'xxxabcxxx')
  ```

  

- 字符串函数：

  ```mysql
  space（n）：返回由n个空格组成的字符串
  
  replace（str,from_str,to_str）:替换字符串SELECT REPLACE('123abc123','123','def')
  
  lower(str)  upper(str):大小写转换
  SELECT LOWER('aBcD')
  SELECT UPPER('aBcD')
  ```

##### 数学函数：

```mysql
abs(n):求绝对值
SELECT ABS(-30)

mod(m,n):求m%n的余数
SELECT MOD(3,2)

floor（n）:表示向下取整
SELECT FLOOR(5.6)

ceiling（n）:表示向上取整
SELECT CEILING(5.6)

round(n): 表示将值 n 四舍五入为整数，无小数位
SELECT ROUND(5.6)

round(n,d): 表示将值 n 四舍五入为小数点后 D 位的数值，D为小数点后小数位数
若要保留 n 值小数点左边的 D 位，可将 D 设为负值
SELECT ROUND(345.6789,2)

pow(x,y):求x的y次幂
SELECT POW(2,3)

PI()：获取圆周率
SELECT PI( )

rand（）：获取一个0.0-1.0之间的随机数
SELECT RAND( )

其他：还有其他很多三角函数，使用时查询即可



```

##### 时间和日期函数:

```mysql
获取当前日期
SELECT CURRENT_DATE()

获取当前时间
SELECT CURRENT_TIME()

获取当前日期和时间
SELECT NOW()

举例
UPDATE t_user SET birthday = NOW() WHERE uname = '吕布'

```

- 时间和日期格式化

  ```mysql
  date_format(data,format)
  SELECT DATE_FORMAT('2018-8-8','%Y年%m月%d日')
  SELECT DATE_FORMAT(CURRENT_DATE(),'%y年%m月%d日')
  UPDATE t_user SET brithday=DATE_FORMAT(CURRENT_DATE(),'%y年%m月%d日') WHERE uname = '吕布'
  format参数可用的值如下：
  %Y  年份，返回4 位整数
  %y  年份，返回2 位整数
  %m  月，返回0-12的整数
  %d  日期，返回0-31之间的整数
  %H  小时 (00..23)
  %h  小时 (01..12)
  %i  分钟(00..59)
  %s  秒 (00..59)
  
  ```

  



### 分页查询和过滤

- 分组：将表中数据分为若干小组，例如分为男人和女人，不同国籍等等

  ```mysql
  语法格式：group by
  查看每个国家有多少人
  SELECT COUNT(*) FROM t_user GROUP BY country;
  绿色部分通过COUNT() 函数返回指定列的行数（有多少条数据）
  蓝色部分通过国家去分组，显示每个国家有多少人
  
  查看每个国家的平均年龄
  SELECT AVG(age) FROM t_user GROUP BY country;
  
  查看每个国家的总人数，年龄总和，平均年龄，最高年龄，最低年龄
  SELECT country,COUNT(uname),SUM(age),AVG(age),MAX(age),MIN(age) FROM t_user GROUP BY country;
  
  查看每个国家的总人数，年龄总和，平均年龄，最高年龄，最低年龄，但是排除某个国家
  SELECT country,COUNT(uname),SUM(age),AVG(age),MAX(age),MIN(age) FROM t_user WHERE country!='吴国' GROUP BY country;
  
  列出每个国家小于20岁的人
  SELECT country,uname FROM t_user WHERE age<20 GROUP BY country;
  
  
  ```

- 过滤：

  ```mysql
  SELECT 列名 FROM 表名 WHERE 过滤条件
  
  使用where，可以用来过滤单行，如果想要过滤分组或者聚合之后的数据，要加having
  
  显示每个国家的平均年龄，但是仅显示那些总年龄超过100的国家
  SELECT country,AVG(age) FROM t_user WHERE SUM(age)>100 GROUP BY country;
  上面的写法报错，where在聚合前先筛选记录，但此时表中并没有sum（age）这条记录
  
  having在聚合后对组记录进行筛选
  SELECT country,AVG(age) FROM t_user GROUP BY country HAVING SUM(age)>100;
  注意顺序：having放在分组之后，因为作用的对象不同。WHERE 子句作用于表和视图，HAVING 子句作用于组
  
  ```
  - having和where：

    ```mysql
    WHERE 在分组和聚合计算之前进行选取（它控制哪些行进入聚合计算），因此，WHERE 子句不能包含聚合函数
    
    HAVING 在分组和聚合之后选取分组以后的行 （求平均年龄大于20的国家）
    而且HAVING 子句总是包含聚集函数
    （严格来讲，你可以写不使用聚集的 HAVING 子句， 但同样的条件用WHERE更有效）
    
    综上所述：
    having要跟在group by之后，对分组查询的结果进行过滤（过滤分组）
    where要出现在group by之前，执行表中所有数据来进行过滤（过滤行）
    另外，having可以用聚合函数，并支持所有where子句操作符
    
    ```

  - where子句操作符：

    ```mysql
    <,>,=,!=,>=,<=,and,not,or,like
    
    其中 <,>,=,!=,>=,<=属于比较运算符
    and，not，or属于逻辑运算符
    SELECT uname FROM t_user WHERE age>10 AND age<30;
    
    between操作符稍显特殊，它需要两个操作符
    SELECT * FROM book WHERE number BETWEEN 2 AND 4
    在使用BETWEEN时，必须指定两个值来限定范围，这两个值必须用AND关键字分隔。 BETWEEN匹配范围中所有的值，包括指定的开始值和结束值
    
    
    空值检查SELECT * FROM book WHERE number IS NOT NULL上述语句返回number不为空的行IS NULL 空值判断
    
    IN操作符：用来指定条件范围，范围中的每个条件都可以进行匹配。 IN取合法值的由逗号分隔的清单，全都括在圆括号中。
    SELECT * FROM book WHERE number IN (2,4)
    IN操作符有两个优点：第一：在使用长的合法选项清单时， IN操作符的语法更清楚且更直观。如WHERE number IN (1,3,5,7,9)。第二：IN是可以包含其他SELECT语句，使得能够更动态地建立WHERE子句
    
    
    NOT操作符：只有一个功能，那就是否定它之后所跟的任何条件：WHERE number NOT IN (1,3,5,7,9)SELECT * FROM book WHERE number NOT BETWEEN 2 AND 4复杂的子句中， NOT非常有用。例如，在与IN操作符联合使用时， NOT使找出与条件列表不匹配的行非常简单。MySQL支持使用NOT对IN 、BETWEEN、like等子句取反。
    
    
    ```

### 表的约束

- 表的约束：保证数据的完整性和安全性
  
- 例如id必须有值或者填写性别时只能是男或女，不能写入其他数据
  
- 主键约束（primary key）：要求主键列数据唯一，并且不能为空

  - 主键约束时数据库中最重要的一种约束
  - 在关系中，主键值不能为空，也不允许出现重复（非空且唯一）
  - 一个表中只允许一个主键
  - 主键是表中能够唯一确定一个行数据的字段

  ```mysql
  CREATE TABLE t_user(  
    id INT NOT NULL,
    PRIMARY KEY (id)
  );
  
  主键字段可以是单字段或多字段的组合
  上面的例子中：first_name,last_name都有可能重复，但多列组合是唯一的，但是每一个单独的列依然可以有重复的值
  当一个列不足以用来表示一条记录的唯一性的时候，就需要设置多个列为复合主键，来标识一条记录的唯一性
  一般情况下，主键的字段长度和字段数目要越少越好 
  
  SQL语句：
  
  CREATE TABLE t_user(  
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    PRIMARY KEY(first_name,last_name)
  );
  
  
  ```

  

- 唯一约束（unique）：要求该列唯一，允许为空

  ```mysql
  CREATE TABLE t_user(  
    id INT PRIMARY KEY AUTO_INCREMENT,    自增必须是唯一非空数字
    uname VARCHAR(32) UNIQUE 
  );
  或者
  CREATE TABLE t_user(  
    id INT PRIMARY KEY AUTO_INCREMENT,
    uname VARCHAR(32),
    UNIQUE KEY(uname)
  );
  
  ```

  

- 非空约束（not null）：某类内容不能为空

- 外键约束（foreign key）：用于两表间建立关系

  - 关系型数据库中的一个表有若干个属性（列），若其中某一个属性组能唯一标识一条记录，该属性组就可以成为一个主键

    比如学生表（学号，姓名，性别，班级）

    其中每个学生的学号是唯一的，学号就是一个主键

    课程表（课程编号，课程名，学分）

    其中课程编号是唯一的，课程编号就是一个主键

    成绩表（学号，课程编号，成绩，班级）

    成绩表中单一一个属性无法唯一标识一条记录，学号和课程号的组合才可以唯一标识一条记录，所以学号和课程号的属性组是一个主键

  - 成绩表中的学号不是成绩表中的主键，但它和学生表中的学号相对应，并且学生表中的学号是学生表的主键，则可以设置成绩表中的学号是学生表的外键

    同理 成绩表中的课程号课程表的外键

  - 外键具有保持数据完整性和一致性的机制，目前MySQL只在InnoDB引擎下支持
  - （ENGINE = INNODB）
  - 外键是表中的一个列，其值必须在另一个表的主键或者唯一键中列出
  - 作为主键的表称为主表，作为外键的表称为依赖表
  - 外键会参照主表的主键或唯一键

- 外键的作用有两点：

  - 1.对子表（外键所在的表）的作用，子表在进行写操作的时候，如果外键字段在父表中找不到对应的匹配，操作就会失败
  - 2.对父表的最用:对父表的主键字段进行删和改时，如果对应的主键在子表中被引用，操作就会失败

- 以下情况创建外键会失败：

  - 外键的引用类型不一样，如主键是int外键是char
  - 找不到主表中引用的列
  - 主键和外键的字符编码不一样

### 存储引擎

- 存储引擎：存储数据的方式
  - 数据库存储引擎是数据库底层软件组件，数据库管理系统使用数据引擎进行创建、查询、更新和删除数据操作
  - 使用不同的存储引擎还可以获得特定的功能
  - InnoDB存储引擎提供了具有提交、回滚和崩溃恢复能力的事务安全，支持外键。但是比起Myisam存储引擎，InnoDB写的处理效率差一些并且会占用更多的磁盘空间。MySQL 5.5.5 之后，InnoDB 作为默认存储引擎
  - Myisam表不支持事务、也不支持外键，但访问速度快，对事务没有要求
  - 建表的时候可以指定引擎
    - create table t_p(...) engine = myisam;
    - alter table t_p engine = innodb;
  - 了解内容：查询当前数据库支持的搜索引擎 show engines

### 索引和视图

#### 索引

- 索引：当数据库中存在很多条记录，例如几十万条，查询速度就成了一个问题
  - 此时可以建立类似目录的数据库对象，实现快速查询，这就是索引
  - 例如在书中查询每个内容时，现在目录中查询，然后根据目录所示的页码找到查询内容，大大缩短了查询时间
  - 索引的作用：索引用于快速找出在某个列中有一特定值的行，不使用索引，MySQL必须从第一条记录开始读完整个表，直到找出相关的行，表越大，查询数据所花费的时间越多，如果表中查询的列有一个索引，MySQL能够快速到达一个位置去搜索数据文件，而不必查看所有数据，那么将会节省很大一部分时间

- 建立一个索引：

  ```mysql
  1，创建表时，主键会默认带有索引
  2，创建一个索引
  CREATE INDEX index_1 ON t_user(uname)
       创建一个索引    索引名  从  表名  在哪个字段
  
  CREATE TABLE mytable(  -- 创建表时直接指定
  ID INT NOT NULL,   
  username VARCHAR(16) NOT NULL,  
  INDEX index_1 (username)  
  ); 
  3，删除索引
  DROP INDEX index_1 ON t_user
  
  ```

#### 视图

- 视图：就是一条select语句执行后返回的结果集（显示结果是一个表）

  ```mysql
  例如之前的分组查询语句：
  -- 查看每个国家的总人数，年龄总和，平均年龄，最高年龄，最低年龄
  SELECT country,COUNT(uname),SUM(age),AVG(age),MAX(age),MIN(age) FROM t_user GROUP BY country;
  
  为上面的语句创建视图：
  CREATE VIEW v_user AS
  	SELECT country,COUNT(uname),SUM(age),AVG(age),MAX(age),MIN(age) FROM t_user 	GROUP BY country;
      SELECT * FROM v_user; --以后在使用上面的查询语句时只需要使用视图名
  
  在创建一个视图时，只存放视图的定义，也就是动态检索数据的查询语句，并不存放视图对应的数据，在用户使用视图时才去求相对应的数据，所以视图称为‘虚表’
  
  ```

- 视图的作用：专门进行某些查询

  - 方便操作：减少复杂的SQL语句，增强可读性

  - 更加安全：在外界访问你的数据时，经常不想让他访问所有数据

    这时候可以建立视图，在视图中写好查询语句，同时限制外界的访问权限只能通过你给定的视图去查询

  - 删除视图：

    ```mysql
    DROP VIEW v_user;
    
    ```

### 事务

- 事务：是一个操作序列，这些操作只能都做，或者都不做，是一个不可分割的工作单位

  - 在操作MySQL过程中，对于一般简单的业务逻辑或者中小型程序而言，无需考虑应用MySQL事务
  - 事务主要用于处理操作量大，复杂度高的数据
  - MySQL中，事务由单独单元中一个或多个SQL语句组成。在这个单元中，每个MySQL语句是相互依赖的。而整个单独单元作为一个不可分割得到整体，要么都做，或者都不做
  - 如果单元中某条SQL语句一旦执行失败或者产生错误，可以让整个单元回滚。所有受到影响的数据将返回到事务开始以前的状态（保证了数据的完整性）

- 在MySQL中只有使用了innodb数据库引擎的数据库或表才支持事务

- 事务语句：

  - 开启：begin 开启一个事务
  - 提交：commit 将事务中的SQL语句提交给数据库
  - 回滚：rollback 取消掉之前的所有操作（撤销事务）

  ```mysql
  CREATE TABLE t_person(
  id INT PRIMARY KEY AUTO_INCREMENT,
  sname VARCHAR(10),
  money INT
  ) TYPE=INNODB;创建一个InnoDB类型的数据表
  或者在创建表之后改变：ALTER TABLE t_person TYPE=INNODB；
  
  INSERT INTO t_person VALUES(1,'小明',1000);
  INSERT INTO t_person VALUES(2,'丽丽',2000);
  
  上面的代码中小明有1000块钱，丽丽有2000块钱
  接下来要实现小明给丽丽转账500元
  
  小明给丽丽转账500元
  BEGIN; -- 开始事物
  UPDATE t_person SET money=money-500 WHERE id=1;
  UPDATE t_person SET money=money+500 WHERE id=2;
  SELECT * FROM t_person; -- 查询结果是否有误
  COMMIT; -- 发现结果无误，提交事物，提交后数据库中数据会修改
  
  创建事务的一般过程是：开始事务、创建事务、应用SELECT语句查询数据、提交事务
  BEGIN; -- 开始事物
  UPDATE t_person SET money=money-500 WHERE id=1;
  UPDATE t_person SET money=money+600 WHERE id=2;
  SELECT * FROM t_person; -- 查询结有误果是否
  ROLLBACK; -- 结果有误，回滚事物，取消所有操作
  
  
  ```

  - 总结：我们可以声明一个事务的开始，在确认提交或者指明放弃前的所有操作，都先在一个叫事务日志的临时环境中进行操作。待操作完成，确保了数据一致性之后，那么我们可以手动提交确认，也可以选择放弃以上操作。

    注意：一旦选择了提交，就不能再利用回滚来撤销更改了

  

### 关联关系的使用

- 表的关系：MySQL相互关联的表之间存在一对一，一对多（多对一），多对多的关系：

  - 1.一对一的关系：表1中的一条数据，对应表2中的一条数据

    - 这种关系即多个表具有相同的主键，A表中的一条数据对应B表中的一条数据。实际中用的并不多，因为完全可以将这总关系的合并为一张表（一夫一妻）

  - 2.一对多（多对一）的关系：表1中的一条数据对应表2中的多条数据

    - 其中表1的主键是表2的外键，（即表1的某字段作为主键，表2的相同字段绑定到表1的主键字段上）

    ```mysql
    CREATE TABLE stu(          -- 学生表
        stuId INT,  
        name VARCHAR(10) NOT NULL,  
        PRIMARY KEY(stuId)  
    ); 
    
    CREATE TABLE score_1(           -- 成绩表
        stuId INT,  
        score VARCHAR(32),      #一个学生有多门成绩
        FOREIGN KEY (stuId) REFERENCES stu(stuId)  
    ); 
    
    
    ```

  - 多对多的关系：

    - 比如：一个老师教很多学生的课，一个学生选了很多老师的课。那么，老师和学生之间就是多对多的关系
    - 多对多的关系要借助第3张表

    ```mysql
    1，首先创建老师表，设置id为主键
    CREATE TABLE teacher(  
        teacherId INT,  
        NAME VARCHAR(10) NOT NULL,  
        PRIMARY KEY(teacherId)  
    );
    
    
    2，然后创建学生表，同样设置id为主键
    CREATE TABLE stu(  
        stuId INT,  
        NAME VARCHAR(10) NOT NULL,  
        PRIMARY KEY(stuId)  
    );
    
    3，最后创建一个课程表，将前两张表关系起来
    CREATE TABLE score(
        scoresname  VARCHAR(32)
        stuId INT,  
        teacherId INT,  
        FOREIGN KEY (stuId) REFERENCES stu(stuId),  
        FOREIGN KEY (teacherId) REFERENCES teacher(teacherId)  
    ); 
    
    ```

- 关联查询

  ```mysql
  CREATE TABLE stu(          -- 学生表
      stuId INT,  
      name VARCHAR(10) NOT NULL,  
      PRIMARY KEY(stuId)  
  ); 
  INSERT INTO stu VALUES (1,'xiaoming');
  CREATE TABLE score(           -- 成绩表
      stuId INT,  
      score INT,  
      FOREIGN KEY (stuId) REFERENCES stu(stuId)  
  ); 
  INSERT INTO score VALUES(1,100);
  
  现在要查询所有学生姓名和对应的成绩：
  SELECT stu.name,score.score 
  FROM stu,score 
  WHERE stu.stuID=score.stuID;
  
  后面的限定条件表示有对应关系才做查询
  
  ```

  

### 子查询

### python连接数据库

### 模拟音乐播放器









## 附录 常见错误和单词

### 单词

### 错误

#### 1 缩进错误

#### 2 键错误

















