"""
03.3주차 - Day 4: ORM심화
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class LearningContent:
    title: str = ""
    description: str = ""
    concepts: List[str] = None
    examples: List[str] = None
    key_takeaways: List[str] = None

    def __post_init__(self):
        if self.concepts is None:
            self.concepts = []
        if self.examples is None:
            self.examples = []
        if self.key_takeaways is None:
            self.key_takeaways = []

class Day4Learning:
    """Day 4: ORM심화"""

    main_topic = LearningContent(
        title="4.1 ORM심화의 기초",
        description="ORM심화에 대한 상세한 설명과 실무 적용 방법을 다룹니다.",
        concepts=[
            "SQLAlchemy",
            "관계매핑",
            "쿼리빌더",
            "마이그레이션",
            "성능"
        ],
        examples=[
            "예제 1: 기본 개념 실습",
            "예제 2: 심화 내용",
            "예제 3: 실무 활용",
            "예제 4: 성능 최적화",
            "예제 5: 트러블슈팅"
        ],
        key_takeaways=[
            "핵심 학습점 1",
            "핵심 학습점 2",
            "핵심 학습점 3"
        ]
    )

    advanced_topic = LearningContent(
        title="4.2 고급 개념",
        description="더 깊이 있는 내용을 다룹니다.",
        concepts=["개념1", "개념2", "개념3", "개념4", "개념5"],
        examples=["예제1", "예제2", "예제3", "예제4", "예제5"],
        key_takeaways=["핵심1", "핵심2", "핵심3"]
    )

    practical_application = LearningContent(
        title="4.3 실무 적용",
        description="실제 프로젝트에서의 적용 방법을 다룹니다.",
        concepts=["개념1", "개념2", "개념3", "개념4", "개념5"],
        examples=["예제1", "예제2", "예제3", "예제4", "예제5"],
        key_takeaways=["핵심1", "핵심2", "핵심3"]
    )

    best_practices = LearningContent(
        title="4.4 모범 사례",
        description="업계 표준과 모범 사례를 다룹니다.",
        concepts=["개념1", "개념2", "개념3", "개념4", "개념5"],
        examples=["예제1", "예제2", "예제3", "예제4", "예제5"],
        key_takeaways=["핵심1", "핵심2", "핵심3"]
    )

    summary_and_optimization = LearningContent(
        title="4.5 정리 및 최적화",
        description="주요 개념을 정리하고 성능 최적화를 다룹니다.",
        concepts=["개념1", "개념2", "개념3", "개념4", "개념5"],
        examples=["예제1", "예제2", "예제3", "예제4", "예제5"],
        key_takeaways=["핵심1", "핵심2", "핵심3"]
    )

    @classmethod
    def get_all_content(cls) -> Dict[str, LearningContent]:
        return {
            "main_topic": cls.main_topic,
            "advanced_topic": cls.advanced_topic,
            "practical_application": cls.practical_application,
            "best_practices": cls.best_practices,
            "summary_and_optimization": cls.summary_and_optimization,
        }
