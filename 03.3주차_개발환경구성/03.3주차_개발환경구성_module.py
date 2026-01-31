from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class WeekDetail:
    week: str = ""
    files: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)
    learning_paragraphs: List[str] = field(default_factory=list)
    code_examples: Dict[str, str] = field(default_factory=dict)


def get_detail() -> WeekDetail:
    """03.3주차_개발환경구성: 상세 학습 기록 (한국어)
    
    웹 프레임워크, 데이터베이스, ORM, 버전 관리, 개발 환경 설정
    """

    w = WeekDetail(week="03.3주차_개발환경구성")

    w.files = [
        "00.강의자료/웹개발기초_Flask.pdf",
        "00.강의자료/데이터베이스설계.pdf",
        "01.daily_mission/Day1_환경설정.ipynb",
        "01.daily_mission/Day2_Flask기초.ipynb",
        "01.daily_mission/Day3_데이터베이스연동.ipynb",
        "02.advanced_mission/Day4_ORM심화.ipynb",
        "02.advanced_mission/Day5_Docker컨테이너화.ipynb",
    ]

    w.tech_stack = [
        "Python 3.9+, 가상환경 (venv, conda)",
        "웹 프레임워크: Flask, FastAPI",
        "데이터베이스: SQLite, MySQL, PostgreSQL",
        "ORM: SQLAlchemy",
        "마이그레이션: Alembic",
        "컨테이너화: Docker, Docker Compose",
        "버전 관리: Git, GitHub",
        "웹 서버: Gunicorn, Nginx",
    ]

    w.learning_paragraphs = [
        (
            "📅 Day 1: 개발 환경 설정 및 버전 관리\n"
            "- 가상환경 생성 및 활성화 (venv, conda)\n"
            "- requirements.txt 작성 및 패키지 관리\n"
            "- Git 기초: init, add, commit, push\n"
            "- .gitignore 설정 (가상환경, __pycache__, .env 제외)\n"
            "- GitHub 레포지토리 생성 및 동기화"
        ),

        (
            "📅 Day 2: Flask 웹 프레임워크 기초\n"
            "- Flask 앱 구조 (app.py, 라우팅)\n"
            "- 요청/응답 처리 (GET, POST)\n"
            "- 템플릿 렌더링 (Jinja2)\n"
            "- 정적 파일 관리 (CSS, JS, 이미지)\n"
            "- 블루프린트를 이용한 모듈화"
        ),

        (
            "📅 Day 3: 데이터베이스 연동 및 CRUD\n"
            "- 데이터베이스 설계 (정규화, 스키마)\n"
            "- SQL 기초 쿼리 (SELECT, INSERT, UPDATE, DELETE)\n"
            "- Flask-SQLAlchemy 연동\n"
            "- 모델 정의 (테이블 구조)\n"
            "- 기본 CRUD 작업 구현"
        ),

        (
            "📅 Day 4: ORM 심화 및 관계 설정\n"
            "- 일대다, 다대다 관계 설정\n"
            "- 외래키 및 제약조건\n"
            "- 쿼리 최적화 (lazy loading vs eager loading)\n"
            "- 트랜잭션 및 롤백\n"
            "- Alembic을 이용한 마이그레이션"
        ),

        (
            "📅 Day 5: Docker를 이용한 컨테이너화\n"
            "- Dockerfile 작성\n"
            "- Docker 이미지 빌드 및 실행\n"
            "- Docker Compose로 다중 서비스 관리\n"
            "- 데이터베이스 컨테이너 설정\n"
            "- 프로덕션 배포 준비"
        ),
    ]

    w.code_examples = {}

    w.code_examples['01_flask_basic.py'] = '''# Day 2: Flask 기본 구조 및 라우팅

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 기본 라우팅
@app.route('/', methods=['GET'])
def index():
    """홈 페이지"""
    return render_template('index.html')

# 동적 라우팅
@app.route('/user/<name>', methods=['GET'])
def greet(name):
    """사용자 인사"""
    return f"안녕하세요, {name}님!"

# REST API - POST 요청
@app.route('/api/data', methods=['POST'])
def create_data():
    """데이터 생성 API"""
    data = request.get_json()
    return jsonify({
        "status": "success",
        "received": data
    }), 201

# REST API - GET 요청 (JSON 응답)
@app.route('/api/items', methods=['GET'])
def get_items():
    """항목 목록 조회"""
    items = [
        {"id": 1, "name": "상품1", "price": 10000},
        {"id": 2, "name": "상품2", "price": 20000}
    ]
    return jsonify(items)

# 에러 핸들링
@app.errorhandler(404)
def not_found(error):
    """404 에러 처리"""
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
'''

    w.code_examples['02_sqlalchemy_orm.py'] = '''# Day 3-4: SQLAlchemy ORM 및 모델 정의

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# 사용자 모델
class User(db.Model):
    """사용자 정보"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 관계 설정: 1 사용자 = N 포스트
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# 포스트 모델
class Post(db.Model):
    """게시물"""
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author.username
        }

# CRUD 작업
def crud_examples():
    """CRUD 예제"""
    # CREATE
    new_user = User(username='john', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()
    
    # READ
    user = User.query.filter_by(username='john').first()
    
    # UPDATE
    user.email = 'john.new@example.com'
    db.session.commit()
    
    # DELETE
    db.session.delete(user)
    db.session.commit()

# 고급 쿼리
def advanced_queries():
    """고급 쿼리 예제"""
    # 조건부 조회
    active_users = User.query.filter(User.created_at > datetime(2024, 1, 1)).all()
    
    # 조인 쿼리
    user_posts = db.session.query(User, Post).join(Post).all()
    
    # 집계 함수
    user_count = User.query.count()
    
    # 페이지네이션
    page_users = User.query.paginate(page=1, per_page=10)
    
    return {
        'active_users': len(active_users),
        'user_count': user_count,
        'page_total': page_users.total
    }
'''

    w.code_examples['03_docker_setup.py'] = '''# Day 5: Dockerfile 및 Docker Compose 설정

# Dockerfile 예제
dockerfile_content = """FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 환경 변수 설정
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 포트 노출
EXPOSE 5000

# 애플리케이션 실행
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
"""

# Docker Compose 예제 (docker-compose.yml)
docker_compose_content = """version: '3.8'

services:
  # 웹 애플리케이션
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=mysql+pymysql://root:password@db:3306/myapp
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs

  # MySQL 데이터베이스
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: myapp
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  # PhpMyAdmin (데이터베이스 관리 도구)
  phpmyadmin:
    image: phpmyadmin
    environment:
      PMA_HOST: db
      PMA_USER: root
      PMA_PASSWORD: password
    ports:
      - "8080:80"
    depends_on:
      - db

volumes:
  mysql_data:

networks:
  default:
    name: app-network
"""

# Docker 빌드 및 실행 명령어
docker_commands = """
# 이미지 빌드
docker build -t my-flask-app .

# 컨테이너 실행
docker run -p 5000:5000 my-flask-app

# Docker Compose로 모든 서비스 시작
docker-compose up -d

# 로그 확인
docker-compose logs -f web

# 컨테이너 중지
docker-compose down
"""

# Python으로 Docker 명령어 실행
import subprocess

def run_docker_commands():
    """Docker 명령어 실행"""
    commands = [
        "docker --version",
        "docker ps",
    ]
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            print(f"$ {cmd}")
            print(result.stdout)
        except Exception as e:
            print(f"오류: {e}")

if __name__ == '__main__':
    print("=== Dockerfile ===")
    print(dockerfile_content)
    print("\\n=== Docker Compose ===")
    print(docker_compose_content)
    print("\\n=== Docker Commands ===")
    print(docker_commands)
'''

    w.code_examples['04_mvc_architecture.py'] = '''# Day 1-5: MVC 패턴을 이용한 계층 분리

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# ============ Model 계층 ============
class UserModel(db.Model):
    """사용자 데이터 모델"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)

# ============ Repository 계층 (데이터 접근) ============
class UserRepository:
    """데이터베이스 접근을 담당"""
    
    @staticmethod
    def create(name, email):
        user = UserModel(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_by_id(user_id):
        return UserModel.query.get(user_id)
    
    @staticmethod
    def get_all():
        return UserModel.query.all()
    
    @staticmethod
    def update(user_id, name, email):
        user = UserModel.query.get(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
        return user
    
    @staticmethod
    def delete(user_id):
        user = UserModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()

# ============ Service 계층 (비즈니스 로직) ============
class UserService:
    """비즈니스 로직을 담당"""
    
    def __init__(self):
        self.repo = UserRepository()
    
    def create_user(self, name, email):
        """사용자 생성 - 유효성 검사 포함"""
        if not name or not email:
            raise ValueError("Name and email are required")
        
        if '@' not in email:
            raise ValueError("Invalid email format")
        
        return self.repo.create(name, email)
    
    def get_user(self, user_id):
        """사용자 조회"""
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user
    
    def list_users(self):
        """모든 사용자 조회"""
        return self.repo.get_all()

# ============ Controller 계층 (라우팅) ============
user_service = UserService()

@app.route('/api/users', methods=['POST'])
def create_user():
    """사용자 생성 엔드포인트"""
    try:
        data = request.get_json()
        user = user_service.create_user(data['name'], data['email'])
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """사용자 조회 엔드포인트"""
    try:
        user = user_service.get_user(user_id)
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/users', methods=['GET'])
def list_users():
    """사용자 목록 조회 엔드포인트"""
    users = user_service.list_users()
    return jsonify([{
        'id': u.id,
        'name': u.name,
        'email': u.email
    } for u in users]), 200

if __name__ == '__main__':
    app.run(debug=True)
'''

    return w


def print_detail():
    d = get_detail()
    print(f"Week: {d.week}")
    print(f"Files: {len(d.files)} files")
    print(f"Tech Stack: {len(d.tech_stack)} technologies")
    print(f"Learning Content: {len(d.learning_paragraphs)} days")
    print(f"Code Examples: {len(d.code_examples)} examples")
