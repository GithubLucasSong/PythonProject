import requests
import re
import os

# 定义一个通用的url模板
url_model = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv_%d.html'
page_num = 1
for page in range(1, 5):
    print('正在下载第{}页数据'.format(page))
    if page == 1:
        url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv.html'
    else:
        url = format(url_model % page)
        print(url)

    if not os.path.exists('./imgLib'):
        os.mkdir('./imgLib')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }


    page_text = requests.get(url=url, headers=headers).text

    # 使用正则将图片地址进行提取

    '''
    <div class="box picblock col3" style="width:186px;height:270px">
        <div>
            <a target="_blank" href="http://sc.chinaz.com/tupian/200616472670.htm" alt="大胆顶级欧美艺术图片">
                <img src2="http://pic2.sc.chinaz.com/Files/pic/pic9/202006/apic25881_s.jpg" alt="大胆顶级欧美艺术图片">
            </a>
        </div>
        <p><a target="_blank" href="http://sc.chinaz.com/tupian/200616472670.htm" alt="大胆顶级欧美艺术图片">大胆顶级欧美艺术图片</a>
        </p>
    </div>
    '''

    re_ex = '<a target="_blank".*?<img src2="(.*?)"'

    img_src = re.findall(re_ex, page_text, re.S)
    for src in img_src:
        img_name = src.split('/')[-1]
        img_path = './imgLib/' + img_name
        img_data = requests.get(url=src, headers=headers).content
        with open(img_path, 'wb') as f:
            f.write(img_data)
            print('下载成功')
