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
    """04.4주차_네트워크와클라우드: 학습 기록 모듈 (한국어)
    
    네트워크 기초, HTTP/API, 클라우드 배포, DevOps 개념 학습.
    """

    w = WeekDetail(week="04.4주차_네트워크와클라우드")

    w.files = [
        "00.강의자료 (네트워크, HTTP, API, 클라우드, DevOps)",
        "01.daily_mission (매일 네트워크/API 미션)",
        "02.advanced_mission (심화 배포 미션)",
        "03.project (실제 서버 배포 프로젝트)",
    ]

    w.tech_stack = [
        "네트워크 기초: IP, 포트, DNS, TCP/UDP",
        "HTTP/HTTPS: 요청-응답, 상태 코드, 헤더",
        "API 설계: RESTful API, 엔드포인트 설계",
        "클라우드: AWS, GCP, Azure 기본 개념",
        "배포: Linux 서버, SSH, 방화벽 설정",
        "DevOps: CI/CD, 자동화, 모니터링",
        "Load Balancing, 캐싱(Redis), CDN",
    ]

    w.learning_paragraphs = [
        (
            "What I practiced: 네트워크의 기초(IP, 포트, DNS) 개념을 이해하고, "
            "HTTP 요청-응답 사이클, 상태 코드(200, 404, 500 등), 요청 헤더/응답 헤더를 직접 관찰했습니다. "
            "REST API 설계 원칙(자원 중심, HTTP 메서드 활용)을 배우고, 실제 API를 구현해보았습니다. "
            "Linux 서버에 SSH로 접속하고, 애플리케이션을 배포해보는 경험을 했습니다."
        ),

        (
            "What I learned: 로컬 개발환경과 서버 운영환경의 근본적 차이를 체감했습니다. "
            "방화벽, 포트 설정, 리버스 프록시(Nginx), SSL 인증서 등 실제 서비스 운영에 필요한 개념들을 배웠습니다. "
            "CI/CD 파이프라인(자동화된 테스트 및 배포), 모니터링(로그, 메트릭), 스케일링 전략을 이해했으며, "
            "Redis, CDN 등을 통한 성능 최적화 방법을 배웠습니다."
        ),

        (
            "Project/Assignment: 실제 클라우드 서버에 Flask/FastAPI 애플리케이션을 배포했습니다. "
            "도메인 설정, SSL 인증서 적용, Nginx 리버스 프록시 구성, 자동 로그 수집을 구현했습니다. "
            "GitHub Actions로 CI/CD 파이프라인을 구축하고, 애플리케이션 로그 및 성능을 모니터링했습니다."
        ),
    ]

    w.code_examples = {}

    w.code_examples['restful_api_design.py'] = '''from flask import Flask, request, jsonify

app = Flask(__name__)

# REST API 설계: 자원 중심, HTTP 메서드 활용
# GET    /api/users         - 모든 사용자 조회
# POST   /api/users         - 새 사용자 생성
# GET    /api/users/{id}    - 특정 사용자 조회
# PUT    /api/users/{id}    - 사용자 정보 업데이트
# DELETE /api/users/{id}    - 사용자 삭제

@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify({"users": []}), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({"id": 1}), 201

@app.route('/api/users/<int:uid>', methods=['GET'])
def get_user(uid):
    return jsonify({"id": uid, "name": "John"}), 200
'''

    w.code_examples['nginx_config.conf'] = '''server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
'''

    return w


def print_detail():
    d = get_detail()
    print("Week:", d.week)
    print("Tech Stack:", len(d.tech_stack), "items")
