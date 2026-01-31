"""
Development Environment Course - Complete Codified Data Structure
개발환경 구성 과정 (03주차) 데이터를 코드로 변환

작성자: 이영기
구성: SeSAC Development Environment Setup 프로그램
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

# ==================== ENUMS ====================


class DayMissionType(Enum):
    """일일 과제 유형"""
    BASIC = "basic"
    ADVANCED = "advanced"


class DayNumber(Enum):
    """일차"""
    DAY_01 = 1
    DAY_02 = 2
    DAY_03 = 3
    DAY_04 = 4
    DAY_05 = 5


class TopicType(Enum):
    """개발환경 구성 주제"""
    UV_FASTAPI = "UV로 FastAPI 라이브러리 추가하기"
    POSTMAN_REQUEST = "Postman으로 Get 요청을 통해 피보나치 함수 호출하기"
    PYTHON_SETUP = "Python 개발환경 설정"
    GIT_BASICS = "Git 기초"
    GIT_ADVANCED = "Git 고급"
    GITHUB_COLLABORATION = "GitHub를 이용한 협업"
    PROJECT_MANAGEMENT = "프로젝트 관리 및 GitHub"
    DOCKER = "Docker 인프라 및 MySQL"
    DATABASE = "데이터베이스 및 MySQL 이해"
    MYSQL_SERVER = "서버에서 MySQL 관리"
    MAINTAINABLE_ARCHITECTURE = "유지보수 가능한 아키텍처"


# ==================== DATA CLASSES ====================


@dataclass
class LectureContent:
    """강의 자료"""
    title: str
    filename: str
    char_count: int
    content_preview: Optional[str] = None
    topics: List[str] = field(default_factory=list)


@dataclass
class DailyMissionContent:
    """일일 과제 내용"""
    day: DayNumber
    mission_type: DayMissionType
    author: str
    title: str
    content: str
    objectives: List[str] = field(default_factory=list)
    tools_used: List[str] = field(default_factory=list)
    completion_status: bool = False


@dataclass
class CourseModule:
    """과정 모듈"""
    module_name: str
    module_number: int
    lectures: List[LectureContent] = field(default_factory=list)
    daily_missions: Dict[int, DailyMissionContent] = field(default_factory=dict)
    advanced_missions: Dict[int, DailyMissionContent] = field(default_factory=dict)
    learning_objectives: List[str] = field(default_factory=list)


# ==================== COURSE DATA ====================


class DevelopmentEnvironmentCourse:
    """개발환경 구성 과정 데이터"""
    
    def __init__(self):
        self.course_name = "Development Environment Setup with SeSAC"
        self.author = "Lee Young-gi (이영기)"
        self.total_days = 5
        self.modules: Dict[str, CourseModule] = {}
        self._initialize_course()
    
    def _initialize_course(self):
        """과정 초기화"""
        # 강의 자료 데이터
        self.lectures = {
            "00_intro": LectureContent(
                title="Development Environment Course Introduction",
                filename="00 Development Environment Course Introduction.pdf",
                char_count=2177,
                topics=["개발환경 구성의 중요성", "과정 개요", "학습 목표"]
            ),
            "01_dev_env": LectureContent(
                title="Creating a Developer Friendly Computer Environment",
                filename="01 Creating a Developer Friendly Computer Environment.pdf",
                char_count=4428,
                topics=["개발 환경 설정", "필수 도구", "시스템 구성"]
            ),
            "03_git_basics": LectureContent(
                title="Git Basics",
                filename="03 Git Basics.pdf",
                char_count=7331,
                topics=["Git 개념", "기본 명령어", "버전 관리"]
            ),
            "04_git_advanced": LectureContent(
                title="Git Advanced",
                filename="04 Git Advanced.pdf",
                char_count=5822,
                topics=["Git 고급 기능", "브랜치 관리", "머지 전략"]
            ),
            "05_github": LectureContent(
                title="GitHub for Collaboration",
                filename="05 GitHub for Collaboration.pdf",
                char_count=5526,
                topics=["GitHub 사용법", "협업 워크플로우", "Pull Request"]
            ),
            "06_project_mgmt": LectureContent(
                title="Project Management and GitHub",
                filename="06 Project Management and GitHub.pdf",
                char_count=3556,
                topics=["프로젝트 관리", "이슈 추적", "GitHub Projects"]
            ),
            "07_docker": LectureContent(
                title="Docker Infrastructure and MySQL",
                filename="07 Docker Infrastructure and MySQL.pdf",
                char_count=8242,
                topics=["Docker 개념", "컨테이너", "MySQL 구성"]
            ),
            "08_database": LectureContent(
                title="Understanding Databases and MySQL",
                filename="08 Understanding Databases and MySQL.pdf",
                char_count=6597,
                topics=["데이터베이스 기초", "MySQL", "SQL 문법"]
            ),
            "09_mysql_server": LectureContent(
                title="Managing MySQL on a Server",
                filename="09 Managing MySQL on a Server.pdf",
                char_count=5692,
                topics=["서버 관리", "MySQL 운영", "성능 최적화"]
            ),
            "10_architecture": LectureContent(
                title="Maintainable Architecture",
                filename="10 Maintainable Architecture.pdf",
                char_count=5616,
                topics=["아키텍처 설계", "유지보수성", "확장성"]
            )
        }
        
        # 일일 과제 (기본)
        self.daily_missions_basic = {
            1: DailyMissionContent(
                day=DayNumber.DAY_01,
                mission_type=DayMissionType.BASIC,
                author="이영기",
                title="Step 1. UV로 FastAPI 라이브러리 추가하기",
                content="UV 패키지 매니저를 사용하여 FastAPI 라이브러리 추가",
                objectives=["UV 이해", "FastAPI 설치", "라이브러리 관리"],
                tools_used=["UV", "FastAPI", "Python"],
                completion_status=True
            ),
            2: DailyMissionContent(
                day=DayNumber.DAY_01,
                mission_type=DayMissionType.BASIC,
                author="이영기",
                title="Step 2. Postman으로 Get 요청을 통해 피보나치 함수 호출하기",
                content="Postman을 사용하여 FastAPI 엔드포인트에 GET 요청 수행",
                objectives=["API 요청", "Postman 사용법", "HTTP 프로토콜"],
                tools_used=["Postman", "FastAPI", "HTTP"],
                completion_status=True
            )
        }
    
    def get_course_summary(self) -> Dict:
        """과정 요약"""
        return {
            "course_name": self.course_name,
            "author": self.author,
            "total_days": self.total_days,
            "lectures_count": len(self.lectures),
            "daily_missions_count": len(self.daily_missions_basic),
            "total_content": sum(lec.char_count for lec in self.lectures.values())
        }
    
    def get_lectures(self) -> Dict[str, LectureContent]:
        """모든 강의 조회"""
        return self.lectures
    
    def get_lecture(self, key: str) -> Optional[LectureContent]:
        """특정 강의 조회"""
        return self.lectures.get(key)
    
    def get_daily_mission(self, day: int) -> Optional[DailyMissionContent]:
        """일일 과제 조회"""
        return self.daily_missions_basic.get(day)


# ==================== LECTURE CONTENT DETAILS ====================


class LectureDetails:
    """강의 상세 내용"""
    
    GIT_BASICS_TOPICS = [
        "Git이란?",
        "버전 관리의 필요성",
        "Git 설치 및 설정",
        "로컬 저장소 생성",
        "기본 명령어 (add, commit, log)",
        "파일 상태 관리",
        ".gitignore 사용법"
    ]
    
    GIT_ADVANCED_TOPICS = [
        "브랜치 생성 및 전환",
        "머지 (Merge)",
        "리베이스 (Rebase)",
        "충돌 해결",
        "태그 (Tag)",
        "스태시 (Stash)",
        "리셋과 리버트"
    ]
    
    GITHUB_COLLABORATION_TOPICS = [
        "GitHub 계정 생성",
        "저장소 생성",
        "원격 저장소 추가 (Remote)",
        "Push와 Pull",
        "Fork와 Clone",
        "Pull Request 만들기",
        "코드 리뷰 프로세스"
    ]
    
    DOCKER_TOPICS = [
        "컨테이너 개념",
        "Docker 이미지",
        "Docker 컨테이너 실행",
        "Dockerfile 작성",
        "Docker Compose",
        "MySQL 컨테이너화",
        "네트워크 구성"
    ]
    
    DATABASE_TOPICS = [
        "데이터베이스 개념",
        "관계형 데이터베이스",
        "MySQL 설치",
        "데이터베이스 생성",
        "테이블 설계",
        "SQL 쿼리",
        "인덱스와 성능"
    ]
    
    ARCHITECTURE_TOPICS = [
        "아키텍처 패턴",
        "MVC 패턴",
        "계층화 아키텍처",
        "마이크로서비스",
        "API 설계",
        "코드 재사용성",
        "테스트 가능한 설계"
    ]


# ==================== MISSION CATEGORIES ====================


class MissionCategories:
    """과제 분류"""
    
    # Day 01 기본 과제
    DAY01_BASIC_MISSIONS = {
        "mission_1": {
            "title": "UV로 FastAPI 라이브러리 추가하기",
            "step": 1,
            "objectives": [
                "UV 패키지 매니저 이해",
                "FastAPI 라이브러리 설치",
                "프로젝트 의존성 관리"
            ],
            "commands": [
                "uv pip install fastapi",
                "uv pip install uvicorn",
                "uv pip freeze"
            ],
            "expected_outcome": "FastAPI와 Uvicorn이 설치되어 프로젝트에서 사용 가능"
        },
        "mission_2": {
            "title": "Postman으로 Get 요청을 통해 피보나치 함수 호출하기",
            "step": 2,
            "objectives": [
                "FastAPI 엔드포인트 생성",
                "GET 요청 처리",
                "Postman에서 API 테스트"
            ],
            "api_endpoint": "/fibonacci/{n}",
            "http_method": "GET",
            "expected_response": "{"result": fibonacci_value, "input": n}"
        }
    }
    
    # Day 02 기본 과제 개요
    DAY02_BASIC_MISSIONS = {
        "description": "Python 개발환경 설정",
        "topics": [
            "Python 설치",
            "가상환경 생성",
            "IDE 설정",
            "첫 번째 프로젝트"
        ]
    }
    
    # Day 03 기본 과제 개요
    DAY03_BASIC_MISSIONS = {
        "description": "Git 기초 사용법",
        "topics": [
            "Git 설치 및 설정",
            "저장소 초기화",
            "파일 커밋",
            "로그 확인"
        ]
    }
    
    # Day 04 기본 과제 개요
    DAY04_BASIC_MISSIONS = {
        "description": "GitHub 협업",
        "topics": [
            "원격 저장소 설정",
            "Push와 Pull",
            "브랜치 관리",
            "Pull Request"
        ]
    }
    
    # Day 05 기본 과제 개요
    DAY05_BASIC_MISSIONS = {
        "description": "Docker와 Database",
        "topics": [
            "Docker 기본",
            "MySQL 컨테이너",
            "데이터베이스 연결",
            "SQL 쿼리 실행"
        ]
    }


# ==================== UTILITY FUNCTIONS ====================


def create_dev_env_course() -> DevelopmentEnvironmentCourse:
    """개발환경 구성 과정 생성"""
    return DevelopmentEnvironmentCourse()


def print_course_overview():
    """과정 개요 출력"""
    course = create_dev_env_course()
    summary = course.get_course_summary()
    
    print("=" * 60)
    print("DEVELOPMENT ENVIRONMENT SETUP COURSE")
    print("=" * 60)
    print(f"Course: {summary['course_name']}")
    print(f"Author: {summary['author']}")
    print(f"Duration: {summary['total_days']} days")
    print(f"Lectures: {summary['lectures_count']}")
    print(f"Total Content: {summary['total_content']} characters")
    print("=" * 60)
    
    print("\n" + "=" * 60)
    print("LECTURES")
    print("=" * 60)
    for key, lecture in course.get_lectures().items():
        print(f"\n[{key}] {lecture.title}")
        print(f"  File: {lecture.filename}")
        print(f"  Characters: {lecture.char_count}")
        if lecture.topics:
            print(f"  Topics: {', '.join(lecture.topics)}")


def print_day01_missions():
    """Day 01 과제 출력"""
    print("\n" + "=" * 60)
    print("DAY 01 - BASIC MISSIONS")
    print("=" * 60)
    
    for mission_key, mission_data in MissionCategories.DAY01_BASIC_MISSIONS.items():
        print(f"\n{mission_key}:")
        print(f"  Title: {mission_data['title']}")
        print(f"  Step: {mission_data['step']}")
        print(f"  Objectives:")
        for obj in mission_data['objectives']:
            print(f"    • {obj}")
        
        if 'commands' in mission_data:
            print(f"  Commands:")
            for cmd in mission_data['commands']:
                print(f"    $ {cmd}")
        
        if 'http_method' in mission_data:
            print(f"  API: {mission_data['http_method']} {mission_data['api_endpoint']}")
            print(f"  Expected Response: {mission_data['expected_response']}")


# ==================== COPYRIGHT NOTICE ====================


class CopyrightNotice:
    """저작권 공지"""
    
    NOTICE = """
    ╔══════════════════════════════════════════════════════════╗
    ║                      저작권 주의                          ║
    ╚══════════════════════════════════════════════════════════╝
    
    (주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
    운영 주체인 (주)업스테이지에게 귀속되어 있습니다.
    
    이 코드화된 버전은 개인의 학습 목적으로만 사용되어야 합니다.
    """
    
    @staticmethod
    def display():
        """공지 표시"""
        print(CopyrightNotice.NOTICE)


# ==================== MAIN ====================


if __name__ == "__main__":
    # 저작권 공지
    CopyrightNotice.display()
    
    # 과정 개요
    print_course_overview()
    
    # Day 01 과제
    print_day01_missions()
    
    print("\n" + "=" * 60)
    print("✓ Development Environment Course Data Loaded")
    print("=" * 60)
