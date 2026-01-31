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
    """04.4주차_네트워크와클라우드: 상세 학습 기록 (한국어)
    
    네트워크 기초, REST API, HTTP/HTTPS, 클라우드 배포, DevOps
    """

    w = WeekDetail(week="04.4주차_네트워크와클라우드")

    w.files = [
        "00.강의자료/네트워크기초.pdf",
        "00.강의자료/웹API설계.pdf",
        "01.daily_mission/Day1_HTTP프로토콜.ipynb",
        "01.daily_mission/Day2_REST_API_설계.ipynb",
        "01.daily_mission/Day3_API_클라이언트.ipynb",
        "02.advanced_mission/Day4_배포및보안.ipynb",
        "02.advanced_mission/Day5_모니터링.ipynb",
    ]

    w.tech_stack = [
        "네트워크: HTTP/HTTPS, TCP/IP, DNS",
        "API: REST, GraphQL, Swagger/OpenAPI",
        "클라이언트: requests, httpx, urllib",
        "웹 서버: Nginx, Apache",
        "CI/CD: GitHub Actions, Jenkins",
        "클라우드: AWS, Azure, Google Cloud",
        "모니터링: Prometheus, Grafana, ELK Stack",
        "보안: SSL/TLS, JWT, 비밀번호 해싱",
    ]

    w.learning_paragraphs = [
        (
            "📅 Day 1: HTTP 프로토콜과 웹 통신\n"
            "- HTTP 메서드: GET, POST, PUT, DELETE, PATCH\n"
            "- HTTP 상태 코드: 1xx, 2xx, 3xx, 4xx, 5xx\n"
            "- 요청/응답 헤더 및 바디\n"
            "- HTTPS와 SSL/TLS 인증서\n"
            "- 쿠키와 세션 관리"
        ),

        (
            "📅 Day 2: RESTful API 설계\n"
            "- REST 아키텍처 원칙 (HATEOAS, 리소스 중심)\n"
            "- 엔드포인트 설계 규칙\n"
            "- 요청/응답 포맷 (JSON)\n"
            "- 에러 핸들링 및 상태 코드\n"
            "- API 버전 관리"
        ),

        (
            "📅 Day 3: API 클라이언트 개발\n"
            "- HTTP 요청 라이브러리 (requests)\n"
            "- API 인증 (API Key, Bearer Token, OAuth)\n"
            "- 요청 재시도 로직\n"
            "- 레이트 제한 처리\n"
            "- 비동기 HTTP 요청 (asyncio)"
        ),

        (
            "📅 Day 4: 배포 및 보안\n"
            "- 웹 애플리케이션 배포 (Gunicorn + Nginx)\n"
            "- CORS (Cross-Origin Resource Sharing) 설정\n"
            "- 입력 검증 및 SQL Injection 방지\n"
            "- 환경 변수 관리 (.env)\n"
            "- HTTPS 인증서 설정"
        ),

        (
            "📅 Day 5: 모니터링 및 로깅\n"
            "- 구조화된 로깅 설정\n"
            "- 애플리케이션 성능 모니터링 (APM)\n"
            "- 메트릭 수집 (Prometheus)\n"
            "- 로그 집계 (ELK Stack)\n"
            "- 경보 및 알림 시스템"
        ),
    ]

    w.code_examples = {}

    w.code_examples['01_http_basics.py'] = '''# Day 1: HTTP 프로토콜 기초

import requests
from typing import Dict, Any

# HTTP 메서드별 요청 예제
def http_methods_example():
    """HTTP 메서드 사용 예제"""
    
    base_url = "https://api.example.com/users"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer token123"
    }
    
    # GET 요청
    response = requests.get(base_url, headers=headers)
    print(f"GET 상태: {response.status_code}")
    
    # POST 요청
    data = {"name": "John", "email": "john@example.com"}
    response = requests.post(base_url, json=data, headers=headers)
    print(f"POST 상태: {response.status_code}")
    print(f"응답: {response.json()}")
    
    # PUT 요청 (전체 업데이트)
    user_id = 1
    updated_data = {"name": "Jane", "email": "jane@example.com"}
    response = requests.put(f"{base_url}/{user_id}", json=updated_data, headers=headers)
    print(f"PUT 상태: {response.status_code}")
    
    # DELETE 요청
    response = requests.delete(f"{base_url}/{user_id}", headers=headers)
    print(f"DELETE 상태: {response.status_code}")

# HTTP 상태 코드 처리
def handle_status_codes():
    """HTTP 상태 코드별 처리"""
    
    url = "https://api.example.com/data"
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print("✓ 성공:", response.json())
        elif response.status_code == 404:
            print("✗ 찾을 수 없음")
        elif response.status_code == 500:
            print("✗ 서버 오류")
        else:
            print(f"상태 코드: {response.status_code}")
        
        response.raise_for_status()  # 오류 상태면 예외 발생
        
    except requests.exceptions.RequestException as e:
        print(f"요청 오류: {e}")
'''

    w.code_examples['02_rest_api_design.py'] = '''# Day 2: REST API 설계

from flask import Flask, request, jsonify
from typing import Dict, Any, List
from datetime import datetime

app = Flask(__name__)

# REST API 설계 원칙에 따른 엔드포인트

# ============ 리소스: /users ============
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    """POST /api/v1/users - 사용자 생성"""
    data = request.get_json()
    
    # 입력 검증
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'name과 email이 필요합니다'}), 400
    
    new_user = {
        'id': 1,
        'name': data['name'],
        'email': data['email'],
        'created_at': datetime.now().isoformat()
    }
    
    return jsonify(new_user), 201

@app.route('/api/v1/users', methods=['GET'])
def list_users():
    """GET /api/v1/users - 사용자 목록 조회"""
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
    ]
    return jsonify(users), 200

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """GET /api/v1/users/{id} - 특정 사용자 조회"""
    user = {'id': user_id, 'name': 'Alice', 'email': 'alice@example.com'}
    return jsonify(user), 200

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """PUT /api/v1/users/{id} - 사용자 전체 업데이트"""
    data = request.get_json()
    updated_user = {
        'id': user_id,
        'name': data.get('name'),
        'email': data.get('email')
    }
    return jsonify(updated_user), 200

@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """DELETE /api/v1/users/{id} - 사용자 삭제"""
    return jsonify({'message': f'사용자 {user_id} 삭제됨'}), 204

# ============ 에러 핸들링 ============
@app.errorhandler(400)
def bad_request(error):
    """400 Bad Request 처리"""
    return jsonify({'error': 'Bad request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    """404 Not Found 처리"""
    return jsonify({'error': 'Not found', 'message': '리소스를 찾을 수 없습니다'}), 404

@app.errorhandler(500)
def internal_error(error):
    """500 Internal Server Error 처리"""
    return jsonify({'error': 'Server error', 'message': '서버 오류 발생'}), 500

if __name__ == '__main__':
    app.run(debug=True)
'''

    w.code_examples['03_api_client.py'] = '''# Day 3: API 클라이언트 개발

import requests
import time
from typing import Optional, Dict, Any
from functools import wraps

class APIClient:
    """REST API 클라이언트"""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self._setup_headers()
    
    def _setup_headers(self):
        """헤더 설정"""
        self.session.headers.update({
            'Content-Type': 'application/json'
        })
        if self.api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {self.api_key}'
            })
    
    def retry_on_failure(max_retries: int = 3, backoff: float = 1.0):
        """재시도 데코레이터"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_retries):
                    try:
                        return func(*args, **kwargs)
                    except requests.exceptions.RequestException as e:
                        if attempt == max_retries - 1:
                            raise
                        wait_time = backoff * (2 ** attempt)
                        print(f"재시도 {attempt + 1}/{max_retries}, {wait_time}초 대기...")
                        time.sleep(wait_time)
            return wrapper
        return decorator
    
    @retry_on_failure(max_retries=3)
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """GET 요청"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    @retry_on_failure(max_retries=3)
    def post(self, endpoint: str, data: Dict) -> Dict:
        """POST 요청"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    
    @retry_on_failure(max_retries=3)
    def put(self, endpoint: str, data: Dict) -> Dict:
        """PUT 요청"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    
    @retry_on_failure(max_retries=3)
    def delete(self, endpoint: str) -> None:
        """DELETE 요청"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, timeout=10)
        response.raise_for_status()

# 사용 예제
if __name__ == '__main__':
    client = APIClient(
        base_url='https://api.example.com',
        api_key='your-api-key'
    )
    
    # GET 요청
    try:
        users = client.get('users', params={'limit': 10})
        print("사용자 목록:", users)
    except Exception as e:
        print(f"오류: {e}")
    
    # POST 요청
    try:
        new_user = client.post('users', {
            'name': 'Alice',
            'email': 'alice@example.com'
        })
        print("생성된 사용자:", new_user)
    except Exception as e:
        print(f"오류: {e}")
'''

    w.code_examples['04_nginx_config.py'] = '''# Day 4: Nginx 리버스 프록시 설정

# nginx.conf 예제 (Nginx 웹 서버 설정 파일)

nginx_config = """
# Nginx 기본 설정 파일

# 워커 프로세스 수
worker_processes auto;

# 에러 로그
error_log /var/log/nginx/error.log warn;

# 이벤트 설정
events {
    worker_connections 1024;
}

http {
    # 기본 설정
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
    # 로깅 포맷
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';
    
    access_log /var/log/nginx/access.log main;
    
    # 성능 최적화
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    
    # Gzip 압축
    gzip on;
    gzip_vary on;
    gzip_types text/plain text/css text/xml text/javascript application/json;
    
    # ============ 리버스 프록시 설정 ============
    upstream backend {
        # 로드 밸런싱: 두 개의 백엔드 서버
        server 127.0.0.1:5000 weight=1;
        server 127.0.0.1:5001 weight=1;
    }
    
    # HTTP 리다이렉트
    server {
        listen 80;
        server_name example.com www.example.com;
        
        # HTTP를 HTTPS로 리다이렉트
        return 301 https://$server_name$request_uri;
    }
    
    # HTTPS 서버
    server {
        listen 443 ssl http2;
        server_name example.com www.example.com;
        
        # SSL 인증서 설정
        ssl_certificate /etc/ssl/certs/example.com.crt;
        ssl_certificate_key /etc/ssl/private/example.com.key;
        
        # SSL 보안 설정
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;
        
        # 보안 헤더
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-Frame-Options "SAMEORIGIN" always;
        
        # 요청 로깅
        access_log /var/log/nginx/access.log main;
        
        # 리버스 프록시 설정
        location / {
            proxy_pass http://backend;
            
            # 헤더 전달
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            
            # 타임아웃
            proxy_connect_timeout 60s;
            proxy_send_timeout 60s;
            proxy_read_timeout 60s;
        }
        
        # API 엔드포인트 (캐싱 비활성화)
        location /api/ {
            proxy_pass http://backend;
            proxy_cache off;
            
            add_header Cache-Control "no-cache, no-store, must-revalidate";
            add_header Pragma "no-cache";
            add_header Expires "0";
        }
        
        # 정적 파일 (캐싱 활성화)
        location ~* \\.(jpg|jpeg|png|gif|ico|css|js|woff|woff2)$ {
            proxy_pass http://backend;
            expires 30d;
            add_header Cache-Control "public, immutable";
        }
    }
}
"""

# Nginx 명령어
nginx_commands = """
# Nginx 설정 파일 검증
sudo nginx -t

# Nginx 시작
sudo systemctl start nginx

# Nginx 재시작
sudo systemctl restart nginx

# Nginx 상태 확인
sudo systemctl status nginx

# 설정 파일 다시 로드
sudo systemctl reload nginx
"""

# Docker에서 Nginx 실행 예제
docker_nginx = """
# Dockerfile
FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY ssl/ /etc/ssl/

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

# Docker 실행
docker build -t my-nginx .
docker run -p 80:80 -p 443:443 my-nginx
"""

print("=== Nginx 설정 ===")
print(nginx_config)
'''

    w.code_examples['05_monitoring.py'] = '''# Day 5: 애플리케이션 모니터링 및 로깅

import logging
import json
import time
from datetime import datetime
from typing import Dict, Any
from functools import wraps

# ============ 구조화된 로깅 설정 ============
class StructuredLogger:
    """구조화된 JSON 로깅"""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # JSON 포맷 핸들러
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)
    
    def log_event(self, event_type: str, **kwargs):
        """이벤트 기반 로깅"""
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'data': kwargs
        }
        self.logger.info(json.dumps(log_data))

# ============ 성능 모니터링 데코레이터 ============
def monitor_performance(logger: StructuredLogger):
    """함수 실행 시간 및 성능 모니터링"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                
                logger.log_event('function_completed', 
                    function=func.__name__,
                    execution_time=execution_time,
                    status='success'
                )
                
                return result
            except Exception as e:
                execution_time = time.time() - start_time
                
                logger.log_event('function_error',
                    function=func.__name__,
                    execution_time=execution_time,
                    error=str(e),
                    status='failed'
                )
                raise
        
        return wrapper
    return decorator

# ============ 메트릭 수집 (Prometheus 스타일) ============
class MetricsCollector:
    """애플리케이션 메트릭 수집"""
    
    def __init__(self):
        self.metrics = {
            'http_requests_total': 0,
            'http_request_duration_seconds': [],
            'database_queries_total': 0,
            'errors_total': 0
        }
    
    def record_request(self, endpoint: str, duration: float, status_code: int):
        """HTTP 요청 기록"""
        self.metrics['http_requests_total'] += 1
        self.metrics['http_request_duration_seconds'].append(duration)
    
    def record_error(self, error_type: str):
        """에러 기록"""
        self.metrics['errors_total'] += 1
    
    def get_metrics(self) -> Dict[str, Any]:
        """메트릭 조회"""
        durations = self.metrics['http_request_duration_seconds']
        avg_duration = sum(durations) / len(durations) if durations else 0
        
        return {
            'http_requests_total': self.metrics['http_requests_total'],
            'http_request_duration_avg': avg_duration,
            'database_queries_total': self.metrics['database_queries_total'],
            'errors_total': self.metrics['errors_total']
        }

# ============ 사용 예제 ============
logger = StructuredLogger('app')
metrics = MetricsCollector()

@monitor_performance(logger)
def process_data(data: str) -> str:
    """데이터 처리 함수"""
    time.sleep(0.1)  # 시뮬레이션
    return f"Processed: {data}"

if __name__ == '__main__':
    # 함수 실행 및 성능 모니터링
    process_data("sample data")
    
    # 메트릭 조회
    print("\\n수집된 메트릭:")
    print(json.dumps(metrics.get_metrics(), indent=2))
'''

    return w


def print_detail():
    d = get_detail()
    print(f"Week: {d.week}")
    print(f"Files: {len(d.files)} files")
    print(f"Tech Stack: {len(d.tech_stack)} technologies")
    print(f"Learning Content: {len(d.learning_paragraphs)} days")
    print(f"Code Examples: {len(d.code_examples)} examples")
