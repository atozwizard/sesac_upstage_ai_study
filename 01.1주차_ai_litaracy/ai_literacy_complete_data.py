"""
AI Literacy Course - Complete Codified Data Structure
SeSAC AI Literacy Program의 모든 과제 내용을 코드로 변환

Note: 이 파일은 저작권 보호 PDF에서 추출한 데이터를 구조화한 것입니다.
저작권: (주)업스테이지 - 교육 목적으로만 사용 가능
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
from datetime import datetime


# ==================== ENUMS ====================


class MissionType(Enum):
    """과제 유형"""
    BASIC = "basic"
    ADVANCED = "advanced"


class ContentType(Enum):
    """콘텐츠 유형"""
    BLOG = "blog"
    INFOGRAPHIC = "infographic"
    SHORT_FORM_VIDEO = "short_form_video"


class AITrend(Enum):
    """AI 트렌드"""
    MCP = "MCP (Model Context Protocol)"
    AI_AGENT = "AI Agent"
    RAG = "RAG"
    PHYSICAL_AI = "Physical AI"
    A2A = "A2A"
    SMALL_LANGUAGE_MODEL = "소형 언어 모델"
    SOVEREIGN_AI = "Sovereign AI"


class Step(Enum):
    """과제 단계"""
    STEP_1 = "Step 1"
    STEP_2 = "Step 2"
    STEP_3 = "Step 3"


# ==================== DATA CLASSES ====================


@dataclass
class AITrendDefinition:
    """AI 트렌드 정의"""
    name: str
    core_concept: str
    practical_examples: List[str] = field(default_factory=list)
    related_companies: List[str] = field(default_factory=list)
    distinction: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'core_concept': self.core_concept,
            'practical_examples': self.practical_examples,
            'related_companies': self.related_companies,
            'distinction': self.distinction
        }


@dataclass
class EvaluationCriteria:
    """평가 기준"""
    interest_level: str  # 관심도
    public_understanding: str  # 대중 이해도
    practical_examples: str  # 실생활 예시
    content_format: str  # 콘텐츠 형식
    production_confidence: str  # 제작 자신감


@dataclass
class SelectionReasoning:
    """트렌드 선택 이유"""
    novelty: str  # 참신함
    public_interest: str  # 대중의 관심도
    perspective: str  # 관점
    content_approach: str  # 콘텐츠 접근 방식
    tool_efficiency: str  # 도구 효율성


@dataclass
class ContentProposal:
    """콘텐츠 제안"""
    selected_trend: str
    selection_reasoning: SelectionReasoning
    selected_formats: List[ContentType]
    format_suitability: str
    expected_difficulties: List[str]
    solutions: List[str]
    preparation_items: List[str]


@dataclass
class BlogContent:
    """블로그 콘텐츠"""
    title: str
    introduction: str  # 200자
    body: str  # 600자
    conclusion: str  # 200자
    references: List[str]
    
    def get_word_count(self) -> int:
        """전체 글자 수"""
        return len(self.introduction) + len(self.body) + len(self.conclusion)


@dataclass
class InfographicContent:
    """인포그래픽 콘텐츠"""
    title: str
    tools_used: str
    core_concept: str  # 3줄 요약
    mechanism_description: str  # 작동 원리 설명
    advantages: List[str]  # 3가지
    disadvantages: List[str]  # 2가지
    related_companies: List[str]  # 로고 3개
    future_outlook: str  # 한 문장
    design_colors: str  # 사용 색상
    layout_structure: str  # 레이아웃
    emphasized_elements: str  # 강조 요소
    file_name: Optional[str] = None


@dataclass
class Mission:
    """일일 과제"""
    day: int
    step: str
    mission_type: MissionType
    author: str
    content_proposal: Optional[ContentProposal] = None
    blog_content: Optional[BlogContent] = None
    infographic_content: Optional[InfographicContent] = None
    submission_date: Optional[str] = None
    
    def get_content_format(self) -> str:
        """완성된 콘텐츠 형식 반환"""
        if self.blog_content:
            return "Blog"
        elif self.infographic_content:
            return "Infographic"
        return "Unknown"


# ==================== DATA DEFINITIONS ====================


class BasicMissionContent:
    """기본 과제 내용"""
    
    # Day 01: AI 트렌드 정리하기
    AI_TRENDS_DATA = {
        "MCP": AITrendDefinition(
            name="MCP (Model Context Protocol)",
            core_concept="AI가 외부 도구나 데이터에 접근할 수 있게 도와주는 공통된 연결 방식",
            practical_examples=[
                "GPT나 Gemini 등의 AI Agent가 Canva나 Suno 등 활용 도구에 접근",
                "Claude에서 처음 표준화",
                "AI Agent가 사용할 팔다리를 엮어주는 역할"
            ],
            related_companies=[
                "Notion: 워크스페이스에 AI 어시스턴트가 안전하게 접근",
                "Figma: AI 어시스턴트가 워크플로에 Figma 활용",
                "Microsoft: Copilot 제품군에 MCP 적용"
            ]
        ),
        "AI_Agent": AITrendDefinition(
            name="AI Agent",
            core_concept="사용자의 목표를 이해하고 스스로 계획을 세우며, 외부 도구 사용 등 다양한 수단으로 작업을 자율적으로 수행",
            practical_examples=[
                "개인화된 영화 추천 자동화",
                "의료분야 진단 보조 어시스턴트"
            ],
            related_companies=[
                "Amazon: 개인화 추천 시스템",
                "IBM Watson: 의료 진단 보조"
            ],
            distinction="어시스턴트는 사용자의 질문에 반응하여 정보를 제공하고 요청된 작업을 수행하지만, "
                       "에이전트는 특정 목표를 달성하기 위해 스스로 판단하고 자율적으로 행동함"
        )
    }


class AdvancedMissionContent:
    """심화 과제 내용"""
    
    # Day 01 심화 과제
    DAY01_SOVEREIGN_AI = {
        "trend": "Sovereign AI",
        "selection_reasoning": SelectionReasoning(
            novelty="폐쇄성과 관계자의 다방면으로의 사용이 가능한 개방성의 공존의 특이함",
            public_interest="대중의 관심도를 특정 키워드로 집중시키면 이해도가 올 것이라고 생각",
            perspective="대한민국은 휴전국으로 아직 전쟁 중인 국가. 국가 안보적 관점에서 고려",
            content_approach="브런치 기고 글과 인포그래픽으로 표현",
            tool_efficiency="AI 툴을 이용하면 주제가 명확하면 금방 나옴"
        ),
        "evaluation_scores": {
            "interest_level": 5,
            "interest_reason": "폐쇄성과 개방성, 유틸리티성이 공존해야 하는 점이 특이함",
            "public_understanding": "휴전국인 대한민국의 상황상 국가안보적 관점에서 소버린 AI의 필요성에 대해 이해하기 쉬움",
            "practical_examples": [
                "회사 인트라넷에서의 내부자료 활용",
                "정부24에서 국민들이 등본이나 여러 자료들을 열람할 수 있지만 직접 수정 불가",
                "관별, 관급별 공무원의 PC에서 등급을 나누어 접근이 가능한 문서가 다름"
            ],
            "content_format": "브런치 글, 인포그래픽",
            "production_confidence": "기본 미션에서 이미 정리한 내용이 있고 예시도 명확하여 금방 가능할 것 같음"
        },
        "blog_content": BlogContent(
            title="AI 시대의 주권: 디지털 식민주의와 소버린 AI",
            introduction="누가 AI를 통제하는가?",
            body="본론 (600자 이상) - 디지털 식민주의, AI의 '두뇌(모델)' 뿐 아니라 '몸(서버)', '혈관(네트워크)', '에너지 공급원(전력/냉각)'까지 모두 직접 갖추는 것",
            conclusion="AI 주권, 고립이 아닌 연결된 자립을 향하여 - 개방형 주권 AI의 발전 전망",
            references=[
                "https://www.technologyreview.kr/전문가-칼럼-기술-주권-98-대전환-소버린-ai가-만/",
                "https://banjjakpro.com/entry/엔비디아가-언급한-소버린-AI는-무엇이며-왜-중요한가/",
                "https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000057867"
            ]
        ),
        "infographic_content": InfographicContent(
            title="국가안보를 위한 소버린 AI의 필요성",
            tools_used="GPT, Canva",
            core_concept="소버린 AI의 핵심 개념 3줄 요약",
            mechanism_description="AI 주권의 작동 원리",
            advantages=[
                "국가 안보 강화",
                "데이터 독립성 확보",
                "기술 주권 확립"
            ],
            disadvantages=[
                "높은 초기 구축 비용",
                "기술 격차 극복의 어려움"
            ],
            related_companies=[
                "China: AI 2030 플랜",
                "Japan: 정책 우선 접근 AI 인프라 대규모 투자",
                "India: 기술 혁신 허브 목표로 민관 협력"
            ],
            future_outlook="개방형 주권 AI의 시대로 향함",
            design_colors="파랑 계열로 국가 안보 이미지 강조",
            layout_structure="상단: 소버린 AI 개념, 중단: 세계 주요국 사례, 하단: 미래 전망",
            emphasized_elements="국가별 투자 규모를 가시화하여 국제 경쟁 상황 강조"
        ),
        "preparation_items": [
            "소버린 AI의 활용 예",
            "국가안보 개념",
            "주권이란 무엇인가"
        ],
        "expected_difficulties": [
            "소버린 AI의 주권이 왜 필요한지에 대한 이해"
        ],
        "solutions": [
            "우리나라의 예를 들어 국가안보적 관점에서 쉽게 이해하게 함"
        ]
    }


# ==================== REPOSITORY CLASS ====================


class AILiteracyCourseRepository:
    """AI 리터러시 과정 데이터 저장소"""
    
    def __init__(self):
        self.course_name = "AI Literacy with SeSAC"
        self.author = "Lee Young-gi (이영기)"
        self.total_days = 5
        self.basic_missions: Dict[int, Mission] = {}
        self.advanced_missions: Dict[int, Mission] = {}
        self._initialize_data()
    
    def _initialize_data(self):
        """데이터 초기화"""
        self._load_basic_missions()
        self._load_advanced_missions()
    
    def _load_basic_missions(self):
        """기본 과제 로드"""
        # 빈 placeholder - 확장 가능
        pass
    
    def _load_advanced_missions(self):
        """심화 과제 로드"""
        # Day 01 심화 과제: Sovereign AI
        day01_advanced = Mission(
            day=1,
            step=Step.STEP_1.value,
            mission_type=MissionType.ADVANCED,
            author="이영기",
            content_proposal=ContentProposal(
                selected_trend="Sovereign AI",
                selection_reasoning=AdvancedMissionContent.DAY01_SOVEREIGN_AI["selection_reasoning"],
                selected_formats=[ContentType.BLOG, ContentType.INFOGRAPHIC],
                format_suitability="요점만 시각화하여 받아들이는 것도 좋고, 좀 더 구체적으로 설명해가는 과정도 좋아서 둘 다 해보기로 함",
                expected_difficulties=AdvancedMissionContent.DAY01_SOVEREIGN_AI["expected_difficulties"],
                solutions=AdvancedMissionContent.DAY01_SOVEREIGN_AI["solutions"],
                preparation_items=AdvancedMissionContent.DAY01_SOVEREIGN_AI["preparation_items"]
            ),
            blog_content=AdvancedMissionContent.DAY01_SOVEREIGN_AI["blog_content"],
            infographic_content=AdvancedMissionContent.DAY01_SOVEREIGN_AI["infographic_content"],
            submission_date="2024-01-15"
        )
        self.advanced_missions[1] = day01_advanced
    
    def get_all_ai_trends(self) -> List[str]:
        """모든 AI 트렌드 조회"""
        return [trend.value for trend in AITrend]
    
    def get_trend_definition(self, trend_name: str) -> Optional[AITrendDefinition]:
        """특정 트렌드 정의 조회"""
        return BasicMissionContent.AI_TRENDS_DATA.get(trend_name)
    
    def get_mission(self, day: int, mission_type: MissionType) -> Optional[Mission]:
        """특정 일차의 과제 조회"""
        if mission_type == MissionType.BASIC:
            return self.basic_missions.get(day)
        else:
            return self.advanced_missions.get(day)
    
    def get_course_summary(self) -> Dict:
        """과정 요약"""
        return {
            "course_name": self.course_name,
            "author": self.author,
            "total_days": self.total_days,
            "ai_trends": self.get_all_ai_trends(),
            "basic_missions_count": len(self.basic_missions),
            "advanced_missions_count": len(self.advanced_missions)
        }
    
    def get_mission_statistics(self) -> Dict:
        """과제 통계"""
        return {
            "total_basic_missions": len(self.basic_missions),
            "total_advanced_missions": len(self.advanced_missions),
            "completed_missions": sum(
                1 for m in list(self.basic_missions.values()) + list(self.advanced_missions.values())
                if m.submission_date is not None
            ),
            "completion_rate": f"{(sum(1 for m in list(self.basic_missions.values()) + list(self.advanced_missions.values()) if m.submission_date) / max(1, len(self.basic_missions) + len(self.advanced_missions)) * 100):.1f}%"
        }


# ==================== COPYRIGHT NOTICE ====================


class CopyrightNotice:
    """저작권 공지"""
    
    NOTICE = """
    ╔══════════════════════════════════════════════════════════╗
    ║                      저작권 주의                          ║
    ╚══════════════════════════════════════════════════════════╝
    
    (주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
    운영 주체인 (주)업스테이지에게 귀속되어 있습니다.
    
    콘텐츠 일부 또는 전부를 다음과 같이 할 수 없습니다:
    - 복사, 복제
    - 판매, 재판매
    - 공개, 공유
    
    이 코드화된 버전은 개인의 학습 목적으로만 사용되어야 합니다.
    """
    
    @staticmethod
    def display():
        """공지 표시"""
        print(CopyrightNotice.NOTICE)


# ==================== UTILITY FUNCTIONS ====================


def create_course_repository() -> AILiteracyCourseRepository:
    """과정 저장소 생성"""
    return AILiteracyCourseRepository()


def print_course_structure():
    """과정 구조 출력"""
    repo = create_course_repository()
    summary = repo.get_course_summary()
    
    print("=" * 60)
    print("AI LITERACY COURSE STRUCTURE")
    print("=" * 60)
    print(f"Course: {summary['course_name']}")
    print(f"Author: {summary['author']}")
    print(f"Duration: {summary['total_days']} days")
    print(f"\nAI Trends Covered:")
    for trend in summary['ai_trends']:
        print(f"  • {trend}")
    print(f"\nMissions:")
    print(f"  • Basic Missions: {summary['basic_missions_count']}")
    print(f"  • Advanced Missions: {summary['advanced_missions_count']}")
    print("=" * 60)


def print_day01_advanced_mission():
    """Day 01 심화 과제 출력"""
    repo = create_course_repository()
    mission = repo.get_mission(1, MissionType.ADVANCED)
    
    if mission:
        print("\n" + "=" * 60)
        print("DAY 01 - ADVANCED MISSION (심화 과제)")
        print("=" * 60)
        print(f"Trend: {mission.content_proposal.selected_trend}")
        print(f"Author: {mission.author}")
        print(f"Selected Formats: {', '.join(f.value for f in mission.content_proposal.selected_formats)}")
        
        if mission.blog_content:
            print(f"\nBlog Title: {mission.blog_content.title}")
            print(f"Word Count: {mission.blog_content.get_word_count()} characters")
        
        if mission.infographic_content:
            print(f"\nInfographic Title: {mission.infographic_content.title}")
            print(f"Tools Used: {mission.infographic_content.tools_used}")
        
        print("=" * 60)


# ==================== MAIN ====================


if __name__ == "__main__":
    # 저작권 공지
    CopyrightNotice.display()
    
    # 과정 구조 출력
    print_course_structure()
    
    # Day 01 심화 과제 출력
    print_day01_advanced_mission()
    
    # 과제 통계
    repo = create_course_repository()
    stats = repo.get_mission_statistics()
    print("\n" + "=" * 60)
    print("MISSION STATISTICS")
    print("=" * 60)
    for key, value in stats.items():
        print(f"{key}: {value}")
    print("=" * 60)
