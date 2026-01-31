"""
AI Literacy Course Content - Codified Version
저작권 보호 PDF 파일들로부터 추출하여 코드화한 AI 리터러시 과정 데이터

작성자: 이영기
구성: SeSAC AI Literacy 프로그램
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum

# ==================== 트렌드 및 개념 정의 ====================


class AITrendType(Enum):
    """AI 트렌드 분류"""
    SOVEREIGN_AI = "sovereign_ai"
    AI_AGENT = "ai_agent"
    RAG = "rag"
    PHYSICAL_AI = "physical_ai"
    MCP = "mcp"
    A2A = "a2a"
    SMALL_LANGUAGE_MODEL = "small_language_model"


class ContentFormat(Enum):
    """콘텐츠 제작 형식"""
    BLOG = "blog"
    INFOGRAPHIC = "infographic"
    VIDEO = "video"


class DayType(Enum):
    """코스 진행 일차"""
    DAY01 = 1
    DAY02 = 2
    DAY03 = 3
    DAY04 = 4
    DAY05 = 5


# ==================== 기본 데이터 클래스 ====================


@dataclass
class EvaluationCriteria:
    """평가 기준"""
    interest_level: str  # 관심도
    public_understanding: str  # 대중 이해도
    practical_examples: str  # 실생활 예시
    content_format: str  # 콘텐츠 형식
    production_confidence: str  # 제작 자신감


@dataclass
class ContentProposal:
    """콘텐츠 제안"""
    selected_trend: AITrendType
    selection_reason: str
    selected_format: ContentFormat
    format_suitability: str
    expected_difficulties: List[str]
    solutions: List[str]


@dataclass
class AITrendInfo:
    """AI 트렌드 정보"""
    name: str
    core_concept: str
    practical_examples: List[str]
    related_companies: List[str]


@dataclass
class MissionDay:
    """일일 과제"""
    day: DayType
    author: str
    mission_type: str  # "basic" 또는 "advanced"
    content_proposals: List[ContentProposal]
    trends_analyzed: List[AITrendInfo]


# ==================== 기본 과제 데이터 ====================


class BasicMissionData:
    """기본 과제 데이터"""

    # Day 01: AI 트렌드 정리하기
    DAY01_AI_TRENDS = {
        "MCP": {
            "name": "MCP (Model Context Protocol)",
            "core_concept": "AI가 외부 도구나 데이터에 접근할 수 있게 도와주는 공통된 연결 방식",
            "practical_examples": [
                "GPT나 Gemini 등의 AI Agent가 Canva나 Suno 등 활용 도구에 접근",
                "Claude에서 표준화",
                "AI Agent가 사용할 팔다리를 엮어주는 역할"
            ],
            "related_companies": [
                "Notion: 워크스페이스에 AI 어시스턴트가 안전하게 접근",
                "Figma: AI 어시스턴트가 워크플로에 Figma 활용",
                "Microsoft: Copilot 제품군에 MCP 적용"
            ]
        },
        "AI_Agent": {
            "name": "AI Agent",
            "core_concept": "사용자의 목표를 이해하고 스스로 계획을 세우며, 외부 도구 사용 등 다양한 수단으로 작업을 자율적으로 수행",
            "practical_examples": [
                "개인화된 영화 추천 자동화",
                "의료분야 진단 보조 어시스턴트"
            ],
            "distinction": "어시스턴트는 사용자의 질문에 반응하여 정보를 제공하고 요청된 작업을 수행하지만, "
                          "에이전트는 특정 목표를 달성하기 위해 스스로 판단하고 자율적으로 행동함"
        }
    }

    # Day 01 답안 데이터
    @staticmethod
    def get_day01_mission_data() -> Dict:
        """Day01 기본 과제 데이터"""
        return {
            "mission_title": "Step 1. AI 트렌드 정리하기",
            "author": "이영기",
            "day": 1,
            "trends_analyzed": BasicMissionData.DAY01_AI_TRENDS,
            "mission_description": "7가지 AI 트렌드 중 1개 이상을 선택하여 핵심 개념, 실생활 활용 예시, 관련 기업 등을 조사",
            "available_trends": [
                "AI Agent",
                "RAG",
                "Physical AI",
                "MCP",
                "A2A",
                "소형 언어 모델",
                "소버린 AI"
            ]
        }


# ==================== 심화 과제 데이터 ====================


class AdvancedMissionData:
    """심화 과제 데이터"""

    @staticmethod
    def get_day01_advanced_mission() -> Dict:
        """Day01 심화 과제: 주제 선택 및 계획"""
        return {
            "mission_title": "Step 1. 주제 선택",
            "author": "이영기",
            "day": 1,
            "selected_trend": "Sovereign AI",
            "selection_reason_summary": "폐쇄성과 개방성의 공존의 특이함",
            "selection_details": {
                "novelty": "소버린 AI의 폐쇄성과 관계자의 다방면으로의 사용이 가능한 개방성의 공존의 특이함",
                "public_interest": "대중의 관심도를 특정 키워드로 집중시키면 이해도가 올 것이라고 생각",
                "national_security": "대한민국은 휴전국으로 아직 전쟁 중인 국가. 국가 안보적 관점에서 고려",
                "content_format_decision": "브런치 기고 글과 인포그래픽으로 표현",
                "tool_experience": "툴을 이용하면 주제가 명확하면 금방 나옴"
            },
            "evaluation_criteria": {
                "interest_level": "기본 미션에서 준 별점과 이유",
                "public_understanding": "비전공자에게 설명하기 쉬운가?",
                "practical_examples": "구체적인 예시를 떠올리기 쉬운가?",
                "content_format": "어떤 형식으로 만들 예정인가? (블로그/인포그래픽/영상)",
                "production_confidence": "60분 안에 완성할 수 있는가?"
            },
            "selected_format": ["Blog", "Infographic"],
            "format_suitability": "요점만 시각화하여 받아들이는 것도 좋고, 좀 더 구체적으로 설명해가는 과정도 좋아서 둘 다 해보기로 함",
            "expected_difficulties": [
                "관계된 용어나 개념을 나도 적절하고 정확하게 이해해야 하는데 아직 그러지 못하는 점"
            ],
            "solutions": [
                "AI 툴을 이용하여 뽑아본다"
            ]
        }


# ==================== AI 리터러시 과정 데이터 구조 ====================


class AILiteracyCourseData:
    """AI 리터러시 전체 과정 데이터"""

    def __init__(self):
        self.author = "이영기"
        self.course_name = "AI Literacy with SeSAC"
        self.basic_missions = self._initialize_basic_missions()
        self.advanced_missions = self._initialize_advanced_missions()

    def _initialize_basic_missions(self) -> Dict[int, Dict]:
        """기본 과제 초기화"""
        return {
            1: BasicMissionData.get_day01_mission_data(),
        }

    def _initialize_advanced_missions(self) -> Dict[int, Dict]:
        """심화 과제 초기화"""
        return {
            1: AdvancedMissionData.get_day01_advanced_mission(),
        }

    def get_mission_by_day(self, day: int, mission_type: str = "basic") -> Optional[Dict]:
        """특정 일차의 과제 조회"""
        missions = self.basic_missions if mission_type == "basic" else self.advanced_missions
        return missions.get(day)

    def get_all_trends(self) -> List[str]:
        """모든 분석된 트렌드 조회"""
        return [
            "AI Agent",
            "RAG",
            "Physical AI",
            "MCP",
            "A2A",
            "소형 언어 모델",
            "소버린 AI"
        ]

    def get_course_structure(self) -> Dict:
        """과정 구조 조회"""
        return {
            "course_name": self.course_name,
            "author": self.author,
            "total_days": 5,
            "mission_types": ["basic", "advanced"],
            "basic_missions_count": len(self.basic_missions),
            "advanced_missions_count": len(self.advanced_missions),
            "ai_trends": self.get_all_trends()
        }


# ==================== 저작권 선언 ====================


class CopyrightNotice:
    """저작권 공지"""

    NOTICE = """
    ※ 저작권 주의
    (주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 운영 주체인 (주)업스테이지에게 귀속되어 있습니다.
    콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매, 공개, 공유 등을 할 수 없습니다.
    
    이 코드화된 버전은 개인의 학습 목적으로만 사용되어야 합니다.
    """

    @staticmethod
    def display_notice():
        """저작권 공지 표시"""
        print(CopyrightNotice.NOTICE)


# ==================== 유틸리티 함수 ====================


def initialize_course() -> AILiteracyCourseData:
    """과정 데이터 초기화"""
    course = AILiteracyCourseData()
    return course


def print_course_overview():
    """과정 개요 출력"""
    course = initialize_course()
    structure = course.get_course_structure()

    print("=" * 60)
    print("AI Literacy Course - Overview")
    print("=" * 60)
    print(f"Course: {structure['course_name']}")
    print(f"Author: {structure['author']}")
    print(f"Total Days: {structure['total_days']}")
    print(f"Basic Missions: {structure['basic_missions_count']}")
    print(f"Advanced Missions: {structure['advanced_missions_count']}")
    print(f"\nAI Trends Covered: {', '.join(structure['ai_trends'])}")
    print("=" * 60)


def get_day01_basic_mission():
    """Day01 기본 과제 조회"""
    course = initialize_course()
    return course.get_mission_by_day(1, "basic")


def get_day01_advanced_mission():
    """Day01 심화 과제 조회"""
    course = initialize_course()
    return course.get_mission_by_day(1, "advanced")


# ==================== 메인 실행 ====================


if __name__ == "__main__":
    # 저작권 공지 표시
    CopyrightNotice.display_notice()

    # 과정 개요 출력
    print_course_overview()

    # Day01 기본 과제 조회
    print("\n" + "=" * 60)
    print("Day 01 - Basic Mission")
    print("=" * 60)
    basic_mission = get_day01_basic_mission()
    if basic_mission:
        print(f"Title: {basic_mission['mission_title']}")
        print(f"Author: {basic_mission['author']}")
        print(f"Available Trends: {', '.join(basic_mission['available_trends'])}")

    # Day01 심화 과제 조회
    print("\n" + "=" * 60)
    print("Day 01 - Advanced Mission")
    print("=" * 60)
    advanced_mission = get_day01_advanced_mission()
    if advanced_mission:
        print(f"Title: {advanced_mission['mission_title']}")
        print(f"Author: {advanced_mission['author']}")
        print(f"Selected Trend: {advanced_mission['selected_trend']}")
        print(f"Selected Format: {', '.join(advanced_mission['selected_format'])}")
