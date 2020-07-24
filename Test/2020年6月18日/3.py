import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
# print(img_src)
img_data = requests.get(url=img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
    fp.write(img_data)

# 软件id ；'	c65d0e88eaf09c62712d4f137a594b3b'
# 打码平台示例代码
from hashlib import md5


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
    return chaojiying.PostPic(im, imgType)['pic_str'] # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()

print(transform_codeImg('./code.jpg',1004))