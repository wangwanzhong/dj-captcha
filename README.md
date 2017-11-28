# demo for django-simple-captcha

第三方验证码模块 [django-simple-captcha](http://django-simple-captcha.readthedocs.io/en/latest/usage.html)，[下载地址](https://github.com/mbi/django-simple-captcha)。


## 安装


```
pip install  django-simple-captcha
```


```
# mysite/settings.py
INSTALLED_APPS = [
    '...',
    'captcha',
]

# 格式
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(hidden_field)s %(image)s'
# 噪点样式
CAPTCHA_NOISE_FUNCTIONS = (
    # 'captcha.helpers.noise_null',       # 没有样式
    # 'captcha.helpers.noise_arcs',     # 线
    'captcha.helpers.noise_dots',       # 点
)
# 图片大小
CAPTCHA_IMAGE_SIZE = (100, 30)
# 字符个数
CAPTCHA_LENGTH = 4
# 超时(minutes)
CAPTCHA_TIMEOUT = 1
# 文字倾斜
CAPTCHA_LETTER_ROTATION = (-10,10)
# 背景颜色
CAPTCHA_BACKGROUND_COLOR = '#FFFFFF'
# 文字颜色
CAPTCHA_FOREGROUND_COLOR = '#0A12E5'
# 验证码类型
# 图片中的文字为随机英文字母，如 mdsh
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为数字表达式，如 1+2=
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'

```


```
python manage.py migrate
```

## [demo](https://github.com/wangwanzhong/dj-captcha)


```
git clone git@github.com:wangwanzhong/dj-captcha.git
cd dj-captcha
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

open http://127.0.0.1:8000/demo/ in browser
