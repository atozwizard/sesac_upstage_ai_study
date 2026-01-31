"""
03.3주차 - Day 2: 웹프레임워크
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

class Day2Learning:
    """Day 2: 웹프레임워크"""

    main_topic = LearningContent(
        title="2.1 웹프레임워크의 기초",
        description="웹프레임워크에 대한 상세한 설명과 실무 적용 방법을 다룹니다.",
        concepts=[
            "Flask",
            "라우팅",
            "미들웨어",
            "에러핸들링",
            "테스트"
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
        title="2.2 고급 개념",
        description="더 깊이 있는 내용을 다룹니다.",
        concepts=["개념1", "개념2", "개념3", "개념4", "개념5"],
        examples=["예제1", "예제2", "예제3", "예제4", "예제5"],
        key_takeaways=["핵심1", "핵심2", "핵심3"]
    )

    practical_application = LearningContent(
        title="2.3 실무 적용",
        description="실제 프로젝트에서의 적용 방법을 다룹니다.",
        concepts=["개념1", "개념2", "개념3", "개념4", "개념5"],
        examples=["예제1", "예제2", "예제3", "예제4", "예제5"],
        key_takeaways=["핵심1", "핵심2", "핵심3"]
    )

    best_practices = LearningContent(
        title="2.4 모범 사례",
        description="업계 표준과 모범 사례를 다룹니다.",
        concepts=["개념1", "개념2", "개념3", "개념4", "개념5"],
        examples=["예제1", "예제2", "예제3", "예제4", "예제5"],
        key_takeaways=["핵심1", "핵심2", "핵심3"]
    )

    summary_and_optimization = LearningContent(
        title="2.5 정리 및 최적화",
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
