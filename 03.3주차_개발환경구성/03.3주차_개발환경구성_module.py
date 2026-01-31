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
    """03.3주차_개발환경구성: 학습 기록 모듈 (한국어)
    
    웹 개발 프레임워크, 데이터베이스, ORM 등 실제 프로젝트에 필요한 개발환경 구성 학습.
    """

    w = WeekDetail(week="03.3주차_개발환경구성")

    w.files = [
        "00.강의자료 (Git, Docker, MySQL, ORM 강의 PDF)",
        "01.daily_mission (매일 환경 구성 미션)",
        "02.advanced_mission (심화 인프라 미션)",
        "03.project (개발환경 구성 프로젝트)",
    ]

    w.tech_stack = [
        "Python 3, Flask/FastAPI",
        "데이터베이스: SQLite, MySQL/PostgreSQL",
        "ORM: SQLAlchemy",
        "아키텍처: 계층형 아키텍처 (Route/Service/Repository)",
        "Git: 커밋 메시지, 브랜치 관리, GitHub 협업",
        "Docker: 이미지, 컨테이너, Docker Compose",
        "데이터 연결: Connection Pool, Transaction",
    ]

    w.learning_paragraphs = [
        (
            "What I practiced: 단순 Python 스크립트에서 벗어나 웹 프레임워크 기반 프로젝트 구조를 익혔습니다. "
            "Flask/FastAPI로 REST API를 작성하고, SQLAlchemy를 통해 데이터베이스와 상호작용을 구현했습니다. "
            "프로젝트 폴더 구조(app/, models/, routes/, repository/, service/ 등)를 설계하고, "
            "Git 커밋 작성법, 브랜치 관리, Docker 기본 명령어, Docker Compose로 MySQL 실행 등을 실습했습니다."
        ),

        (
            "What I learned: 대규모 프로젝트의 코드 구조화 방식(MVC 패턴, 계층형 아키텍처)을 이해했습니다. "
            "Route 계층(API 요청 처리), Service 계층(비즈니스 로직), Repository 계층(DB 접근)으로 책임을 분리하고, "
            "ORM을 사용해 SQL 직접 작성 대신 객체 기반으로 데이터를 조작하는 방법을 배웠습니다. "
            "또한 Connection Pool을 통한 효율적인 DB 연결 관리, 트랜잭션 제어, 환경 변수 관리를 체감했습니다."
        ),

        (
            "Project/Assignment: 채팅 시스템이나 블로그를 Flask/FastAPI로 구현하고, "
            "계층형 아키텍처로 리팩토링했습니다. SQLAlchemy 모델로 테이블을 매핑하고, "
            "Repository에서 CRUD 작업을 수행, Service에서 비즈니스 로직을 처리, Route에서 API를 제공하는 흐름을 완성했습니다. "
            "Docker Compose로 로컬 MySQL 환경을 구성하고, 좋은 Git 커밋 메시지를 작성해 협업 준비를 갖추었습니다."
        ),
    ]

    w.code_examples = {}

    w.code_examples['layered_architecture.py'] = '''# Route 계층 (API 엔드포인트)
from flask import Flask, request, jsonify
from service.user_service import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = user_service.create_user(data['name'], data['email'])
    return jsonify(user), 201

# Service 계층 (비즈니스 로직)
class UserService:
    def __init__(self):
        self.repo = UserRepository()
    
    def create_user(self, name, email):
        user = User(name=name, email=email)
        return self.repo.save(user)

# Repository 계층 (DB 접근)
class UserRepository:
    def save(self, user):
        session.add(user)
        session.commit()
        return {"id": user.id, "name": user.name, "email": user.email}
'''

    w.code_examples['sqlalchemy_orm_crud.py'] = '''from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

engine = create_engine('mysql+pymysql://user:password@localhost/mydb')
Session = sessionmaker(bind=engine)
session = Session()

# CREATE
new_user = User(username='john', email='john@example.com')
session.add(new_user)
session.commit()

# READ
user = session.query(User).filter(User.email == 'john@example.com').first()

# UPDATE
user.username = 'jane'
session.commit()

# DELETE
session.delete(user)
session.commit()
'''

    w.code_examples['docker_compose.yml'] = '''version: "3.8"

services:
  mysql:
    image: mysql:8.0
    container_name: my_mysql
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: mydb
      MYSQL_USER: app_user
      MYSQL_PASSWORD: app_password
    volumes:
      - mysql_data:/var/lib/mysql

  adminer:
    image: adminer
    ports:
      - "8080:8080"
    depends_on:
      - mysql

volumes:
  mysql_data:
'''

    return w


def print_detail():
    d = get_detail()
    print("Week:", d.week)
    print("Files:", len(d.files), "items")
    print("Tech Stack:", len(d.tech_stack), "items")
    print("Learning Paragraphs:", len(d.learning_paragraphs), "sections")
    print("Code Examples:", list(d.code_examples.keys()))
