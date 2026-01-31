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
    """02.2주차_알고리즘: 학습 기록 모듈 (한국어)

    이 파일은 깃허브 공개용으로 다음 규칙을 따릅니다:
    - 원본 강의자료/노트북의 전체 텍스트를 포함하지 않습니다.
    - 주차별로 "실습한 내용(What I practiced)", "배운 점(What I learned)", "프로젝트/과제 요약"을 한국어로 상세히 기록합니다.
    - 코드 예제는 교육·설명 목적의 축약된 예시만 포함합니다.
    """

    w = WeekDetail(week="02.2주차_알고리즘")

    # 사용한 주요 파일들(공개용으로 일부만 표기, venv/임시파일 제외)
    w.files = [
        "00.강의자료/lecture01.pdf",
        "00.강의자료/Lecture 2.pdf",
        "01.daily_mission/Day1_daily_mission(문제)_leetcode001.ipynb",
        "02.advanced_mission/Day3_advanced_mission(문제)_leetcode200.ipynb",
        "02.advanced_mission/Day5_advanced_mission(문제)_leetcode-056.ipynb",
    ]

    # 이번 주 주요 개념/기술 스택 요약
    w.tech_stack = [
        "Python 3",
        "자료구조: 리스트, 스택, 큐, 링크드리스트, 트리",
        "알고리즘: 브루트포스, 투포인터, 해시맵, 정렬, 이진 탐색, 분할 정복, 단조 스택",
        "탐색: DFS, BFS",
        "복잡도 분석: 시간복잡도(O), 공간복잡도"
    ]

    # 상세 학습 기록: What I practiced / What I learned / Project summary
    w.learning_paragraphs = [
        (
            "What I practiced: 이번 주에는 알고리즘 문제 풀이의 기초를 반복 학습했습니다. "
            "Two Sum(브루트포스→해시맵), Two Pointers(정렬/부분합), 링크드리스트 관련 문제(중간 노드 찾기, 뒤집기, 사이클 검출), "
            "스택을 이용한 괄호 유효성 검증 및 단조 스택/힙을 이용한 문제들을 연습했습니다. 각 문제에서 먼저 간단한(브루트포스) 구현으로 정답을 확인한 뒤, "
            "적절한 자료구조로 시간 복잡도를 개선하는 연습을 했습니다."
        ),

        (
            "What I learned: 문제 해결의 반복적 패턴을 몸에 익혔습니다. 첫째, 문제를 정확히 이해하고 엣지 케이스를 정의할 것, "
            "둘째, 단순한 구현으로 정답의 정확성을 확보할 것, 셋째, 해시맵이나 투포인터, 단조 스택 등 자료구조를 적용해 성능을 개선할 것. "
            "특히 Two Sum에서는 해시맵을 사용해 한 번의 순회로 해결하는 방법(O(N))을 확인했고, 링크드리스트에서는 포인터 조작의 안전성(다음 노드 임시 저장 등)을 체득했습니다."
        ),

        (
            "Project/Assignment: 과제로는 여러 Daily/Advanced 미션 문제를 풀고, 각 풀이의 시간/공간 복잡도를 정리해 제출했습니다. "
            "제출 전 체크리스트는 (1) 예제와 추가 케이스 실행, (2) 주석·코드 정리, (3) 실행 결과 캡처 및 문서화였습니다. "
            "또한 단조 스택 예제(Temperatures)와 힙 기반 예제(Kth largest)에서 각 방법의 시간복잡도 차이를 비교했습니다."
        ),
    ]

    # 교육용 축약 코드 예제 (설명과 간단 테스트 포함)
    w.code_examples = {}

    w.code_examples['two_sum_hashmap.py'] = '''from typing import List

def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
    """한 번의 순회로 두 수의 합이 target이 되는 인덱스를 반환합니다. 시간복잡도 O(N)."""
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []

# 간단한 테스트
if __name__ == '__main__':
    print(two_sum_hashmap([2,7,11,15], 9))  # [0, 1]
'''

    w.code_examples['two_sum_bruteforce.py'] = '''from typing import List

def two_sum_bruteforce(nums: List[int], target: int):
    """브루트포스 방식: 모든 쌍을 검사합니다. 시간복잡도 O(N^2)."""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

if __name__ == '__main__':
    print(two_sum_bruteforce([3,2,4], 6))  # [1, 2]
'''

    w.code_examples['linkedlist_middle.py'] = '''class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head: Node) -> Node:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 설명: fast가 두 칸씩 이동하므로 slow는 중간 지점에 위치한다.
'''

    return w


def print_detail():
    d = get_detail()
    print("Week:", d.week)
    print("Files:", d.files)
    print("Techs:", d.tech_stack)
    print("\nLearning paragraphs:")
    for p in d.learning_paragraphs:
        print(" -", p)
    print("\nCode example files:")
    for k in d.code_examples.keys():
        print(" -", k)
