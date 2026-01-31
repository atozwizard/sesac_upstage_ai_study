from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class WeekDetail:
    week: str = ""
    files: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)
    learning_paragraphs: List[str] = field(default_factory=list)
    code_examples: Dict[str, str] = field(default_factory=dict)


def get_detail() -> WeekDetail:
    """02.2주차_알고리즘: 상세 학습 기록 (한국어)
    
    알고리즘 기초, 자료구조, 시간복잡도 분석, 실습 문제 해결
    """

    w = WeekDetail(week="02.2주차_알고리즘")

    w.files = [
        "00.강의자료/알고리즘_기초.pdf",
        "00.강의자료/자료구조_완벽가이드.pdf",
        "01.daily_mission/Day1_시간복잡도.ipynb",
        "01.daily_mission/Day2_배열과탐색.ipynb",
        "01.daily_mission/Day3_연결리스트.ipynb",
        "02.advanced_mission/Day4_정렬알고리즘.ipynb",
        "02.advanced_mission/Day5_그래프기초.ipynb",
    ]

    w.tech_stack = [
        "Python 3.9+",
        "자료구조: 배열, 연결 리스트, 스택, 큐, 해시맵, 힙",
        "정렬 알고리즘: 버블 정렬, 선택 정렬, 병합 정렬, 퀵 정렬",
        "탐색 알고리즘: 선형 탐색, 이진 탐색",
        "그래프: BFS, DFS, 다익스트라",
        "시간복잡도: O(1), O(log n), O(n), O(n log n), O(n²)",
    ]

    w.learning_paragraphs = [
        (
            "📅 Day 1: 시간복잡도와 공간복잡도 이해\n"
            "- Big-O 표기법의 개념과 의미\n"
            "- 다양한 시간복잡도 분석 (O(1), O(n), O(n²), O(log n) 등)\n"
            "- 실제 코드에서 시간복잡도 계산하기\n"
            "- 알고리즘 선택의 중요성\n"
            "- 최악, 평균, 최선의 경우 분석"
        ),

        (
            "📅 Day 2: 배열과 탐색 알고리즘\n"
            "- 배열의 특징 (인덱싱, 접근 시간)\n"
            "- Two Sum 문제: 해시맵을 이용한 최적화 (O(n) -> O(1) 접근)\n"
            "- 선형 탐색 vs 이진 탐색 비교\n"
            "- 정렬 배열에서의 이진 탐색 구현\n"
            "- 슬라이딩 윈도우 기법"
        ),

        (
            "📅 Day 3: 연결 리스트와 포인터\n"
            "- 연결 리스트의 구조 (노드, 포인터)\n"
            "- 배열 vs 연결 리스트 성능 비교\n"
            "- 연결 리스트 기본 연산 (삽입, 삭제, 순회)\n"
            "- Two Pointer 기법: 중간값 찾기, 사이클 감지\n"
            "- 연결 리스트 역순 뒤집기"
        ),

        (
            "📅 Day 4: 정렬 알고리즘 심화\n"
            "- 버블 정렬, 선택 정렬, 삽입 정렬 (O(n²))\n"
            "- 병합 정렬 (O(n log n), 안정 정렬)\n"
            "- 퀵 정렬 (O(n log n) 평균, 분할 정복)\n"
            "- 힙 정렬 (O(n log n), 최악도 보장)\n"
            "- 정렬 알고리즘 비교 및 선택 기준"
        ),

        (
            "📅 Day 5: 그래프와 탐색 심화\n"
            "- 그래프 표현법 (인접 행렬, 인접 리스트)\n"
            "- 깊이 우선 탐색 (DFS) 구현\n"
            "- 너비 우선 탐색 (BFS) 구현\n"
            "- 최단 경로: 다익스트라 알고리즘\n"
            "- 최종 프로젝트: 미로 찾기, 경로 최적화"
        ),
    ]

    w.code_examples = {}

    w.code_examples['01_time_complexity.py'] = '''# Day 1: 시간복잡도 분석 예제

# O(1) - 상수 시간
def get_first_element(arr):
    """배열의 첫 번째 원소 접근"""
    return arr[0]

# O(n) - 선형 시간
def linear_search(arr, target):
    """선형 탐색 - 모든 원소 확인"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# O(n²) - 이차 시간
def bubble_sort(arr):
    """버블 정렬 - 중첩 루프"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(log n) - 로그 시간
def binary_search(arr, target):
    """이진 탐색 - 범위를 반으로 줄임"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n log n) - 병합 정렬
def merge_sort(arr):
    """분할 정복을 이용한 정렬"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """두 개의 정렬된 배열을 병합"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 테스트
print("O(log n) 테스트:", binary_search([1, 3, 5, 7, 9], 7))
print("O(n log n) 테스트:", merge_sort([5, 2, 8, 1, 9]))
'''

    w.code_examples['02_two_sum_hashmap.py'] = '''# Day 2: Two Sum 문제 - 해시맵을 이용한 최적화

def two_sum_bruteforce(arr, target):
    """브루트 포스: O(n²) 시간복잡도"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

def two_sum_hashmap(arr, target):
    """해시맵 활용: O(n) 시간복잡도"""
    # 번호: 인덱스 저장
    num_map = {}
    
    for i, num in enumerate(arr):
        # 필요한 보수값 찾기
        complement = target - num
        
        if complement in num_map:
            # 찾았으면 즉시 반환
            return [num_map[complement], i]
        
        # 현재 번호 저장
        num_map[num] = i
    
    return []

def two_sum_sorted(arr, target):
    """정렬 후 투포인터: O(n log n) 시간복잡도"""
    arr = sorted(enumerate(arr), key=lambda x: x[1])
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left][1] + arr[right][1]
        
        if current_sum == target:
            return [arr[left][0], arr[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# 테스트
test_arr = [2, 7, 11, 15]
test_target = 9

print("브루트 포스:", two_sum_bruteforce(test_arr, test_target))  # [0, 1]
print("해시맵:", two_sum_hashmap(test_arr, test_target))          # [0, 1]
print("정렬+포인터:", two_sum_sorted(test_arr, test_target))      # [0, 1]
'''

    w.code_examples['03_linked_list.py'] = '''# Day 3: 연결 리스트와 투 포인터 기법

class Node:
    """연결 리스트의 노드"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    """연결 리스트 클래스"""
    def __init__(self):
        self.head = None
    
    def append(self, val):
        """리스트의 끝에 원소 추가"""
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)
    
    def find_middle(self):
        """투 포인터로 중간값 찾기 (O(n))"""
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.val if slow else None
    
    def has_cycle(self):
        """사이클 감지 (Floyd's Cycle Detection)"""
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def reverse(self):
        """연결 리스트 역순 뒤집기"""
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
        return self.head
    
    def to_list(self):
        """연결 리스트를 파이썬 리스트로 변환"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

# 테스트
ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)

print("원본:", ll.to_list())
print("중간값:", ll.find_middle())

ll.reverse()
print("역순:", ll.to_list())
'''

    w.code_examples['04_sorting_algorithms.py'] = '''# Day 4: 다양한 정렬 알고리즘 비교

def bubble_sort(arr):
    """버블 정렬: O(n²) 시간, O(1) 공간, 안정 정렬"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """퀵 정렬: O(n log n) 평균, O(n²) 최악, O(log n) 공간"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    """힙 정렬: O(n log n) 최악도 보장, O(1) 공간"""
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    
    # 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 정렬
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

# 테스트
test_arr = [64, 34, 25, 12, 22, 11, 90]

print("버블 정렬:", bubble_sort(test_arr.copy()))
print("퀵 정렬:", quick_sort(test_arr.copy()))
print("힙 정렬:", heap_sort(test_arr.copy()))
'''

    w.code_examples['05_graph_traversal.py'] = '''# Day 5: 그래프 탐색 (BFS, DFS, 다익스트라)

from collections import deque, defaultdict

class Graph:
    """그래프 클래스"""
    def __init__(self):
        self.graph = defaultdict(list)
        self.directed = False
    
    def add_edge(self, u, v, weight=1):
        """간선 추가"""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def dfs(self, start):
        """깊이 우선 탐색 (DFS) - 재귀"""
        visited = set()
        result = []
        
        def helper(node):
            visited.add(node)
            result.append(node)
            
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    helper(neighbor)
        
        helper(start)
        return result
    
    def bfs(self, start):
        """너비 우선 탐색 (BFS) - 큐 사용"""
        visited = set([start])
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dijkstra(self, start):
        """다익스트라 알고리즘 - 최단 경로"""
        import heapq
        
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances

# 테스트
g = Graph()
for u, v in [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]:
    g.add_edge(u, v)

print("DFS:", g.dfs('A'))
print("BFS:", g.bfs('A'))

# 가중 그래프
g2 = Graph()
g2.add_edge('A', 'B', 1)
g2.add_edge('A', 'C', 4)
g2.add_edge('B', 'C', 2)
g2.add_edge('B', 'D', 5)
g2.add_edge('C', 'D', 1)

print("최단 경로:", g2.dijkstra('A'))
'''

    return w


def print_detail():
    d = get_detail()
    print(f"Week: {d.week}")
    print(f"Files: {len(d.files)} files")
    print(f"Tech Stack: {len(d.tech_stack)} technologies")
    print(f"Learning Content: {len(d.learning_paragraphs)} days")
    print(f"Code Examples: {len(d.code_examples)} examples")
