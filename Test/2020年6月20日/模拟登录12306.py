from time import sleep
from selenium.webdriver import ActionChains  # 动作链类
from hashlib import md5
import requests
from PIL import Image  # 进行裁剪
from selenium import webdriver


# 超级鹰
class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def transform_codeImg(imgPath, imgType):
    chaojiying = Chaojiying_Client('lucassong', 'lucassong', '905973')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, imgType)['pic_str']  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()


'''
实现流程
可以对登录首页进行截图，在通过裁剪的操作将验证码图片进行获取
验证码图片提交给打码平台进行识别
'''
# code_text = transform_codeImg('./code.jpg', 1902)
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://kyfw.12306.cn/otn/login/init')
sleep(1)
# 首页的截图
bro.save_screenshot('./main.png')
# 将验证码图片进行裁剪
img_tag = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
location = img_tag.location  # img_tag标签在页面中的起始位置
print('location:',location)
size = img_tag.size  # img_tag在页面中显示的尺寸
print('size:',size)
# 存储的就是验证码图片左下角和右上角的坐标
rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
# 接下来就可以根据rangle进行验证码的裁剪
i = Image.open('./main.png')
frame = i.crop(rangle)  # 根据rangle进行指定区域裁剪
frame.save('./code.png')

# 将验证码图片提交给超级鹰
result = transform_codeImg('./code.png', 9004)
# 将170,70|4,150转换成[[170,70],[4,150]]
all_list = []  # [[170,70],[4,150]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)

for loc in all_list:
    x = loc[0]
    y = loc[1]
    print(x, y)
    ActionChains(bro).move_to_element_with_offset(img_tag, x, y).click().perform()
    sleep(1)

user_tag = bro.find_element_by_id('username')
user_tag.send_keys('123456')
pwd_tag = bro.find_element_by_id('password')
pwd_tag.send_keys('666666')
sleep(2)
bro.find_element_by_id('loginSub').click()
sleep(5)
bro.quit()
