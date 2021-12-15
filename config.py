# 파이보에 ORM 적용

import os

BASE_DIR = os.path.dirname(__file__) # 현재파일이 있는 폴더
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
