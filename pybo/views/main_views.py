# 블루프린트 사용, 렌더 템플릿

from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix="/")

@bp.route('/hello')
def hello_pybo():
    return '블루프린트를 사용한 페이지입니다. 헬로 파이보 함수입니다.'

@bp.route('/') # 여기로 접속하면 다른 페이지로 전환 됨
def index():
    return redirect(url_for('question._list')) # (1) 블루프린트 이름 (2) 함수명

