## 初期設定

* インストール

```
$ python -m venv logue_api
$ cd logue_api
$ . ./bin/activate
$ pip install django djangorestframework django-markdownx
$ django-admin startproject logue_api_project .
$ python manage.py startapp logue_api_app
```

* 起動確認

```
$ python manage.py runserver
```

* 初期設定

```
$ vim logue_api_project/settings.py

(以下の箇所を変更)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'markdownx',
    'logue_api_app'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}

$ python manage.py makemigration logue_api_app
$ python manage.py migrate
```

* admin

```
$ python manage.py createsuperuser
# runserverして、http://localhost:8000/admin にアクセス
# 適当にデータを作成とかできる
```

* 鍵

```
$ vim logue_app_project/settings.py

(以下の箇所を変更)

from pathlib import Path
import develop as env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.DEBUG


$ vim .gitignore

(develop.py, prod.pyを追加)
環境切り替えは後々考える
```

* debug
    * launch.jsonを作成
    * settings.jsonに使用するpythonのパスを書く