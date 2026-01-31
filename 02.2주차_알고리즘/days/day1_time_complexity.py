"""
02.2주차_알고리즘 - Day 1: 시간복잡도
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

class Day1Learning:
    """Day 1: 시간복잡도와 공간복잡도"""

    time_complexity_basics = LearningContent(
        title="1.1 시간복잡도(Time Complexity) 기초",
        description="""
        알고리즘의 성능을 분석하는 가장 중요한 개념이 시간복잡도입니다. 시간복잡도는 입력 크기 n에 따라 
        알고리즘이 얼마나 오래 걸리는지를 나타내는 척도입니다. Big-O 표기법을 사용하여 최악의 경우 
        시간 복잡도를 표현합니다. 이를 통해 데이터 규모가 커질 때 알고리즘 성능이 어떻게 변하는지 
        예측할 수 있습니다. O(1)에서 O(n!), O(2^n) 등 다양한 복잡도가 존재하며, 각각의 특성을 
        이해하는 것은 효율적인 알고리즘 설계에 필수적입니다.
        """,
        concepts=[
            "Big-O 표기법의 의미",
            "시간복잡도의 실질적 의미",
            "함수의 성장률 비교",
            "다항식 vs 지수 시간복잡도",
            "복잡도 분류: 상수, 로그, 선형 등",
            "실행 시간 예측"
        ],
        examples=[
            "O(1): 상수 시간 - 배열 인덱싱, 해시맵 접근",
            "O(log n): 로그 시간 - 이진 탐색, 이진 트리 탐색",
            "O(n): 선형 시간 - 배열 순회, 선형 탐색",
            "O(n log n): 선형 로그 시간 - 병합 정렬, 퀵 정렬",
            "O(n²): 이차 시간 - 버블 정렬, 중첩 루프"
        ],
        key_takeaways=[
            "Big-O는 최악의 경우 성능을 나타내며, 상수항과 낮은 차수는 무시",
            "같은 입력 크기라도 복잡도가 낮을수록 실행 시간이 훨씬 짧음",
            "알고리즘 선택 시 입력 크기 범위를 고려하여 최적의 복잡도 선택 필요"
        ]
    )

    big_o_notation = LearningContent(
        title="1.2 Big-O 표기법 상세 분석",
        description="""
        Big-O 표기법은 알고리즘의 상한선(upper bound)을 나타냅니다. 예를 들어 O(n)은 입력 크기 n에 
        선형적으로 증가하는 시간을 의미합니다. Big-O 표기법에서 상수는 무시되므로 O(2n)과 O(5n)은 
        모두 O(n)으로 표현됩니다. 또한 가장 높은 차수의 항만 고려하므로 O(n² + n)은 O(n²)로 표현됩니다.
        이러한 점화식 해석 방법을 통해 복잡한 알고리즘도 그 특성을 빠르게 파악할 수 있습니다. 
        실무에서는 주어진 입력 크기에 대해 어느 정도 시간이 소요될지 추정하는 데 사용됩니다.
        """,
        concepts=[
            "점근표기법: Big-O, Big-Omega, Big-Theta",
            "상수항 무시의 의미",
            "낮은 차수 항 무시",
            "복잡도 순서: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)",
            "실제 실행 시간과의 관계",
            "복잡도 그래프 해석"
        ],
        examples=[
            "O(1) 예제: 배열의 첫 번째 요소 접근",
            "O(n) 예제: 배열 합 계산",
            "O(n²) 예제: 중첩 루프로 모든 쌍 비교",
            "O(log n) 예제: 정렬된 배열에서 이진 탐색",
            "O(n log n) 예제: 병합 정렬 또는 퀵 정렬"
        ],
        key_takeaways=[
            "Big-O 표기법은 입력 크기가 매우 클 때의 성장률을 중심으로 표현",
            "상수항이나 낮은 차수 항은 큰 입력에서 무시할 수 있는 수준",
            "같은 Big-O라도 상수가 다르면 실제 성능은 크게 차이날 수 있음"
        ]
    )

    space_complexity = LearningContent(
        title="1.3 공간복잡도(Space Complexity) 분석",
        description="""
        공간복잡도는 알고리즘이 사용하는 메모리 양을 입력 크기 n의 함수로 나타냅니다. 시간복잡도와 
        마찬가지로 Big-O 표기법을 사용하여 표현합니다. O(1) 공간은 입력 크기와 무관하게 고정된 메모리만 
        사용하는 경우이고, O(n)은 입력 크기만큼 추가 메모리가 필요한 경우입니다. 시간과 공간은 트레이드오프 
        관계가 있어서, 메모리를 더 사용하여 시간을 단축하거나 그 반대로 할 수 있습니다. 
        메모리 제약이 있는 임베디드 시스템에서는 공간복잡도가 중요한 고려 사항입니다.
        """,
        concepts=[
            "메모리 사용량 분석",
            "재귀 호출의 스택 메모리",
            "보조 자료구조 메모리",
            "in-place 알고리즘 vs 추가 메모리 사용 알고리즘",
            "시간-공간 트레이드오프",
            "메모리 최적화 기법"
        ],
        examples=[
            "O(1) 공간: in-place 버블 정렬",
            "O(n) 공간: 배열 복사, 병합 정렬",
            "O(log n) 공간: 재귀 깊이 (이진 탐색 재귀)",
            "O(n) 공간: 트리/그래프 BFS 큐, 해시맵",
            "O(2^n) 공간: 재귀 호출 스택 (피보나치)"
        ],
        key_takeaways=[
            "공간복잡도는 알고리즘의 보조 메모리 사용량만 고려",
            "스택 메모리(재귀)와 힙 메모리(동적 할당)를 구분하여 분석",
            "메모리 제약 환경에서는 O(1) 또는 O(log n) 공간 알고리즘을 선호"
        ]
    )

    calculating_complexity = LearningContent(
        title="1.4 복잡도 계산 방법론",
        description="""
        복잡도를 계산하려면 코드를 분석하여 기본 연산의 반복 횟수를 세어야 합니다. 순차적 구문은 
        각각의 복잡도를 더하고, 중첩된 루프는 곱합니다. 조건문은 최악의 경우를 기준으로 하며, 
        함수 호출은 호출된 함수의 복잡도를 포함합니다. 재귀 함수의 복잡도는 점화식으로 표현하며, 
        마스터 정리(Master Theorem)를 사용하여 해결할 수 있습니다. 
        실무에서는 분석을 간소화하기 위해 지배항만 고려하는 것이 일반적입니다.
        """,
        concepts=[
            "기본 연산 식별 (산술, 비교, 할당)",
            "순차 구문의 합",
            "조건문의 최악의 경우",
            "루프 분석 (합 공식)",
            "중첩 루프 분석",
            "점화식 해결 (마스터 정리)"
        ],
        examples=[
            "단일 루프: for i in range(n) → O(n)",
            "중첩 루프: 2개 루프 → O(n²), 3개 루프 → O(n³)",
            "순차 구문: O(n) + O(n²) = O(n²)",
            "조건문: if 조건이면 O(n), 아니면 O(1) → 최악은 O(n)",
            "재귀: T(n) = 2T(n/2) + O(n) → 마스터 정리로 O(n log n)"
        ],
        key_takeaways=[
            "중첩 루프는 곱셈, 순차 구문은 덧셈으로 계산",
            "조건부 분기는 최악의 경우만 고려",
            "재귀 함수는 호출 깊이와 호출당 비용을 함께 분석"
        ]
    )

    practical_analysis = LearningContent(
        title="1.5 실무 적용과 최적화 전략",
        description="""
        실무에서 복잡도 분석은 개발 단계부터 필수적입니다. 입력 크기 범위를 파악하고 필요한 성능 
        목표를 설정한 후, 그에 맞는 알고리즘을 선택해야 합니다. 예를 들어 n이 1,000 이하라면 O(n²) 
        알고리즘도 충분하지만, n이 1,000,000이면 O(n log n) 이상이 필요합니다. 알고리즘을 선택한 후에는 
        프로파일링을 통해 실제 성능을 측정하고 필요시 최적화합니다. 
        복잡도 분석과 실제 성능이 일치하지 않을 수 있으므로 항상 검증이 필요합니다.
        """,
        concepts=[
            "입력 크기 범위별 허용 복잡도",
            "성능 목표 설정",
            "알고리즘 선택 기준",
            "프로파일링과 벤치마킹",
            "최적화 기법",
            "복잡도와 실제 성능의 괴리"
        ],
        examples=[
            "n ≤ 10: O(n!) 가능, 모든 순열 탐색",
            "n ≤ 10³: O(n³) 가능, 3중 루프",
            "n ≤ 10⁶: O(n log n) 필요, 정렬 알고리즘",
            "n ≤ 10⁸: O(n) 필요, 선형 탐색",
            "n ≤ 10⁹: O(log n) 또는 O(1) 필요"
        ],
        key_takeaways=[
            "입력 크기가 작으면 높은 복잡도도 실행 가능, 정확성 우선",
            "입력 크기가 크면 낮은 복잡도가 필수적",
            "복잡도 분석 후에도 반드시 성능 테스트 필요"
        ]
    )

    @classmethod
    def get_all_content(cls) -> Dict[str, LearningContent]:
        """모든 학습 내용을 딕셔너리로 반환"""
        return {
            "time_complexity_basics": cls.time_complexity_basics,
            "big_o_notation": cls.big_o_notation,
            "space_complexity": cls.space_complexity,
            "calculating_complexity": cls.calculating_complexity,
            "practical_analysis": cls.practical_analysis,
        }

    @classmethod
    def print_summary(cls) -> None:
        """학습 내용 요약 출력"""
        contents = cls.get_all_content()
        print("=" * 70)
        print("📚 Day 1: 시간복잡도와 공간복잡도")
        print("=" * 70)
        for key, content in contents.items():
            print(f"\n📌 {content.title}")
            print(f"설명: {content.description[:100]}...")
            print(f"주요 개념: {', '.join(content.concepts[:3])}...")
