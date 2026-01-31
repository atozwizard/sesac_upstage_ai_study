from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class WeekSummary:
    week: str = ""
    files: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)
    raw_texts: Dict[str, str] = field(default_factory=dict)

def get_summary() -> WeekSummary:
    s = WeekSummary(week="02.2주차_알고리즘")
    s.files = ['.ipynb_checkpoints\\ApplicationQuestion-checkpoint.ipynb', '.ipynb_checkpoints\\Day1_advanced_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Day1_daily_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Day2_advanced_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Day2_daily_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Untitled-checkpoint.ipynb', '.ipynb_checkpoints\\자료구조와알고리즘-checkpoint.py', '00.강의자료\\Lecture 10.pdf', '00.강의자료\\Lecture 2.pdf', '00.강의자료\\Lecture 3.pdf', '00.강의자료\\Lecture 4.pdf', '00.강의자료\\Lecture 5.pdf', '00.강의자료\\Lecture 6.pdf', '00.강의자료\\Lecture 7.pdf', '00.강의자료\\Lecture 8.pdf', '00.강의자료\\Lecture 9.pdf', '00.강의자료\\lecture01.pdf', '01.daily_mission\\.ipynb_checkpoints\\Day4_daily_mission(문제)-checkpoint.ipynb', '01.daily_mission\\.ipynb_checkpoints\\Day4_daily_mission(문제)_leetcode215-checkpoint.ipynb', '01.daily_mission\\.ipynb_checkpoints\\Day5_daily_mission(문제)-checkpoint.ipynb', '01.daily_mission\\Day1_daily_mission(문제)_leetcode001.ipynb', '01.daily_mission\\Day2_daily_mission(문제).ipynb', '01.daily_mission\\Day3_daily_mission(문제)_leetcode104.ipynb', '01.daily_mission\\Day4_daily_mission(문제)_leetcode215.ipynb', '01.daily_mission\\Day5_daily_mission(문제).ipynb', '02.2주차_알고리즘_module.py', '02.advanced_mission\\.ipynb_checkpoints\\Day4_advanced_mission(문제)-checkpoint.ipynb', '02.advanced_mission\\.ipynb_checkpoints\\Day5_advanced_mission(문제)_leetcode-056-checkpoint.ipynb', '02.advanced_mission\\Day1_advanced_mission(문제).ipynb', '02.advanced_mission\\Day2_advanced_mission(문제).ipynb', '02.advanced_mission\\Day3_advanced_mission(문제)_leetcode200.ipynb', '02.advanced_mission\\Day4_advanced_mission(문제).ipynb', '02.advanced_mission\\Day5_advanced_mission(문제)_leetcode-056.ipynb', 'ApplicationQuestions1-4.py', 'README_GENERATED.md', 'README_TECHSTACK.md', 'README_TECHSTACK_DRAFT.md', '__pycache__\\02.2주차_알고리즘_module.cpython-313.pyc', 'accomplicationQuestion_5-6.py', 'appicationQuestion9.py', 'applicationQuestion_lec8.py', 'applicationquestion10.py', 'extracted_content\\ApplicationQuestion-checkpoint.ipynb.txt', 'extracted_content\\Day1_advanced_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day1_advanced_mission(문제).ipynb.txt', 'extracted_content\\Day1_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day1_daily_mission(문제)_leetcode001.ipynb.txt', 'extracted_content\\Day2_advanced_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day2_advanced_mission(문제).ipynb.txt', 'extracted_content\\Day2_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day2_daily_mission(문제).ipynb.txt', 'extracted_content\\Day3_advanced_mission(문제)_leetcode200.ipynb.txt', 'extracted_content\\Day3_daily_mission(문제)_leetcode104.ipynb.txt', 'extracted_content\\Day4_advanced_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day4_advanced_mission(문제).ipynb.txt', 'extracted_content\\Day4_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day4_daily_mission(문제)_leetcode215-checkpoint.ipynb.txt', 'extracted_content\\Day4_daily_mission(문제)_leetcode215.ipynb.txt', 'extracted_content\\Day5_advanced_mission(문제)_leetcode-056-checkpoint.ipynb.txt', 'extracted_content\\Day5_advanced_mission(문제)_leetcode-056.ipynb.txt', 'extracted_content\\Day5_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day5_daily_mission(문제).ipynb.txt', 'extracted_content\\Lecture 10.txt', 'extracted_content\\Lecture 2.txt', 'extracted_content\\Lecture 3.txt', 'extracted_content\\Lecture 4.txt', 'extracted_content\\Lecture 5.txt', 'extracted_content\\Lecture 6.txt', 'extracted_content\\Lecture 7.txt', 'extracted_content\\Lecture 8.txt', 'extracted_content\\Lecture 9.txt', 'extracted_content\\Untitled-checkpoint.ipynb.txt', 'extracted_content\\extracted_content.json', 'extracted_content\\lecture01.txt', 'extracted_content\\강의마무리_코랩 세션_Wrap Up 리포트.txt', '강의마무리_코랩 세션_Wrap Up 리포트.pdf', '자료구조와알고리즘.py']
    s.tech_stack = []
    s.raw_texts = {}
    s.raw_texts['ApplicationQuestion-checkpoint.ipynb.txt'] = """02
    1.middle of a given linked list
    #중간값 찾기
    #투 포인터, slow pointer 한번에 한칸씩 이동, fast pointer 한번에 두칸씩 이동
    #fast pointer가 리스트의 끝(none)에 도달 했을 때, slow pointer는 정확히 리스트의 중간에 위치.     

        class Node():
            def __init__(self, val = 0, next = None): \"\"\"val은 value데이터=0 인것은 노드를 생성할 때 실수로 데이터를 넣지 않더라도,
                                                        프로그램이 멈추지 않고 숫자 0을 기본 데이터로 가지게 한다. 주로 숫자데이터를 다룰 것이라는 점도 암시.
                                                        next=None은 이 노드가 기차의 마지막 칸임을 나타내는 중요한 신호.
                                                        처음 생성된 노드는 어디에도 연결되어있지 않으므로 아무것도 가리키지 않는 다는 뜻의 None이
                                                        가장 적절한 초기값이다.\"\"\"
                self.val = val
                self.next = next
                
            def findmiddle(head:Node) -> Node:
                slow = head
                fast = head  #0이 아닌 head로 객체지정하는 것은 LinkedList 의 특성때문.
                            \"\"\"노드(데이터)들이 메모리 여기저기에 흩어져 있다. 
                            각 노드는 오직 자신이 가진 next포인터를 통해서만 다음 노드가 어디있는지 알수 있다.
                            따라서, 컴퓨터는 0의 위치로 가달라고 하면 알아듣지 못함. 대신
                            기차의 맨 앞칸(head)주소를 줄테니 여기서부터 시작해 라고 알려줘야 함
                            head는 첫번째 노드 객체 그 자체. slow=0 이라 한다면 노드가 아니라 숫자0 이 됨.
                            숫자 0에는 .next라는 속성이 없기 때문에 에러\"\"\"
                
                while fast and fast.next:
                    slow = slow.next        #1칸이동
                    fast = fast.next.next   #2칸이동
                
                return slow  #slow가 가리키는 곳이 중간값

2.reverse a given linked list
    #세 개의 포인터
    \"\"\"링크드리스트를 뒤집으려면 현재 노드뿐만 아니라, 이전 노드와
    다음 노드의 정보가 동시에 필요함, 이전 현재 다음 포인터.prev, curr, next_node\"\"\"
    # 기차 칸들의 연결고리를 하나씩 끊어서 반대방향으로 다시 잇는 작업

        class Node():
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
                
            def reverselist(head:Node) -> Node:
                prev = None
                curr = head
                
                while curr:
                    next_node = curr.next \"\"\"현재 노드의 다음노드 위치를 next_node라는 변수에 잠시 저장
                                            바로 다음 줄에서 현재노드의 다음을 이전 노드로 바꾸면, 다음 칸 포인터를 잃어버림\"\"\"
                    curr.next = prev #현재노드 다음을 뒤로 돌림
                    
                    prev = curr #현재노드가 이전노드가 됨
                    curr = next_node #다음 칸으로 넘어가서 다음 작업을 준비
                    
                return prev

 3.detect cycle,circular linked
    #언젠가는 만난다, 투 포인터. 순환한다면 fast pointer는 한 바퀴를 앞질러 slow pointer를 따라잡아 만나게 된다.
    

        class Node():
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
                
            def cycle(head: Node) -> bool:
                if not head or not head.next:  \"\"\"not head: 연결 리스트에 노드가 하나도 없는상태. 
                                                비교할 대상 자체가 없으므로 당연히 순환이 없다.
                                                not head.next: 첫칸 다음이없다, 노드가 하나뿐인 상태.
                                                자기 자신에게 다시 돌아오는 특수한 경우가 아니라면, 노드가 하나일때는
                                                순환이 만들어지지 않는다
                                                이런 상황들을 미리 걸러내는 예외처리 Guard Clause\"\"\"
                    return False
                
                slow = head  #출발선 정렬
                fast = head
                
                while fast and fast.next:
                    slow = slow.next #1칸이동
                    fast = fast.next.next #2칸이동
                    
                    if slow == fast: #둘이 만나면, 사이클 있다!
                        return True
                
                return False #fast가 끝에 도달하면 사이클 없음

03 괄호 balance
    use stack to check if a string with parantheses is well-formed
    \"(3+4)*(2+5)\" is well-formed
    \"((2*2)*3+1)\" is not well-formed
    \")(2+2\" is not well-formed
    what if we have more than one types of parentheses?
    \"{(2+1)*(3+2)-22}*7\" is well-formed
    \"{(7+2}*3)\" is not well-formed

class Solution:
            def isValid(self, s: str) -> bool:

                # TODO: 여기에 스택 기반 알고리즘을 구현하세요.

                stack = [] #괄호 쌓을 리스트
                pair = { \")\" : \"(\" , \"}\" : \"{\", \"]\" : \"[\" }  #짝맞출 딕셔너리

                for x in s:   #s를 하나씩 순회해
                    
                    if x in pair:       #   - 닫힌 괄호일 때 pair안에 있으면
                            
                        if not stack:    #   - 스택이 비어있는 경우 False
                            return False  #pop하기 전에 비어있는지 먼저 확인해야한다

                        top = stack.pop()     #stack에 쌓은 마지막것을 꺼내, top이라 하자
                        if top != pair[x]:  #꺼낸 top이, pair의 짝과 안맞으면
                            return False  #False
                            
                    else: #   - 닫힌 괄호가 아닐 때
                        if x in \"({[\":
                            stack.append(x) #  stack에 append 쌓아놔

                    #   - 반복이 끝난 뒤 스택이 비어 있는지 확인
                return len(stack) == 0

            raise NotImplementedError


"""
    s.raw_texts['Day1_advanced_mission(문제)-checkpoint.ipynb.txt'] = """# Day 1. 배열과 알고리즘으로 문제 해결하기 – 심화 미션

이 노트북은 **in-place 배열 조작**과 **two-pointer 전략**을 연습하기 위한 심화 과제용입니다.

## 🎯 학습 목표
- 추가 메모리를 거의 사용하지 않는 **in-place 알고리즘** 개념을 이해한다.
- **two-pointer 패턴(write/read 포인터 등)** 을 실제 문제에 적용해본다.
- 간단한 최적화를 통해 전체 연산 횟수를 줄이는 아이디어를 연습한다.

---
## 오늘의 심화 문제: LeetCode #283 – Move Zeroes

정수 배열 `nums`가 주어질 때,
배열 안의 모든 `0`을 **배열의 뒤쪽으로 이동**시키되,
`0이 아닌 원소들의 상대적 순서는 유지`하도록 배열을 재배치하세요.

이 작업은 **in-place**, 즉 **새로운 배열을 생성하지 않고** 수행해야 합니다.

### 예시
1. 입력: `nums = [0, 1, 0, 3, 12]` → 출력: `[1, 3, 12, 0, 0]`
2. 입력: `nums = [0]` → 출력: `[0]`

### 제한 조건
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

### Follow-up
- 전체 연산(스왑/대입)의 횟수를 어떻게 하면 최소화할 수 있을까요?


## 🛠️ Prerequisites
본 미션에서는 다음과 같은 Python 표준 라이브러리를 사용합니다.
* **`from typing import List`**: `nums` 배열의 타입을 명시하기 위해 사용합니다.
* 별도의 외장 라이브러리 설치 없이 기본 Python 환경에서 실행 가능합니다.

---
## Step 1. Two-pointer로 `moveZeroes` 구현하기

### 아이디어 힌트
- 하나의 포인터는 **현재 읽고 있는 위치(read)** 를 가리킵니다.
- 다른 포인터는 **0이 아닌 값을 쓸 위치(write)** 를 가리킵니다.
- `nums`를 앞에서부터 순회하면서, 0이 아닌 값을 발견하면 `write` 위치에 옮기고 `write`를 한 칸 증가시킵니다.
- 마지막에 `write` 뒤에 남은 위치들을 모두 0으로 채웁니다.

아래 템플릿을 활용해 코드를 완성해 보세요.

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
      \"\"\"nums 리스트 안의 모든 0을 뒤로 보내고,
      0이 아닌 원소들의 상대적 순서를 유지하도록 in-place로 수정합니다.

      시간복잡도 & 아이디어:
          TODO: 사용한 two-pointer 전략과 시간복잡도(O(N))를 설명해 보세요.
      \"\"\"
      # TODO: two-pointer(write/read) 방식으로 구현해 보세요.
      #   - 추가 리스트를 만들지 말고(nums를 그대로 수정) in-place로 해결해야 합니다.
      #   - 필요하다면 포인터 변수(write, read)를 두고, 반복문을 한 번만 도는 구현을 시도해 보세요.



### ✅ 테스트 코드
아래 셀을 실행해 다양한 케이스에서 함수가 잘 동작하는지 확인해 보세요.
테스트를 **스스로 1~2개 더 추가**하면 더 좋습니다!

def test_move_zeroes(nums):
    print(f\"입력  before: {nums}\")
    Solution().moveZeroes(nums)
    print(f\"출력  after : {nums}\\n\")

test_cases = [
    [0, 1, 0, 3, 12],
    [0],
    [1, 2, 3],
    [0, 0, 0, 1],
]

for case in test_cases:
    test_move_zeroes(case)


---
## Step 2. 연산 횟수와 최적화 아이디어

아래에 본인이 구현한 알고리즘의 **시간복잡도와 연산 패턴**을 정리해 보세요.

- 우리는 리스트를 몇 번 순회했나요?
- 불필요한 스왑/대입 연산을 줄일 수 있는 방법은 무엇인가요?
- 두 포인터를 활용함으로써 **전체 복잡도를 어떻게 유지(O(N))** 했는지 설명해 보세요.

---

### ✏️ 정리 (학생 작성)

- 내가 사용한 포인터의 역할:
  -
- 전체 시간복잡도와 그 이유:
  -
- 연산 횟수를 더 줄일 수 있는 아이디어가 있다면:
  -


---
## 제출 전 체크리스트 (심화)
- [ ] `moveZeroes`가 **in-place**로 동작한다. (새 리스트를 만들지 않았다)
- [ ] 두 포인터 아이디어를 코드에 반영했다.
- [ ] 최소 3개 이상의 테스트 케이스를 실행해 보았다.
- [ ] 시간복잡도와 알고리즘 아이디어를 말/글로 설명할 수 있다.

수고 많았어요! 👏 배열 알고리즘과 two-pointer 패턴은 이후에도 계속 반복해서 등장합니다.


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day1_advanced_mission(문제).ipynb.txt'] = """# Day 1. 배열과 알고리즘으로 문제 해결하기 – 심화 미션

이 노트북은 **in-place 배열 조작**과 **two-pointer 전략**을 연습하기 위한 심화 과제용입니다.

## 🎯 학습 목표
- 추가 메모리를 거의 사용하지 않는 **in-place 알고리즘** 개념을 이해한다.
- **two-pointer 패턴(write/read 포인터 등)** 을 실제 문제에 적용해본다.
- 간단한 최적화를 통해 전체 연산 횟수를 줄이는 아이디어를 연습한다.

---
## 오늘의 심화 문제: LeetCode #283 – Move Zeroes

정수 배열 `nums`가 주어질 때,
배열 안의 모든 `0`을 **배열의 뒤쪽으로 이동**시키되,
`0이 아닌 원소들의 상대적 순서는 유지`하도록 배열을 재배치하세요.

이 작업은 **in-place**, 즉 **새로운 배열을 생성하지 않고** 수행해야 합니다.

### 예시
1. 입력: `nums = [0, 1, 0, 3, 12]` → 출력: `[1, 3, 12, 0, 0]`
2. 입력: `nums = [0]` → 출력: `[0]`

### 제한 조건
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

### Follow-up
- 전체 연산(스왑/대입)의 횟수를 어떻게 하면 최소화할 수 있을까요?


## 🛠️ Prerequisites
본 미션에서는 다음과 같은 Python 표준 라이브러리를 사용합니다.
* **`from typing import List`**: `nums` 배열의 타입을 명시하기 위해 사용합니다.
* 별도의 외장 라이브러리 설치 없이 기본 Python 환경에서 실행 가능합니다.

---
## Step 1. Two-pointer로 `moveZeroes` 구현하기

### 아이디어 힌트
- 하나의 포인터는 **현재 읽고 있는 위치(read)** 를 가리킵니다.
- 다른 포인터는 **0이 아닌 값을 쓸 위치(write)** 를 가리킵니다.
- `nums`를 앞에서부터 순회하면서, 0이 아닌 값을 발견하면 `write` 위치에 옮기고 `write`를 한 칸 증가시킵니다.
- 마지막에 `write` 뒤에 남은 위치들을 모두 0으로 채웁니다.

아래 템플릿을 활용해 코드를 완성해 보세요.

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
      
      write = 0 #쓰기 위치 0 시-작

      for read in range(len(nums)): #읽으러 nums 의 인덱스 길이만큼 순회할 것이다
          if nums[read] != 0: #읽은 위치의 값이 0이 아니면!
              nums[write], nums[read] = nums[read], nums[write] #쓰기위치의 값과 읽기위치의 값을 바꿔라
              write += 1  #그리고나서 읽기는 한 칸 가,, 0이면 어떻게 됨, 그냥가는가?
              #응, 지나감. 조건문 때문에 0이면 아무런 일도 하지 않고, 다음순서로 넘어간다, 읽기 1증가
              #이때, 쓰기는 가만히 있는데, 이 자리가, 나중에 0이 아닌 수를 받아줄 자리가 된다
              #그럼 앞에 모인 수들의 순서는?
              #앞에서부터 차례대로, 먼저 발견한 순서대로 갖다놓기 때문에 먼저 발견된 놈이 무조건 더 앞에 자리한다.
              # 애초 뒤죽박죽이면 이렇게 해도 뒤죽박죽아닌가.
              # 맞아.이건 전체리스트를 크기순으로 정렬-sorting 하는게 아니야
              # 이 알고리즘은 0만 골라서 뒤로 보내고, 나머지 숫자들은 원래순서 그대로 유지해
              # 원본 배열에서 0이 아닌 애들끼리 누가 더 앞에 있었냐 하는 \"상대적<순서>\"를 따지는 거
      \"\"\"nums 리스트 안의 모든 0을 뒤로 보내고,
      0이 아닌 원소들의 상대적 순서를 유지하도록 in-place로 수정합니다.

      예를들면, 게시글 목록에서 '광고'나 '삭제된글'은 맨 뒤로 보내주세요, 하지만 남은 게시글들은
      원래 올린 시간순서(원본순서) 그대로 보여줘야 합니다, 같은 경우 투 포인터 전략을 써야한다.

      딱 한 번 순회 하지만! 리스트의 길이에 따라 시간도 늘어나니까! 시간복잡도는 N이다.
      데이터 개수에 비례해서 작업량이 늘어나는 선형 시간(linear time)구조인 것.
      
      브루트포스의 이중 반복문을 한다면, 0을 하나 찾을 때마다 나머지 숫자들을 앞으로 당기고, 
      다시 시작해야 하므로 이것도 N*N 이었겠다.

      그리고, 한 번의 순회동안 본 것을 기록해두지 않았고, 기존리스트의 자리만 맞바꾸었다.
      공간복잡도는 리스트의 길이에 상관없는 부분이다! 다만 \"이 알고리즘을 풀기위해 추가로 빌려온
      빈 메모리가 얼마나 큰가?\" 이다.
      
      리스트가 10개든 100개든, read 와 write 두개의 변수만 추가로 사용했잖아.
      리스트가 아무리 커져도 새로 만드는 변수의 갯수는 늘어나지 않는다.
      ---데이터 양이 아무리 많아져도 내가 쓰는 추가메모리는 항상 일정하다 는 뜻에서 O(1) 인것.

      정리를 해보면, 
      추가메모리를 안쓰는 알고리즘이지만 O(1), 모든 숫자를 한 번씩은 훑어야 하므로,
      시간은 데이터 길이에 비례해서 든다 O(N).

      시간복잡도 O(N), 공간복잡도 O(1)


      시간복잡도 & 아이디어:
          TODO: 사용한 two-pointer 전략과 시간복잡도(O(N))를 설명해 보세요.
      \"\"\"
      # TODO: two-pointer(write/read) 방식으로 구현해 보세요.
      #   - 추가 리스트를 만들지 말고(nums를 그대로 수정) in-place로 해결해야 합니다.
      #   - 필요하다면 포인터 변수(write, read)를 두고, 반복문을 한 번만 도는 구현을 시도해 보세요.



### ✅ 테스트 코드
아래 셀을 실행해 다양한 케이스에서 함수가 잘 동작하는지 확인해 보세요.
테스트를 **스스로 1~2개 더 추가**하면 더 좋습니다!

def test_move_zeroes(nums):
    print(f\"입력  before: {nums}\")
    Solution().moveZeroes(nums)
    print(f\"출력  after : {nums}\\n\")

test_cases = [
    [0, 1, 0, 3, 12],
    [0],
    [1, 2, 3],
    [0, 0, 0, 1],
]

for case in test_cases:
    test_move_zeroes(case)



test_cases2 = [
    [5, 1, 0, 3, 12, 2, 0, 0, 0],
    [0, 100, 20, 0, 0, 2764],
    [1, 2, 3, 0, 0, 3, 2, 1],
    [0, 0, 0, 1],
]

for case2 in test_cases2:
    test_move_zeroes(case2)


---
## Step 2. 연산 횟수와 최적화 아이디어

아래에 본인이 구현한 알고리즘의 **시간복잡도와 연산 패턴**을 정리해 보세요.

- 우리는 리스트를 몇 번 순회했나요?
- 불필요한 스왑/대입 연산을 줄일 수 있는 방법은 무엇인가요?
- 두 포인터를 활용함으로써 **전체 복잡도를 어떻게 유지(O(N))** 했는지 설명해 보세요.

---

### ✏️ 정리 (학생 작성)

- 내가 사용한 포인터의 역할 - 전체 시간복잡도와 그 이유:
  -  write = 0 #쓰기 위치 0 시-작

      for read in range(len(nums)): #읽으러 nums 의 인덱스 길이만큼 순회할 것이다
          if nums[read] != 0: #읽은 위치의 값이 0이 아니면!
              nums[write], nums[read] = nums[read], nums[write] #쓰기위치의 값과 읽기위치의 값을 바꿔라
              write += 1  #그리고나서 읽기는 한 칸 가,, 0이면 어떻게 됨, 그냥가는가?
              #응, 지나감. 조건문 때문에 0이면 아무런 일도 하지 않고, 다음순서로 넘어간다, 읽기 1증가
              #이때, 쓰기는 가만히 있는데, 이 자리가, 나중에 0이 아닌 수를 받아줄 자리가 된다
              #그럼 앞에 모인 수들의 순서는?
              #앞에서부터 차례대로, 먼저 발견한 순서대로 갖다놓기 때문에 먼저 발견된 놈이 무조건 더 앞에 자리한다.
              # 애초 뒤죽박죽이면 이렇게 해도 뒤죽박죽아닌가.
              # 맞아.이건 전체리스트를 크기순으로 정렬-sorting 하는게 아니야
              # 이 알고리즘은 0만 골라서 뒤로 보내고, 나머지 숫자들은 원래순서 그대로 유지해
              # 원본 배열에서 0이 아닌 애들끼리 누가 더 앞에 있었냐 하는 \"상대적<순서>\"를 따지는 거
      \"\"\"nums 리스트 안의 모든 0을 뒤로 보내고,
      0이 아닌 원소들의 상대적 순서를 유지하도록 in-place로 수정합니다.

      예를들면, 게시글 목록에서 '광고'나 '삭제된글'은 맨 뒤로 보내주세요, 하지만 남은 게시글들은
      원래 올린 시간순서(원본순서) 그대로 보여줘야 합니다, 같은 경우 투 포인터 전략을 써야한다.

      딱 한 번 순회 하지만! 리스트의 길이에 따라 시간도 늘어나니까! 시간복잡도는 N이다.
      데이터 개수에 비례해서 작업량이 늘어나는 선형 시간(linear time)구조인 것.
      
      브루트포스의 이중 반복문을 한다면, 0을 하나 찾을 때마다 나머지 숫자들을 앞으로 당기고, 
      다시 시작해야 하므로 이것도 N*N 이었겠다.

      그리고, 한 번의 순회동안 본 것을 기록해두지 않았고, 기존리스트의 자리만 맞바꾸었다.
      공간복잡도는 리스트의 길이에 상관없는 부분이다! 다만 \"이 알고리즘을 풀기위해 추가로 빌려온
      빈 메모리가 얼마나 큰가?\" 이다.
      
      리스트가 10개든 100개든, read 와 write 두개의 변수만 추가로 사용했잖아.
      리스트가 아무리 커져도 새로 만드는 변수의 갯수는 늘어나지 않는다.
      ---데이터 양이 아무리 많아져도 내가 쓰는 추가메모리는 항상 일정하다 는 뜻에서 O(1) 인것.

      정리를 해보면, 
      추가메모리를 안쓰는 알고리즘이지만 O(1), 모든 숫자를 한 번씩은 훑어야 하므로,
      시간은 데이터 길이에 비례해서 든다 O(N).

      시간복잡도 O(N), 공간복잡도 O(1)

     

- 연산 횟수를 더 줄일 수 있는 아이디어가 있다면:
  -해시맵 방식으로 이걸 풀면 어떨까,

  해시맵 방식은 '값'을 가지고 '인덱스'를 찾거나 '개수'를 셀 때 쓴댄다. 근데 만약 억지로 해시맵으로 0을 뒤로 보낸다면,

  일단, 리스트 1번 순회하면서 0이 아닌 숫자의 원래 순서를 기록하고

  0이 몇개인지 세고,

  해시맵에 기록한 숫자들을 순서대로 채워넣고,

  세어놓은 0의 갯수만큼 0을 채워넣는다.

  이렇게 하면, 새로 리스트를 만드는 것과 다름이 없네.

시간복잡도는 리스트만큼이니 O(N)이고, 공간복잡도 또한 리스트만큼이니 O(N)이다.
굳이 안써도 될 메모리를 써야 하겠다. 같은 크기만큼.
리스트가 크면 클 수록 쓸데없이 써야할 메모리가 커지는.

결론, 연산 횟수를 줄이려면, 무얼 해야하는지 알아야, 그에 딱 맞는 효율적인 알고리즘을 써야 하겠다. 모르면 물어보자.



---
## 제출 전 체크리스트 (심화)
- [ ] `moveZeroes`가 **in-place**로 동작한다. (새 리스트를 만들지 않았다)
- [ ] 두 포인터 아이디어를 코드에 반영했다.
- [ ] 최소 3개 이상의 테스트 케이스를 실행해 보았다.
- [ ] 시간복잡도와 알고리즘 아이디어를 말/글로 설명할 수 있다.

수고 많았어요! 👏 배열 알고리즘과 two-pointer 패턴은 이후에도 계속 반복해서 등장합니다.


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day1_daily_mission(문제)-checkpoint.ipynb.txt'] = """# Day 1. 배열과 알고리즘으로 문제 해결하기 – 데일리 미션

이 노트북은 **배열과 기초 알고리즘 설계**를 연습하기 위한 데일리 미션용입니다.

## 🎯 학습 목표
- 배열의 인덱스 기반 접근 방식과 메모리 구조를 이해한다.
- 브루트 포스(Brute Force)와 해시맵(Hash Map) 알고리즘의 **시간복잡도 차이**를 체험한다.
- 같은 문제를 두 가지 방식으로 풀어보고, 어떤 상황에서 더 나은 방법을 선택해야 하는지 정리한다.

---
## 오늘의 문제: LeetCode #1 – Two Sum

정수 배열 `nums`와 정수 `target`이 주어질 때,
배열에서 **합이 `target`이 되는 서로 다른 두 수의 인덱스**를 반환하세요.

### 조건
- 각 입력에는 **정확히 하나의 해**만 존재합니다.
- 같은 원소를 두 번 사용할 수 없습니다.
- 반환 순서는 상관 없습니다.

### 예시
1. `nums = [2, 7, 11, 15]`, `target = 9` → 출력: `[0, 1]`
2. `nums = [3, 2, 4]`, `target = 6` → 출력: `[1, 2]`
3. `nums = [3, 3]`, `target = 6` → 출력: `[0, 1]`

### 제한 조건
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **단 하나의 정답만 존재**

---
아래 Step 1 → Step 3 순서대로 문제를 해결한 뒤, 마지막에 정리까지 완료해 주세요.

## 🛠️ Prerequisites
본 미션에서는 다음과 같은 Python 표준 라이브러리를 사용합니다.
* **`from typing import List`**: `nums` 배열의 타입을 명시하기 위해 사용합니다.
* 별도의 외장 라이브러리 설치 없이 기본 Python 환경에서 실행 가능합니다.

## Step 1. Brute Force로 Two Sum 풀어보기

가장 직관적인 방법은 **모든 쌍 `(i, j)`를 직접 비교**하는 것입니다.

### 요구 사항
- 이중 반복문을 사용해 `nums[i] + nums[j] == target` 인 쌍을 찾으세요.
- 정답이 되는 인덱스 두 개를 리스트로 반환하세요. (예: `[i, j]`)
- **시간복잡도 분석**: 왜 이 알고리즘이 `O(N^2)` 인지, 함수의 docstring 또는 아래 마크다운에 적어보세요.

from typing import List

def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    \"\"\"Two Sum 문제를 브루트 포스 방식으로 해결합니다.

    시간복잡도:
        TODO: 왜 이 알고리즘의 시간복잡도가 O(N^2)인지 설명을 적어보세요.
    \"\"\"
    # TODO: 이중 for 문을 사용해 모든 (i, j) 쌍을 확인하고,
    #       합이 target이 되는 인덱스를 찾아 반환하세요.
    #       정답이 하나만 존재한다고 가정해도 됩니다.
    raise NotImplementedError


### ✅ 테스트 코드 (수정하지 말고, 위 함수를 구현한 뒤 실행해 보세요)

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]

for nums, target, expected in test_cases:
    result = two_sum_bruteforce(nums, target)
    print(f\"nums={nums}, target={target} → result={result}, expected={expected}\")


---
## Step 2. Hash Map을 이용해 O(N)으로 개선하기

이번에는 **dictionary(해시맵)** 를 사용해 시간복잡도를 `O(N)`으로 줄여봅니다.

### 아이디어 힌트
- 리스트를 앞에서부터 순회하면서, 현재 값 `num`에 대해 **필요한 값** `target - num` 을 계산합니다.
- 그 값이 이미 dictionary 안에 있다면, 두 인덱스를 바로 반환할 수 있습니다.
- 없다면, 현재 값과 인덱스를 dictionary에 저장합니다.

### 요구 사항
- dictionary를 사용해 **한 번의 순회**만으로 풀이해 보세요.
- 함수 안에 시간복잡도(`O(N)`)를 명시하고, Brute Force 방식과 무엇이 다른지 짧게 적어보세요.

def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
    \"\"\"Two Sum 문제를 해시맵 방식으로 해결합니다.

    시간복잡도:
        TODO: 왜 이 알고리즘의 시간복잡도가 O(N)인지 설명을 적어보세요.
    \"\"\"
    # TODO: dict를 사용하여, 한 번의 순회로 정답을 찾는 코드를 작성해 보세요.
    # 예시 아이디어:
    #   - seen = {}
    #   - for i, num in enumerate(nums):
    #         필요한 값 = target - num
    #         필요한 값이 seen에 있는지 확인
    #         없다면 현재 값과 인덱스를 seen에 저장
    raise NotImplementedError


### ✅ 테스트 코드 (Step 1과 동일한 테스트 케이스를 사용합니다)

for nums, target, expected in test_cases:
    result = two_sum_hashmap(nums, target)
    print(f\"nums={nums}, target={target} → result={result}, expected={expected}\")


---
## Step 3. Brute Force vs Hash Map 비교 정리

아래 마크다운 셀에 두 방식의 차이점을 정리해 보세요. (키워드만이 아니라 문장으로 설명해보면 좋습니다.)

### 비교 관점
- 접근 방식 차이 (어떻게 문제를 바라보는가?)
- 시간복잡도 비교 (`O(N^2)` vs `O(N)`)
- 메모리 사용량 (추가 자료구조 사용 여부)
- 실전에서 어떤 상황에서 어떤 방식을 선택할지

---
아래 셀을 직접 수정해서 본인의 정리를 작성하세요.

### ✏️ 정리 (학생 작성)

- Brute Force 방식:
  -
- Hash Map 방식:
  -
- 두 방식의 공통점 & 차이점:
  - 시간복잡도:
  - 메모리 사용:
  - 구현 난이도:
  - 실제로 내가 쓴다면?


---
## Step 4. 제출 전 체크리스트
- [ ] Brute Force 코드가 정상 동작한다.
- [ ] Hash Map 코드가 정상 동작한다.
- [ ] 두 방식의 시간복잡도와 차이에 대한 나만의 설명을 적었다.
- [ ] 예시 테스트 케이스 결과가 문제 설명과 일치한다.
- [ ] (과제용) 실행 결과를 캡처해 별도 제출 또는 첨부 준비를 했다.

수고하셨습니다! 😄


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day1_daily_mission(문제)_leetcode001.ipynb.txt'] = """# Day 1. 배열과 알고리즘으로 문제 해결하기 – 데일리 미션

이 노트북은 **배열과 기초 알고리즘 설계**를 연습하기 위한 데일리 미션용입니다.

## 🎯 학습 목표
- 배열의 인덱스 기반 접근 방식과 메모리 구조를 이해한다.
- 브루트 포스(Brute Force)와 해시맵(Hash Map) 알고리즘의 **시간복잡도 차이**를 체험한다.
- 같은 문제를 두 가지 방식으로 풀어보고, 어떤 상황에서 더 나은 방법을 선택해야 하는지 정리한다.

---
## 오늘의 문제: LeetCode #1 – Two Sum

정수 배열 `nums`와 정수 `target`이 주어질 때,
배열에서 **합이 `target`이 되는 서로 다른 두 수의 인덱스**를 반환하세요.

### 조건
- 각 입력에는 **정확히 하나의 해**만 존재합니다.
- 같은 원소를 두 번 사용할 수 없습니다.
- 반환 순서는 상관 없습니다.

### 예시
1. `nums = [2, 7, 11, 15]`, `target = 9` → 출력: `[0, 1]`
2. `nums = [3, 2, 4]`, `target = 6` → 출력: `[1, 2]`
3. `nums = [3, 3]`, `target = 6` → 출력: `[0, 1]`

### 제한 조건
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **단 하나의 정답만 존재**

---
아래 Step 1 → Step 3 순서대로 문제를 해결한 뒤, 마지막에 정리까지 완료해 주세요.

## 🛠️ Prerequisites
본 미션에서는 다음과 같은 Python 표준 라이브러리를 사용합니다.
* **`from typing import List`**: `nums` 배열의 타입을 명시하기 위해 사용합니다.
* 별도의 외장 라이브러리 설치 없이 기본 Python 환경에서 실행 가능합니다.

## Step 1. Brute Force로 Two Sum 풀어보기

가장 직관적인 방법은 **모든 쌍 `(i, j)`를 직접 비교**하는 것입니다.

### 요구 사항
- 이중 반복문을 사용해 `nums[i] + nums[j] == target` 인 쌍을 찾으세요.
- 정답이 되는 인덱스 두 개를 리스트로 반환하세요. (예: `[i, j]`)
- **시간복잡도 분석**: 왜 이 알고리즘이 `O(N^2)` 인지, 함수의 docstring 또는 아래 마크다운에 적어보세요.

from typing import List

def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    \"\"\"Two Sum 문제를 브루트 포스 방식으로 해결합니다.

    시간복잡도: #전체를 비교하기위해 인풋 n개를 n번만큼 n회 비교하니까 시간복잡도가 O(N^2)
        TODO: 왜 이 알고리즘의 시간복잡도가 O(N^2)인지 설명을 적어보세요.
    \"\"\"

    # TODO: 이중 for 문을 사용해 모든 (i, j) 쌍을 확인하고,
    #       합이 target이 되는 인덱스를 찾아 반환하세요.
    #       정답이 하나만 존재한다고 가정해도 됩니다.
    
    for i in range(len(nums)):  # 첫번째 인덱스 숫자
        for j in range(i + 1, len(nums)): # 두번째 인덱스 숫자
            if nums[i] + nums[j] == target:
                return(nums[i],nums[j])   #인덱스 반환받아야하니까 return함수 // 출력이 아니라 반환하세요라고함

    #전체를 비교하기위해 인풋 n개를 n번만큼 n회 비교하니까 시간복잡도가 O(N^2)
    raise NotImplementedError
    



### ✅ 테스트 코드 (수정하지 말고, 위 함수를 구현한 뒤 실행해 보세요)

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]

for nums, target, expected in test_cases:
    result = two_sum_bruteforce(nums, target)
    print(f\"nums={nums}, target={target} → result={result}, expected={expected}\")


---
## Step 2. Hash Map을 이용해 O(N)으로 개선하기

이번에는 **dictionary(해시맵)** 를 사용해 시간복잡도를 `O(N)`으로 줄여봅니다.

### 아이디어 힌트
- 리스트를 앞에서부터 순회하면서, 현재 값 `num`에 대해 **필요한 값** `target - num` 을 계산합니다.
- 그 값이 이미 dictionary 안에 있다면, 두 인덱스를 바로 반환할 수 있습니다.
- 없다면, 현재 값과 인덱스를 dictionary에 저장합니다.

### 요구 사항
- dictionary를 사용해 **한 번의 순회**만으로 풀이해 보세요.
- 함수 안에 시간복잡도(`O(N)`)를 명시하고, Brute Force 방식과 무엇이 다른지 짧게 적어보세요.

def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
    \"\"\"Two Sum 문제를 해시맵 방식으로 해결합니다.

    시간복잡도: 리스트를 n개만큼 한번씩만 순회하면서 값을 찾으니 O(N)
        TODO: 왜 이 알고리즘의 시간복잡도가 O(N)인지 설명을 적어보세요.
    \"\"\"
    # TODO: dict를 사용하여, 한 번의 순회로 정답을 찾는 코드를 작성해 보세요.
    # 예시 아이디어:
    #   - seen = {}
    #   - for i, num in enumerate(nums):
    #         need필요한 값 = target - num
    #         need필요한 값이 seen에 있는지 확인 if need in seen :
    #         없다면 현재 값과 인덱스를 seen에 저장 append?, return [seen[need]]
    
    seen = {} # 
    
    for i , num in enumerate(nums): #enumerate로 인덱스와 값을 동시에 순회,
        need = target - num
        if need in seen: #need가 seen에 있는지 확인,있으면
            return [seen[need],i] #있는 그 값의 인덱스, 인덱스 내놔
        seen[num] = i  #없으면 seen에 i인덱스에 need 구할때 넣은 num값을 넣어놔

    
# 거짓일때는?? 반환 안됨

#타겟값이 정해져 있어서 가능한거잖음. 값이 정해져 있을때에만 답을 찾는건가.
    #타겟이 주어지지 않는다면 n^2만큼 돌려서 타겟을 만든 다음, 검증해야하는?  
    #????
    # 무얼 찾아야 하는지 타켓이 명확할 때 사용할 수 있는 솔루션이겠다.
    raise NotImplementedError


### ✅ 테스트 코드 (Step 1과 동일한 테스트 케이스를 사용합니다)

for nums, target, expected in test_cases:
    result = two_sum_hashmap(nums, target)
    
    print(f\"nums={nums}, target={target} → result={result}, expected={expected}\")


---
## Step 3. Brute Force vs Hash Map 비교 정리

아래 마크다운 셀에 두 방식의 차이점을 정리해 보세요. (키워드만이 아니라 문장으로 설명해보면 좋습니다.)

### 비교 관점
- 접근 방식 차이 (어떻게 문제를 바라보는가?)
- 시간복잡도 비교 (`O(N^2)` vs `O(N)`)
- 메모리 사용량 (추가 자료구조 사용 여부)
- 실전에서 어떤 상황에서 어떤 방식을 선택할지

---
아래 셀을 직접 수정해서 본인의 정리를 작성하세요.

### ✏️ 정리 (학생 작성)

- 브루트 포스 Brute Force 방식: 하나하나 다 해보는 것이다. 자물쇠번호를 풀기위해 0000부터 9999가지 전부 대입하는 것과 같다. 따라서, 시도할 리스트가 길어지면 시간이 어마어마해진다.(N^2)
  - 데이터가 10배 늘어나면 연산횟수는 100배
- 해시맵 Hash Map 방식: 한 번 본 숫자를 해시맵이라는 메모장에 적어두는 방식. 리스트를 딱 한 번만 훑는다. 짝꿍(타겟-현재숫자)이 메모장에 적혀있는지를 확인해, 입구에서 방명록을 확인하고 해당 번호로 가는 것과 같다.
  - 데이터가 10배 늘어나면 연산횟수도 10배 
- 두 방식의 공통점 & 차이점: 이미 본 데이터를 기억하냐, 매번 새로 찾아 헤매냐
- 이중 반복문으로 모든 쌍을 검사하냐, 단일 반복문과 메모리 활용으로 한번에 가냐
  - 시간복잡도: N^2, N
  - 메모리 사용: 추가메모라를 거의 안쓰지만/ 해시맵 저장공간이 추가로 필요하다
  - 구현 난이도: 브루트포스방식이 냅다 돌리면 되니까 구현은 쉬워보였다.
  - 지금이야 이중문을 썼다지만, 삼중 사중 얼마든지 돌릴 수 있지않나. 그러나 시간이 오래걸린다는 것은 곧 비용과도 직결되는 문제이니 해시맵을 이해해보려 노력해야겠다.
  - 실제로 내가 쓴다면?
- 데이터 개수 (N),브루트 포스 (O(N2)),해시맵 (O(N)),차이
    100개,\"10,000번 연산 (0.0001초)\",100번 연산 (찰나),체감 안 됨
    \"10,000개\",1억 번 연산 (약 1초),\"10,000번 연산 (0.0001초)\",1만 배 차이
    \"100,000개\",100억 번 연산 (약 1.6분),\"100,000번 연산 (0.001초)\",약 10만 배 차이
    \"1,000,000개\",1조 번 연산 (약 2.7시간),\"1,000,000번 연산 (0.01초)\",넘사벽
해시맵을 써야겠네.

---
## Step 4. 제출 전 체크리스트
- [ ] Brute Force 코드가 정상 동작한다.
- [ ] Hash Map 코드가 정상 동작한다.
- [ ] 두 방식의 시간복잡도와 차이에 대한 나만의 설명을 적었다.
- [ ] 예시 테스트 케이스 결과가 문제 설명과 일치한다.
- [ ] (과제용) 실행 결과를 캡처해 별도 제출 또는 첨부 준비를 했다.

수고하셨습니다! 😄


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day2_advanced_mission(문제)-checkpoint.ipynb.txt'] = """# Day 2. 스택으로 문제 해결하기 – 심화 미션 (Daily Temperatures)

이 노트북은 **Monotonic Stack(단조 스택)** 패턴을 연습하기 위한 심화 과제용입니다.
LeetCode **#739 Daily Temperatures** 문제를 풀며, 스택을 이용한 **인덱스 기반 문제 해결**을 경험합니다.

## 🎯 학습 목표
- 스택에 **값이 아닌 인덱스(index)** 를 저장하여 문제를 푸는 패턴을 익힌다.
- **Monotonic Stack(단조 증가/단조 감소 스택)** 의 개념을 이해하고 구현한다.
- 온도 배열에서 \"다음에 더 따뜻한 날\"까지의 거리를 효율적으로 계산한다.

---
## 문제: LeetCode #739 — Daily Temperatures

정수 배열 `temperatures` 가 주어질 때, **각 날짜마다** 현재 온도보다 더 따뜻한 날이 오기까지
몇 일을 기다려야 하는지 계산해서 배열로 반환하세요.

더 따뜻한 날이 없다면 `0`을 기록합니다.

### 예시
1. `temperatures = [73,74,75,71,69,72,76,73]`
   → 출력: `[1,1,4,2,1,1,0,0]`
2. `temperatures = [30, 40, 50, 60]`
   → 출력: `[1,1,1,0]`
3. `temperatures = [30, 60, 90]`
   → 출력: `[1,1,0]`

### 제한 조건
- `1 <= temperatures.length <= 10**5`
- `30 <= temperatures[i] <= 100`

---
아래 **Step 1 → Step 3** 순서로 심화 미션을 진행하세요.

## 🛠️ Prerequisites
본 미션은 Python 표준 라이브러리만을 사용하여 해결하며, 다음 모듈을 활용합니다.
* **`from typing import List`**: 리스트 데이터의 타입을 명시하기 위해 사용합니다.
* 별도의 라이브러리 설치(pip install)는 필요하지 않으며, Python 3.x 환경에서 즉시 실행 가능합니다.

## Step 1. 문제 이해 & 단순(Brute Force) 아이디어 생각해 보기

먼저, 스택 없이 **가장 단순한 방법**을 떠올려 보고 시간복잡도를 분석해 봅시다.

- i번째 날에 대해, 그 다음 날들 `i+1, i+2, ...` 을 하나씩 보면서
  **처음으로 더 따뜻한 날**을 찾는 방식은 어떤 시간복잡도를 가질까요?
- 이 방식이 `O(N^2)` 인 이유를 설명해 보세요.

아래에 본인의 생각을 정리해 보세요.

### ✏️ Brute Force 아이디어 & 시간복잡도 (학생 작성)

- 단순한 해결 방법 설명: 오늘부터 시작해서 오늘보다 따듯한 날이 나올 때까지, 내일, 모레를 하나씩 다 확인해본다,브루트포스
- 1.리스트의 첫 날부터 마지막 날까지 하나씩 선택(선택일)
- 2.선택일 이후의 날들을 하나씩 살펴보며 선택일보다 온도가 높은 날을 찾음
- 3.찾으면 그날과 선택일의 날짜차이(인덱스차이)를 결과리스트에 적는다
- 4.끝까지 가도 더 따듯한 날이 없다면 0을 적는다
- 이 방법의 시간복잡도 분석 (왜 O(N^2)?):
  -주어진 N개의 모든 날짜마다 뒤에 남은 모든 날을 확인해야하므로 N회차
  -N*N
- N 이 10만(`10**5`)일 때, 이 방법이 왜 비효율적인지:
  -10**10만큼 해야하니 시간이 오래걸린다.


---
## Step 2. Monotonic Stack(단조 스택) 아이디어 이해하기

### Monotonic Stack이란?
- 스택 안의 원소들이 **항상 한 방향으로 정렬된 상태(단조 증가 / 단조 감소)** 를 유지하도록 관리하는 스택입니다.
- 이 문제에서는 \"미래의 더 큰 값\"을 빠르게 찾기 위해, **온도가 높은 날을 찾을 때까지** 이전 인덱스를 스택에 쌓아두었다가,
  더 따뜻한 날을 만나면 스택에서 꺼내면서 거리(날짜 차이)를 계산합니다.

### 핵심 아이디어 (단조 감소 스택)
- 스택에는 **인덱스(index)** 를 저장합니다.
- 스택 안의 인덱스들은 항상 **온도가 내림차순(같거나 더 높은)** 이 되도록 유지합니다.
- 새로운 날 `i`의 온도 `temperatures[i]` 가 **스택 top의 온도보다 높다면**, 그 날이 바로
  스택 top에 쌓여 있던 날짜들의 \"다음 더 따뜻한 날\"이 됩니다.
- 이 과정을 반복하면서, 한 번씩만 스택에 `push`/`pop` 하면 전체 시간복잡도는 `O(N)` 이 됩니다.

위 내용을 스스로 이해한 표현으로 아래에 다시 요약해 보세요.

### ✏️ Monotonic Stack 정리 (학생 작성)

- 스택에 **값이 아닌 인덱스를 저장**하는 이유:
  -날짜차이를 계산해야하기 때문에
  -값인 온도만 저장하면 며칠 뒤인지 알 수 없다
  -인덱스 자체가 날짜의 역할을 한다. 인덱스 차로 며칠 뒤인지 알 수 있다,
  -해당 인덱스로 온도값도 볼 수 있다.
- 우리가 유지하려는 \"단조성\"(증가/감소)은 어떤 방향이며, 그 이유는?
  -스택 아래쪽이 높고, 위로갈수록 낮은 온도
  -현재온도보다 더 따듯한 날을 아직 찾지 못한 날짜들이, 온도가 높은 순서에서
  -낮은 순서로 쌓인다.
  -만약 선택일의 온도가 전일 보다 낮다면, 기다려야하므로 선택일은 스택에 추가된다
  -만약 선택일의 온도가 전일 보다 높다면, 데이터를 꺼낸다
- 새로운 온도를 만났을 때, 스택에서 `pop` 해야 하는 조건은?
  -선택일의 온도 > 스택 탑 인덱스 온도


---
## Step 3. Python 코드 구현 – `dailyTemperatures`

아래 템플릿을 참고해서 Monotonic Stack 기반 알고리즘을 구현해 보세요.

### 구현 요구사항
- 반환값: 각 인덱스 `i`에 대해, **더 따뜻한 날까지 기다려야 하는 일수**를 담은 리스트
- 더 따뜻한 날이 없으면 `0`
- 시간복잡도: `O(N)`
- 스택에는 **인덱스만 저장**합니다.


 \"\"\"Daily Temperatures 문제를 Monotonic Stack으로 해결합니다.

        아이디어 요약:
            TODO: 단조 스택이 어떻게 동작하는지, 간단히 한국어로 정리해 보세요.

           ///////////////// 정리가 안되어요! 살려줘///////////////////

        시간복잡도:
            TODO: 왜 이 알고리즘이 O(N)인지 설명해 보세요.
        \"\"\"

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        n = len(temperatures)
        answer = [0] * n  # 각 인덱스별 정답을 저장할 배열

        stack = []  # 인덱스를 저장하는 스택 (단조 감소 스택)

        # TODO: 여기에 Monotonic Stack 알고리즘을 구현하세요.
        for curr_day, curr_temp in enumerate(temperatures):
        
        #   - i를 0부터 n-1까지 순회
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
        #   - 현재 온도가 스택 top 인덱스의 온도보다 높으면, pop 하면서
        #     answer[top] = i - top  값을 채우기

            stack.append(curr_day)
        return answer
        #   - 스택에는 항상 아직 더 따뜻한 날을 찾지 못한 인덱스만 남도록 유지

        raise NotImplementedError


### ✅ 테스트 코드
아래 셀을 실행해 예제 입력과 몇 가지 추가 케이스에 대해 결과를 확인해 보세요.
필요하다면 테스트 케이스를 직접 더 추가해도 좋습니다.

def run_tests():
    sol = Solution()
    tests = [
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([30,60,90], [1,1,0]),
        ([100, 90, 80], [0,0,0]),  # 항상 감소하는 경우
    ]

    for temps, expected in tests:
        result = sol.dailyTemperatures(temps)
        print(f\"temperatures={temps}\\n  result  = {result}\\n  expected= {expected}\\n\")

run_tests()


---
## Step 4. 정리 및 자기 점검

아래에 오늘의 심화 미션에서 배운 점을 정리해 보세요.

- Monotonic Stack 패턴을 다른 문제(예: \"Next Greater Element\")에 어떻게 응용할 수 있을까요?
- 단순 `O(N^2)` 방식과 비교했을 때, 구현 난이도와 직관성은 어땠나요?

### ✏️ 정리 (학생 작성)

- 오늘 새로 알게 된 개념/키워드:
  -inkedlist stack queue lifo fifo 시간,공간복잡도 꼬리포인터
- Monotonic Stack을 한 문장으로 정의해 본다면:
  -스택 내부 원소들을 일정한 순서로 유지
- 이 패턴을 적용할 수 있을 것 같은 다른 문제 유형:
  -


---
## 제출 전 체크리스트 ✅ (심화)
- [ ] `dailyTemperatures` 함수가 **O(N)** 시간복잡도로 구현되었다.
- [ ] 스택에는 **온도가 아니라 인덱스**를 저장한다.
- [ ] 스택 `pop` 조건과 `answer[index] = i - index` 계산이 정확하다.
- [ ] 예시 테스트 케이스가 모두 올바르게 통과한다.
- [ ] Monotonic Stack의 개념을 말로 설명할 수 있다.

잘 해냈어요! 💪 Day 2 심화에서 배운 Monotonic Stack은 이후 여러 고급 문제에서 반복해서 등장할 핵심 도구입니다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day2_advanced_mission(문제).ipynb.txt'] = """# Day 2. 스택으로 문제 해결하기 – 심화 미션 (Daily Temperatures)

이 노트북은 **Monotonic Stack(단조 스택)** 패턴을 연습하기 위한 심화 과제용입니다.
LeetCode **#739 Daily Temperatures** 문제를 풀며, 스택을 이용한 **인덱스 기반 문제 해결**을 경험합니다.

## 🎯 학습 목표
- 스택에 **값이 아닌 인덱스(index)** 를 저장하여 문제를 푸는 패턴을 익힌다.
- **Monotonic Stack(단조 증가/단조 감소 스택)** 의 개념을 이해하고 구현한다.
- 온도 배열에서 \"다음에 더 따뜻한 날\"까지의 거리를 효율적으로 계산한다.

---
## 문제: LeetCode #739 — Daily Temperatures

정수 배열 `temperatures` 가 주어질 때, **각 날짜마다** 현재 온도보다 더 따뜻한 날이 오기까지
몇 일을 기다려야 하는지 계산해서 배열로 반환하세요.

더 따뜻한 날이 없다면 `0`을 기록합니다.

### 예시
1. `temperatures = [73,74,75,71,69,72,76,73]`
   → 출력: `[1,1,4,2,1,1,0,0]`
2. `temperatures = [30, 40, 50, 60]`
   → 출력: `[1,1,1,0]`
3. `temperatures = [30, 60, 90]`
   → 출력: `[1,1,0]`

### 제한 조건
- `1 <= temperatures.length <= 10**5`
- `30 <= temperatures[i] <= 100`

---
아래 **Step 1 → Step 3** 순서로 심화 미션을 진행하세요.

## 🛠️ Prerequisites
본 미션은 Python 표준 라이브러리만을 사용하여 해결하며, 다음 모듈을 활용합니다.
* **`from typing import List`**: 리스트 데이터의 타입을 명시하기 위해 사용합니다.
* 별도의 라이브러리 설치(pip install)는 필요하지 않으며, Python 3.x 환경에서 즉시 실행 가능합니다.

## Step 1. 문제 이해 & 단순(Brute Force) 아이디어 생각해 보기

먼저, 스택 없이 **가장 단순한 방법**을 떠올려 보고 시간복잡도를 분석해 봅시다.

- i번째 날에 대해, 그 다음 날들 `i+1, i+2, ...` 을 하나씩 보면서
  **처음으로 더 따뜻한 날**을 찾는 방식은 어떤 시간복잡도를 가질까요?
- 이 방식이 `O(N^2)` 인 이유를 설명해 보세요.

아래에 본인의 생각을 정리해 보세요.

### ✏️ Brute Force 아이디어 & 시간복잡도 (학생 작성)

- 단순한 해결 방법 설명: 오늘부터 시작해서 오늘보다 따듯한 날이 나올 때까지, 내일, 모레를 하나씩 다 확인해본다,브루트포스
- 1.리스트의 첫 날부터 마지막 날까지 하나씩 선택(선택일)
- 2.선택일 이후의 날들을 하나씩 살펴보며 선택일보다 온도가 높은 날을 찾음
- 3.찾으면 그날과 선택일의 날짜차이(인덱스차이)를 결과리스트에 적는다
- 4.끝까지 가도 더 따듯한 날이 없다면 0을 적는다
- 이 방법의 시간복잡도 분석 (왜 O(N^2)?):
  -주어진 N개의 모든 날짜마다 뒤에 남은 모든 날을 확인해야하므로 N회차
  -N*N
- N 이 10만(`10**5`)일 때, 이 방법이 왜 비효율적인지:
  -10**10만큼 해야하니 시간이 오래걸린다.


---
## Step 2. Monotonic Stack(단조 스택) 아이디어 이해하기

### Monotonic Stack이란?
- 스택 안의 원소들이 **항상 한 방향으로 정렬된 상태(단조 증가 / 단조 감소)** 를 유지하도록 관리하는 스택입니다.
- 이 문제에서는 \"미래의 더 큰 값\"을 빠르게 찾기 위해, **온도가 높은 날을 찾을 때까지** 이전 인덱스를 스택에 쌓아두었다가,
  더 따뜻한 날을 만나면 스택에서 꺼내면서 거리(날짜 차이)를 계산합니다.

### 핵심 아이디어 (단조 감소 스택)
- 스택에는 **인덱스(index)** 를 저장합니다.
- 스택 안의 인덱스들은 항상 **온도가 내림차순(같거나 더 높은)** 이 되도록 유지합니다.
- 새로운 날 `i`의 온도 `temperatures[i]` 가 **스택 top의 온도보다 높다면**, 그 날이 바로
  스택 top에 쌓여 있던 날짜들의 \"다음 더 따뜻한 날\"이 됩니다.
- 이 과정을 반복하면서, 한 번씩만 스택에 `push`/`pop` 하면 전체 시간복잡도는 `O(N)` 이 됩니다.

위 내용을 스스로 이해한 표현으로 아래에 다시 요약해 보세요.

### ✏️ Monotonic Stack 정리 (학생 작성)

- 스택에 **값이 아닌 인덱스를 저장**하는 이유:
  -날짜차이를 계산해야하기 때문에
  -값인 온도만 저장하면 며칠 뒤인지 알 수 없다
  -인덱스 자체가 날짜의 역할을 한다. 인덱스 차로 며칠 뒤인지 알 수 있다,
  -해당 인덱스로 온도값도 볼 수 있다.
- 우리가 유지하려는 \"단조성\"(증가/감소)은 어떤 방향이며, 그 이유는?
  -스택 아래쪽이 높고, 위로갈수록 낮은 온도
  -현재온도보다 더 따듯한 날을 아직 찾지 못한 날짜들이, 온도가 높은 순서에서
  -낮은 순서로 쌓인다.
  -만약 선택일의 온도가 전일 보다 낮다면, 기다려야하므로 선택일은 스택에 추가된다
  -만약 선택일의 온도가 전일 보다 높다면, 데이터를 꺼낸다
- 새로운 온도를 만났을 때, 스택에서 `pop` 해야 하는 조건은?
  -선택일의 온도 > 스택 탑 인덱스 온도


---
## Step 3. Python 코드 구현 – `dailyTemperatures`

아래 템플릿을 참고해서 Monotonic Stack 기반 알고리즘을 구현해 보세요.

### 구현 요구사항
- 반환값: 각 인덱스 `i`에 대해, **더 따뜻한 날까지 기다려야 하는 일수**를 담은 리스트
- 더 따뜻한 날이 없으면 `0`
- 시간복잡도: `O(N)`
- 스택에는 **인덱스만 저장**합니다.


 \"\"\"Daily Temperatures 문제를 Monotonic Stack으로 해결합니다.

        아이디어 요약:
            TODO: 단조 스택이 어떻게 동작하는지, 간단히 한국어로 정리해 보세요.

           ///////////////// 정리가 안되어요! 살려줘///////////////////

        시간복잡도:
            TODO: 왜 이 알고리즘이 O(N)인지 설명해 보세요.
        \"\"\"

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        n = len(temperatures)
        answer = [0] * n  # 각 인덱스별 정답을 저장할 배열

        stack = []  # 인덱스를 저장하는 스택 (단조 감소 스택)

        # TODO: 여기에 Monotonic Stack 알고리즘을 구현하세요.
        for curr_day, curr_temp in enumerate(temperatures):
        
        #   - i를 0부터 n-1까지 순회
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
        #   - 현재 온도가 스택 top 인덱스의 온도보다 높으면, pop 하면서
        #     answer[top] = i - top  값을 채우기

            stack.append(curr_day)
        return answer
        #   - 스택에는 항상 아직 더 따뜻한 날을 찾지 못한 인덱스만 남도록 유지

        raise NotImplementedError


### ✅ 테스트 코드
아래 셀을 실행해 예제 입력과 몇 가지 추가 케이스에 대해 결과를 확인해 보세요.
필요하다면 테스트 케이스를 직접 더 추가해도 좋습니다.

def run_tests():
    sol = Solution()
    tests = [
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([30,60,90], [1,1,0]),
        ([100, 90, 80], [0,0,0]),  # 항상 감소하는 경우
    ]

    for temps, expected in tests:
        result = sol.dailyTemperatures(temps)
        print(f\"temperatures={temps}\\n  result  = {result}\\n  expected= {expected}\\n\")

run_tests()


---
## Step 4. 정리 및 자기 점검

아래에 오늘의 심화 미션에서 배운 점을 정리해 보세요.

- Monotonic Stack 패턴을 다른 문제(예: \"Next Greater Element\")에 어떻게 응용할 수 있을까요?
- 단순 `O(N^2)` 방식과 비교했을 때, 구현 난이도와 직관성은 어땠나요?

### ✏️ 정리 (학생 작성)

- 오늘 새로 알게 된 개념/키워드:
  -inkedlist stack queue lifo fifo 시간,공간복잡도 꼬리포인터
- Monotonic Stack을 한 문장으로 정의해 본다면:
  -스택 내부 원소들을 일정한 순서로 유지
- 이 패턴을 적용할 수 있을 것 같은 다른 문제 유형:
  -


---
## 제출 전 체크리스트 ✅ (심화)
- [ ] `dailyTemperatures` 함수가 **O(N)** 시간복잡도로 구현되었다.
- [ ] 스택에는 **온도가 아니라 인덱스**를 저장한다.
- [ ] 스택 `pop` 조건과 `answer[index] = i - index` 계산이 정확하다.
- [ ] 예시 테스트 케이스가 모두 올바르게 통과한다.
- [ ] Monotonic Stack의 개념을 말로 설명할 수 있다.

잘 해냈어요! 💪 Day 2 심화에서 배운 Monotonic Stack은 이후 여러 고급 문제에서 반복해서 등장할 핵심 도구입니다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day2_daily_mission(문제)-checkpoint.ipynb.txt'] = """# Day 2. 스택으로 문제 해결하기 – 데일리 미션 (Valid Parentheses)

이 노트북은 **스택(Stack)** 을 활용해 LeetCode **#20 Valid Parentheses** 문제를 푸는 데일리 미션용입니다.

## 🎯 학습 목표
- 스택의 **LIFO(Last-In, First-Out)** 구조와 `push`/`pop` 연산을 이해한다.
- 문자열 속 괄호 패턴을 **스택으로 검증하는 알고리즘**을 설계하고 구현한다.
- 시간복잡도 `O(N)` 알고리즘을 직접 작성하고 분석한다.

---
## 문제: LeetCode #20 — Valid Parentheses

문자열 `s` 가 주어졌을 때, 문자열이 **올바른 괄호 구성(valid parentheses)** 인지 판별하는 함수를 작성하세요.

문자열 `s` 는 `'(', ')', '{', '}', '[', ']'` 문자로만 이루어져 있습니다.

올바른 괄호의 조건은 다음과 같습니다.
1. 열린 괄호는 **반드시 동일한 종류의 닫힌 괄호**로 닫혀야 한다.
2. 열린 괄호는 **올바른 순서**로 닫혀야 한다.
3. 모든 괄호는 **짝이 맞아야 한다.**

### 예시
1. `s = \"()\"` → `True`
2. `s = \"()[]{}\"` → `True`
3. `s = \"(]\"` → `False`
4. `s = \"([)]\"` → `False`
5. `s = \"{[]}\"` → `True`

### 제한 조건
- `1 <= s.length <= 10**4`
- `s` 는 `'()[]{}'` 만을 포함합니다.

---
아래 **Step 1 → Step 4** 순서로 미션을 수행해 주세요.

## 🛠️ Prerequisites
본 미션은 Python 표준 기능을 활용하며, 별도의 라이브러리 설치가 필요하지 않습니다.
* **Stack 구현**: Python의 기본 `list`를 활용하여 `push`(append) 및 `pop` 연산을 수행합니다.
* **데이터 구조**: `dict`를 활용해 괄호 쌍을 매핑하여 코드의 가독성을 높입니다.

## Step 1. 문제 이해 & 기본 테스트 케이스 정리

아래 마크다운 셀에 본인이 이해한 문제를 **자신의 말로 정리**해 보세요.

- 어떤 입력이 들어오는가?
- 어떤 출력을 만들어야 하는가?
- 어떤 경우에 `True`, 어떤 경우에 `False` 가 되는가?

또한, 떠오르는 **추가 테스트 케이스**(엣지 케이스 포함)를 2~3개 적어보세요.

### ✏️ 내가 이해한 문제 설명 (학생 작성)

- 문제 요약:주어진 문자열의 괄호가 동일한 종류의 올바른순서로 짝이 맞게 닫혀있느냐를 판별하는 함수 작성
- 입력 형태:string
- 출력 형태:bool
- `True` 가 되는 조건:올바른 괄호구성,순서,종류,짝이 맞다
- `False` 가 되는 조건: 무언가 하나라도 아니다

### ✏️ 추가 테스트 케이스 아이디어
- 예) `\"((((\"`, `\"\"`, `\"([]\"`, `\"[{()}]\"` 등
- 내가 생각한 테스트:

\"(3+4)*(2+5)\" is well-formed

\"((2*2)*3+1)\" is not well-formed

\")(2+2\" is not well-formed

what if we have more than one types of parentheses?

\"{(2+1)*(3+2)-22}*7\" is well-formed

\"{(7+2}*3)\" is not well-formed

---
## Step 2. 스택 기반 알고리즘 설계

스택을 활용해 올바른 괄호를 판단하는 알고리즘을 설계해봅시다.

### 아이디어 힌트
- 문자열을 **왼쪽에서 오른쪽으로 한 글자씩** 순회합니다.
- 열린 괄호 `'(' , '{' , '['` 가 나오면 **스택에 push** 합니다.
- 닫힌 괄호가 나오면, 스택에서 하나 꺼내(pop) **짝이 맞는지 확인**합니다.
  - 스택이 비어 있다면? → 잘못된 문자열입니다.
  - 스택 top과 짝이 맞지 않는다면? → 잘못된 문자열입니다.
- 문자열을 모두 확인한 후 **스택이 비어 있으면** 올바른 괄호 문자열입니다.

아래 셀에 본인의 알고리즘을 **자연어/의사코드(pseudocode)** 로 먼저 적어보세요.

### ✏️ 알고리즘 설계 (학생 작성)

1.문자열을 왼쪽에서 오른쪽으로 한글자씩 순회

2.if 열린 괄호 \"(\", \"{\" ,\"[\" 이 나오면:  스택에 push (append)

3.if 닫힌 괄호가 나오면, 스택 탑에서 하나 꺼내 pop 짝이 맞는지 확인

4.if 스택이 비어있다: 잘못된 문자열 False

if 스택에서 꺼낸 top과 짝이 맞지 않는다 : 잘못된 문자열 False

5.문자열을 모두 확인(스택을 다 꺼내고) 비어있으면 올바른 문자열 : True

※ 이 단계에서 충분히 설계해두면, 코드 구현이 훨씬 쉬워집니다.

---
## Step 3. Python 코드 구현

이제 설계한 알고리즘을 실제 코드로 옮겨 봅시다.

가능하면 **다음 조건을 만족하는 코드**를 작성해 보세요.
- Python 리스트를 스택처럼 사용 (`append`, `pop`)
- 괄호 짝 매칭은 `dict` 를 사용하면 더 깔끔합니다. 예: `pairs = {')':'(', ']':'[', '}':'{'}`
- 시간복잡도는 `O(N)` 이어야 합니다.

아래 템플릿을 참고해 `isValid` 메서드를 완성하세요.

 \"\"\"주어진 문자열 s가 올바른 괄호 문자열인지 판별합니다.

        알고리즘 아이디어:
            TODO: 여기서 스택을 어떻게 사용할지 간단히 설명해 보세요.

            1.문자열을 왼쪽에서 오른쪽으로 한글자씩 순회
            2.if 열린 괄호 \"(\", \"{\" ,\"[\" 이 나오면 스택에 push append
            3.if 닫힌 괄호가 나오면, 스택에서 하나 꺼내 pop 짝이 맞는지 확인
            4.if 스택이 비어있다: 잘못된 문자열 False
              if 스택에서 꺼낸 top과 짝이 맞지 않는다 : 잘못된 문자열 False
              짝은 { \")\" : \"(\" , \"}\" : \"{\", \"]\" : \"[\" }
            5.문자열을 모두 확인(스택을 다 꺼내고) 비어있으면 올바른 문자열 : True

        시간복잡도:
            TODO: 왜 이 알고리즘의 시간복잡도가 O(N)인지 설명해 보세요.
            1번 순회하는 동안 입력된 N개의 문자열을 하나씩 검증하므로 N만큼 걸린다
        \"\"\"

class Solution:
    def isValid(self, s: str) -> bool:

        # TODO: 여기에 스택 기반 알고리즘을 구현하세요.

        stack = [] #괄호 쌓을 리스트
        pair = { \")\" : \"(\" , \"}\" : \"{\", \"]\" : \"[\" }  #짝맞출 딕셔너리

        for x in s:   #s를 하나씩 순회해
            if not x in pair:      #   - 열린 괄호일 때, pair의 key에 없다
                stack.append(x) #  stack에 append 쌓아놔

            if x in pair:       #   - 닫힌 괄호일 때
                top = stack.pop()     #stack에 쌓은 마지막것을 꺼내, top이라 하자
                if top != pair[x]:  #꺼낸 top이, pair의 짝과 안맞으면
                    return False  #False

                if not stack:    #   - 스택이 비어있는 경우 예외 처리
                    return False

            #   - 반복이 끝난 뒤 스택이 비어 있는지 확인
        return len(stack) == 0

        raise NotImplementedError


### ✅ 테스트 코드
아래 셀을 실행해서 다양한 입력에 대해 `isValid` 가 올바르게 동작하는지 확인해 보세요.
필요하다면 테스트 케이스를 더 추가해도 좋습니다.

def run_tests():
    sol = Solution()
    tests = [
        (\"()\", True),
        (\"()[]{}\", True),
        (\"(]\", False),
        (\"([)]\", False),
        (\"{[]}\", True),
    ]

    for s, expected in tests:
        result = sol.isValid(s)
        print(f\"s='{s}' → result={result}, expected={expected}\")

run_tests()


---
## Step 4. 시간복잡도 분석 & 정리

아래에 본인의 코드에 대한 **시간복잡도/공간복잡도 분석**과 함께,
스택이 없었다면 어떤 방식으로 풀 수 있을지(그리고 왜 비효율적인지)를 간단히 적어보세요.

### ✏️ 정리 (학생 작성)

- 시간복잡도 분석:
  -
- 공간복잡도 분석:
  -
- 이 문제에서 스택이 왜 잘 맞는 도구인지:
  -
- 스택을 사용하지 않는다면 어떤 방식이 있을지, 그리고 단점은?
  -


---
## 제출 전 체크리스트 ✅
- [ ] 스택(list)을 사용해 구현했다.
- [ ] 스택이 비어 있는 상태에서 `pop` 하지 않도록 예외 처리를 했다.
- [ ] 예제 테스트 케이스가 모두 기대한 값으로 나온다.
- [ ] 시간복잡도 `O(N)` 분석을 코드/마크다운에 적었다.
- [ ] 노트북 상단부터 하단까지 실행이 끊김 없이 잘 동작한다.

수고 많았어요! 🎉 Day 2의 기본 스택 패턴은 이후 수많은 문제의 기본기가 됩니다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위

class Solution:
    def isValid(self, s: str) -> bool:
        \"\"\"주어진 문자열 s가 올바른 괄호 문자열인지 판별합니다.

        알고리즘 아이디어:
            TODO: 여기서 스택을 어떻게 사용할지 간단히 설명해 보세요.

        시간복잡도:
            TODO: 왜 이 알고리즘의 시간복잡도가 O(N)인지 설명해 보세요.
        \"\"\"
        # TODO: 여기에 스택 기반 알고리즘을 구현하세요.
        #   - 열린 괄호일 때의 처리
        #   - 닫힌 괄호일 때의 처리
        #   - 스택이 비어있는 경우 예외 처리
        #   - 반복이 끝난 뒤 스택이 비어 있는지 확인

        q = []
        input_count = 0

        for char in s:
            if ord(char) == 40 or ord(char) == 91 or ord(char) == 123:
              q.append(char)
              input_count += 1
              continue

            if(len(q) <= 0):
              return False

            pop = ord(q.pop())
            pop = pop // 10

            if(pop != ord(char) // 10):
                return False

        if(len(q) == 0 and len(s)/2 == input_count):
          return True
        else:
          return False

        raise NotImplementedError


def run_tests():
    sol = Solution()
    tests = [
        (\"()\", True),
        (\"()[]{}\", True),
        (\"(]\", False),
        (\"([)]\", False),
        (\"{[]}\", True),
        (\"})]}\", False),
        (\"([)]\", False)
    ]

    for s, expected in tests:
        result = sol.isValid(s)
        print(f\"s='{s}' → result={result}, expected={expected}\")

run_tests()
"""
    s.raw_texts['Day2_daily_mission(문제).ipynb.txt'] = """# Day 2. 스택으로 문제 해결하기 – 데일리 미션 (Valid Parentheses)

이 노트북은 **스택(Stack)** 을 활용해 LeetCode **#20 Valid Parentheses** 문제를 푸는 데일리 미션용입니다.

## 🎯 학습 목표
- 스택의 **LIFO(Last-In, First-Out)** 구조와 `push`/`pop` 연산을 이해한다.
- 문자열 속 괄호 패턴을 **스택으로 검증하는 알고리즘**을 설계하고 구현한다.
- 시간복잡도 `O(N)` 알고리즘을 직접 작성하고 분석한다.

---
## 문제: LeetCode #20 — Valid Parentheses

문자열 `s` 가 주어졌을 때, 문자열이 **올바른 괄호 구성(valid parentheses)** 인지 판별하는 함수를 작성하세요.

문자열 `s` 는 `'(', ')', '{', '}', '[', ']'` 문자로만 이루어져 있습니다.

올바른 괄호의 조건은 다음과 같습니다.
1. 열린 괄호는 **반드시 동일한 종류의 닫힌 괄호**로 닫혀야 한다.
2. 열린 괄호는 **올바른 순서**로 닫혀야 한다.
3. 모든 괄호는 **짝이 맞아야 한다.**

### 예시
1. `s = \"()\"` → `True`
2. `s = \"()[]{}\"` → `True`
3. `s = \"(]\"` → `False`
4. `s = \"([)]\"` → `False`
5. `s = \"{[]}\"` → `True`

### 제한 조건
- `1 <= s.length <= 10**4`
- `s` 는 `'()[]{}'` 만을 포함합니다.

---
아래 **Step 1 → Step 4** 순서로 미션을 수행해 주세요.

## 🛠️ Prerequisites
본 미션은 Python 표준 기능을 활용하며, 별도의 라이브러리 설치가 필요하지 않습니다.
* **Stack 구현**: Python의 기본 `list`를 활용하여 `push`(append) 및 `pop` 연산을 수행합니다.
* **데이터 구조**: `dict`를 활용해 괄호 쌍을 매핑하여 코드의 가독성을 높입니다.

## Step 1. 문제 이해 & 기본 테스트 케이스 정리

아래 마크다운 셀에 본인이 이해한 문제를 **자신의 말로 정리**해 보세요.

- 어떤 입력이 들어오는가?
- 어떤 출력을 만들어야 하는가?
- 어떤 경우에 `True`, 어떤 경우에 `False` 가 되는가?

또한, 떠오르는 **추가 테스트 케이스**(엣지 케이스 포함)를 2~3개 적어보세요.

### ✏️ 내가 이해한 문제 설명 (학생 작성)

- 문제 요약:주어진 문자열의 괄호가 동일한 종류의 올바른순서로 짝이 맞게 닫혀있느냐를 판별하는 함수 작성
- 입력 형태:string
- 출력 형태:bool
- `True` 가 되는 조건:올바른 괄호구성,순서,종류,짝이 맞다
- `False` 가 되는 조건: 무언가 하나라도 아니다

### ✏️ 추가 테스트 케이스 아이디어
- 예) `\"((((\"`, `\"\"`, `\"([]\"`, `\"[{()}]\"` 등
- 내가 생각한 테스트:

\"(3+4)*(2+5)\" is well-formed

\"((2*2)*3+1)\" is not well-formed

\")(2+2\" is not well-formed

what if we have more than one types of parentheses?

\"{(2+1)*(3+2)-22}*7\" is well-formed

\"{(7+2}*3)\" is not well-formed

---
## Step 2. 스택 기반 알고리즘 설계

스택을 활용해 올바른 괄호를 판단하는 알고리즘을 설계해봅시다.

### 아이디어 힌트
- 문자열을 **왼쪽에서 오른쪽으로 한 글자씩** 순회합니다.
- 열린 괄호 `'(' , '{' , '['` 가 나오면 **스택에 push** 합니다.
- 닫힌 괄호가 나오면, 스택에서 하나 꺼내(pop) **짝이 맞는지 확인**합니다.
  - 스택이 비어 있다면? → 잘못된 문자열입니다.
  - 스택 top과 짝이 맞지 않는다면? → 잘못된 문자열입니다.
- 문자열을 모두 확인한 후 **스택이 비어 있으면** 올바른 괄호 문자열입니다.

아래 셀에 본인의 알고리즘을 **자연어/의사코드(pseudocode)** 로 먼저 적어보세요.

### ✏️ 알고리즘 설계 (학생 작성)

1.문자열을 왼쪽에서 오른쪽으로 한글자씩 순회

2.if 열린 괄호 \"(\", \"{\" ,\"[\" 이 나오면:  스택에 push (append)

3.if 닫힌 괄호가 나오면, 스택 탑에서 하나 꺼내 pop 짝이 맞는지 확인

4.if 스택이 비어있다: 잘못된 문자열 False

if 스택에서 꺼낸 top과 짝이 맞지 않는다 : 잘못된 문자열 False

5.문자열을 모두 확인(스택을 다 꺼내고) 비어있으면 올바른 문자열 : True

※ 이 단계에서 충분히 설계해두면, 코드 구현이 훨씬 쉬워집니다.

---
## Step 3. Python 코드 구현

이제 설계한 알고리즘을 실제 코드로 옮겨 봅시다.

가능하면 **다음 조건을 만족하는 코드**를 작성해 보세요.
- Python 리스트를 스택처럼 사용 (`append`, `pop`)
- 괄호 짝 매칭은 `dict` 를 사용하면 더 깔끔합니다. 예: `pairs = {')':'(', ']':'[', '}':'{'}`
- 시간복잡도는 `O(N)` 이어야 합니다.

아래 템플릿을 참고해 `isValid` 메서드를 완성하세요.

\"\"\"주어진 문자열 s가 올바른 괄호 문자열인지 판별합니다.

        알고리즘 아이디어:
            TODO: 여기서 스택을 어떻게 사용할지 간단히 설명해 보세요.

            1.문자열을 왼쪽에서 오른쪽으로 한글자씩 순회
            2.if 열린 괄호 \"(\", \"{\" ,\"[\" 이 나오면 스택에 push append
            3.if 닫힌 괄호가 나오면, 스택에서 하나 꺼내 pop 짝이 맞는지 확인
            4.if 스택이 비어있다: 잘못된 문자열 False
              if 스택에서 꺼낸 top과 짝이 맞지 않는다 : 잘못된 문자열 False
              짝은 { \")\" : \"(\" , \"}\" : \"{\", \"]\" : \"[\" }
            5.문자열을 모두 확인(스택을 다 꺼내고) 비어있으면 올바른 문자열 : True

        시간복잡도:
            TODO: 왜 이 알고리즘의 시간복잡도가 O(N)인지 설명해 보세요.
            1번 순회하는 동안 입력된 N개의 문자열을 하나씩 검증하므로 N만큼 걸린다
        \"\"\"




class Solution:
    def isValid(self, s: str) -> bool:

        # TODO: 여기에 스택 기반 알고리즘을 구현하세요.

        stack = [] #괄호 쌓을 리스트
        pair = { \")\" : \"(\" , \"}\" : \"{\", \"]\" : \"[\" }  #짝맞출 딕셔너리

        for x in s:   #s를 하나씩 순회해
            
            if x in pair:       #   - 닫힌 괄호일 때 pair안에 있으면
                    
                if not stack:    #   - 스택이 비어있는 경우 False
                    return False  #pop하기 전에 비어있는지 먼저 확인해야한다

                top = stack.pop()     #stack에 쌓은 마지막것을 꺼내, top이라 하자
                if top != pair[x]:  #꺼낸 top이, pair의 짝과 안맞으면
                    return False  #False
                    
            else: #   - 닫힌 괄호가 아닐 때
                if x in \"({[\":
                    stack.append(x) #  stack에 append 쌓아놔

            #   - 반복이 끝난 뒤 스택이 비어 있는지 확인
        return len(stack) == 0

        raise NotImplementedError


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {\")\": \"(\", \"}\": \"{\", \"]\": \"[\"}
        opens = \"({[\"  # 열린 괄호 정의

        for x in s:
            # 1. 닫힌 괄호인 경우
            if x in pair:
                if not stack:
                    return False
                top = stack.pop()
                if top != pair[x]:
                    return False
            
            # 2. 열린 괄호인 경우에만 스택에 넣기 (수정된 부분)
            elif x in opens:
                stack.append(x)
            
            # 3. 그 외 숫자나 연산자 등은 그냥 무시하고 지나감
            else:
                continue

        return len(stack) == 0

### ✅ 테스트 코드
아래 셀을 실행해서 다양한 입력에 대해 `isValid` 가 올바르게 동작하는지 확인해 보세요.
필요하다면 테스트 케이스를 더 추가해도 좋습니다.

def run_tests():
    sol = Solution()
    tests = [
        (\"()\", True),
        (\"()[]{}\", True),
        (\"(]\", False),
        (\"([)]\", False),
        (\"{[]}\", True),
        (\"(3+4)*(2+5)\",True),
        (\"((2*2)*3+1)\",True),
        (\")(2+2)\",False),
        (\"{(2+1)*(3+2)-22}*7\",True),
        (\"{(7+2}*3)\",False)
    ]

    for s, expected in tests:
        result = sol.isValid(s)
        print(f\"s='{s}' → result={result}, expected={expected}\")

run_tests()


---
## Step 4. 시간복잡도 분석 & 정리

아래에 본인의 코드에 대한 **시간복잡도/공간복잡도 분석**과 함께,
스택이 없었다면 어떤 방식으로 풀 수 있을지(그리고 왜 비효율적인지)를 간단히 적어보세요.

### ✏️ 정리 (학생 작성)

- 시간복잡도 분석:
  - O(N) , 주어진 문자열 N개 만큼 1회 순회
- 공간복잡도 분석:
  - o(N) , 주어진 문자열 N개들의 괄호를 별도로 쌓아서 1회 비교하므로
- 이 문제에서 스택이 왜 잘 맞는 도구인지:
  - 괄호의 특징. 열리면 닫아야 하는 특징 때문에, 가장 마지막에 쌓은 것을 비교해야 하므로
  - 후입선출 LIFO 방식에 어울린다
- 스택을 사용하지 않는다면 어떤 방식이 있을지, 그리고 단점은?
  - 큐는 먼저 넣은것이 먼저 나오므로 짝이 맞지 않음.
  - 해시테이블인 딕셔너리는 개수나 위치를 찾을 때는 유리하지만 순서를 기억해야하는 이 경우에 활용하기 어려울 것 같다.각 괄호가 몇 번째 자리에 있는지를 기억하는 인덱스를 저장하는 방식을 써야 한다. 공간복잡도가 커진다.

---
## 제출 전 체크리스트 ✅
- [ ] 스택(list)을 사용해 구현했다.
- [ ] 스택이 비어 있는 상태에서 `pop` 하지 않도록 예외 처리를 했다.
- [ ] 예제 테스트 케이스가 모두 기대한 값으로 나온다.
- [ ] 시간복잡도 `O(N)` 분석을 코드/마크다운에 적었다.
- [ ] 노트북 상단부터 하단까지 실행이 끊김 없이 잘 동작한다.

수고 많았어요! 🎉 Day 2의 기본 스택 패턴은 이후 수많은 문제의 기본기가 됩니다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위

class Solution:
    def isValid(self, s: str) -> bool:
        \"\"\"주어진 문자열 s가 올바른 괄호 문자열인지 판별합니다.

        알고리즘 아이디어:
            TODO: 여기서 스택을 어떻게 사용할지 간단히 설명해 보세요.

        시간복잡도:
            TODO: 왜 이 알고리즘의 시간복잡도가 O(N)인지 설명해 보세요.
        \"\"\"
        # TODO: 여기에 스택 기반 알고리즘을 구현하세요.
        #   - 열린 괄호일 때의 처리
        #   - 닫힌 괄호일 때의 처리
        #   - 스택이 비어있는 경우 예외 처리
        #   - 반복이 끝난 뒤 스택이 비어 있는지 확인

        q = []
        input_count = 0

        for char in s:
            if ord(char) == 40 or ord(char) == 91 or ord(char) == 123:
              q.append(char)
              input_count += 1
              continue

            if(len(q) <= 0):
              return False

            pop = ord(q.pop())
            pop = pop // 10

            if(pop != ord(char) // 10):
                return False

        if(len(q) == 0 and len(s)/2 == input_count):
          return True
        else:
          return False

        raise NotImplementedError


def run_tests():
    sol = Solution()
    tests = [
        (\"()\", True),
        (\"()[]{}\", True),
        (\"(]\", False),
        (\"([)]\", False),
        (\"{[]}\", True),
        (\"})]}\", False),
        (\"([)]\", False)
    ]

    for s, expected in tests:
        result = sol.isValid(s)
        print(f\"s='{s}' → result={result}, expected={expected}\")

run_tests()
"""
    s.raw_texts['Day3_advanced_mission(문제)_leetcode200.ipynb.txt'] = """# Day 3. 트리와 그래프로 탐색하기 – 심화 미션

이 노트북은 2차원 격자(지도)를 **그래프**로 보는 관점을 연습하고,
DFS 또는 BFS를 사용해 **연결 요소 개수(섬의 개수)** 를 세는 심화 미션용입니다.

문제는 LeetCode **#200 – Number of Islands** 를 기반으로 합니다.

## 🎯 학습 목표
- 2D grid 를 \"정점: 칸, 간선: 상하좌우 인접\"인 그래프로 모델링할 수 있다.
- DFS 또는 BFS로 **연결된 영역(connected component)** 을 순회하는 패턴을 익힌다.
- 방문 처리(visited 배열 또는 grid 값을 변경)의 중요성을 이해한다.
- 다양한 테스트 케이스에서 섬의 개수를 정확히 세고, 대각선 연결은 같은 섬이 아님을 주의한다.

---
## 문제: Number of Islands

> `m x n` 크기의 2D 이진 그리드 `grid` 가 주어질 때,
> 섬(island)의 개수를 반환하세요.

- `'1'` → 땅(land)
- `'0'` → 물(water)
- 상하좌우(가로 또는 세로)로 인접한 `'1'` 들은 **하나의 섬**으로 간주합니다.
- 대각선으로만 연결된 경우는 **다른 섬**입니다.

### 예시
1.
```text
11110
11010
11000
00000
```
→ 섬의 개수: 1

2.
```text
11000
11000
00100
00011
```
→ 섬의 개수: 3

### 제한 조건
- `1 <= m, n <= 300`
- `grid[i][j]` 는 `'0'` 또는 `'1'`

---

## 🛠️ Prerequisites
본 미션은 파이썬 표준 라이브러리를 활용하며, 효율적인 알고리즘 구현을 위해 아래 모듈들을 사용합니다.
* **`from typing import List, Optional`**: 데이터 구조의 타입을 명확히 정의하기 위해 사용합니다.
* **`from collections import deque`**: BFS 탐색 시 효율적인 큐(Queue) 연산을 위해 사용합니다.
* 별도의 외부 패키지 설치는 필요하지 않습니다.

## Step 1. 문제 이해 & 그래프로 바라보기

아래에 **grid를 그래프로 보는 관점**과, \"섬의 개수를 센다\"는 것이 무엇을 의미하는지
자신의 말로 정리해 보세요.

### ✏️ 정리 (학생 작성)

- grid 를 그래프로 본다면, 정점과 간선은 각각 무엇인가?
  - 정점(vertex): 각 칸, 2차원좌표에서 (x,y)로 식별될 수 있는 각각의 칸
  - 간선(edge): 인접한 다른 칸으로 이동할 수 있는 연결성, 지금 문제는 4방향의 엣지가 가능. 상하좌우.현재칸에서 (x+-1, y),(x,y+-1) 만 엣지(간선)연결이 가능
- 섬의 개수를 세는 것은 그래프 용어로 어떤 문제와 동일한가?
  -연결요소(connected components)찾기, 서로 연결되어 있는 정점들의 덩어리가 몇 개 인가?
- 대각선으로만 연결된 `'1'` 들을 다른 섬으로 처리해야 하는 이유:
  - 인접성(adjacency)이 다르다. 문제에서 4방향으로 상하좌우 연결성을 택했다. 따라서 대각선방향으로는 직접적인 간선(엣지)이 없다. 간선이 없으므로 연결요소가 아니며, 서로 다른 섬이다.


---
## Step 2. DFS로 `numIslands` 구현하기

우선 DFS(재귀 또는 스택)를 사용해 섬의 개수를 세는 함수를 구현해 봅시다.

### 아이디어 (DFS 버전)
- 격자의 모든 칸 `(r, c)` 를 순회합니다.
- 만약 `grid[r][c] == '1'` 이고 아직 방문하지 않았다면, **새로운 섬의 시작**입니다.
  - `count += 1`
  - DFS/BFS로 상하좌우로 연결된 모든 `'1'` 를 방문 처리합니다.
- 모든 칸을 검사한 후의 `count` 가 섬의 개수입니다.

방문 처리는 다음 두 방법 중 하나를 선택할 수 있습니다.
1. `visited` 라는 2D 배열을 따로 두기
2. 방문한 육지 칸을 `'1'` → `'0'` 으로 바꾸기 (in-place 변경)

아래 템플릿에서 **DFS 버전**을 먼저 완성해 보세요.

from typing import List

class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        \"\"\"DFS를 이용해 섬의 개수를 세는 함수입니다.

        아이디어:
            TODO: 위에서 정리한 DFS 아이디어를 간단히 적어보세요.
            격자의 모든 칸을 순회, 1,육지를 찾는다.
            육지를 발견하면 그 칸을 방문완료 표시하고, dfs로 연결된 모든 육지를 방문,
            하나의 섬을 완전히 방문완료한다. 과정이 시작될 때마다 섬의 개수를 1 증가.

        시간복잡도:
            TODO: 이 알고리즘의 시간복잡도(O(m * n)) 와 그 이유를 적어보세요.
            m은 행의 갯수, n은 열의 갯수이므로 모든 칸을 방문한다는.
            모든 칸을 1번씩만 방문하므로 전체 칸의 갯수에 비례한다.
        \"\"\"
        # TODO: grid 전체를 순회하며, '1' 을 만나면 DFS로 연결된 영역을 모두 방문 처리하고
        #       섬의 개수를 1 증가시키는 방식으로 구현해 보세요.
        
        if not grid:
            return 0   #base case
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):  #r은 행(row, 세로축), c는 열(column, 가로축)을 의미함
                        #행 번호가 커질수록 아래로 가
                        #열 번호가 커질수록 오른쪽으로 가
            #1. 범위를 벗어나거나 0인경우 탐색 중단
            if r < 0 or r >=0 or c < 0 or c >= n or grid[r][c] == '0':   #base case
                return
            
            grid[r][c] = '0' #방문처리 다시 방문하지 않도록 1을 0으로 바꿈
                
            dfs(r + 1, c) #하 
            dfs(r - 1, c) #상 
            dfs(r, c + 1) #우
            dfs(r, c - 1) #좌????
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1': #육지를 발견하면
                    count += 1          #새로운 섬 카운트
                    dfs(r, c)           #연결된 모든 육지를 0으로
                    
        return count
            #any corner / edge case????
        raise NotImplementedError


### ✅ DFS 버전 테스트 코드
아래 예시들을 포함해, 최소 3개 이상의 테스트 케이스에서 결과를 확인해 보세요.
테스트 케이스를 1~2개 직접 추가하면 더 좋습니다.

def run_tests_dfs():
    sol = SolutionDFS()

    tests = [
        ([list(\"11110\"), list(\"11010\"), list(\"11000\"), list(\"00000\")], 1),
        ([list(\"11000\"), list(\"11000\"), list(\"00100\"), list(\"00011\")], 3),
        ([list(\"0\")], 0),
    ]

    for grid, expected in tests:
        # grid 는 함수 안에서 변경될 수 있으므로, 테스트 간 영향을 막기 위해 복사본 사용
        grid_copy = [row[:] for row in grid]
        result = sol.numIslands(grid_copy)
        print(\"grid=\")
        for row in grid:
            print(\"  \", \"\".join(row))
        print(f\"expected={expected}, result={result}\\n\")

run_tests_dfs()


---
## Step 3. (선택) BFS로도 구현해 보기

여유가 있다면, 이번에는 **BFS(큐)** 를 이용해 같은 문제를 풀어보세요.
DFS 버전과 로직은 거의 같지만, 내부 탐색을 재귀 대신 큐로 구현합니다.

아래 템플릿은 선택 사항이며, 구현하지 않아도 기본 미션은 완료입니다.
하지만 DFS/BFS 둘 다 구현해 보면 그래프 탐색 패턴 이해에 큰 도움이 됩니다 🙂

from collections import deque

class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        \"\"\"BFS(큐)를 이용해 섬의 개수를 세는 함수입니다.

        TODO: BFS 탐색 아이디어를 간단히 정리해 보세요.
        1.격자를 순회하며 1을 발견하면 섬의 개수 count 1 증가
        2.발견된 1의 좌표를 큐에 넣고, 방문처리, 0으로 변경
        3.큐가 빌 때까지 for 문으로 반복:
            - 맨처음 좌표를 큐에서 꺼내,popleft,상하좌우 확인 - bfs방식
            - 인접한 칸 중 1인 곳이 있다면 큐에 넣고 0 으로 변경
        4.큐가 비면 하나의 섬이 가진 모든 육지가 방문처리, 다음탐색
        \"\"\"
        # TODO: DFS 대신 큐를 사용해 상하좌우로 퍼져 나가는 방식으로 구현해 보세요.
        
        if not grid:
            return 0
        
        rows = len(grid) #전체 행 개수
        cols = len(grid[0]) #전체 열 개수
        count = 0   #섬의 개수
        
        #1. 격자 전체를 하나씩 순회
        for r in range(rows):
            for c in range(cols):  #m*n을 순회하므로 O(m*n) 그리드 전체 크기에 비례
                #1을 발견하면 새로운 섬 탐색 시작
                if grid[r][c] == '1':
                    count += 1
                    
                    #2.발견된 1의 좌표를 큐에 넣고 방문처리 (0으로 변경)
                    queue = deque([(r,c)])
                    grid[r][c] = '0'
                    
                    #3.큐가 빌 때까지 반복(연결된 모든 육지 지우기)
                    while queue:
                        curr_r, curr_c = queue.popleft() #큐에서 현재 좌표 꺼내기
                        
                        #상 현재행에서 -1
                        nr, nc = curr_r - 1, curr_c
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            queue.append((nr,nc))
                            grid[nr][nc] = '0'
                            
                        #하 현재행에서 +1    
                        nr, nc = curr_r + 1, curr_c
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            queue.append((nr,nc))
                            grid[nr][nc] = '0'
                            
                        #좌 현재열에서 -1
                        nr, nc = curr_r , curr_c - 1
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            queue.append((nr,nc))
                            grid[nr][nc] = '0'
                            
                        #우 현재열에서 +1
                        nr, nc = curr_r , curr_c + 1
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            queue.append((nr,nc))
                            grid[nr][nc] = '0'
                            
        return count #모든 격자 순회가 끝나면 최종 섬의 개수 반환
                            
        raise NotImplementedError


# 방향 정보를 미리 정의 (이게 벡터입니다!)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

# 이제 4개의 if문 대신 이렇게 씁니다.
for dr, dc in directions:
    nr = curr_r + dr
    nc = curr_c + dc
    
    # 여기서 if문 딱 한 번만 써서 검사합니다.
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
        queue.append((nr, nc))
        grid[nr][nc] = '0'
        
\"\"\"2. 왜 이 방식이 더 좋은가요? (비유 없이)
실수 방지: 아까처럼 if문을 4번 쓰면, 복사해서 붙여넣다가 nr을 nc로 잘못 적거나 +1을 -1로 적는 실수가 자주 일어납니다. 이 방식은 수식 하나만 잘 쓰면 됩니다.

수정의 용이성: 만약 \"대각선까지 포함해서 8방향을 검사하라\"는 요구가 들어오면, directions 리스트에 4개 좌표만 추가하면 끝납니다. if문을 8번 쓸 필요가 없죠.

가독성: \"이 루프는 주변 방향을 탐색하는구나\"라고 로직이 한눈에 들어옵니다.\"\"\"

while queue:
    curr_r, curr_c = queue.popleft()
    
    # 상, 하, 좌, 우 변화량을 반복문으로 돌립니다.
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = curr_r + dr, curr_c + dc
        
        # 경계 검사와 육지 확인을 딱 한 번만 수행!
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
            queue.append((nr, nc))
            grid[nr][nc] = '0'

---
## Step 4. DFS/BFS와 그래프 관점 정리

### ✏️ 정리 (학생 작성)

- 이 문제에서 **정점/간선** 을 어떻게 정의했는지 다시 한 번 정리해 보세요.
  - 정점은 각각의 행,열에 따른 각 칸, 간선은 각 칸의 연결, 4방향 간선.
- DFS를 사용할 때의 장점 / 단점:
  -코드가 간결해보인다, 내부 동작이 복잡하다, 섬이 너무 크면 강제종료,
- BFS를 사용할 때의 장점 / 단점 (구현했다면):
  -할 일을 전부 나열해서 코드가 길고 복잡해보인다, 동작이 투명하다, 섬이 아무리 커도 차근차근 다 지운다
- 섬의 개수를 세는 문제를 다른 도메인(예: 영역 개수 세기, 네트워크 컴포넌트 개수 등)에
  어떻게 응용할 수 있을지 떠오르는 예시:
  -네트워크! 수업중 교수님이 말씀하신, 소셜네트워크 분석, 게임에서의 스킬트리?
  서로 영향을 주고 받는 개체들을 하나의 덩어리로 묶어서 전체 덩어리가 몇개인지 파악하는 것

---
## ✅ 제출 전 체크리스트
- [ ] 다양한 테스트 케이스에서 섬의 개수가 정확하게 계산된다.
- [ ] 대각선으로만 연결된 `'1'` 들은 **다른 섬**으로 처리된다.
- [ ] DFS 또는 BFS 중 최소 한 가지 방식으로 완성된 구현이 있다.
- [ ] 방문 처리 방식이 일관되고, 무한 루프 없이 종료된다.
- [ ] grid 를 그래프로 보는 관점과, DFS/BFS가 \"그래프 탐색\"이라는 사실을 설명할 수 있다.

수고 많았습니다! 🌊 Day 3 심화 미션까지 완료했다면, 트리와 그래프 탐색의 핵심 패턴을
한 번씩 모두 경험한 것입니다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위

def dfs(self):
    unvisted = self.v.copy()
    stack = stack()

    while not unvisited.is_empty():
        visit(unvisited[0]) #visit origin
        stack.push(unvisted[0])
        del unvisted[0]
        
        while not stack.is_empty():
            curr = stack.peek()
            if there remains an unvisited city from curr:
                next = select an unvisited city from curr
                visit(next)
                stack.push(next)
                delete next from unvisited
                
            else:
                stack.pop() #backtracking

from collections import deque

class undirected_graph():
    def __init__(self, nodes, edges):
        self.v = nodes[:] 
        self.e = {node: [] for node in nodes} 
        for (u, v) in edges:
            self.e[u].append(v) 
            self.e[v].append(u) 

    def dfs(self):
        unvisited = self.v[:] 
        visited_order = []    
        stack = []            

        while unvisited: 
            start_node = unvisited[0] 
            
            visited_order.append(start_node) 
            stack.append(start_node)         
            unvisited.remove(start_node)     
                
            while stack: 
                curr = stack[-1] 
                found_next = False 
                
                for neighbor in self.e[curr]: 
                    if neighbor in unvisited: 
                        visited_order.append(neighbor) 
                        stack.append(neighbor)         
                        unvisited.remove(neighbor)     
                        found_next = True 
                        break 
                
                # [중요] if문은 while stack 안에, for문 밖에 있어야 함
                if not found_next: 
                    stack.pop() 
                        
        return visited_order

    def bfs(self):
        unvisited = self.v[:]  
        visited_order = []     
        queue = deque()        

        while unvisited:       
            start_node = unvisited[0] 
            queue.append(start_node)  
            unvisited.remove(start_node) 

            while queue:       
                curr = queue.popleft() 
                visited_order.append(curr) 

                for neighbor in self.e[curr]: 
                    if neighbor in unvisited: 
                        queue.append(neighbor) 
                        unvisited.remove(neighbor)
            
        return visited_order

def bfs(self):
    unvisited = self.v.copy()
    queue = Queue()
    while not unvisited.is_empty():
        queue.enqueue(some unvisited node)
        
        while not queue.is_empty():
            curr = queue.dequeue()
            visit(curr)
            delete curr from unvisited
            
            for city in all unvisited cities connected from curr:
                queue.enqueue(city)
                



###테스트코드
# 1. 그래프 데이터 준비
# 노드: a, b, c, d (서로 연결됨) / e, f (둘이서만 연결됨)
nodes = ['a', 'b', 'c', 'd', 'e', 'f']
edges = [
    ('a', 'b'), ('a', 'c'), 
    ('b', 'd'), ('c', 'd'),
    ('e', 'f')
]

# 2. 그래프 객체 생성
graph = undirected_graph(nodes, edges)

# 3. DFS 실행
dfs_result = graph.dfs()
print(f\"DFS 방문 순서: {dfs_result}\")

# 4. BFS 실행
bfs_result = graph.bfs()
print(f\"BFS 방문 순서: {bfs_result}\")

#accomplicationQuestion

\"\"\"Symmetric 두 이진트리가 대칭 확인, 거울에 비친 듯 같은지 확인하는\"\"\"
def Symmetric(root1, root2):
    if not root1 and not root2: #둘 다 비어있ㅇ면 같은것 true
        return True
    
    if not root1 or not root2 or root1.val != root2.val:
        #한쪽만 비거나, 값이 다르면 짝이 안맞다. false
        return False
    
    return Symmetric(root1.left,root2.right) and Symmetric(root1.right, root2.left)
# 왼쪽-오른쪽, 오른쪽-왼쪽 이 서로 대칭인지 확인



\"\"\"Balance 두 이진트리가 균형인지 확인, 왼쪽과 오른쪽의 키 차이가 1보다 크면 안된다는 규칙 검사\"\"\"
def checkHeight(node):
    if not node: return 0 #노드가 비어있으면 height는 0
    
    left_h = checkHeight(node.left)
    right_h = checkHeight(node.right)
    
    if left_h == -1 or right_h == -1 : return -1
    #불균형 -1 이 발견된다면 불합격 -1 반환
    
    if abs(left_h - right_h) > 1: return -1
    #키차이가 1보다 크면 불합격 -1로 반환
    
    return max(left_h, right_h) + 1
    #정상이면 더 큰쪽 높이에 1을 더해 보고??
    
def Balanced(root):
    return checkHeight(root) != -1


\"\"\"유효한 바이너리 서치 트리 BST 인지 확인, 모든 왼쪽은 나보다 작고, 모든 오른쪽은 나보다 큰지 검사\"\"\"
def validBST(node, min_val=float('-inf'), max_val=float('inf')):
    #끝까지 에러없이 내려가면 true
    if not node: return True
    
    #현재 노드의 값이 정해진 범위(min~max)를 벗어나면 false
    if not (min_val < node.val < max_val):
        return False

    #왼쪽으로 갈 땐 최대값을 나로 제한, 오른쪽으로갈 땐 최소값을 나로 제한
    return (validBST(node.left, min_val, node.val) and 
            validBST(node.right, node.val, max_val))  
    #왼쪽으로 갈때 최소값min_val은 그대로 지키되, 최대값은 나node.val보다작아야해, 
    #오른쪽으로 갈때 최대값max_val은 그대로 유지하되, 최소값은 나node.val보다는 커야해
    #왼쪽으로도 오른쪽으로도 합격이어야 전체가 합격
    
\"\"\"노드마다 고유한 허용범위를 부여하고, 아래로 내려갈수록 그범위를 깍아감
모든 노드를 딱 한번씩만 검사하므로 시간복잡도 O(N)\"\"\"



"""
    s.raw_texts['Day3_daily_mission(문제)_leetcode104.ipynb.txt'] = """# Day 3. 트리와 그래프로 탐색하기 – 데일리 미션

이 노트북은 **이진 트리의 최대 깊이(Maximum Depth)** 를 구하는 문제를 통해
재귀 DFS와 BFS(레벨 순회)를 모두 연습하는 데일리 미션용입니다.

문제는 LeetCode **#104 – Maximum Depth of Binary Tree** 를 기반으로 합니다.

## 🎯 학습 목표
- 이진 트리의 **높이(최대 깊이) 정의**를 명확히 이해한다.
- 재귀 DFS로 \"현재 노드 기준 서브트리의 높이\"를 계산하는 패턴을 익힌다.
- `collections.deque` 를 이용한 **BFS 레벨 순회**로 깊이를 구해 본다.
- DFS와 BFS의 차이를 **호출 스택 vs 큐**, 재귀 vs 반복 관점에서 비교한다.

---
## 문제: Maximum Depth of Binary Tree

> 이진 트리의 루트 노드 `root` 가 주어졌을 때, 이 트리의 **최대 깊이(maximum depth)** 를 반환하세요.

- 최대 깊이란, **루트에서 가장 깊은 리프까지 가는 경로에 포함된 노드의 개수**입니다.
- 빈 트리(`root is None`) 라면 깊이는 `0` 입니다.

### 예시
1. `root = [3,9,20,null,null,15,7]` → 출력: `3`
2. `root = [1,null,2]` → 출력: `2`

### 제한 조건
- 트리의 노드 개수: `0 <= number of nodes <= 10^4`
- 각 노드 값: `-100 <= Node.val <= 100`

---
이제 아래 **Step 1 → Step 4** 순서로 미션을 진행해 주세요.

## 🛠️ Prerequisites
본 미션은 파이썬 표준 라이브러리를 활용하며, 효율적인 알고리즘 구현을 위해 아래 모듈들을 사용합니다.
* **`from typing import List, Optional`**: 데이터 구조의 타입을 명확히 정의하기 위해 사용합니다.
* **`from collections import deque`**: BFS 탐색 시 효율적인 큐(Queue) 연산을 위해 사용합니다.
* 별도의 외부 패키지 설치는 필요하지 않습니다.

## Step 1. 문제 이해 및 TreeNode 구조 복습

LeetCode에서 사용하는 `TreeNode` 클래스는 다음과 같이 정의되어 있습니다.

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

아래 셀에 **내가 이해한 '트리의 최대 깊이' 정의**와
`root is None` 인 경우 어떤 값을 반환해야 하는지 정리해 보세요.

### ✏️ 내가 이해한 문제 (학생 작성)

- 트리의 최대 깊이란 무엇인가?
  - 더 이상 이어지는 엣지가 없는 트리중 가장 height가 큰 것
  - 가장 깊은 리프까지 가는데 포함된 노드의 갯수
- 루트가 없는 빈 트리(`root is None`) 의 깊이는 왜 0이어야 할까?
  - 트리는 루트 아래 이어지는 노드가 있어야 하는데, 시작하는 루트조차 없으니까 height == 0 이다




---
## Step 2. 재귀 DFS로 최대 깊이 구현하기

DFS(깊이 우선 탐색)를 이용하면, **현재 노드 기준으로 왼쪽/오른쪽 서브트리의 높이**를 각각 구한 뒤
그 중 큰 값에 1을 더해서 현재 노드의 높이를 구할 수 있습니다.

### 아이디어
- 기저 사례(base case): 노드가 `None` 이면 높이는 0
- 재귀 관계: `1 + max(왼쪽 서브트리 높이, 오른쪽 서브트리 높이)`

아래 템플릿의 `maxDepth_dfs` 를 재귀 DFS 방식으로 구현해 보세요.

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


class SolutionDFS:
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        \"\"\"재귀 DFS를 사용하여 이진 트리의 최대 깊이를 계산합니다.

        아이디어:
            TODO: 위에서 정리한 DFS 아이디어를 간단히 한 줄로 적어보세요.
                    루트부터 바닥까지 내려가며 1+max(왼쪽 깊이, 오른쪽 깊이) 반복
                
        시간복잡도:
            TODO: 이 알고리즘의 시간복잡도와 그 이유를 적어보세요. (힌트: 모든 노드를 정확히 한 번씩 방문)
                    O(N) 트리 내 모든 노드를 한 번씩 방문하므로
        \"\"\"
        # TODO: 기저 사례와 재귀 관계를 이용해 함수를 완성해 보세요.
        
        if root is None:
            return 0
        #노드가 없으면 깊이는 0, 재귀가 멈추는 지점
        
        left_depth = self.maxDepth_dfs(root.left) #왼쪽 몇층?
        right_depth = self.maxDepth_dfs(root.right) #오른쪽 몇층?
        
        return max(left_depth,right_depth) + 1
        # 왼쪽과 오른쪽중 더 깊은 쪽을 선택하고 현재 노드의 높이인 1을 더함
        \"\"\"왼쪽이 2층이고 오른쪽이 3층이라면, 더 높은쪽인 3층을 고르고, 현재노드도 한 층을 차지하니까
        +1을 해서 최종적으로 4층이라고 보고하는 것\"\"\"
        raise NotImplementedError


\"\"\"개념은 사알짝 알겠는데, 표현하는걸 모르겠어, 
아래 테스트코드의 인풋부터 저게 왜 트리이지?? 하고 있는데\"\"\"

### ✅ DFS 버전 테스트 코드
아래에는 리스트 표현을 이용해 간단한 트리를 만들어주는 헬퍼 함수가 있습니다.
DFS 버전을 구현한 뒤 셀을 실행해 정상 동작하는지 확인해 보세요.

리스트 표현은 LeetCode 스타일의 **level-order** 표기법을 간단히 흉내낸 것입니다.
(`None` 은 자식이 없음을 의미합니다.)

from collections import deque

def build_tree_from_list(values: list[int | None]) -> TreeNode | None:
    \"\"\"간단한 level-order 리스트 표현으로부터 이진 트리를 생성하는 헬퍼 함수입니다.
    예: [3, 9, 20, None, None, 15, 7]
    \"\"\"
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    queue: deque[TreeNode] = deque([root])

    for val_left, val_right in zip(it, it):
        node = queue.popleft()
        if val_left is not None:
            node.left = TreeNode(val_left)
            queue.append(node.left)
        if val_right is not None:
            node.right = TreeNode(val_right)
            queue.append(node.right)
    return root


# 간단한 테스트
examples = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),
]

solver = SolutionDFS()
for arr, expected in examples:
    root = build_tree_from_list(arr)
    result = solver.maxDepth_dfs(root)
    print(f\"input={arr}, expected={expected}, result={result}\")


---
## Step 3. BFS(레벨 순회)로 최대 깊이 구현하기

이번에는 **큐(queue)** 를 사용해 트리를 레벨 단위로 순회하면서 깊이를 구해 보겠습니다.

### 아이디어 (한 가지 방식 예시)
- 큐에 `(노드, 현재 깊이)` 를 함께 넣고, 하나씩 꺼내면서 최대 깊이를 갱신한다.
  또는
- \"현재 큐 길이만큼 반복 → 한 레벨 처리 → `depth += 1`\" 패턴을 사용한다.

어느 쪽이든 상관 없지만, 코드 안에 **어떤 방식으로 깊이를 증가시켰는지** 주석으로 설명해 보세요.

from collections import deque

class SolutionBFS:
    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        \"\"\"BFS(레벨 순회)를 사용하여 이진 트리의 최대 깊이를 계산합니다.

        아이디어:
            TODO: 큐를 어떻게 사용해 레벨 단위로 깊이를 세는지 요약해 보세요.
                FIFO, 방문하는 노드에 인덱스를 부텨 주면서, 그 인덱스 순서로 찾아가서 붙어 있는
                노드들에 방문, 반복. 지금 몇 번째 층을 다 훑었는지를 세는.
                큐를 사용해 같은 층에 있는 노드들을 한꺼번에 처리. 연결된 노드를 넣어 한 층이 처리가 끝날때마다
                깊이를 1씩 증가
        시간복잡도:
            TODO: 이 알고리즘의 시간복잡도와 그 이유를 적어보세요.
                모든 노드를 한 번 씩 큐에 넣고 빼야하니까, O(N) 노드 갯수에 비례
                
        \"\"\"
        # TODO: BFS 레벨 순회 방식으로 구현해 보세요.
        if not root:
            return 0 #루트가 비었으면 0
        
        queue = deque([root]) #초기화 : 루트노드를 큐에 삽입
        depth = 0 #시작, 깊이 카운터
        
        while queue:  #큐가 빌 때까지 반복(트리의 모든 레벨을 순회)
            level_size = len(queue) #현재 레벨의 노드 갯수 측정
            
            for _ in range(level_size): #현재 레벨에 있는 노드들만 모두 꺼내
                curr_node = queue.popleft() #큐의 맨 앞 노드 추출
                if curr_node.left:  #추출된 노드의 자식노드들을 차례로 큐에 삽입
                    queue.append(curr_node.left) #왼쪽거 왼쪽에
                if curr_node.right:
                    queue.append(curr_node.right) #오른쪽거 오른쪽에
                    
            depth += 1 #한층 훑어서 깊이 증가
            \"\"\"한 레벨의 모든 노드들을 다 뽑아내고 나면, 큐에는 오직
                        다음레벨의 노드들만 남는. 이때 뎁스 1 증가\"\"\"
        
        return depth
        raise NotImplementedError


### ✅ DFS / BFS 결과 비교 테스트
DFS와 BFS가 **항상 동일한 결과**를 내는지 확인해 보세요.
테스트 케이스를 1~2개 더 추가해도 좋습니다.

solver_dfs = SolutionDFS()
solver_bfs = SolutionBFS()

examples = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),
    ([1, 2, 3, 4, 5, None, None], 3),  # 추가 예시
]

for arr, expected in examples:
    root = build_tree_from_list(arr)
    d = solver_dfs.maxDepth_dfs(root)
    b = solver_bfs.maxDepth_bfs(root)
    print(f\"input={arr}\\n  expected={expected}, dfs={d}, bfs={b}\\n\")
    
    
    
# 추가할 테스트 케이스
extra_examples = [
    ([1, 2, None, 3, None, 4, None], 4),      # 케이스 1: 왼쪽 편향 트리
    ([1, 2, 3, 4, 5, 6, 7], 3),               # 케이스 2: 꽉 찬 이진 트리
]

for arr, expected in extra_examples:
    root = build_tree_from_list(arr)
    d = solver_dfs.maxDepth_dfs(root)
    b = solver_bfs.maxDepth_bfs(root)
    print(f\"input={arr}\\n  expected={expected}, dfs={d}, bfs={b}\\n\")


---
## Step 4. DFS vs BFS 차이점 정리

아래에 두 방식의 차이를 정리해 봅시다.

### 비교 관점
- 사용하는 자료구조 (호출 스택 vs 큐)  재귀호출(시스템 스택) vs FIFO자료구조 queue
- 재귀 vs 반복  경로별 끝까지 갔다가 복귀 vs 레벨 별로 한층씩 훑기
- 구현 난이도 / 직관성   dfs가 bfs보다 코드가 간결하고 직관적
- 시간복잡도 / 공간복잡도   시간복잡도는 같다./ dfs는 트리가 옆으로 넓어도 깊지 않으면 메모리를
                          적게 쓰고, bfs는 트리가 아무리 깊어도 넓지 않으면 메모리를 적게 쓴다

### ✏️ 정리 (학생 작성)

- DFS 방식의 장점 / 단점:
  - 코드가 간결하다. 위에서처럼 몇 줄 정도/ 
    직관적. 내 높이는 자식높이+1이라는 논리가 트리구조와 잘 맞는다
    트리가 너무 깊어지면 (수만개 노드가 한줄이면) 강제종료
- BFS 방식의 장점 / 단점:
  -루트에서 가장 가까운 층부터 차례대로 내려가므로 가장가까운노드 를 찾을때 유리
   트리가 옆으로 넓을 경우, 마지막 레벨 근처에서 한꺼번에 많은 노드가 큐에 담겨 
   메모리 사용량 증가
   구현이 복잡함, 큐, 루프구성 등 작성할 코드가 dfs보다 많다
- 두 방법 모두의 시간복잡도는 왜 O(N) 인가?
  - 두 방법 모두 노드의 갯수만큼만 딱 한 번 순회하므로
- 내가 실무/코딩 테스트에서 이 문제를 만난다면 어떤 방식을 선택할지?
  - 경우에 따라 달리 해야겠네. 어떤 트리인지 모르면 간결한 dfs를 선택.


---
## ✅ 제출 전 체크리스트
- [ ] `root is None` 인 경우에도 에러 없이 동작한다.
- [ ] DFS 재귀 버전에서 기저 사례와 재귀 관계가 명확하다.
- [ ] BFS 버전에서 큐를 사용해 레벨 단위로 순회하며 깊이를 올바르게 계산한다.
- [ ] 최소 3개 이상의 테스트 케이스에서 DFS/BFS 결과가 일치한다.
- [ ] 노트북 안에 코드와 결과, 간단한 설명이 함께 정리되어 있다.

수고했어요! 😊 이제 2D grid를 그래프로 보는 심화 미션으로 넘어가 봅시다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day4_advanced_mission(문제)-checkpoint.ipynb.txt'] = """# Day 4. 힙과 이진 탐색으로 문제 해결하기 – 심화 미션 (Rotated Sorted Array)

이 노트북은 **회전된 정렬 배열(rotated sorted array)** 에서 이진 탐색을 변형하여
원소를 찾는 문제를 다루는 심화 미션용입니다.

문제는 LeetCode **Search in Rotated Sorted Array** 를 기반으로 합니다.

## 🎯 학습 목표
- 회전된 정렬 배열의 구조를 이해한다.
- \"항상 한 쪽 구간은 정렬되어 있다\"는 성질을 이용해
  **변형된 이진 탐색 O(log n)** 알고리즘을 설계한다.
- 선형 탐색(`O(n)`)이 아닌, 진짜 로그 시간 탐색을 구현하는 연습을 한다.

---
## 문제: Search in Rotated Sorted Array

> **서로 다른(distinct) 정수** 로 구성된 오름차순 정렬 배열 `nums` 가 있습니다.
> 이 배열은 어떤 알 수 없는 인덱스 `k` 에서 **왼쪽으로 회전(left rotated)** 되었을 수 있습니다.

예를 들어,
- 원래 배열: `[0,1,2,4,5,6,7]`
- 인덱스 3만큼 회전 → `[4,5,6,7,0,1,2]`

이제 회전되었을 수도 있는 배열 `nums` 와 정수 `target` 이 주어졌을 때,
- `target` 이 배열 안에 존재하면 그 **인덱스** 를,
- 존재하지 않으면 `-1` 을 반환하세요.

### 예시
1. `nums = [4,5,6,7,0,1,2], target = 0` → `4`
2. `nums = [4,5,6,7,0,1,2], target = 3` → `-1`
3. `nums = [1], target = 0` → `-1`

### 제한 조건 (요약)
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i], target <= 10^4`
- `nums` 의 모든 값은 **서로 다르며**, 원래는 오름차순 정렬 상태였다가 회전되었을 수 있습니다.
- 알고리즘은 반드시 **O(log n)** 이어야 합니다.

---

## 🛠️ Prerequisites
본 미션은 파이썬 표준 라이브러리를 활용하며, 효율적인 알고리즘 구현을 위해 아래 모듈들을 사용합니다.
* **`from typing import List, Optional`**: 데이터 구조의 타입을 명확히 정의하기 위해 사용합니다.

## Step 1. 문제 이해 & 단순 접근과의 비교

먼저 이 문제를 **그냥 선형 탐색으로 풀면** 어떻게 되는지, 그리고 왜 안 되는지 생각해 봅시다.

### ✏️ 정리 (학생 작성)

- 단순 선형 탐색(linear search)로 풀면 시간복잡도는 얼마인가? 여기서 왜 요구 조건에 안 맞는가?
  - 전부 하나씩 다 봐야한다. O(N). 요구한 O(logN)에 맞지 않는다.\"logN 이려면 반드시 범위의 절반을 날려야 한다\"
  - 
  - 
- 회전되기 전의 배열 구조는 어떤 모습이며, 회전 후에는 어떤 특징을 가지는가?
  -회전되기 전에 오름차순, 회전 후 모든 요소의 인덱스가 (-(len(nums)-k))
- 배열에 끊긴 지점이 생기고, 그 지점을 기준으로 양쪽으로 각각의 오름차순이 생김
  
- 이 문제에서 이진 탐색을 그대로 적용할 수 없는 이유와,
  \"한 쪽 구간은 항상 정렬되어 있다\"는 관찰이 왜 중요한지:
  - 회전했을 수도 있고, 아닐 수도 있기 때문에 확정해야 하는 이진 탐색은 불가.
  - 회전여부가 확정되면 쓸 수 있지 않나?
  - 항상 정렬되어 있는 한쪽 구간은 이진탐색을 쓸수 있다?!


---
## Step 2. 핵심 아이디어: 항상 한 쪽 구간은 정렬되어 있다

이 문제의 핵심은 다음 한 줄로 요약됩니다.

> `mid` 를 기준으로 왼쪽 구간 또는 오른쪽 구간 중 **한 쪽은 반드시 정렬되어 있다.**

### 알고리즘 개요
1. 항상 이진 탐색처럼 `left`, `right`, `mid` 를 유지합니다.
2. `nums[left] <= nums[mid]` 이면, **왼쪽 구간이 정렬** 되어 있는 것입니다.
   - 이 경우, `target` 이 왼쪽 정렬 구간 안에 있는지 범위를 비교해서
     - 왼쪽으로 탐색 범위를 줄일지,
     - 오른쪽을 볼지 결정합니다.
3. 그렇지 않으면, **오른쪽 구간이 정렬** 되어 있는 경우입니다.
   - 이때도 마찬가지로, `target` 이 오른쪽 정렬 구간 안에 속하는지 보고
     어느 쪽을 버릴지 결정합니다.

아래에 본인이 이해한 분기 로직을 자연어로 한 번 더 정리해 보세요.

### ✏️ 정렬 구간 판별 & 분기 로직 요약 (학생 작성)

- `nums[left] <= nums[mid]` 인 경우 (왼쪽 구간 정렬):
  - 이때 `target` 이 왼쪽 구간에 속하는 조건은?
    -if nums[left]<= target <= mid
  - 속하면 어디를 남기고, 어디를 버리는가?
    -왼쪽을 남기고, 오른쪽 버림
     right = mid -1, else left = mid + 1
- 반대로 오른쪽 구간이 정렬된 경우:
  - 이때 `target` 이 오른쪽 구간에 속하는 조건은?
    -if mid =< target =< nums[right]
  - 속하면 어디를 남기고, 어디를 버리는가?
    -왼쪽 버리고 , 오른쪽 남김
    left = mid +1, else right = mid -1


---
## Step 3. 변형된 이진 탐색 구현하기

이제 위에서 정리한 아이디어를 코드로 옮겨봅시다.

### 요구 사항
- 함수 시그니처:
  ```python
  class Solution:
      def search(self, nums: List[int], target: int) -> int:
  ```
- `target` 이 존재하면 **인덱스** 를, 없으면 `-1` 을 반환합니다.
- 시간복잡도는 반드시 `O(log n)` 이어야 합니다.
- 선형 탐색(`for` 로 전체를 도는 방식)이나 슬라이싱 기반 탐색은 사용하지 않습니다.

아래 템플릿을 완성해 보세요.

from typing import List

#데일리미션의 퀵셀렉트와 비슷한데???


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        \"\"\"회전된 정렬 배열에서 target의 인덱스를 찾습니다.

        아이디어:
            - 매 반복마다 mid를 기준으로 왼쪽/오른쪽 중 어느 쪽이 정렬 구간인지 판별합니다.
            - target이 정렬된 구간 안에 속하는지에 따라 탐색 범위를 절반으로 줄입니다.

        시간복잡도:
            - 매 단계마다 탐색 범위를 절반으로 줄이므로 O(log n) 입니다.
        \"\"\"
        left, right = 0, len(nums) - 1
        
        while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[left] <= nums[mid]:
                    if nums[left]<= target < nums[mid]:
                        right = mid - 1
                    else: left = mid + 1
                                            
                else: # nums[right] >= nums[mid]
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else: right = mid - 1
        return -1
        # TODO: while 루프 안에서 mid를 계산하고,
        #       정렬된 구간을 판별한 뒤, target의 위치에 따라
        #       left/right 를 조정하는 로직을 작성해 보세요.
        # 힌트:
        #   - if nums[mid] == target: 바로 mid 반환
        #   - elif 왼쪽 구간이 정렬되어 있다면:
        #        target이 왼쪽 구간에 속하는지 비교 후, left/right 이동
        #   - else: 오른쪽 구간이 정렬되어 있는 경우
        #        target이 오른쪽 구간에 속하는지 비교 후, left/right 이동

        raise NotImplementedError


### ✅ 테스트 코드
아래 셀을 실행해 예시 입력 및 몇 가지 추가 케이스에서 결과를 확인해 보세요.
테스트 케이스를 스스로 더 추가해 보면 좋습니다.

def run_tests():
    sol = Solution()
    tests = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([5,1,3], 3, 2),
        ([5,1,3], 5, 0),
        ([1,2,3,4,5,6,7,8,9],5,4)
    ]

    for nums, target, expected in tests:
        result = sol.search(nums, target)
        print(f\"nums={nums}, target={target} → result={result}, expected={expected}\")

run_tests()


---
## Step 4. 정리 및 자기 점검

### ✏️ 정리 (학생 작성)

- 이 문제에서 **정렬 + 탐색** 사고가 어떻게 사용되었는지 한 문단으로 요약해 보세요.
  -피벗한 mid를 기준으로 좌우의 정렬되어있을 것을 가정하고, 타겟을 탐색하며 범위를 좁혀가며 찾는다.
- 내가 작성한 코드에서 가장 헷갈렸던 조건(또는 버그가 많이 났던 부분)은?
  -정렬되어 있다면을 가정하여 타겟의 값을 비교하며 시작과 끝점을 이동하는 부분이 헷갈렸음
- 회전이 전혀 없는 경우(그냥 정렬 배열)에도 코드가 잘 동작하는지?
  -ㅇㅇ
- 동일한 패턴을 적용할 수 있을 것 같은 다른 문제 유형(예: 최소값 찾기, 중복 허용 버전 등):
  -회전된 정렬배열에서 최소값 찾기
  -산모양배열에서 최대값찾기

---
## ✅ 제출 전 체크리스트
- [ ] 선형 탐색이 아닌, 변형된 이진 탐색으로 구현했다.
- [ ] 회전된 배열의 구조 및 \"한 쪽 구간은 정렬\" 조건을 코드로 잘 옮겼다.
- [ ] target이 존재할 때는 인덱스, 없을 때는 -1을 반환한다.
- [ ] 예시 및 추가 테스트 케이스에서 기대한 결과가 나온다.
- [ ] 전체 알고리즘의 시간복잡도가 `O(log n)` 임을 설명할 수 있다.

수고 많았습니다! Day 4 심화 미션까지 완료했다면, 힙과 이진 탐색을 활용한
대표적인 패턴들을 한 번씩 모두 경험한 것입니다 🎯


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day4_advanced_mission(문제).ipynb.txt'] = """# Day 4. 힙과 이진 탐색으로 문제 해결하기 – 심화 미션 (Rotated Sorted Array)

이 노트북은 **회전된 정렬 배열(rotated sorted array)** 에서 이진 탐색을 변형하여
원소를 찾는 문제를 다루는 심화 미션용입니다.

문제는 LeetCode **Search in Rotated Sorted Array** 를 기반으로 합니다.

## 🎯 학습 목표
- 회전된 정렬 배열의 구조를 이해한다.
- \"항상 한 쪽 구간은 정렬되어 있다\"는 성질을 이용해
  **변형된 이진 탐색 O(log n)** 알고리즘을 설계한다.
- 선형 탐색(`O(n)`)이 아닌, 진짜 로그 시간 탐색을 구현하는 연습을 한다.

---
## 문제: Search in Rotated Sorted Array

> **서로 다른(distinct) 정수** 로 구성된 오름차순 정렬 배열 `nums` 가 있습니다.
> 이 배열은 어떤 알 수 없는 인덱스 `k` 에서 **왼쪽으로 회전(left rotated)** 되었을 수 있습니다.

예를 들어,
- 원래 배열: `[0,1,2,4,5,6,7]`
- 인덱스 3만큼 회전 → `[4,5,6,7,0,1,2]`

이제 회전되었을 수도 있는 배열 `nums` 와 정수 `target` 이 주어졌을 때,
- `target` 이 배열 안에 존재하면 그 **인덱스** 를,
- 존재하지 않으면 `-1` 을 반환하세요.

### 예시
1. `nums = [4,5,6,7,0,1,2], target = 0` → `4`
2. `nums = [4,5,6,7,0,1,2], target = 3` → `-1`
3. `nums = [1], target = 0` → `-1`

### 제한 조건 (요약)
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i], target <= 10^4`
- `nums` 의 모든 값은 **서로 다르며**, 원래는 오름차순 정렬 상태였다가 회전되었을 수 있습니다.
- 알고리즘은 반드시 **O(log n)** 이어야 합니다.

---

## 🛠️ Prerequisites
본 미션은 파이썬 표준 라이브러리를 활용하며, 효율적인 알고리즘 구현을 위해 아래 모듈들을 사용합니다.
* **`from typing import List, Optional`**: 데이터 구조의 타입을 명확히 정의하기 위해 사용합니다.

## Step 1. 문제 이해 & 단순 접근과의 비교

먼저 이 문제를 **그냥 선형 탐색으로 풀면** 어떻게 되는지, 그리고 왜 안 되는지 생각해 봅시다.

### ✏️ 정리 (학생 작성)

- 단순 선형 탐색(linear search)로 풀면 시간복잡도는 얼마인가? 여기서 왜 요구 조건에 안 맞는가?
  - 전부 하나씩 다 봐야한다. O(N). 요구한 O(logN)에 맞지 않는다.\"logN 이려면 반드시 범위의 절반을 날려야 한다\"
  - 
  - 
- 회전되기 전의 배열 구조는 어떤 모습이며, 회전 후에는 어떤 특징을 가지는가?
  -회전되기 전에 오름차순, 회전 후 모든 요소의 인덱스가 (-(len(nums)-k))
- 배열에 끊긴 지점이 생기고, 그 지점을 기준으로 양쪽으로 각각의 오름차순이 생김
  
- 이 문제에서 이진 탐색을 그대로 적용할 수 없는 이유와,
  \"한 쪽 구간은 항상 정렬되어 있다\"는 관찰이 왜 중요한지:
  - 회전했을 수도 있고, 아닐 수도 있기 때문에 확정해야 하는 이진 탐색은 불가.
  - 회전여부가 확정되면 쓸 수 있지 않나?
  - 항상 정렬되어 있는 한쪽 구간은 이진탐색을 쓸수 있다?!


---
## Step 2. 핵심 아이디어: 항상 한 쪽 구간은 정렬되어 있다

이 문제의 핵심은 다음 한 줄로 요약됩니다.

> `mid` 를 기준으로 왼쪽 구간 또는 오른쪽 구간 중 **한 쪽은 반드시 정렬되어 있다.**

### 알고리즘 개요
1. 항상 이진 탐색처럼 `left`, `right`, `mid` 를 유지합니다.
2. `nums[left] <= nums[mid]` 이면, **왼쪽 구간이 정렬** 되어 있는 것입니다.
   - 이 경우, `target` 이 왼쪽 정렬 구간 안에 있는지 범위를 비교해서
     - 왼쪽으로 탐색 범위를 줄일지,
     - 오른쪽을 볼지 결정합니다.
3. 그렇지 않으면, **오른쪽 구간이 정렬** 되어 있는 경우입니다.
   - 이때도 마찬가지로, `target` 이 오른쪽 정렬 구간 안에 속하는지 보고
     어느 쪽을 버릴지 결정합니다.

아래에 본인이 이해한 분기 로직을 자연어로 한 번 더 정리해 보세요.

### ✏️ 정렬 구간 판별 & 분기 로직 요약 (학생 작성)

- `nums[left] <= nums[mid]` 인 경우 (왼쪽 구간 정렬):
  - 이때 `target` 이 왼쪽 구간에 속하는 조건은?
    -if nums[left]<= target <= mid
  - 속하면 어디를 남기고, 어디를 버리는가?
    -왼쪽을 남기고, 오른쪽 버림
     right = mid -1, else left = mid + 1
- 반대로 오른쪽 구간이 정렬된 경우:
  - 이때 `target` 이 오른쪽 구간에 속하는 조건은?
    -if mid =< target =< nums[right]
  - 속하면 어디를 남기고, 어디를 버리는가?
    -왼쪽 버리고 , 오른쪽 남김
    left = mid +1, else right = mid -1


---
## Step 3. 변형된 이진 탐색 구현하기

이제 위에서 정리한 아이디어를 코드로 옮겨봅시다.

### 요구 사항
- 함수 시그니처:
  ```python
  class Solution:
      def search(self, nums: List[int], target: int) -> int:
  ```
- `target` 이 존재하면 **인덱스** 를, 없으면 `-1` 을 반환합니다.
- 시간복잡도는 반드시 `O(log n)` 이어야 합니다.
- 선형 탐색(`for` 로 전체를 도는 방식)이나 슬라이싱 기반 탐색은 사용하지 않습니다.

아래 템플릿을 완성해 보세요.

from typing import List

#데일리미션의 퀵셀렉트와 비슷한데???


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        \"\"\"회전된 정렬 배열에서 target의 인덱스를 찾습니다.

        아이디어:
            - 매 반복마다 mid를 기준으로 왼쪽/오른쪽 중 어느 쪽이 정렬 구간인지 판별합니다.
            - target이 정렬된 구간 안에 속하는지에 따라 탐색 범위를 절반으로 줄입니다.

        시간복잡도:
            - 매 단계마다 탐색 범위를 절반으로 줄이므로 O(log n) 입니다.
        \"\"\"
        left, right = 0, len(nums) - 1
        
        while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[left] <= nums[mid]:
                    if nums[left]<= target < nums[mid]:
                        right = mid - 1
                    else: left = mid + 1
                                            
                else: # nums[right] >= nums[mid]
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else: right = mid - 1
        return -1
        # TODO: while 루프 안에서 mid를 계산하고,
        #       정렬된 구간을 판별한 뒤, target의 위치에 따라
        #       left/right 를 조정하는 로직을 작성해 보세요.
        # 힌트:
        #   - if nums[mid] == target: 바로 mid 반환
        #   - elif 왼쪽 구간이 정렬되어 있다면:
        #        target이 왼쪽 구간에 속하는지 비교 후, left/right 이동
        #   - else: 오른쪽 구간이 정렬되어 있는 경우
        #        target이 오른쪽 구간에 속하는지 비교 후, left/right 이동

        raise NotImplementedError


### ✅ 테스트 코드
아래 셀을 실행해 예시 입력 및 몇 가지 추가 케이스에서 결과를 확인해 보세요.
테스트 케이스를 스스로 더 추가해 보면 좋습니다.

def run_tests():
    sol = Solution()
    tests = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([5,1,3], 3, 2),
        ([5,1,3], 5, 0),
        ([1,2,3,4,5,6,7,8,9],5,4)
    ]

    for nums, target, expected in tests:
        result = sol.search(nums, target)
        print(f\"nums={nums}, target={target} → result={result}, expected={expected}\")

run_tests()


---
## Step 4. 정리 및 자기 점검

### ✏️ 정리 (학생 작성)

- 이 문제에서 **정렬 + 탐색** 사고가 어떻게 사용되었는지 한 문단으로 요약해 보세요.
  -피벗한 mid를 기준으로 좌우의 정렬되어있을 것을 가정하고, 타겟을 탐색하며 범위를 좁혀가며 찾는다.
- 내가 작성한 코드에서 가장 헷갈렸던 조건(또는 버그가 많이 났던 부분)은?
  -정렬되어 있다면을 가정하여 타겟의 값을 비교하며 시작과 끝점을 이동하는 부분이 헷갈렸음
- 회전이 전혀 없는 경우(그냥 정렬 배열)에도 코드가 잘 동작하는지?
  -ㅇㅇ
- 동일한 패턴을 적용할 수 있을 것 같은 다른 문제 유형(예: 최소값 찾기, 중복 허용 버전 등):
  -회전된 정렬배열에서 최소값 찾기
  -산모양배열에서 최대값찾기

---
## ✅ 제출 전 체크리스트
- [ ] 선형 탐색이 아닌, 변형된 이진 탐색으로 구현했다.
- [ ] 회전된 배열의 구조 및 \"한 쪽 구간은 정렬\" 조건을 코드로 잘 옮겼다.
- [ ] target이 존재할 때는 인덱스, 없을 때는 -1을 반환한다.
- [ ] 예시 및 추가 테스트 케이스에서 기대한 결과가 나온다.
- [ ] 전체 알고리즘의 시간복잡도가 `O(log n)` 임을 설명할 수 있다.

수고 많았습니다! Day 4 심화 미션까지 완료했다면, 힙과 이진 탐색을 활용한
대표적인 패턴들을 한 번씩 모두 경험한 것입니다 🎯


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day4_daily_mission(문제)-checkpoint.ipynb.txt'] = """# Day 4. 힙과 이진 탐색으로 문제 해결하기 – 데일리 미션 (Kth Largest)

이 노트북은 **힙(Priority Queue)** 를 활용해 LeetCode **#215 – Kth Largest Element in an Array**
문제를 푸는 데일리 미션용입니다.

## 🎯 학습 목표
- 전체 정렬을 하지 않고도 **k번째로 큰 원소**를 찾는 방법을 이해한다.
- `heapq` 모듈을 활용하여 **min-heap 기반 top-k 패턴**을 구현한다.
- 정렬(`O(n log n)`) vs 힙(`O(n log k)`) vs QuickSelect(평균 `O(n)`)의
  시간복잡도 차이를 설명할 수 있다.

---
## 문제: Kth Largest Element in an Array

> 정수 배열 `nums` 와 정수 `k` 가 주어질 때,
> 배열을 내림차순 정렬했을 때의 **k번째로 큰 값(Kth largest)** 를 반환하세요.

- \"서로 다른 값의 k번째\"가 아니라, **정렬 순서 기준으로 k번째**입니다.
- 전체를 정렬하지 않고도 풀 수 있을까요?

### 예시
1. `nums = [3,2,1,5,6,4], k = 2` → 출력: `5`
2. `nums = [3,2,3,1,2,4,5,5,6], k = 4` → 출력: `4`

### 제한 조건 (문제 요약)
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---
이제 아래 **Step 1 → Step 4** 순서로 미션을 진행해 주세요.

## 🛠️ Prerequisites
본 미션은 효율적인 데이터 처리를 위해 파이썬 내장 모듈을 활용합니다.
* **`import heapq`**: 최소 힙(min-heap)을 사용하여 $O(n \\log k)$의 시간복잡도로 문제를 해결합니다.
* **`from typing import List`**: 리스트 데이터의 타입을 명시하기 위해 사용합니다.
* 별도의 설치 없이 Python 3.x 환경의 표준 라이브러리만으로 실행 가능합니다.

## Step 1. 문제 이해 및 접근 방식 비교

먼저, 이 문제를 풀 수 있는 여러 가지 방법을 떠올려 봅시다.

### 대표적인 세 가지 접근
1. **전체 정렬 방식**
   - `nums.sort()` 로 전체 정렬 후, 뒤에서 k번째 원소를 꺼낸다.
   - 시간복잡도: `O(n log n)`

2. **min-heap 기반 top-k 방식** (오늘 구현할 방법)
   - 크기가 **항상 k 이하**가 되도록 min-heap을 유지한다.
   - heap 크기가 k를 초과하면 가장 작은 값을 pop한다.
   - 최종적으로 heap의 루트(가장 작은 값)가 \"k번째로 큰 값\"이 된다.
   - 시간복잡도: `O(n log k)`

3. **QuickSelect (선택 알고리즘)**
   - 퀵 정렬의 `partition` 아이디어로 평균 `O(n)`에 k번째 원소를 찾는다.
   - 구현은 조금 복잡하지만, 이론적으로 더 빠르다(평균).

아래에 본인이 이해한 세 방법의 차이를 간단히 정리해 보세요.

### ✏️ 세 가지 접근 방식 요약 (학생 작성)

- 전체 정렬 방식 (장점/단점):
  - 한 번 정렬해두면, 다른 순위의 값도 O(1)에 찾을 수 있다
  - k번째만 궁금한데, 나머지 모든 숫자의 순서까지 모두 정리해야한다 O(N*logN)
    
- min-heap 방식 (장점/단점):
  - 크기가 k인 힙을 유지할 때, 가장 작은 값인 루트가 k가 된다
  - 배열 전체를 기억할 필요없이, k개의 공간이 필요함
  - k가 아주 크다면 전체 정렬과 속도차이가 거의 없다 O(N*logk)

- QuickSelect (장점/단점, 느낌):
  - 이진탐색과 유사하다!!
  - 시간복잡도 O(N) 
  - 그러나 한쪽으로 노드가 쏠린경우엔 O(N*N) 이 될 수도 있다.


---
## Step 2. `heapq` 로 min-heap 기반 Kth Largest 구현하기

파이썬에서는 `heapq` 모듈이 **min-heap** 을 제공합니다.

### 아이디어 (top-k 패턴)
- 빈 배열 `heap = []` 를 준비합니다.
- `nums` 의 원소들을 하나씩 보면서 **heap에 push** 합니다.
- 만약 heap의 크기가 `k` 를 초과하면, `heappop` 으로 **가장 작은 값을 제거**합니다.
- 모든 원소를 처리한 뒤, heap[0] (루트)가 바로 **k번째로 큰 원소**가 됩니다.

아래 템플릿을 참고해서 `findKthLargest` 메서드를 완성해 보세요.

from typing import List
import heapq

##퀵셀렉트인가?? 데일리미션의 그것과 비슷한데

class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  #heap을 빈 리스트로 지정
        for num in nums: #nums 순회하면서
            heapq.heappush(heap, num) #매 원소마다 heappush(최소힙 유지), 
            \"\"\"heappush함수는 값을 단순히 리스트 끝에 넣는 것이 아니라, 
            최소힙의 성질을 유지하도록 내부적으로 재배치작업을 자동으로 수행하비다\"\"\"
            
            if len(heap) > k : #heap크기가 k를 초과하면 가장 작은 값 제거
                heapq.heappop(heap)  
                \"\"\"값을 빼는 순간 가장 뒤에있던 값을 루트로 가져온 뒤
                                        아래로 슥 내려보내며 다시 최소힙 유지\"\"\"
               
        return heap[0]  #반복이 끝나면 루트값 내놔(최소값, 이 경우 k번째 큰 값)

        \"\"\"heapq 함수들을 통해서만 리스트를 조작한다면, 그 리스트는 항상 최소힙
        상태를 유지하게 된다!!
        
        전체 숫자 N개를 다 훑는다.
            이 힙은 항상 크기 k를 유지한다. logk. 따라서 시간복잡도 O(N*logk)\"\"\"



        
        \"\"\"min-heap을 사용해 k번째로 큰 원소를 찾는 함수입니다.

        아이디어:
            - 크기가 항상 k 이하가 되도록 min-heap을 유지합니다.
            - heap에 원소를 push 하다가, 크기가 k+1이 되면 가장 작은 값을 pop합니다.
            - 최종적으로 heap[0] 에 남는 값이 k번째로 큰 값입니다.

        시간복잡도:
            - 각 원소마다 push/pop 이 최대 한 번씩 일어나며, 각 연산은 O(log k)이므로
              전체 시간복잡도는 O(n log k) 입니다.
        \"\"\"
        # TODO: 위 설명에 따라 코드를 직접 작성해 보세요.
        #   1. 빈 리스트를 heap으로 사용 (heap = [])
        #   2. nums를 순회하면서, 매 원소마다 heappush
        #   3. 만약 len(heap) > k 가 되면 heappop으로 가장 작은 값 제거
        #   4. 반복이 끝난 뒤 heap[0] 을 반환
        raise NotImplementedError


### ✅ 테스트 코드 (수정하지 말고, 위 함수를 완성한 뒤 실행해 보세요)

추가로 본인이 직접 케이스를 1~2개 더 넣어도 좋습니다.

def run_tests_heap():
    sol = SolutionHeap()
    tests = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([2,1], 1, 2),  # 가장 큰 값
    ]

    for nums, k, expected in tests:
        result = sol.findKthLargest(nums, k)
        print(f\"nums={nums}, k={k} → result={result}, expected={expected}\")

run_tests_heap()


---
## Step 3. (선택) QuickSelect로 평균 O(n)에 도전하기

여유가 있다면, QuickSelect 방식으로도 같은 문제를 풀어 보세요.

### 아이디어 매우 간단 요약
- 퀵 정렬의 `partition` 과 비슷하게, 피벗을 기준으로 배열을 두 부분으로 나눕니다.
- 피벗의 정렬상 위치 `idx` 가 우리가 찾는 `k번째` 위치인지 확인합니다.
  - `idx` 가 목표보다 왼쪽/오른쪽이면, 그쪽 부분 배열에 대해서만 재귀적으로 반복합니다.
- 평균적으로 `O(n)` 에 k번째 원소를 찾을 수 있습니다.

완전히 구현하기 부담스럽다면, **의사 코드 수준으로라도** 아래 셀에 정리해 보세요.

# class SolutionQuickSelect:
#     def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
#         heap = []
#         first = 0
#         last = len(list) -1
        
#         while first <= last: #first 와 last의 거리를 좁혀갈거야
#             mid = (first + last) // 2
#             if list[mid] == k: #mid인덱스 값이 k와 같으면 mid 인덱스를 내놔
#                 return mid
#             elif list[mid] < k: #mid인덱스 값이 k보다 작으면, 시작인덱스를 mid인덱스 오른쪽1칸에서 다시
#                 first = mid + 1
#             else:
#                 last = mid -1 #mid인덱스 값이 k보다 크면, 끝 인덱스를 mid인덱스 왼쪽1칸으로 다시
#         return -1

\"\"\"문제!, nums는 정렬이 되어있지 않다! 그럼 먼저 num를 정렬하면 되지!!
--->>>NO!! 퀵셀릭트quick select 라는것은, 임의의 피벗(기준점, 중심점)을 정해 정렬했을 때의
    진짜 인덱스를 찾아내고, k와 비교하며 범위를 좁혀야한다.  ?????네????? \"\"\"

class SolutionQuickSelect:
    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
#k번째 큰 인덱스는, len(nums)-k 해야 정렬한 리스트에서 인덱스에서 찾을 수 있음
        target = len(nums)-k
        left, right = 0, len(nums)-1 #초기 범위 설정, nums의 맨앞부터 맨뒤

        while left <= right:
            p_idx = self.partition(nums, left, right)#피벗 인덱스는 반환받은 인덱스i이다

            if p_idx == target:
                return nums[p_idx]

            elif p_idx < target:
                left = p_idx + 1
            else: # p_idx > target
                right = p_idx - 1
        return -1 #찾는게 없다! 뭔가 잘못됨!
        
        # 랜덤.피벗인덱스선택(p_idx)
        # while P_idx를 기준으로 삼고 이보다 작으면 왼쪽, 크면 오른쪽으로 둘거야:
        #     partition() 을 먼저 수행해서 p_idx의 인덱스를 내놔
        #     if p_idx = k 이면 retrun p_idx
        #     if p_idx < k **k보다 왼쪽에 있으면** 이면 한칸 오른쪽에서 탐색해
        #     if p_idx > k **k보다 오른쪽에 있으면** 이면 한칸 왼쪽에서 탐색해

    def partition(self, nums:List[int], left:int, right:int)  -> int:
        #랜덤인덱스 피벗 뽑아, 오른쪽 끝에것과 교체-nums[right]
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
        #nums[right]를 p 피벗,기준값으로
        p = nums[right]
        #투포인터
        i = left

        for j in range(left,right): #for루프를 돌면서 정렬을 할것이다!
            if nums[j] <= p: #p 보다 작거나 같은 숫자발견하면
                nums[i],nums[j] = nums[j],nums[i] #발견한 숫자와 i와 교체??
                i += 1 
        #nums[j]가 p보다 크다면, 아무것도 안하고 j만 다음칸으로 넘어간다

        #루프가 끝나면 인덱스0 부터 인덱스i-1까지 모두 p보다 작은 수
        #인덱스 i에 p가 들어가야한다
        #nums[right]=p 이므로, 인덱스 i와 right를 교체
        nums[i],nums[right] = nums[right],nums[i]
        #p가 들어간 인덱스i를 반환
        return i
    
   




        \"\"\"(선택) QuickSelect로 k번째 큰 원소를 찾는 함수입니다.

        TODO:
            - partition(분할) 함수를 내부에 정의한 뒤,
              재귀 또는 while 루프로 quickselect를 구현해 보세요.
            - 구현이 부담된다면, pass로 두고 주석/마크다운으로만 아이디어를 정리해도 좋습니다.
        \"\"\"
        # TODO: QuickSelect 구현에 도전해보고 싶다면 이 부분을 채워보세요.
        raise NotImplementedError


---
## Step 4. 시간복잡도 분석 및 정리

아래에 **정렬 vs 힙 vs QuickSelect** 의 시간복잡도와,
실제 코딩 테스트/실무에서 어떤 방식을 선택할지에 대한 생각을 정리해 보세요.

### ✏️ 정리 (학생 작성)

- 전체 정렬 방식의 시간복잡도와 특징:
  -O(NlogN), 한 번 정렬해두면 이진 탐색도 할 수 있고 무엇이든 찾기 쉽다
  -데이터가 많아질수록 힙이나 퀵셀렉트보다 느리다
  모든 데이터의 순서가 중요할 때, 데이터를 한 번 정렬해두고 여러번 검색해야 할 때
  
- min-heap(top-k) 방식의 시간복잡도와 특징:
  -O(Nlogk), 데이터를 다 줄세우지 않고!, 누가 제일 큰지,작은지만 관리하는 느슨한 정렬상태를 유지하는.
  - 완전 정렬보다 빠르다
  - 새로운 데이터가 추가되는 상황에서도 최소값/최대값을 일정하게 뺄 수 있다 O(logN)
  - 실시간으로 우선순위가 높은 데이터를 처리해야 할 때(응급실), 데이터가 계속 들어오고 나가는 상황일 때

- QuickSelect의 평균/최악 시간복잡도와 특징:
  -O(N)/O(N*N), 정렬의 원리를 이용하되, target이 되는 k번째만 탐색
  - 임의의 피벗(기준점)을 기준으로 큰 쪽이나 작은 쪽, 한 쪽만 파고 들어감
  - 나머지 절반의 순서가 어떻게 되든 상관하지 않기 때문에 엄청 빠름
  - 다른 숫자는 관심 없고, 딱 target만 알고 싶을 때
- 내가 이 문제를 다시 푼다면 어떤 방식을 선택할지, 그 이유:
  -경우를 잘 따져봐야지 않을까? 데이터가 너무 많지만 않다면 정렬을, 계속 들어온다면 힙을

---
## ✅ 제출 전 체크리스트
- [ ] 전체 정렬을 사용하지 않고 min-heap으로 문제를 해결했다.
- [ ] heap 크기를 k로 유지하는 로직이 올바르게 구현되었다.
- [ ] 예제/엣지 케이스 테스트가 정상적으로 통과된다.
- [ ] 시간복잡도 `O(n log k)` 을 설명할 수 있다.
- [ ] (선택) QuickSelect 아이디어를 간단히라도 정리해 보았다.

수고 많았습니다! 🙂 이제 회전된 정렬 배열에서의 이진 탐색을 다루는 심화 미션으로 넘어가 봅시다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day4_daily_mission(문제)_leetcode215-checkpoint.ipynb.txt'] = """# Day 4. 힙과 이진 탐색으로 문제 해결하기 – 데일리 미션 (Kth Largest)

이 노트북은 **힙(Priority Queue)** 를 활용해 LeetCode **#215 – Kth Largest Element in an Array**
문제를 푸는 데일리 미션용입니다.

## 🎯 학습 목표
- 전체 정렬을 하지 않고도 **k번째로 큰 원소**를 찾는 방법을 이해한다.
- `heapq` 모듈을 활용하여 **min-heap 기반 top-k 패턴**을 구현한다.
- 정렬(`O(n log n)`) vs 힙(`O(n log k)`) vs QuickSelect(평균 `O(n)`)의
  시간복잡도 차이를 설명할 수 있다.

---
## 문제: Kth Largest Element in an Array

> 정수 배열 `nums` 와 정수 `k` 가 주어질 때,
> 배열을 내림차순 정렬했을 때의 **k번째로 큰 값(Kth largest)** 를 반환하세요.

- \"서로 다른 값의 k번째\"가 아니라, **정렬 순서 기준으로 k번째**입니다.
- 전체를 정렬하지 않고도 풀 수 있을까요?

### 예시
1. `nums = [3,2,1,5,6,4], k = 2` → 출력: `5`
2. `nums = [3,2,3,1,2,4,5,5,6], k = 4` → 출력: `4`

### 제한 조건 (문제 요약)
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---
이제 아래 **Step 1 → Step 4** 순서로 미션을 진행해 주세요.

## 🛠️ Prerequisites
본 미션은 효율적인 데이터 처리를 위해 파이썬 내장 모듈을 활용합니다.
* **`import heapq`**: 최소 힙(min-heap)을 사용하여 $O(n \\log k)$의 시간복잡도로 문제를 해결합니다.
* **`from typing import List`**: 리스트 데이터의 타입을 명시하기 위해 사용합니다.
* 별도의 설치 없이 Python 3.x 환경의 표준 라이브러리만으로 실행 가능합니다.

## Step 1. 문제 이해 및 접근 방식 비교

먼저, 이 문제를 풀 수 있는 여러 가지 방법을 떠올려 봅시다.

### 대표적인 세 가지 접근
1. **전체 정렬 방식**
   - `nums.sort()` 로 전체 정렬 후, 뒤에서 k번째 원소를 꺼낸다.
   - 시간복잡도: `O(n log n)`

2. **min-heap 기반 top-k 방식** (오늘 구현할 방법)
   - 크기가 **항상 k 이하**가 되도록 min-heap을 유지한다.
   - heap 크기가 k를 초과하면 가장 작은 값을 pop한다.
   - 최종적으로 heap의 루트(가장 작은 값)가 \"k번째로 큰 값\"이 된다.
   - 시간복잡도: `O(n log k)`

3. **QuickSelect (선택 알고리즘)**
   - 퀵 정렬의 `partition` 아이디어로 평균 `O(n)`에 k번째 원소를 찾는다.
   - 구현은 조금 복잡하지만, 이론적으로 더 빠르다(평균).

아래에 본인이 이해한 세 방법의 차이를 간단히 정리해 보세요.

### ✏️ 세 가지 접근 방식 요약 (학생 작성)

- 전체 정렬 방식 (장점/단점):
  - 한 번 정렬해두면, 다른 순위의 값도 O(1)에 찾을 수 있다
  - k번째만 궁금한데, 나머지 모든 숫자의 순서까지 모두 정리해야한다 O(N*logN)
    
- min-heap 방식 (장점/단점):
  - 크기가 k인 힙을 유지할 때, 가장 작은 값인 루트가 k가 된다
  - 배열 전체를 기억할 필요없이, k개의 공간이 필요함
  - k가 아주 크다면 전체 정렬과 속도차이가 거의 없다 O(N*logk)

- QuickSelect (장점/단점, 느낌):
  - 이진탐색과 유사하다!!
  - 시간복잡도 O(N) 
  - 그러나 한쪽으로 노드가 쏠린경우엔 O(N*N) 이 될 수도 있다.


---
## Step 2. `heapq` 로 min-heap 기반 Kth Largest 구현하기

파이썬에서는 `heapq` 모듈이 **min-heap** 을 제공합니다.

### 아이디어 (top-k 패턴)
- 빈 배열 `heap = []` 를 준비합니다.
- `nums` 의 원소들을 하나씩 보면서 **heap에 push** 합니다.
- 만약 heap의 크기가 `k` 를 초과하면, `heappop` 으로 **가장 작은 값을 제거**합니다.
- 모든 원소를 처리한 뒤, heap[0] (루트)가 바로 **k번째로 큰 원소**가 됩니다.

아래 템플릿을 참고해서 `findKthLargest` 메서드를 완성해 보세요.

from typing import List
import heapq

##퀵셀렉트인가?? 데일리미션의 그것과 비슷한데

class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  #heap을 빈 리스트로 지정
        for num in nums: #nums 순회하면서
            heapq.heappush(heap, num) #매 원소마다 heappush(최소힙 유지), 
            \"\"\"heappush함수는 값을 단순히 리스트 끝에 넣는 것이 아니라, 
            최소힙의 성질을 유지하도록 내부적으로 재배치작업을 자동으로 수행하비다\"\"\"
            
            if len(heap) > k : #heap크기가 k를 초과하면 가장 작은 값 제거
                heapq.heappop(heap)  
                \"\"\"값을 빼는 순간 가장 뒤에있던 값을 루트로 가져온 뒤
                                        아래로 슥 내려보내며 다시 최소힙 유지\"\"\"
               
        return heap[0]  #반복이 끝나면 루트값 내놔(최소값, 이 경우 k번째 큰 값)

        \"\"\"heapq 함수들을 통해서만 리스트를 조작한다면, 그 리스트는 항상 최소힙
        상태를 유지하게 된다!!
        
        전체 숫자 N개를 다 훑는다.
            이 힙은 항상 크기 k를 유지한다. logk. 따라서 시간복잡도 O(N*logk)\"\"\"



        
        \"\"\"min-heap을 사용해 k번째로 큰 원소를 찾는 함수입니다.

        아이디어:
            - 크기가 항상 k 이하가 되도록 min-heap을 유지합니다.
            - heap에 원소를 push 하다가, 크기가 k+1이 되면 가장 작은 값을 pop합니다.
            - 최종적으로 heap[0] 에 남는 값이 k번째로 큰 값입니다.

        시간복잡도:
            - 각 원소마다 push/pop 이 최대 한 번씩 일어나며, 각 연산은 O(log k)이므로
              전체 시간복잡도는 O(n log k) 입니다.
        \"\"\"
        # TODO: 위 설명에 따라 코드를 직접 작성해 보세요.
        #   1. 빈 리스트를 heap으로 사용 (heap = [])
        #   2. nums를 순회하면서, 매 원소마다 heappush
        #   3. 만약 len(heap) > k 가 되면 heappop으로 가장 작은 값 제거
        #   4. 반복이 끝난 뒤 heap[0] 을 반환
        raise NotImplementedError


### ✅ 테스트 코드 (수정하지 말고, 위 함수를 완성한 뒤 실행해 보세요)

추가로 본인이 직접 케이스를 1~2개 더 넣어도 좋습니다.

def run_tests_heap():
    sol = SolutionHeap()
    tests = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([2,1], 1, 2),  # 가장 큰 값
    ]

    for nums, k, expected in tests:
        result = sol.findKthLargest(nums, k)
        print(f\"nums={nums}, k={k} → result={result}, expected={expected}\")

run_tests_heap()


---
## Step 3. (선택) QuickSelect로 평균 O(n)에 도전하기

여유가 있다면, QuickSelect 방식으로도 같은 문제를 풀어 보세요.

### 아이디어 매우 간단 요약
- 퀵 정렬의 `partition` 과 비슷하게, 피벗을 기준으로 배열을 두 부분으로 나눕니다.
- 피벗의 정렬상 위치 `idx` 가 우리가 찾는 `k번째` 위치인지 확인합니다.
  - `idx` 가 목표보다 왼쪽/오른쪽이면, 그쪽 부분 배열에 대해서만 재귀적으로 반복합니다.
- 평균적으로 `O(n)` 에 k번째 원소를 찾을 수 있습니다.

완전히 구현하기 부담스럽다면, **의사 코드 수준으로라도** 아래 셀에 정리해 보세요.

# class SolutionQuickSelect:
#     def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
#         heap = []
#         first = 0
#         last = len(list) -1
        
#         while first <= last: #first 와 last의 거리를 좁혀갈거야
#             mid = (first + last) // 2
#             if list[mid] == k: #mid인덱스 값이 k와 같으면 mid 인덱스를 내놔
#                 return mid
#             elif list[mid] < k: #mid인덱스 값이 k보다 작으면, 시작인덱스를 mid인덱스 오른쪽1칸에서 다시
#                 first = mid + 1
#             else:
#                 last = mid -1 #mid인덱스 값이 k보다 크면, 끝 인덱스를 mid인덱스 왼쪽1칸으로 다시
#         return -1

\"\"\"문제!, nums는 정렬이 되어있지 않다! 그럼 먼저 num를 정렬하면 되지!!
--->>>NO!! 퀵셀릭트quick select 라는것은, 임의의 피벗(기준점, 중심점)을 정해 정렬했을 때의
    진짜 인덱스를 찾아내고, k와 비교하며 범위를 좁혀야한다.  ?????네????? \"\"\"

class SolutionQuickSelect:
    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
#k번째 큰 인덱스는, len(nums)-k 해야 정렬한 리스트에서 인덱스에서 찾을 수 있음
        target = len(nums)-k
        left, right = 0, len(nums)-1 #초기 범위 설정, nums의 맨앞부터 맨뒤

        while left <= right:
            p_idx = self.partition(nums, left, right)#피벗 인덱스는 반환받은 인덱스i이다

            if p_idx == target:
                return nums[p_idx]

            elif p_idx < target:
                left = p_idx + 1
            else: # p_idx > target
                right = p_idx - 1
        return -1 #찾는게 없다! 뭔가 잘못됨!
        
        # 랜덤.피벗인덱스선택(p_idx)
        # while P_idx를 기준으로 삼고 이보다 작으면 왼쪽, 크면 오른쪽으로 둘거야:
        #     partition() 을 먼저 수행해서 p_idx의 인덱스를 내놔
        #     if p_idx = k 이면 retrun p_idx
        #     if p_idx < k **k보다 왼쪽에 있으면** 이면 한칸 오른쪽에서 탐색해
        #     if p_idx > k **k보다 오른쪽에 있으면** 이면 한칸 왼쪽에서 탐색해

    def partition(self, nums:List[int], left:int, right:int)  -> int:
        #랜덤인덱스 피벗 뽑아, 오른쪽 끝에것과 교체-nums[right]
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
        #nums[right]를 p 피벗,기준값으로
        p = nums[right]
        #투포인터
        i = left

        for j in range(left,right): #for루프를 돌면서 정렬을 할것이다!
            if nums[j] <= p: #p 보다 작거나 같은 숫자발견하면
                nums[i],nums[j] = nums[j],nums[i] #발견한 숫자와 i와 교체??
                i += 1 
        #nums[j]가 p보다 크다면, 아무것도 안하고 j만 다음칸으로 넘어간다

        #루프가 끝나면 인덱스0 부터 인덱스i-1까지 모두 p보다 작은 수
        #인덱스 i에 p가 들어가야한다
        #nums[right]=p 이므로, 인덱스 i와 right를 교체
        nums[i],nums[right] = nums[right],nums[i]
        #p가 들어간 인덱스i를 반환
        return i
    
   




        \"\"\"(선택) QuickSelect로 k번째 큰 원소를 찾는 함수입니다.

        TODO:
            - partition(분할) 함수를 내부에 정의한 뒤,
              재귀 또는 while 루프로 quickselect를 구현해 보세요.
            - 구현이 부담된다면, pass로 두고 주석/마크다운으로만 아이디어를 정리해도 좋습니다.
        \"\"\"
        # TODO: QuickSelect 구현에 도전해보고 싶다면 이 부분을 채워보세요.
        raise NotImplementedError


---
## Step 4. 시간복잡도 분석 및 정리

아래에 **정렬 vs 힙 vs QuickSelect** 의 시간복잡도와,
실제 코딩 테스트/실무에서 어떤 방식을 선택할지에 대한 생각을 정리해 보세요.

### ✏️ 정리 (학생 작성)

- 전체 정렬 방식의 시간복잡도와 특징:
  -O(NlogN), 한 번 정렬해두면 이진 탐색도 할 수 있고 무엇이든 찾기 쉽다
  -데이터가 많아질수록 힙이나 퀵셀렉트보다 느리다
  모든 데이터의 순서가 중요할 때, 데이터를 한 번 정렬해두고 여러번 검색해야 할 때
  
- min-heap(top-k) 방식의 시간복잡도와 특징:
  -O(Nlogk), 데이터를 다 줄세우지 않고!, 누가 제일 큰지,작은지만 관리하는 느슨한 정렬상태를 유지하는.
  - 완전 정렬보다 빠르다
  - 새로운 데이터가 추가되는 상황에서도 최소값/최대값을 일정하게 뺄 수 있다 O(logN)
  - 실시간으로 우선순위가 높은 데이터를 처리해야 할 때(응급실), 데이터가 계속 들어오고 나가는 상황일 때

- QuickSelect의 평균/최악 시간복잡도와 특징:
  -O(N)/O(N*N), 정렬의 원리를 이용하되, target이 되는 k번째만 탐색
  - 임의의 피벗(기준점)을 기준으로 큰 쪽이나 작은 쪽, 한 쪽만 파고 들어감
  - 나머지 절반의 순서가 어떻게 되든 상관하지 않기 때문에 엄청 빠름
  - 다른 숫자는 관심 없고, 딱 target만 알고 싶을 때
- 내가 이 문제를 다시 푼다면 어떤 방식을 선택할지, 그 이유:
  -경우를 잘 따져봐야지 않을까? 데이터가 너무 많지만 않다면 정렬을, 계속 들어온다면 힙을

---
## ✅ 제출 전 체크리스트
- [ ] 전체 정렬을 사용하지 않고 min-heap으로 문제를 해결했다.
- [ ] heap 크기를 k로 유지하는 로직이 올바르게 구현되었다.
- [ ] 예제/엣지 케이스 테스트가 정상적으로 통과된다.
- [ ] 시간복잡도 `O(n log k)` 을 설명할 수 있다.
- [ ] (선택) QuickSelect 아이디어를 간단히라도 정리해 보았다.

수고 많았습니다! 🙂 이제 회전된 정렬 배열에서의 이진 탐색을 다루는 심화 미션으로 넘어가 봅시다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day4_daily_mission(문제)_leetcode215.ipynb.txt'] = """# Day 4. 힙과 이진 탐색으로 문제 해결하기 – 데일리 미션 (Kth Largest)

이 노트북은 **힙(Priority Queue)** 를 활용해 LeetCode **#215 – Kth Largest Element in an Array**
문제를 푸는 데일리 미션용입니다.

## 🎯 학습 목표
- 전체 정렬을 하지 않고도 **k번째로 큰 원소**를 찾는 방법을 이해한다.
- `heapq` 모듈을 활용하여 **min-heap 기반 top-k 패턴**을 구현한다.
- 정렬(`O(n log n)`) vs 힙(`O(n log k)`) vs QuickSelect(평균 `O(n)`)의
  시간복잡도 차이를 설명할 수 있다.

---
## 문제: Kth Largest Element in an Array

> 정수 배열 `nums` 와 정수 `k` 가 주어질 때,
> 배열을 내림차순 정렬했을 때의 **k번째로 큰 값(Kth largest)** 를 반환하세요.

- \"서로 다른 값의 k번째\"가 아니라, **정렬 순서 기준으로 k번째**입니다.
- 전체를 정렬하지 않고도 풀 수 있을까요?

### 예시
1. `nums = [3,2,1,5,6,4], k = 2` → 출력: `5`
2. `nums = [3,2,3,1,2,4,5,5,6], k = 4` → 출력: `4`

### 제한 조건 (문제 요약)
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---
이제 아래 **Step 1 → Step 4** 순서로 미션을 진행해 주세요.

## 🛠️ Prerequisites
본 미션은 효율적인 데이터 처리를 위해 파이썬 내장 모듈을 활용합니다.
* **`import heapq`**: 최소 힙(min-heap)을 사용하여 $O(n \\log k)$의 시간복잡도로 문제를 해결합니다.
* **`from typing import List`**: 리스트 데이터의 타입을 명시하기 위해 사용합니다.
* 별도의 설치 없이 Python 3.x 환경의 표준 라이브러리만으로 실행 가능합니다.

## Step 1. 문제 이해 및 접근 방식 비교

먼저, 이 문제를 풀 수 있는 여러 가지 방법을 떠올려 봅시다.

### 대표적인 세 가지 접근
1. **전체 정렬 방식**
   - `nums.sort()` 로 전체 정렬 후, 뒤에서 k번째 원소를 꺼낸다.
   - 시간복잡도: `O(n log n)`

2. **min-heap 기반 top-k 방식** (오늘 구현할 방법)
   - 크기가 **항상 k 이하**가 되도록 min-heap을 유지한다.
   - heap 크기가 k를 초과하면 가장 작은 값을 pop한다.
   - 최종적으로 heap의 루트(가장 작은 값)가 \"k번째로 큰 값\"이 된다.
   - 시간복잡도: `O(n log k)`

3. **QuickSelect (선택 알고리즘)**
   - 퀵 정렬의 `partition` 아이디어로 평균 `O(n)`에 k번째 원소를 찾는다.
   - 구현은 조금 복잡하지만, 이론적으로 더 빠르다(평균).

아래에 본인이 이해한 세 방법의 차이를 간단히 정리해 보세요.

### ✏️ 세 가지 접근 방식 요약 (학생 작성)

- 전체 정렬 방식 (장점/단점):
  - 한 번 정렬해두면, 다른 순위의 값도 O(1)에 찾을 수 있다
  - k번째만 궁금한데, 나머지 모든 숫자의 순서까지 모두 정리해야한다 O(N*logN)
    
- min-heap 방식 (장점/단점):
  - 크기가 k인 힙을 유지할 때, 가장 작은 값인 루트가 k가 된다
  - 배열 전체를 기억할 필요없이, k개의 공간이 필요함
  - k가 아주 크다면 전체 정렬과 속도차이가 거의 없다 O(N*logk)

- QuickSelect (장점/단점, 느낌):
  - 이진탐색과 유사하다!!
  - 시간복잡도 O(N) 
  - 그러나 한쪽으로 노드가 쏠린경우엔 O(N*N) 이 될 수도 있다.


---
## Step 2. `heapq` 로 min-heap 기반 Kth Largest 구현하기

파이썬에서는 `heapq` 모듈이 **min-heap** 을 제공합니다.

### 아이디어 (top-k 패턴)
- 빈 배열 `heap = []` 를 준비합니다.
- `nums` 의 원소들을 하나씩 보면서 **heap에 push** 합니다.
- 만약 heap의 크기가 `k` 를 초과하면, `heappop` 으로 **가장 작은 값을 제거**합니다.
- 모든 원소를 처리한 뒤, heap[0] (루트)가 바로 **k번째로 큰 원소**가 됩니다.

아래 템플릿을 참고해서 `findKthLargest` 메서드를 완성해 보세요.

from typing import List
import heapq

##퀵셀렉트인가?? 데일리미션의 그것과 비슷한데

class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  #heap을 빈 리스트로 지정
        for num in nums: #nums 순회하면서
            heapq.heappush(heap, num) #매 원소마다 heappush(최소힙 유지), 
            \"\"\"heappush함수는 값을 단순히 리스트 끝에 넣는 것이 아니라, 
            최소힙의 성질을 유지하도록 내부적으로 재배치작업을 자동으로 수행하비다\"\"\"
            
            if len(heap) > k : #heap크기가 k를 초과하면 가장 작은 값 제거
                heapq.heappop(heap)  
                \"\"\"값을 빼는 순간 가장 뒤에있던 값을 루트로 가져온 뒤
                                        아래로 슥 내려보내며 다시 최소힙 유지\"\"\"
               
        return heap[0]  #반복이 끝나면 루트값 내놔(최소값, 이 경우 k번째 큰 값)

        \"\"\"heapq 함수들을 통해서만 리스트를 조작한다면, 그 리스트는 항상 최소힙
        상태를 유지하게 된다!!
        
        전체 숫자 N개를 다 훑는다.
            이 힙은 항상 크기 k를 유지한다. logk. 따라서 시간복잡도 O(N*logk)\"\"\"



        
        \"\"\"min-heap을 사용해 k번째로 큰 원소를 찾는 함수입니다.

        아이디어:
            - 크기가 항상 k 이하가 되도록 min-heap을 유지합니다.
            - heap에 원소를 push 하다가, 크기가 k+1이 되면 가장 작은 값을 pop합니다.
            - 최종적으로 heap[0] 에 남는 값이 k번째로 큰 값입니다.

        시간복잡도:
            - 각 원소마다 push/pop 이 최대 한 번씩 일어나며, 각 연산은 O(log k)이므로
              전체 시간복잡도는 O(n log k) 입니다.
        \"\"\"
        # TODO: 위 설명에 따라 코드를 직접 작성해 보세요.
        #   1. 빈 리스트를 heap으로 사용 (heap = [])
        #   2. nums를 순회하면서, 매 원소마다 heappush
        #   3. 만약 len(heap) > k 가 되면 heappop으로 가장 작은 값 제거
        #   4. 반복이 끝난 뒤 heap[0] 을 반환
        raise NotImplementedError


### ✅ 테스트 코드 (수정하지 말고, 위 함수를 완성한 뒤 실행해 보세요)

추가로 본인이 직접 케이스를 1~2개 더 넣어도 좋습니다.

def run_tests_heap():
    sol = SolutionHeap()
    tests = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([2,1], 1, 2),  # 가장 큰 값
    ]

    for nums, k, expected in tests:
        result = sol.findKthLargest(nums, k)
        print(f\"nums={nums}, k={k} → result={result}, expected={expected}\")

run_tests_heap()


---
## Step 3. (선택) QuickSelect로 평균 O(n)에 도전하기

여유가 있다면, QuickSelect 방식으로도 같은 문제를 풀어 보세요.

### 아이디어 매우 간단 요약
- 퀵 정렬의 `partition` 과 비슷하게, 피벗을 기준으로 배열을 두 부분으로 나눕니다.
- 피벗의 정렬상 위치 `idx` 가 우리가 찾는 `k번째` 위치인지 확인합니다.
  - `idx` 가 목표보다 왼쪽/오른쪽이면, 그쪽 부분 배열에 대해서만 재귀적으로 반복합니다.
- 평균적으로 `O(n)` 에 k번째 원소를 찾을 수 있습니다.

완전히 구현하기 부담스럽다면, **의사 코드 수준으로라도** 아래 셀에 정리해 보세요.

# class SolutionQuickSelect:
#     def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
#         heap = []
#         first = 0
#         last = len(list) -1
        
#         while first <= last: #first 와 last의 거리를 좁혀갈거야
#             mid = (first + last) // 2
#             if list[mid] == k: #mid인덱스 값이 k와 같으면 mid 인덱스를 내놔
#                 return mid
#             elif list[mid] < k: #mid인덱스 값이 k보다 작으면, 시작인덱스를 mid인덱스 오른쪽1칸에서 다시
#                 first = mid + 1
#             else:
#                 last = mid -1 #mid인덱스 값이 k보다 크면, 끝 인덱스를 mid인덱스 왼쪽1칸으로 다시
#         return -1

\"\"\"문제!, nums는 정렬이 되어있지 않다! 그럼 먼저 num를 정렬하면 되지!!
--->>>NO!! 퀵셀릭트quick select 라는것은, 임의의 피벗(기준점, 중심점)을 정해 정렬했을 때의
    진짜 인덱스를 찾아내고, k와 비교하며 범위를 좁혀야한다.  ?????네????? \"\"\"

class SolutionQuickSelect:
    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
#k번째 큰 인덱스는, len(nums)-k 해야 정렬한 리스트에서 인덱스에서 찾을 수 있음
        target = len(nums)-k
        left, right = 0, len(nums)-1 #초기 범위 설정, nums의 맨앞부터 맨뒤

        while left <= right:
            p_idx = self.partition(nums, left, right)#피벗 인덱스는 반환받은 인덱스i이다

            if p_idx == target:
                return nums[p_idx]

            elif p_idx < target:
                left = p_idx + 1
            else: # p_idx > target
                right = p_idx - 1
        return -1 #찾는게 없다! 뭔가 잘못됨!
        
        # 랜덤.피벗인덱스선택(p_idx)
        # while P_idx를 기준으로 삼고 이보다 작으면 왼쪽, 크면 오른쪽으로 둘거야:
        #     partition() 을 먼저 수행해서 p_idx의 인덱스를 내놔
        #     if p_idx = k 이면 retrun p_idx
        #     if p_idx < k **k보다 왼쪽에 있으면** 이면 한칸 오른쪽에서 탐색해
        #     if p_idx > k **k보다 오른쪽에 있으면** 이면 한칸 왼쪽에서 탐색해

    def partition(self, nums:List[int], left:int, right:int)  -> int:
        #랜덤인덱스 피벗 뽑아, 오른쪽 끝에것과 교체-nums[right]
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
        #nums[right]를 p 피벗,기준값으로
        p = nums[right]
        #투포인터
        i = left

        for j in range(left,right): #for루프를 돌면서 정렬을 할것이다!
            if nums[j] <= p: #p 보다 작거나 같은 숫자발견하면
                nums[i],nums[j] = nums[j],nums[i] #발견한 숫자와 i와 교체??
                i += 1 
        #nums[j]가 p보다 크다면, 아무것도 안하고 j만 다음칸으로 넘어간다

        #루프가 끝나면 인덱스0 부터 인덱스i-1까지 모두 p보다 작은 수
        #인덱스 i에 p가 들어가야한다
        #nums[right]=p 이므로, 인덱스 i와 right를 교체
        nums[i],nums[right] = nums[right],nums[i]
        #p가 들어간 인덱스i를 반환
        return i
    
   




        \"\"\"(선택) QuickSelect로 k번째 큰 원소를 찾는 함수입니다.

        TODO:
            - partition(분할) 함수를 내부에 정의한 뒤,
              재귀 또는 while 루프로 quickselect를 구현해 보세요.
            - 구현이 부담된다면, pass로 두고 주석/마크다운으로만 아이디어를 정리해도 좋습니다.
        \"\"\"
        # TODO: QuickSelect 구현에 도전해보고 싶다면 이 부분을 채워보세요.
        raise NotImplementedError


---
## Step 4. 시간복잡도 분석 및 정리

아래에 **정렬 vs 힙 vs QuickSelect** 의 시간복잡도와,
실제 코딩 테스트/실무에서 어떤 방식을 선택할지에 대한 생각을 정리해 보세요.

### ✏️ 정리 (학생 작성)

- 전체 정렬 방식의 시간복잡도와 특징:
  -O(NlogN), 한 번 정렬해두면 이진 탐색도 할 수 있고 무엇이든 찾기 쉽다
  -데이터가 많아질수록 힙이나 퀵셀렉트보다 느리다
  모든 데이터의 순서가 중요할 때, 데이터를 한 번 정렬해두고 여러번 검색해야 할 때
  
- min-heap(top-k) 방식의 시간복잡도와 특징:
  -O(Nlogk), 데이터를 다 줄세우지 않고!, 누가 제일 큰지,작은지만 관리하는 느슨한 정렬상태를 유지하는.
  - 완전 정렬보다 빠르다
  - 새로운 데이터가 추가되는 상황에서도 최소값/최대값을 일정하게 뺄 수 있다 O(logN)
  - 실시간으로 우선순위가 높은 데이터를 처리해야 할 때(응급실), 데이터가 계속 들어오고 나가는 상황일 때

- QuickSelect의 평균/최악 시간복잡도와 특징:
  -O(N)/O(N*N), 정렬의 원리를 이용하되, target이 되는 k번째만 탐색
  - 임의의 피벗(기준점)을 기준으로 큰 쪽이나 작은 쪽, 한 쪽만 파고 들어감
  - 나머지 절반의 순서가 어떻게 되든 상관하지 않기 때문에 엄청 빠름
  - 다른 숫자는 관심 없고, 딱 target만 알고 싶을 때
- 내가 이 문제를 다시 푼다면 어떤 방식을 선택할지, 그 이유:
  -경우를 잘 따져봐야지 않을까? 데이터가 너무 많지만 않다면 정렬을, 계속 들어온다면 힙을

---
## ✅ 제출 전 체크리스트
- [ ] 전체 정렬을 사용하지 않고 min-heap으로 문제를 해결했다.
- [ ] heap 크기를 k로 유지하는 로직이 올바르게 구현되었다.
- [ ] 예제/엣지 케이스 테스트가 정상적으로 통과된다.
- [ ] 시간복잡도 `O(n log k)` 을 설명할 수 있다.
- [ ] (선택) QuickSelect 아이디어를 간단히라도 정리해 보았다.

수고 많았습니다! 🙂 이제 회전된 정렬 배열에서의 이진 탐색을 다루는 심화 미션으로 넘어가 봅시다.

###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day5_advanced_mission(문제)_leetcode-056-checkpoint.ipynb.txt'] = """# Day 5. 구간 병합 알고리즘 – 심화 미션
## LeetCode #56 — Merge Intervals

이 노트북은 Day 5 심화 과제인 **정렬 + 병합(sweep)** 패턴을 구현하기 위한 학생용 템플릿입니다.

---
## 🎯 학습 목표
- 정렬된 구간(intervals)을 순차적으로 탐색하며 병합하는 알고리즘을 이해한다.
- \"정렬 → 선형 스캔 → 조건 분기\" 패턴을 구현한다.
- 병합 조건(`start <= last_end`)을 정확히 다룬다.
- 시간복잡도 O(n log n) + O(n) 을 설명할 수 있다.

---
## 📌 문제 설명
서로 겹치는 모든 구간(intervals)을 병합하여, 병합된 구간만 포함하는 배열을 반환하세요.

### 예시
입력: `[[1,3],[2,6],[8,10],[15,18]]`
출력: `[[1,6],[8,10],[15,18]]`

---
## 🛠️ Prerequisites
본 미션은 효율적인 데이터 처리를 위해 파이썬 내장 모듈을 활용합니다.
* **`import heapq`**: 최소 힙(min-heap)을 사용하여 $O(n \\log k)$의 시간복잡도로 문제를 해결합니다.
* **`from typing import List`**: 리스트 데이터의 타입을 명시하기 위해 사용합니다.
* 별도의 설치 없이 Python 3.x 환경의 표준 라이브러리만으로 실행 가능합니다.

---
## Step 1. 문제 이해 & 예시 분석
병합조건을 조건으로 시작과 끝의 겹치는 구간을 하나로 병합하여 시작과 끝점을 도출한다

### ✏️ 예시 분석 (학생 작성)
- 왜 [1,3] 과 [2,6] 은 병합되는가?
- 1~3구간에  2~6구간의 시작이 겹친다, 병합하여 1~6 구간이 된다
- 앞 구간의 끝나는 점이, 뒷 구간의 시작점보다 크거나 같다면 겹친다
- 왜 [8,10] 과 [15,18] 은 병합되지 않는가?
- 8~10과 15~18은 각 끝점과 시작점 사이 겹치는 구간이 없다.

---
## Step 2. 핵심 패턴 파악하기 — \"정렬 후 선형 스캔\"

병합 알고리즘의 핵심 단계는 다음과 같습니다:
1. intervals 를 시작점을 기준으로 정렬한다.
2. 결과 리스트 `merged = []` 를 준비한다.
3. intervals 를 앞에서부터 탐색한다.
4. merged 가 비어있거나, 현재 구간이 이전 구간과 겹치지 않는다면 → append
5. 겹친다면 → 이전 구간의 end 값을 max(end, new_end) 로 갱신

아래에 스스로 요약해보세요.

### ✏️ 병합 조건 요약 (학생 작성)
- 겹친다고 판단하는 조건:
- 앞 구간의 끝나는 점이, 뒷 구간의 시작점보다 크거나 같다면 겹친다
- Interval_A[1] >= Interval_B[0]
- 
- 겹치지 않는다고 판단하는 조건:
- 앞 구간의 끝나는 점이, 뒷 구간의 시작점보다 작다면 겹치지 않는다.
- nterval_A[1] < Interval_B[0]
- 
- 병합 시 업데이트해야 하는 값: 앞 구간의 끝점을 , 뒷 구간의 끝점으로 업데이트
- 앞구간이 뒷구간을 완전히 포함하고 있는 경우도 있을 수 있다!!
- 앞구간의 끝점을 앞구간의 끝점과 뒷구간의 끝점 중 더 큰 값으로 업데이트 해야 함!
-  max(앞 구간 끝점, 뒷구간 끝점)




---
## Step 3. 코드 템플릿 완성하기
`TODO` 부분을 직접 채워 넣어 문제를 해결하세요.


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        \"\"\"
        intervals를 병합하여 새로운 리스트를 반환합니다.
        알고리즘 구조:
        1) 정렬
        2) 선형 스캔하며 병합
        \"\"\"

        # 1) intervals 정렬
        # TODO: 시작점 기준으로 정렬하기
        for i in range(len(intervals)):
            smallest = i
            for j in range(i+1, len(intervals)):
                if intervals[j][0] < intervals[smallest][0]:
                    smallest = j
            intervals[i], intervals[smallest] = intervals[smallest], intervals[i]
        
        merged = []
        #위에서 전부 시작점기준으로 소팅해놨으니까 시작점끼리 겹치는것 없고, 
        #오름차순이야
        
        # 2) 병합 진행
        for interval in intervals: #intervals 에 있는 각 인덱스들을 꺼내서 볼꺼야
            start, end = interval  #그 리스트들의 인덱스를 각각 start, end 라고 하자고
            
            # TODO: merged가 비었거나, 겹치지 않는 경우 → 새 구간 추가
            if not merged:
                merged.append(interval) #merged가 비었잖아?, 그 interval값을 추가해
                #그래서 merged가 생겼지? 
                #start(interval[0]) > merged[-1][1](merged 마지막인덱스의 end값) 이면 안겹쳐, 
                #추가해
            if start > merged[-1][1]: #이게 겹치지 않는 경우야. 바로 추가해
                merged.append(interval)

            if start <= merged[-1][1]:
                #앞구간이 뒷구간을 완전히 포함할 수도 있으니까
                #앞구간 끝점과 뒷구간 끝점중 큰것을 골라서
                #merged의 마지막 값의 끝점에 넣어.
                #왜냐하면, 이 경우는 앞구간과 뒷구간이 겹치는 경우잖아?
                #병합했을 때 앞구간의 시작점을 따르니까, append할게 아니라
                # 앞구간의 끝점을 앞구간과 뒷구간의 끝점중 큰 값으로 하는거야
                #이해함?
                merged[-1][1] = max(merged[-1][1],end) #interval의 [1]을 end로 하자고 했어

            # TODO: 겹치는 경우 → 마지막 구간의 end 업데이트
            #       max(old_end, end)

            ##if만 사용한 코드를 if/else로 바꿀 수 있겠으나
            ##이해의 측면에서 냅둠.
            ##어차피 append하는 not merged와 겹치지 않는 경우는 or로 합치고,
            ##마지막 겹치는 부분은 조건 떼고, else 로 두면 됩니다!
        

        return merged


---
## Step 4. 테스트 수행
실행하여 결과가 맞는지 확인하세요.


def run_tests():
    sol = Solution()
    tests = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,2],[3,4]], [[1,2],[3,4]]),
        ([[1,10],[2,3],[4,5]], [[1,10]]),
    ]

    for intervals, expected in tests:
        result = sol.merge(intervals)
        print(f\"intervals={intervals} → result={result}, expected={expected}\")

run_tests()


---
## Step 5. 시간복잡도 분석 & 정리


### ✏️ 복잡도 분석 (학생 작성)
- 정렬 단계 시간복잡도:O(N^2) 선택정렬을 사용했고,  전체 리스트 N번 돌면서 N개 다 살펴봐야함, N*N 의 비교
- 병합 단계(time):O(N) 소팅된 각 인덱스들 한번씩 다 살펴봐야하므로 
- 총 시간복잡도:N^2 + N 인데 오래걸리는 단계만 남으므로 O(N^2)
- 공간복잡도: 정렬단계에서는 in-place로 해결했으나, O(1), 병합단계에서 merged라는 리스트를 별도로 만들어야 했으므로 O(N)


---
## 제출 전 체크리스트
- [ ] intervals 정렬을 올바르게 했는가?
- [ ] 병합 조건을 정확히 구현했는가?
- [ ] 다양한 테스트로 검증했는가?
- [ ] 시간복잡도를 설명할 수 있는가?

수고했습니다! Day 5까지 완료하면 자료구조 문제 해결의 핵심 패턴을 모두 한 번씩 경험했습니다 🎉


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day5_advanced_mission(문제)_leetcode-056.ipynb.txt'] = """# Day 5. 구간 병합 알고리즘 – 심화 미션
## LeetCode #56 — Merge Intervals

이 노트북은 Day 5 심화 과제인 **정렬 + 병합(sweep)** 패턴을 구현하기 위한 학생용 템플릿입니다.

---
## 🎯 학습 목표
- 정렬된 구간(intervals)을 순차적으로 탐색하며 병합하는 알고리즘을 이해한다.
- \"정렬 → 선형 스캔 → 조건 분기\" 패턴을 구현한다.
- 병합 조건(`start <= last_end`)을 정확히 다룬다.
- 시간복잡도 O(n log n) + O(n) 을 설명할 수 있다.

---
## 📌 문제 설명
서로 겹치는 모든 구간(intervals)을 병합하여, 병합된 구간만 포함하는 배열을 반환하세요.

### 예시
입력: `[[1,3],[2,6],[8,10],[15,18]]`
출력: `[[1,6],[8,10],[15,18]]`

---
## 🛠️ Prerequisites
본 미션은 효율적인 데이터 처리를 위해 파이썬 내장 모듈을 활용합니다.
* **`import heapq`**: 최소 힙(min-heap)을 사용하여 $O(n \\log k)$의 시간복잡도로 문제를 해결합니다.
* **`from typing import List`**: 리스트 데이터의 타입을 명시하기 위해 사용합니다.
* 별도의 설치 없이 Python 3.x 환경의 표준 라이브러리만으로 실행 가능합니다.

---
## Step 1. 문제 이해 & 예시 분석
병합조건을 조건으로 시작과 끝의 겹치는 구간을 하나로 병합하여 시작과 끝점을 도출한다

### ✏️ 예시 분석 (학생 작성)
- 왜 [1,3] 과 [2,6] 은 병합되는가?
- 1~3구간에  2~6구간의 시작이 겹친다, 병합하여 1~6 구간이 된다
- 앞 구간의 끝나는 점이, 뒷 구간의 시작점보다 크거나 같다면 겹친다
- 왜 [8,10] 과 [15,18] 은 병합되지 않는가?
- 8~10과 15~18은 각 끝점과 시작점 사이 겹치는 구간이 없다.

---
## Step 2. 핵심 패턴 파악하기 — \"정렬 후 선형 스캔\"

병합 알고리즘의 핵심 단계는 다음과 같습니다:
1. intervals 를 시작점을 기준으로 정렬한다.
2. 결과 리스트 `merged = []` 를 준비한다.
3. intervals 를 앞에서부터 탐색한다.
4. merged 가 비어있거나, 현재 구간이 이전 구간과 겹치지 않는다면 → append
5. 겹친다면 → 이전 구간의 end 값을 max(end, new_end) 로 갱신

아래에 스스로 요약해보세요.

### ✏️ 병합 조건 요약 (학생 작성)
- 겹친다고 판단하는 조건:
- 앞 구간의 끝나는 점이, 뒷 구간의 시작점보다 크거나 같다면 겹친다
- Interval_A[1] >= Interval_B[0]
- 
- 겹치지 않는다고 판단하는 조건:
- 앞 구간의 끝나는 점이, 뒷 구간의 시작점보다 작다면 겹치지 않는다.
- nterval_A[1] < Interval_B[0]
- 
- 병합 시 업데이트해야 하는 값: 앞 구간의 끝점을 , 뒷 구간의 끝점으로 업데이트
- 앞구간이 뒷구간을 완전히 포함하고 있는 경우도 있을 수 있다!!
- 앞구간의 끝점을 앞구간의 끝점과 뒷구간의 끝점 중 더 큰 값으로 업데이트 해야 함!
-  max(앞 구간 끝점, 뒷구간 끝점)




---
## Step 3. 코드 템플릿 완성하기
`TODO` 부분을 직접 채워 넣어 문제를 해결하세요.


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        \"\"\"
        intervals를 병합하여 새로운 리스트를 반환합니다.
        알고리즘 구조:
        1) 정렬
        2) 선형 스캔하며 병합
        \"\"\"

        # 1) intervals 정렬
        # TODO: 시작점 기준으로 정렬하기
        for i in range(len(intervals)):
            smallest = i
            for j in range(i+1, len(intervals)):
                if intervals[j][0] < intervals[smallest][0]:
                    smallest = j
            intervals[i], intervals[smallest] = intervals[smallest], intervals[i]
        
        merged = []
        #위에서 전부 시작점기준으로 소팅해놨으니까 시작점끼리 겹치는것 없고, 
        #오름차순이야
        
        # 2) 병합 진행
        for interval in intervals: #intervals 에 있는 각 인덱스들을 꺼내서 볼꺼야
            start, end = interval  #그 리스트들의 인덱스를 각각 start, end 라고 하자고
            
            # TODO: merged가 비었거나, 겹치지 않는 경우 → 새 구간 추가
            if not merged:
                merged.append(interval) #merged가 비었잖아?, 그 interval값을 추가해
                #그래서 merged가 생겼지? 
                #start(interval[0]) > merged[-1][1](merged 마지막인덱스의 end값) 이면 안겹쳐, 
                #추가해
            if start > merged[-1][1]: #이게 겹치지 않는 경우야. 바로 추가해
                merged.append(interval)

            if start <= merged[-1][1]:
                #앞구간이 뒷구간을 완전히 포함할 수도 있으니까
                #앞구간 끝점과 뒷구간 끝점중 큰것을 골라서
                #merged의 마지막 값의 끝점에 넣어.
                #왜냐하면, 이 경우는 앞구간과 뒷구간이 겹치는 경우잖아?
                #병합했을 때 앞구간의 시작점을 따르니까, append할게 아니라
                # 앞구간의 끝점을 앞구간과 뒷구간의 끝점중 큰 값으로 하는거야
                #이해함?
                merged[-1][1] = max(merged[-1][1],end) #interval의 [1]을 end로 하자고 했어

            # TODO: 겹치는 경우 → 마지막 구간의 end 업데이트
            #       max(old_end, end)

            ##if만 사용한 코드를 if/else로 바꿀 수 있겠으나
            ##이해의 측면에서 냅둠.
            ##어차피 append하는 not merged와 겹치지 않는 경우는 or로 합치고,
            ##마지막 겹치는 부분은 조건 떼고, else 로 두면 됩니다!
        

        return merged


---
## Step 4. 테스트 수행
실행하여 결과가 맞는지 확인하세요.


def run_tests():
    sol = Solution()
    tests = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,2],[3,4]], [[1,2],[3,4]]),
        ([[1,10],[2,3],[4,5]], [[1,10]]),
    ]

    for intervals, expected in tests:
        result = sol.merge(intervals)
        print(f\"intervals={intervals} → result={result}, expected={expected}\")

run_tests()


---
## Step 5. 시간복잡도 분석 & 정리


### ✏️ 복잡도 분석 (학생 작성)
- 정렬 단계 시간복잡도:O(N^2) 선택정렬을 사용했고,  전체 리스트 N번 돌면서 N개 다 살펴봐야함, N*N 의 비교
- 병합 단계(time):O(N) 소팅된 각 인덱스들 한번씩 다 살펴봐야하므로 
- 총 시간복잡도:N^2 + N 인데 오래걸리는 단계만 남으므로 O(N^2)
- 공간복잡도: 정렬단계에서는 in-place로 해결했으나, O(1), 병합단계에서 merged라는 리스트를 별도로 만들어야 했으므로 O(N)


---
## 제출 전 체크리스트
- [ ] intervals 정렬을 올바르게 했는가?
- [ ] 병합 조건을 정확히 구현했는가?
- [ ] 다양한 테스트로 검증했는가?
- [ ] 시간복잡도를 설명할 수 있는가?

수고했습니다! Day 5까지 완료하면 자료구조 문제 해결의 핵심 패턴을 모두 한 번씩 경험했습니다 🎉


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day5_daily_mission(문제)-checkpoint.ipynb.txt'] = """# Day 5. 동적 프로그래밍 기초 – 데일리 미션
## LeetCode #70 — Climbing Stairs

이 노트북은 Day 5 데일리 미션인 **Climbing Stairs (DP)** 문제를 풀이하기 위한 학생용 템플릿입니다.

---
## 🎯 학습 목표
- DP의 기초 패턴(작은 문제의 해를 이용해 큰 문제 해결하기)을 이해한다.
- Climbing Stairs 문제에서 점화식을 스스로 도출한다.
- 반복 DP(O(n))로 효율적으로 해결한다.
- 에지 케이스(n=1,2)를 정확히 다룬다.

---
## 📌 문제 설명
당신은 계단을 오르고 있습니다. 꼭대기에 도달하려면 **n개의 계단**을 올라야 합니다. 매번 한 번에 **1계단 또는 2계단**을 오를 수 있습니다.

**꼭대기까지 올라갈 수 있는 서로 다른 방법의 수를 구하세요.**

### 예시
- n = 2 → 2가지 방법 (1+1, 2)
- n = 3 → 3가지 방법 (1+1+1, 1+2, 2+1)

---
## 🛠️ Prerequisites
본 미션은 추가적 라이브러리 명시 없이 설계 가능합니다.

---
## Step 1. 문제 이해 및 테스트 케이스 분석
아래 칸에 직접 정리해보세요.


### ✏️ 테스트 케이스 분석 (학생 작성)
- n=1 일 때 경우의 수:1; 1가지
- n=2 일 때 경우의 수:1+1, 2; 2가지
- n=3 일 때 경우의 수:1+1+1,2+1,1+2; 3가지
- 직접 n=4, n=5 를 손으로 구해보면?
- n=4 일때, 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2 ; 5가지
- n=5 일때, 1+1+1+1+1, 2+1+2, 1+2+2, 2+2+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1 ; 8가지

---
## Step 2. DP 점화식 세우기
DP의 핵심은 **현재 칸으로 오기 위한 이전 상태들**을 찾는 것입니다.

힌트: `f(n) = f(n-1) + f(n-2)` 와 유사한 구조입니다.

아래에 점화식을 스스로 정의해 보세요.

### ✏️ 점화식 작성 (학생 작성)
- f(1) = 1
- f(2) = 2
- f(3) = f(2)+f(1) = 2 + 1 =3
- f(4) = f(3) + f(2)= 3 + 2 = 5
- f(n) = f(n-1)+f(n-2) (단 n>2)


---
## Step 3. 반복 DP 방식으로 코드 구현하기
`O(n)` 반복문으로 해결합니다.

아래 템플릿을 완성하세요.

class Solution:
    def climbStairs(self, n: int) -> int:
        \"\"\"
        반복 DP를 사용해 f(n)을 계산하는 함수입니다.
        점화식 기반으로 bottom-up 방식으로 구현하세요.

        요구사항:
        - n=1,2 에 대한 에지 케이스 처리
        - O(n) 반복 DP
        \"\"\"
        if n <= 2:  ##계단이 1개나 2개 일때는 바로 반환
            return n  ##엣지케이스 처리됨

        dp = [0]*(n + 1) 
        \"\"\"인덱스 번호를 계단 칸수와 맞추기위해서 n+1,
        0을 n+1번 반복해서 리스트를 만들어놔
        ex>n=5,dp = [0,0,0,0,0,0]
        
        하필 인덱스에 0을 넣어 리스트를 만드는 것은, 
        비어있음, 아직 값이 채워지지 않음을 의미하는 초기값이다!!
        
        나중에, 코드를 실행하면서 dp[3] = 3 처럼 값을 채워넣을 텐데
        만약 값이 안바뀌고 여전히 0 이라면 아직 계산이 안됬거나 방법이
        없구나- 라고 알수있대\"\"\"

        dp[1] = 1
        dp[2] = 2  # 초기값처리, f(n) = f(n-1) + f(n-2), n >2 임

        for i in range(3, n + 1):  #n은 값이 주어질거고, 3부터 n+1까지 루프를 돌건데.
            dp[i] = dp[i-1] + dp[i-2]  #n이 3이면 range(3,4) 이고, range는 끝 숫자는 포함하지않으므로
                                        # i는 3 딱 하나만 실행된다

        return dp[n] #원하는 것은 n개의 계단을 오르는 방법의 총 가짓수 이므로
                    #for 반복문이 끝나고나면, 마지막 계산값인 dp[n]값을 출력해야
                    #우리가 원하는 값을 알 수 있다
        
        # TODO: 코드를 완성하세요.
        raise NotImplementedError


---
## Step 3-2. 코드 테스트
아래 테스트를 실행하여 올바른 값이 출력되는지 확인하세요.


def run_tests():
    sol = Solution()
    tests = [1,2,3,10,45]
    for n in tests:
        print(f\"n={n}, ways={sol.climbStairs(n)}\")

run_tests()


---
## Step 4. 시간복잡도 & 공간복잡도 분석
아래에 직접 정리해보세요.


### ✏️ 복잡도 분석 (학생 작성)
- 시간복잡도: O(N), 주어진n만큼 반복문을 돌려야 한다. N에 비례함
- 공간복잡도: O(n), 새로운 리스트를 만들어 n개만큼 저장해야 한다. 리스트의 크기가 N에 따라 결정된다


---
## Step 5. 코드 정리 & 결과 캡처
- 주석 포함해 코드 정리
- 테스트 결과를 실행해 스크린샷 촬영 (제출 시 포함)


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Day5_daily_mission(문제).ipynb.txt'] = """# Day 5. 동적 프로그래밍 기초 – 데일리 미션
## LeetCode #70 — Climbing Stairs

이 노트북은 Day 5 데일리 미션인 **Climbing Stairs (DP)** 문제를 풀이하기 위한 학생용 템플릿입니다.

---
## 🎯 학습 목표
- DP의 기초 패턴(작은 문제의 해를 이용해 큰 문제 해결하기)을 이해한다.
- Climbing Stairs 문제에서 점화식을 스스로 도출한다.
- 반복 DP(O(n))로 효율적으로 해결한다.
- 에지 케이스(n=1,2)를 정확히 다룬다.

---
## 📌 문제 설명
당신은 계단을 오르고 있습니다. 꼭대기에 도달하려면 **n개의 계단**을 올라야 합니다. 매번 한 번에 **1계단 또는 2계단**을 오를 수 있습니다.

**꼭대기까지 올라갈 수 있는 서로 다른 방법의 수를 구하세요.**

### 예시
- n = 2 → 2가지 방법 (1+1, 2)
- n = 3 → 3가지 방법 (1+1+1, 1+2, 2+1)

---
## 🛠️ Prerequisites
본 미션은 추가적 라이브러리 명시 없이 설계 가능합니다.

---
## Step 1. 문제 이해 및 테스트 케이스 분석
아래 칸에 직접 정리해보세요.


### ✏️ 테스트 케이스 분석 (학생 작성)
- n=1 일 때 경우의 수:1; 1가지
- n=2 일 때 경우의 수:1+1, 2; 2가지
- n=3 일 때 경우의 수:1+1+1,2+1,1+2; 3가지
- 직접 n=4, n=5 를 손으로 구해보면?
- n=4 일때, 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2 ; 5가지
- n=5 일때, 1+1+1+1+1, 2+1+2, 1+2+2, 2+2+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1 ; 8가지

---
## Step 2. DP 점화식 세우기
DP의 핵심은 **현재 칸으로 오기 위한 이전 상태들**을 찾는 것입니다.

힌트: `f(n) = f(n-1) + f(n-2)` 와 유사한 구조입니다.

아래에 점화식을 스스로 정의해 보세요.

### ✏️ 점화식 작성 (학생 작성)
- f(1) = 1
- f(2) = 2
- f(3) = f(2)+f(1) = 2 + 1 =3
- f(4) = f(3) + f(2)= 3 + 2 = 5
- f(n) = f(n-1)+f(n-2) (단 n>2)


---
## Step 3. 반복 DP 방식으로 코드 구현하기
`O(n)` 반복문으로 해결합니다.

아래 템플릿을 완성하세요.

class Solution:
    def climbStairs(self, n: int) -> int:
        \"\"\"
        반복 DP를 사용해 f(n)을 계산하는 함수입니다.
        점화식 기반으로 bottom-up 방식으로 구현하세요.

        요구사항:
        - n=1,2 에 대한 에지 케이스 처리
        - O(n) 반복 DP
        \"\"\"
        if n <= 2:  ##계단이 1개나 2개 일때는 바로 반환
            return n  ##엣지케이스 처리됨

        dp = [0]*(n + 1) 
        \"\"\"인덱스 번호를 계단 칸수와 맞추기위해서 n+1,
        0을 n+1번 반복해서 리스트를 만들어놔
        ex>n=5,dp = [0,0,0,0,0,0]
        
        하필 인덱스에 0을 넣어 리스트를 만드는 것은, 
        비어있음, 아직 값이 채워지지 않음을 의미하는 초기값이다!!
        
        나중에, 코드를 실행하면서 dp[3] = 3 처럼 값을 채워넣을 텐데
        만약 값이 안바뀌고 여전히 0 이라면 아직 계산이 안됬거나 방법이
        없구나- 라고 알수있대\"\"\"

        dp[1] = 1
        dp[2] = 2  # 초기값처리, f(n) = f(n-1) + f(n-2), n >2 임

        for i in range(3, n + 1):  #n은 값이 주어질거고, 3부터 n+1까지 루프를 돌건데.
            dp[i] = dp[i-1] + dp[i-2]  #n이 3이면 range(3,4) 이고, range는 끝 숫자는 포함하지않으므로
                                        # i는 3 딱 하나만 실행된다

        return dp[n] #원하는 것은 n개의 계단을 오르는 방법의 총 가짓수 이므로
                    #for 반복문이 끝나고나면, 마지막 계산값인 dp[n]값을 출력해야
                    #우리가 원하는 값을 알 수 있다
        
        # TODO: 코드를 완성하세요.
        raise NotImplementedError


---
## Step 3-2. 코드 테스트
아래 테스트를 실행하여 올바른 값이 출력되는지 확인하세요.


def run_tests():
    sol = Solution()
    tests = [1,2,3,10,45]
    for n in tests:
        print(f\"n={n}, ways={sol.climbStairs(n)}\")

run_tests()


---
## Step 4. 시간복잡도 & 공간복잡도 분석
아래에 직접 정리해보세요.


### ✏️ 복잡도 분석 (학생 작성)
- 시간복잡도: O(N), 주어진n만큼 반복문을 돌려야 한다. N에 비례함
- 공간복잡도: O(n), 새로운 리스트를 만들어 n개만큼 저장해야 한다. 리스트의 크기가 N에 따라 결정된다


---
## Step 5. 코드 정리 & 결과 캡처
- 주석 포함해 코드 정리
- 테스트 결과를 실행해 스크린샷 촬영 (제출 시 포함)


###**콘텐츠 라이선스**
<font color='red'><b>**(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다.**</b></font>

콘텐츠 일부 또는 전부를 **복사, 복제, 판매, 재판매 공개, 공유** 등을 할 수 없습니다. 유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다.

유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다.
* 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
* 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
* 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
* 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
* 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
* 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위
* 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위"""
    s.raw_texts['Lecture 10.txt'] = """Lecture 10:
Problem Solving & Coding
김수경
이화여자대학교 인공지능융합전공 소속© 2025 Upstage Co., Ltd.
1
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의 지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한관리자에게 귀속되어 있습니다 .
콘텐츠일부또는전부를복사 , 복제 , 판매 , 재판매공개 , 공유등을할수없습니다 . 
유출될경우지식재산권 침해에대한책임을부담할수있습니다 . 
유출에해당하여 금지되는 행위의예시는다음과같습니다 . 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education 의콘텐츠임을 알아볼 수있는 저작물을 작성 , 공개하는 행위
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트 /실습 수행 이외의 목적으로 사용하는 행위
Problem 1 –Hash Table
https://leetcode.com/problems/two -sum/10 Problem Solving & Coding
Problem 1 –Hash Table10 Problem Solving & Coding
Problem 2 –Graph (BFS/DFS)
https://leetcode.com/problems/number -of-islands/10 Problem Solving & Coding
Problem 2 –Graph (BFS/DFS)10 Problem Solving & Coding
Problem 3 –Tree
https://leetcode.com/problems/maximum -depth -of-binary -
tree/description/10 Problem Solving & Coding
Problem 3 –Tree10 Problem Solving & Coding
Problem 4 –Heap
https://leetcode.com/problems/kth -largest -element -in-an-array/10 Problem Solving & Coding
Problem 4 –Heap10 Problem Solving & Coding
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['Lecture 2.txt'] = """Lecture 2:
Arrays & Linked Lists
김수경
이화여자대학교 인공지능융합전공 소속© 2025 Upstage Co., Ltd.
1
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의 지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한관리자에게 귀속되어 있습니다 .
콘텐츠일부또는전부를복사 , 복제 , 판매 , 재판매공개 , 공유등을할수없습니다 . 
유출될경우지식재산권 침해에대한책임을부담할수있습니다 . 
유출에해당하여 금지되는 행위의예시는다음과같습니다 . 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education 의콘텐츠임을 알아볼 수있는 저작물을 작성 , 공개하는 행위
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트 /실습 수행 이외의 목적으로 사용하는 행위
3Arrays01
4Arrays02 Arrays & Linked Lists
● An array is an object comprising a numbered sequence of memory boxes
○ More fundamental data structure that Python lists are built on.
○ This is why we can easily access the i-th element of list A by using A[i].
● An array comprises
○ Fixed integer length (N) –should be set when initializing it
○ A sequence of Nmemory boxes (numbered 0 through N-1)
[1] http://1moment.t istory.com[1] 
Array
(Fixed length)List
(Dynamic length)
Resizing
Shifting
Copying
Internal Implementation: Memory
● Internally, all variables and constants we use in our program should be stored somewhere in memory .
○ For a single variable of a primitive type (int, float, …), we know its size (how many bits are needed).
3 10a = 3 b = 10 b += 7
17c = 1234567890L
123456789002 Arrays & Linked Lists
5
Index 0 1 2 3 4 5 6 7 8 9
Value 0 0 0 0 0 0 0 0 -0 0Array Resizing
● Two problems of an array due to its fixed length
○ Memory wastage : if it contains only n<< Nvalid elements
○ Memory shortage : if it wants to contain more than Nelements
● Array resizing: create another larger array and copy all the elements
○ L.append(3) when the current array is full.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
L
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 2110
010
3
Create 
a new long array O(1)Create(copy) 
a new long array O(N)Add 
a new element O(1)02 Arrays & Linked Lists
6
Internal Implementation: Memory
● Now, let ’s think about the time complexity!
○ Theoretical time complexity for a.append(6) ?
○ Actual time complexity fora.append(6) , if there ’s no enough space after it?
3 1017
12345678901 2 3 4 5a.append(6)
This is not ideal, since we do not have to know how memory space is 
being used at every moment!O(1)
O(N)02 Arrays & Linked Lists
7
Array Resizing
● Array resizing is expensive: new memory boxes and copy operation
○ Increasing size by one every time is not efficient (too many resizing)
○ Increasing size too much at once is not efficient either (memory wastage)
● To resize fewer, Python list size grows as 0, 4, 8, 16, 25, 35, 46, 58, …
○ Mild over -allocation proportional to the current size
● Anyway, is there any better way of organizing a collection of data to support append and pop easily?02 Arrays & Linked Lists
8
9Linked Lists02
Linked Lists
● Main idea:
○ Allow each element in the list to be scattered in the memory .
○ Instead, each element points to the next one .
3 1017
12345678901 2 3 4 5l.append (5)
1 2 7 3 4 5 4 55
7 2 13579246810l.append (7) l.append (2)02 Arrays & Linked Lists
10
Linked Lists
● Class Node
○ Because we always need to store the item and the pointer to the next node, let ’s make this as a class!
class Node():
def __init__ (self, x):
self.item = x
self.next = None
a = Node(5)
b = Node(6)
a.next = b5a
6b
print(a.item)
print(a.next.item)5
6itemnext02 Arrays & Linked Lists
11
Review: Python Object Reference
p = Node(5)
p = Node(6)p.item q.item
5
6
q = p 6 6
q = Node(9) 6 9
p = None Error! 9
q = p Error! Error!
02 Arrays & Linked Lists
12
Singly Linked List
● Let’s design the singly linked list data structure. What functionalities do we need?
○ Creating an empty list
○ Adding / inserting a new item
○ Retrieving an item
○ Deleting / removing an existing item
5a
6
itemnext3 7at position i02 Arrays & Linked Lists
13
Singly Linked List
● Class LinkedList
○ We keep only the reference to the first node .
○ At creation, first node is None , having no element in the list.
class Node():
def __init__ (self, x):
self.item = x
self.next = Noneclass LinkedList ():
def __init__ (self):
self.first = None
def insert(self, x, i):
# insert x at [i]
def get(self, i):
# get item at [i]
def delete(self, i):
# delete item at [i]5first
6
itemnext02 Arrays & Linked Lists
14
Inserting an Item at position i
● Step 1: Creating a new node with the given item.
5first
6
itemnext3 7
4● Step 2: Traverse to the ( i-1)-th position.
● Step 3: Set the new node ’s next as the original i-th node.
● Step 4: Update the ( i-1)-th node ’s next as the new node.Example:
insert “4”at position 2.
curr curr02 Arrays & Linked Lists
15
Inserting an Item at position i
● Step 1 : Creating a new node with the given item.
● Step 2 : Traverse to the ( i-1)-th position.
● Step 3 : Set the new node ’s next as the original i-th node.
● Step 4 : Update the ( i-1)-th node ’s next as the new node.def insert(self, x, i):
# insert x at [i]
new_node = Node(x)
pos = 0
curr = self.first
while pos < i -1:
curr = curr.next
pos += 1
new_node.next = curr.next
curr.next = new_nodeclass Node():
def __init__ (self, x):
self.item = x
self.next = None
5first
6
itemnext3 7
4curr curr
new_node
Step 1Step 2
Step 3 Step 402 Arrays & Linked Lists
16
Does it work at the end?
● Step 1: Creating a new node with the given item.
● Step 2: Traverse to the ( i-1)-th position.
● Step 3: Set the new node ’s next as the original i-th node.
● Step 4: Update the ( i-1)-th node’s next as the new node.Example:
insert “4”at position 4.02 Arrays & Linked Lists
175first
6
itemnext3 7
4curr curr curr curr

Does this work at the beginning?
● Step 1: Creating a new node with the given item.
5first
6
itemnext3 7
4● Step 2: Traverse to the ( i-1)-th position.
● We need special treatment when we insert at position 0!Example:
insert “4”at position 0.
curr curr curr curri -1 = -1 
02 Arrays & Linked Lists
18
Inserting an Item at position i
● If inserting at the first position:
○ Step 1: Creating a new node with the given item.
○ Step 2 : Set the new node ’s next as the original first node .
○ Step 3 : Update the first node reference to the new node.
● else:
○ Step 1: Creating a new node with the given item.
○ Step 2: Traverse to the ( i-1)-th position.
○ Step 3: Set the new node ’s next as the original i-th node.
○ Step 4: Update the ( i-1)-th node ’s next as the new node.def insert(self, x, i):
# insert x at [i]
if i == 0:
new_node = Node(x)
new_node.next = self.first
self.first = new_node
else:
new_node = Node(x)
pos = 0
curr = self.first
while pos < i -1:
curr = curr.next
pos += 1
new_node.next = curr.next
curr.next = new_nodeCheck : does this work when we insert the very first item 
(that is, does it work when self.first = None )?02 Arrays & Linked Lists
19
Inserting an Item at position i
def insert(self, x, i):
# insert x at [i]
if i == 0:
new_node = Node(x)
new_node.next = self.first
self.first = new_node
else:
new_node = Node(x)
pos = 0
curr = self.first
while pos < i -1:
curr = curr.next
pos += 1
new_node.next = curr.next
curr.next = new_nodeCheck : what happens with our code if i> last position?
It will crash here, 
when it tries to access None.next
7curr
…None
We should prevent this, instead of letting the users to be 
responsible!02 Arrays & Linked Lists
20
Size Variable
● First try:
○ Let’s add a check at the beginning, if iis within the 
valid range.
○ Valid range?def insert(self, x, i):
# insert x at [i]
if i == 0:
new_node = Node(x)
new_node.next = 
self.first
self.first = new_node
else:
new_node = Node(x)
pos = 0
curr = self.first
while pos < i -1:
curr = curr.next
pos += 1
new_node.next = curr.next
curr.next = new_nodeFrom 0 to current length (item count)if i > size: return
● But, how do we know the size?
○ A naive way: traverse from the first until we meet 
None .
○ This is not efficient, since we need to traverse N
items whenever we insert a new item, regardless of 
the target position. 
○ Any better way?elif i <= size:02 Arrays & Linked Lists
21
Size Variable
● Solution : Let ’s keep the size variable in the class, and 
maintain it whenever we insert or delete an element.
● Time complexity?
class LinkedList ():
def __init__ (self):
self.first = None
self.size = 0
def insert(self, x, i):
# insert x at [i]
def get(self, i):
# get item at [i]
def delete(self, i):
# delete item at [i]def insert(self, x, i):
# insert x at [i]
if i == 0:
new_node = Node(x)
new_node.next = self.first
self.first = new_node
self.size += 1
elif i <= self.size:
new_node = Node(x)
pos = 0
curr = self.first
while pos < i -1:
curr = curr.next
pos += 1
new_node.next = curr.next
curr.next = new_node
self.size += 1O(1)02 Arrays & Linked Lists
22
Retrieving an Item at position i –Homework
● Basic logic
○ Step 1: Traverse to the i-th position.
○ Step 2: Return the item in the node.
● Any special cases to consider?
○ Check if your implementation works when
■i = 0
■i > self.size
■self.size = 0
■ …def get(self, i):
# get item at [i]
# TODO(students): implement!
return ?02 Arrays & Linked Lists
23
Deleting an Item at position i
● Step 1: Traverse to the ( i-1)-th position.
5first
6
itemnext3 7● Step 2: Set the ( i-1)-th node ’s next as the target ’s next.Example:
delete item at position 2.
curr currThis node is no longer accessible. 
“3”is no longer in your list!02 Arrays & Linked Lists
24
Deleting an Item at position i
● Step 1 : Traverse to the ( i-1)-th position.
● Step 2 : Set the ( i-1)-th node ’s next as the target ’s next.def delete(self, i):
# delete item at [i]
pos = 0
curr = self.first
while pos < i -1:
curr = curr.next
pos += 1
curr.next = curr.next.next
self.size -= 1class Node():
def __init__ (self, x):
self.item = x
self.next = None
5first
6
itemnext3 7curr curr
Any edge case here?
Step 2Step 102 Arrays & Linked Lists
25
Does this work at the end?
5first
6
itemnext3 7curr● Step 1: Traverse to the ( i-1)-th position.
● Step 2: Set the ( i-1)-th node ’s next as the target ’s next.Example:
delete item at position 3.
02 Arrays & Linked Lists
26
Does this work at the beginning?
5first
itemnextcurr● Step 1: Traverse to the ( i-1)-th position.
● Step 2: Set the ( i-1)-th node ’s next as the target ’s next.Example:
delete item at position 0.
i -1 = -1 
Again, we need special treatment when we delete the first one!
def delete(self, i):
# delete item at [i]
pos = 0
curr = self.first
while pos < i -1:
curr = curr.next
pos += 1
curr.next = curr.next.next
self.size -= 1This condition is 
never satisfied.if i == 0:
self.first = self.first.next
else:
...02 Arrays & Linked Lists
27
Time Complexity
● Time complexity of Linked List?
Task Worst case Average case Best case
Insertion
Retrieval
DeletionO(N)
O(N)
O(N)O(N)
O(N)
O(N)O(1)
O(1)
O(1)
Happen when?02 Arrays & Linked Lists
28
Doubly Linked List
● Sometimes it is useful to have ability to access previous items.
● No asymptotic benefit on complexity.02 Arrays & Linked Lists
[1] https://maryash.github.io/235/p rojects/p roject_3/project _3.html[1] 
29
Comparison
● Array
○ Consecutive memory space is assigned.
○ Fixed length
○ Random access is supported in O(1) .
○ Suffers from item shifting .
● Linked list
○ Scattered in the memory space.
○ Additional space is needed for storing the next reference.
○ No random access allowed. (Linear traversal is required, taking O( N).)
○ No shifting is needed even with size change.02 Arrays & Linked Lists
30
31Applications of Linked Lists03
Application Questions
● Print the middle of a given linked list. (Assume list size is not maintained.)
5 7 2 8 2 4 9● Brute -force solution
○ Traverse the entire list to count the number of elements.
○ Traverse half of them again.
○ → O( N)02 Arrays & Linked Lists
32
Application Questions
● Reverse a given linked list.
5 7 2 8 2 4 9
9 4 2 8 2 7 502 Arrays & Linked Lists
33
Application Questions
● Detect if there is a cycle in the given linked list.
5 7 2 8
2
4902 Arrays & Linked Lists
34
www.upstage.ai © 2025 Upstage Co., Ltd.
35
"""
    s.raw_texts['Lecture 3.txt'] = """Lecture 3:
Stacks & Queues
김수경
이화여자대학교 인공지능융합전공 소속© 2025 Upstage Co., Ltd.
1
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의 지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한관리자에게 귀속되어 있습니다 .
콘텐츠일부또는전부를복사 , 복제 , 판매 , 재판매공개 , 공유등을할수없습니다 . 
유출될경우지식재산권 침해에대한책임을부담할수있습니다 . 
유출에해당하여 금지되는 행위의예시는다음과같습니다 . 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education 의콘텐츠임을 알아볼 수있는 저작물을 작성 , 공개하는 행위
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트 /실습 수행 이외의 목적으로 사용하는 행위
Today: Stacks & Queues
● Stack
○ Last In, First out ( LIFO )
○ Access only to the most -recently added item.
● Queue
○ First In, First out ( FIFO )
○ Access only to the item that was added earliest .03 Stacks & Queues
[1] https://gohighbrow.co m/[1] 
3
4Stacks01
Stack Examples
Stack of cafeteria dishes
Backspacing with keyboard03 Stacks & Queues
[1]https://www.cs.vassar.edu/~cs125/lectures/lect 9 -Stacks/ch07.p df
[2] https://kr.123rf.com/photo_15834863_ 키보드 -키-버튼의 -아이콘을 -설정 -문자 -백-스페이스 -삭제 .html[1] [2] 
5
Stack Example: Checking Balances of Braces
03 Stacks & Queues
[1]https://www.slideshare.net/slideshow/stack -10033613/10033613[1] 
6
Stack Terminologies
● What functionality do we want to have with Class Stack?
○ Adding a new element ( push )
○ Retrieving the most recent item ( peek )
○ Deleting an item ( pop )
3push
1522pop03 Stacks & Queues
7
Stack Class Design
● Array -based Implementation
○ We use Python List for simplicity here. class Stack():
def __init__ (self):
self.data = []
self.top = -1
def push(self, x):
# insert x
def peek(self):
# get item
def pop(self):
# delete an item
def is_empty (self):
return (self.top == -1)3 15 22
topdataInternal data structure to store 
elements in the stack.
Indicates where is the 
most -recently added 
item.
We use this to decide if the stack 
is empty!03 Stacks & Queues
8
Stack Class Implementation
● Push
○ Do NOT specify where to insert.
○ The new element is added only at the top.class Stack():
def __init__ (self):
self.data = []
self.top = -1
def push(self, x):
self.data.append(x)
self.top += 1
def peek(self):
# get item
def pop(self):
# delete an item
def is_empty (self):
return (self.top == -1)3 15 22
topdataNew element is added at the end 
of theList with append .
Then, move the top 
position by 1.x03 Stacks & Queues
9
Stack Class Implementation
● Peek
○ Again, do NOT specify where to retrieve.
○ Stack always retrieves only the top element.class Stack():
def __init__ (self):
self.data = []
self.top = -1
def push(self, x):
self.data.append(x)
self.top += 1
def peek(self):
if not self.is_empty():
return self.data[self.top]
else: return None
def pop(self):
# delete an item
def is_empty (self):
return (self.top == -1)3 15 22
topdataFirst check if the stack 
contains any data to 
retrieve.
Retrieve the most 
recently -added item.1703 Stacks & Queues
10
Stack Class Implementation
● Pop
○ Again, do NOT specify from where to delete.
○ Stack always pops only the top element.class Stack():
def __init__ (self):
self.data = []
self.top = -1
def push(self, x):
self.data.append(x)
self.top += 1
def peek(self):
if not self.is_empty():
return self.data[self.top]
else: return None
def pop(self):
if not self.is_empty():
del self.data[self.top]
self.top -= 1
else: return None
def is_empty (self): (omitted)3 15 22 17
topdataRemove the top item, then 
move the top pointer by 1!
Note that with Python list , we may not explicitly need the 
variabletop ; instead, we may simply use 
len(self.list) to figure out the top position.03 Stacks & Queues
11
Stack Class Design
● Reference -based Implementation
○ We may implement this by using a Linked List .
○ Recall that the singly linked list is accessed from the first element , 
sequentially.
■ We may naturally use the first element as the top element!
■ Thus, we don’t have to maintain the top index.class Stack():
def __init__ (self):
self.data = LinkedList()
def push(self, x):
# insert x
def peek(self):
# get item
def pop(self):
# delete an item
def is_empty (self):
return self.data.is_empty()17 22 15 3
First
(Top)data
Exercise : implement this function in 
your Linked List by yourself!03 Stacks & Queues
12
Stack Class Implementation
● How to implement push, peek, pop?
○ Use the functions of the Linked List!
class Stack():
def __init__ (self):
self.data = LinkedList()
def push(self, x):
# insert x
def peek(self):
# get item
def pop(self):
# delete an item
def is_empty (self):
return self.data.is_empty()self.data.insert(x, 0)
return self.data.get(0)
self.data.delete(0)class LinkedList ():
def __init__ (self):
self.first = None
def insert(self, x, i):
# insert x at [i]
def get(self, i):
# get item at [i]
def delete(self, i):
# delete item at [i]03 Stacks & Queues
13
Time Complexity
● Time complexity of Stack?
Task Array -based Reference -based
Insertion
Retrieval
DeletionO(1)
O(1)
O(1)O(1)
O(1)
O(1)
= Best cases only in linked list
Stack is more efficient than (more general) array or linked 
list, if the data and problem satisfy stack’s condition!03 Stacks & Queues
14
15Applications of Stacks
(Homework)02
Application Questions
● Use stack(s) to check if a string with parentheses is well -formed.
○ “(3+4)*(2+5) ” is well -formed.
○ “((2*2)*3+1 ” is not well -formed.
○ “)(2+2 ” is not well -formed.
● What if we have more than one types of parentheses?
○ “{(2+1)*(3+2) -22}*7 ” is well -formed.
○ “{(7+2}*3) ” is not well -formed.03 Stacks & Queues
16
17Queues03
Queue Examples
Line of passengers at airport 
securityDrink older milk first
03 Stacks & Queues
[1]https://www.nbcnews.com/busin ess/travel/tsa -replaces -head -security -airpor t -lines -keep -get ting -lon ger -n579021
[2]https://brunch.co.kr/@myolivenot e/1974[1] [2] 
18
Queue Terminologies
● Similarly to the stack, queue also uses its own jargons:
○ Adding a new element ( enqueue )
○ Retrieving the oldest item ( peek )
○ Deleting an item ( dequeue )3enqueue1522
dequeue
11903 Stacks & Queues
19
Queue Class Design
● Array -based Implementation
○ We use Python List for simplicity here.class Queue():
def __init__ (self):
self.data = []
self.last = -1
def enqueue(self, x):
# insert x
def peek(self):
# get item
def dequeue(self):
# delete an item
def is_empty (self):
return (self.last == -1)3 15 22
lastdataInternal data structure to store 
elements in the stack.
Indicates where is the 
most -recently added 
item.
We use this to decide if the 
queue is empty!03 Stacks & Queues
20
Queue Class Implementation
● Enqueue
○ Insert always at the end (last).
○ Same as push in stack.class Queue():
def __init__ (self):
self.data = []
self.last = -1
def enqueue(self, x):
self.data.append(x)
self.last += 1
def peek(self):
# get item
def dequeue(self):
# delete an item
def is_empty (self):
return (self.last == -1)3 15 22
lastdataNew element is added at the end of 
the List with append .
Then, move the top 
position by 1.x
Time complexity? O(1)03 Stacks & Queues
21
Queue Class Implementation
● Peek
○ We retrieve always the oldest item, which is located at 
the first.class Queue():
def __init__ (self):
self.data = []
self.last = -1
def enqueue(self, x):
self.data.append(x)
self.last += 1
def peek(self):
if not self.is_empty():
return self.data[0]
else: return None
def dequeue(self):
# delete an item
def is_empty (self):
return (self.last == -1)3 15 22
lastdataFirst check if the stack 
contains any data to 
retrieve.
Retrieve the 
first item.17
Time complexity? O(1)03 Stacks & Queues
22
Queue Class Implementation
● Dequeue
○ We dequeue always the oldest item, located at the first.class Queue():
def __init__ (self):
self.data = []
self.last = -1
def enqueue(self, x):
self.data.append(x)
self.last += 1
def peek(self):
if not self.is_empty():
return self.data[0]
else: return None
def dequeue(self):
if not self.is_empty():
del self.data[0]
self.last -= 1
def is_empty (self): (omitted)3 15 22 17
lastdataDequeue the first 
item, then move the 
last reference.
15 22 17
Time complexity? O(N) 
A naive List -based implementation 
is problematic.
More special care is needed, but it is 
beyond the scope of this course.03 Stacks & Queues
23
Queue Class Design
● Reference -based Implementation
○ Similarly to Stack, let’s try Linked List .
○ As we enqueue and dequeue from different ends, we may 
keep references for both!
■ The beginning is naturally provided by the Linked List, 
so we only need to add the last reference.class Queue():
def __init__ (self):
self.data = LinkedList()
self.last = None
def enqueue(self, x):
# insert x
def peek(self):
# get item
def dequeue(self):
# delete an item
def is_empty (self):
return self.data.is_empty()17 22 15 3
firstdata
last03 Stacks & Queues
24
Queue Class Implementation
● How to implement enqueue, peek, dequeue?
○ Use the functions of the Linked List!
class Queue():
def __init__ (self):
self.data = LinkedList()
self.last = None
def enqueue(self, x):
# insert x
def peek(self):
# get item
def dequeue(self):
# delete an item
def is_empty (self):
return self.data.is_empty()return self.data.get(0)
self.data.delete(0)class LinkedList ():
def __init__ (self):
self.first = None
def insert(self, x, i):
# insert x at [i]
def get(self, i):
# get item at [i]
def delete(self, i):
# delete item at [i]03 Stacks & Queues
25
Queue Class Implementation
● How to implement enqueue, peek, dequeue?
○Enqueue is not as simple as others!
○ First, we do not know the last index .
○ Even though we maintain it, the insert of 
LinkedList will traverse the entire list , taking O(N) 
.
○ To avoid this, we need to take advantage of the 
self.last reference directly!class Queue():
def __init__ (self):
self.data = LinkedList()
self.last = None
def enqueue(self, x):
# insert x
def peek(self):
return self.data.get(0)
def dequeue(self):
self.data.delete(0)
def is_empty (self):
return 
self.data.is_empty()self.data.insert(x, ?)
new_node = Node(x)
if self.last is None:
self.data.first = new_node
else:
self.last.next = new_node  
self.last = new_node03 Stacks & Queues
26
Time Complexity
● Time complexity of Queue?
Task Array -based Reference -based
Insertion
Retrieval
DeletionO(1)
O(1)
O(1)O(1)
O(1)
O(1)
= Best cases only in linked list
We need special implementation to make 
deletion in O(1).03 Stacks & Queues
27
28Applications of Queues04
Application Questions
● Implement Queue using two Stacks.
○ Main idea: use the first stack for enqueue, and the other for dequeue.
○ Whenever we get a dequeue request but the second stack is empty, pop all elements from the first stack 
and push them into the second stack.
Stack for enqueue Stack for dequeue03 Stacks & Queues
29
www.upstage.ai © 2025 Upstage Co., Ltd.
30
"""
    s.raw_texts['Lecture 4.txt'] = """Lecture 4:
Hash Tables
김수경
이화여자대학교  인공지능융합전공  소속© 2025 Upstage Co., Ltd.
1
2저작권  안내
(주)업스테이지가  제공하는  모든  교육  콘텐츠의  지식재산권은
운영  주체인  (주)업스테이지  또는  해당  저작물의  적법한  관리자에게  귀속되어  있습니다 .
콘텐츠  일부  또는  전부를  복사 , 복제 , 판매 , 재판매  공개 , 공유  등을  할 수 없습니다 . 
유출될  경우  지식재산권  침해에  대한  책임을  부담할  수 있습니다 . 
유출에  해당하여  금지되는  행위의  예시는  다음과  같습니다 . 
● 콘텐츠를  재가공하여  온/오프라인으로  공개하는  행위
● 콘텐츠의  일부  또는  전부를  이용하여  인쇄물을  만드는  행위
● 콘텐츠의  전부  또는  일부를  녹취  또는  녹화하거나  녹취록을  작성하는  행위
● 콘텐츠의  전부  또는  일부를  스크린  캡쳐하거나  카메라로  촬영하는  행위
● 지인을  포함한  제3자에게  콘텐츠의  일부  또는  전부를  공유하는  행위
● 다른  정보와  결합하여  Upstage Education 의 콘텐츠임을  알아볼  수 있는  저작물을  작성 , 공개하는  행위
● 제공된  데이터의  일부  혹은  전부를  Upstage Education 프로젝트 /실습  수행  이외의  목적으로  사용하는  행위
Data Structures So Far
Insertion Retrieval Deletion Restriction
Sorted Array
Sorted Linked list
Stack
Queue
Hash TableO(N)
O(N)
O(1)O(log N)
O(N)
O(1)O(N)
O(N)
O(1)
O(1)
O(1)O(1)
O(1)O(1)
O(1)LIFO
FIFO
● 911 emergency calls and locating caller’s address
● Airline information system
● Web searchNeeded for applications that 
need radically fast operations:04 Hash Tables
3
4Data Indexed Arrays01
Data Indexed Arrays
● A regular list: [2, 5, 9, 10]
○ In this setting, we take O( N) to search a particular value.
Index[0][1][2][3]
Value 2 5 9 10
● What if we represent the data in a data -indexed array ?
Index [0][1][2][3][4][5][6][7][8][9][10]
Value F F T F F T F F F T T04 Hash Tables
5
Data Indexed Arrays
Index [0][1][2][3][4][5][6][7][8][9][10]
Value F F F F F F F F F F F● A data -indexed array has all possible data as its indices !
○ Initially, all values of the array are False  (i.e., di_array[x] = False  for all x in di_array ), meaning 
the array is empty.
○ When we insert  some value, the corresponding index becomes True .
○ Here, we assume that no duplicate keys are allowed.
di_array = DataIndexedArray()
di_array.insert(3)
di_array.insert(6)
di_array.delete(3)
T T04 Hash Tables
6
Data Indexed Arrays
● Why is this good?
○ We can insert, delete, and retrieve values in O(1) !
● Any problem then?
○ We can’t deal with values larger than 10 (the array size).
○ In other words, we need to use very large memory space  if we’d like to deal with large number, even though 
the data size itself is small.
○ It is not trivial how to deal with non -integer values , like string or floating point numbers.
di_array.insert(“ewha\") di_array.insert(21057381)
04 Hash Tables
7
Strings in Data Indexed Arrays
● Recall that each character can be represented as an 
ASCII code value (0~255).
○ “ewha”:
■ e: 101
■ w: 87
■ h : 104
■ a: 97
○ “ewha” 256: (101 ×2563) + (87 ×2562) + 
(104 ×256) + 97
● In this way, a string can be represented as a unique 
integer .
04 Hash Tables
[1]https://nl.pint erest.com/pin/395261304802336725/[1] 
8
Large Numbers in Data Indexed Arrays
● But still, we can’t avoid the problem of treating large numbers.
○ We may need some way to put arbitrary integers  in a reasonable size of memory .
Index[0][1][2][3][4][5][6][7][8] …[999]
Value F F F F F F F F F … Fdi_array.insert(21057381)04 Hash Tables
9
10Hash Tables02
Hash Table
Given a key, a function (called hash function ) determines where to locate it.
→ As long as this function can compute the address in O(1),
   insertion / retrieval / deletion can be still within O(1) .
Input range : the data domain
(e.g., string, arbitrarily large 
integer)Address calculator  should 
output an integer between 0 and 
table_size - 1.04 Hash Tables
[1] https://www.slideshare.net/slideshow/hashing -in-data -struct ure -is-presented -in-these -slides/274382978[1] 
11
Hash Functions
● A good hash function:
○ Easy and fast  to compute (in O(1))
○ Scatter  the data evenly  on the hash table.
● Selection digits
○ h(001 36482 5) = 35
● Folding
○ h(001364825) = 001 + 364 + 825 = 1190
● Modulo arithmetic
○ h(x) = x mod  table_size
○ h(1004) = 4 (if table_size = 100)
○ This is widely used, as it maps the integers uniformly  
over the internal array regardless of its size!
Hmm, then what should we do if 
two different keys coincidently 
map to the same address ?
Modulo operator (%)
x % y is the remainder 
when we divide x by y .04 Hash Tables
12
Collision
● Yes, unfortunately, it can happen with all hash functions we listed 
 .
○ Collision : the phenomenon that two keys are mapped into the same location in the hash table.
● Selection digits
○ h(001 36482 5) =  h(741 32538 5) = 35
● Folding
○ h(001364825) = h(825364001) = 1190
● Modulo arithmetic
○ h(2205) = h(2405) = 5 if table_size = 10004 Hash Tables
[1]https://www.cs.colostate.edu/~cs165/.Sp ring20/slides/16 -Hashing.pdf[1] 
13
Collision Resolution
● Collision is unavoidable; so, we need a method to resolve it efficiently.
● There are two groups of approaches:
○ Open addressing : allowing the items to be located in another place if the collision happened.
○ Separate chaining : allowing more than one item to be located at a place.
Open Addressing
4567
Let’s find another place to put it.Separate chaining
4567 7597Let’s put it there together with the 
existing one(s).Example: According to our hash function, 4567 
needs to be located at [22], but it is already 
occupied 
 .04 Hash Tables
[1]https://www.cs.colostate.edu/~cs165/.Sp ring20/slides/16 -Hashing.pdf[1] 
14
Open Addressing
● Linear probing : if the designated spot is occupied, try the right next 
index , until it finds an available one.
hi(x) = ( h0(x) + i) mod  table_size
● Causes primary clustering :
○ All keys mapped to [22], [23], [24], [25], … will suffer from 
collision.
○ If this cluster gets bigger, insertion / retrieval / deletion of keys 
corresponding to this region will take O( N) instead of O(1).
○ Gets significantly worse especially if consecutive numbers are 
sequentially added. ( e.g., 22 → 23 → 24, …)
04 Hash Tables
[1]https://www.cs.colostate.edu/~cs165/.Sp ring20/slides/16 -Hashing.pdf[1] 
15
Open Addressing
● Quadratic probing : if the designated spot is occupied, try the next set of 
indices, quadratically increasing  with the number of trials.
hi(x) = ( h0(x) + i2) mod  table_size
● Solves primary clustering :
○ Items collided at [23] suffers less from significant collisions 
originally happened at [22].
● Still suffers from secondary clustering :
○ For items collided at the same index for the first time, they must 
always follow the same trace.
04 Hash Tables
[1]https://www.cs.colostate.edu/~cs165/.Sp ring20/slides/16 -Hashing.pdf[1] 
16
Open Addressing
● Double Hashing : using two different hash functions to reduce 
collision probability.
hi(x) = ( α(x) + i * β(x)) mod  table_size
where α(x), β(x): some hash functions
● Can avoid primary and secondary clustering, since we probe with 
different steps depending on the input.h0(58)
h0(14)
h0(91)58
91
14h1(14)h1(91)04 Hash Tables
17
Separate Chaining
● Each location of the hash table is allowed to have more than one item.
○ A simplest example: a reference to a linked list.
04 Hash Tables
[1] https://med ium.com/@ramyjzh/d ata -struct ures -for-dummies -hash -tables -579ddd 1a4389[1] 
18
Separate Chaining
● Actually, we can put any other data structure that support key -based search.
04 Hash Tables
[1] https://med ium.com/@ramyjzh/d ata -struct ures -for-dummies -hash -tables -579ddd 1a4389[1] 
19
Performance of a Hash Table
● In general, having more items in the table reduces performance of a hash table.
○ This is unique to hash tables, unlike most other data structures!
● Let’s define load factor ( α) formally:  N/M
○ N: the actual number of elements inserted
○ M: the number of indices (table_size)
● With open addressing , α is always between 0 and 1. Once it reaches to 1,
we can’t add more data because there is no more available space.
○ If α gets close to 1 , there are probably lots of collisions, meaning longer processing time .
● With separate chaining , load factor can be > 1.
○ In this case, load factor means the average chain length per index, which is equivalent to th e expected 
number of linear traversal  to locate an item.
○ Obviously, higher load factor means slower data processing.04 Hash Tables
20
Efficiency of Hashing
When the load factor is low, hash table achieves ≈O(1), 
regardless of the collision resolution method.04 Hash Tables
[1]https://www.eecs.yorku.ca/course_archive/2003 -04/F/2011/2011A/DatStr_152_HashTab les.pdf[1] 
21
How to Decide the Table Size ( M)
● If we know the data size ( N) to be inserted, we can set M = N/α, where α is the desired load factor.
○ With small α, we focus more on speed.
○ With large α, we care more about the memory space.
○ It is known that α = 0.6~0.75  is a good balance between them.
● What if we don’t know the data size?
○ We have no choice but to dynamically adapt.
○ Starting with some default size (say, 101), then ( roughly ) double it when the load factor becomes larger 
than some threshold ( e.g., 0.6~0.75).04 Hash Tables
22
0 1 2 3 4
valuesindex 5 6 7 8 9Resizing Example
M=5N=0
α=00 1 2 3 4
valuesindex
M=5N=1
α=0.2M=5N=2
α=0.4M=5N=3
α=0.6M=5N=4
α=0.8
M=5N=5
α=1.0M=5N=6
α=1.2M=5N=7
α=1.4M=5N=8
α=1.6
Resizing!
Redistributing all 
items!M=10N=8
α=0.804 Hash Tables
23
Time Complexity of Resizing
● Besides resizing, hash table achieves O(1) insertion, deletion, and retrieval.
● Resizing is obviously not free 
○ Resizing a hash table with N items requires O(N) time to redistribute all N items.
● A good news 
 : we don’t always resize since one resizing operation doubles the number of indices.
○ The number of redistributing items while inserting N items:
■ 1 + 2 + 4 + 8 + ….  + N = 2N - 1
○ Overall, redistributing cost becomes O((2 N-1)/N) = O(1) on average !04 Hash Tables
24
25Implementations:
Dictionary vs Set in Python03
Python Dictionary
>>> tel = {'jerry': 1086, 'jose': 8249}
>>> tel[‘soo'] = 4127
>>> tel
{'jerry': 1086, 'jose': 8249, ＇soo': 5564}
>>> tel['jose']
8249
>>> del tel['jerry']
>>> tel['shawn'] = 8080
>>> tel
{'jose': 8249, ‘soo': 5564, 'shawn': 8080}
>>> list(tel)
['jose', ‘soo', 'shawn']
>>> sorted(tel)
['shawn', ‘soo', 'jose']
>>> 'jinri' in tel
False
>>> 'jeongwoo' not in tel
TrueInsertion
Retrieval
Deletion● Python internally provides the 
hash table under the name of 
Dictionary .
○ Key -value pairs  are 
stored in a hash table.
○ Key are unique and 
hashable.
○ Insertion, retrieval, 
deletion supported in 
O(1) .04 Hash Tables
26
Python Set
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b
{'r', 'd', 'b'}
>>> a | b
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b
{'a', 'c'}
>>> a ^ b
{'r', 'd', 'b', 'm', 'z', 'l'}Unique letters in a
Set difference
Set OR● If you don’t have an associated value , you 
may use Python Set , instead of Dictionary .
○ Only elements (keys) are stored in 
the hash table.
○ Elements are unique and hashable.
○ Insertion, retrieval, deletion supported 
in O(1) .Set AND
Set XOR04 Hash Tables
27
28Applications of Hash Tables04
Problem 1 - Palindrome
04 Hash Tables
29
Problem 2 - Smallest Missing Integer
● Given a list of integers, return the smallest positive integer which is not in that list.
Examples:
● [7, 2, 3, 5, 4, 1]  → 6
● [-1, 5, 2, 3, 9] → 1
● [17, 25, 4308, 1, 99] → 2# TODO(students): implement this!
def smallest_missing_pos_int (self, list):
  for each item in the list:
    insert into a hash table (hastset)
  for i = 1, 2, 3, ...:
    if the hash table contains i: keep going
    else: return i
Note : think about how many times we should iterate here.04 Hash Tables
30
Problem 3 – Two Sum
04 Hash Tables
31
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['Lecture 5.txt'] = """Lecture 5:
Tree
김수경
이화여자대학교  인공지능융합전공  소속© 2025 Upstage Co., Ltd.
1
2저작권  안내
(주)업스테이지가  제공하는  모든  교육  콘텐츠의  지식재산권은
운영  주체인  (주)업스테이지  또는  해당  저작물의  적법한  관리자에게  귀속되어  있습니다 .
콘텐츠  일부  또는  전부를  복사 , 복제 , 판매 , 재판매  공개 , 공유  등을  할 수 없습니다 . 
유출될  경우  지식재산권  침해에  대한  책임을  부담할  수 있습니다 . 
유출에  해당하여  금지되는  행위의  예시는  다음과  같습니다 . 
● 콘텐츠를  재가공하여  온/오프라인으로  공개하는  행위
● 콘텐츠의  일부  또는  전부를  이용하여  인쇄물을  만드는  행위
● 콘텐츠의  전부  또는  일부를  녹취  또는  녹화하거나  녹취록을  작성하는  행위
● 콘텐츠의  전부  또는  일부를  스크린  캡쳐하거나  카메라로  촬영하는  행위
● 지인을  포함한  제3자에게  콘텐츠의  일부  또는  전부를  공유하는  행위
● 다른  정보와  결합하여  Upstage Education 의 콘텐츠임을  알아볼  수 있는  저작물을  작성 , 공개하는  행위
● 제공된  데이터의  일부  혹은  전부를  Upstage Education 프로젝트 /실습  수행  이외의  목적으로  사용하는  행위
Definition of Tree
● A general tree T is partitioned into disjoint subsets:
○ A single node r, the root
○ Sets of general trees, called subtrees  of r● Terminology
○ node (vertex)
○ edge
○ parent
○ child
○ siblings
○ root
○ leaf
○ ancestor
○ descendant
○ subtree
05 Tree
3
Tree Examples
05 Tree
[1]http://18president.p a.go.kr/cheon gwad ae/organization/go vernment.php
[2] https://kr.pinterest.com/pin/146578162866571659/[1] [2] 
4
5Binary Tree01
Definition of Binary Tree
● T is binary tree , if
○ T is empty, or
○ T is partitioned into three disjoint subsets:
■ A single node r, the root
■ Up to two sets that are binary trees , called left and right subtrees of r
r
TL TR05 Tree
6
An Example of Binary Tree
● Algebraic expressions
05 Tree
[1]https://user.ceng.met u.edu.tr/~t can/ceng301_s1516/Schedule/week10.pdf[1] 
7
Height of a Tree
● Def. Height  of a Tree: the number of nodes  on the longest path from the root to a leaf.
Height: 3 Height: 5Height: 705 Tree
[1]https://user.ceng.met u.edu.tr/~t can/ceng301_s1516/Schedule/week10.pdf[1] 
8
Full Binary Tree
● Def. A binary tree T of height h is called Full binary tree , if
○ it is empty ( h = 0), or
○ both its left and right subtrees are full (of height h - 1).
Full BT of Height 0
Full BT of
Height 1Full BT of
Height 2Full BT of
Height 3
Full BT of Height 4
So now, you may feel why this is called full binary tree:
it is filled with nodes at all possible positions !05 Tree
] 
9
Complete Binary Tree
● Def. A binary tree T is called Complete binary tree , if
○ T is full down to level h - 1, and
○ with level h filled in from left to right.
Complete BT of
Height 2Complete BT of
Height 3Complete BT of Height 4
Must be filled (to be complete)
Optionally filled (to be complete)05 Tree
10
[1][2]
[3] [4] [5] [6][0]Array -based Implementation
● Recall: Array is a fundamental data structure with contiguous fixed -length chunk  of memory space.
○ When we implement List  with an array, it was straightforward to map the indices.
○ How can we assign designated indices for a binary tree?
● Let’s assume the tree is full, and assign the indices from 
root, left to right.
[7][8][9][10] [11][12][13][14]8
972
3 415
5 2 1 8 7 3 4 9 … …[0][1][2][3][4][5][6][7][8][9]
Height 1 Height 2 Height 3 Height 4
This implementation is efficient if the tree is 
(almost) full or complete.05 Tree
11
Array -based Implementation
● One more thing to consider: How can we figure out direct children  of a node?
○ With a tree, we usually access data from the root to the leaf.
○ Common rule connecting a node to its children?
[1][2]
[3] [4] [5] [6][0]
[7][8][9][10] [11][12][13][14]8
72
3
9 215● From parent, its left child :
[parent index] * 2 + 1  
● Right child:
[parent index] * 2 + 2  
● Similarly, from a child, its parent :
[child index - 1] // 205 Tree
12
Array -based Implementation
● Now, think about more general case: the tree may not be close to complete.
○ If we don’t have a node, we may set None  (or some other indicator for emptiness).
5 2 1 8 No
ne3No
neNo
ne7 …[0][1][2][3][4][5][6][7][8][9]
[1][2]
[3] [4] [5] [6][0]
[7][8][9][10] [11][12][13][14]8
72
3
9 215
● This implementation becomes less efficient  if the tree gets far from full or complete .05 Tree
13
Reference -based Implementation
● It is similar to the linked list; instead of having a single 
link to another node, Binary Tree Node has two 
references  to other nodes!
class TreeNode ():
  def __init__ (self, x):
    self.item = x
    self.left = None
    self.right = None
class BinaryTree ():
  def __init__ (self, node):
    self.root = node05 Tree
[1]http://ocw.ut m.my/file.php /31/Mod ule/ocwSearchTreeDec2011.pdf[1] 
14
Tree Traversal
● Traversal: visiting all nodes once
○ It is not straightforward to visit all nodes in a given tree, unlike an array or a linked list.
● There can be many different ways of traversal. We cover a few widely -used ones:
r
TL TRr
TL TRr
TL TR
Preorder
Root  - Left - Right21
3
Inorder
Left - Root  - RightPostorder
Left - Right - Root12
3 13
2
● Inside each subtree, the same rule applies recursively.05 Tree
15
Tree Traversal Example
● Preorder traversal?60
20 70
10 40
30 50● Inorder traversal?● Postorder traversal?
60 {20 subtree} 70
60 20 10 {40 subtree}  70
60 20 10 40 30 50  70
{20 subtree} 60 70
10 20 {40 subtree}  60 70
10 20 30 40 50  60 70{20 subtree} 70 60
10 {40 subtree} 20  70 60
10 30 50 40  20 70 6005 Tree
16
Tree Traversal Implementation
● Use recursion!
○ Base case: empty tree. Do nothing!
○ General case: 2 recursive calls + visiting the root.
○ The order depends on {pre, in, post} -order.
def preorder (node):
  if node is not None:
    print(node.item)
    preorder (node.left)
    preorder (node.right)
preorder (root)def inorder(node):
  if node is not None:
    inorder(node.left)
    print(node.item)
    inorder(node.right)
inorder(root)05 Tree
17
18Binary Search Tree02
Definition of Binary Search Tree
● Each node has a search key .
○ There are no duplicates  among the search keys in a binary search tree.
● For each node n, it satisfies:
○ n’s key is greater than all keys in its left subtree TL.
○ n’s key is less than all keys in its right subtree TR.
○ Both TL and TR are binary search trees.r
TL TR< <05 Tree
19
Binary Search Tree Examples
Check!  All these 3 BSTs contain the same data.05 Tree
[1]https://user.ceng.met u.edu.tr/~t can/ceng301_s1516/Schedule/week10.pdf[1] 
20
Binary Search Tree Operations
● Insert  a new item into a binary search tree.
● Retrieve  (search ) the item with a given search key from a binary search tree.
● Delete  the item with a given search key from a binary search tree.
● For all, according to the rule that {left subtree} < root < {right subtree} at all levels!05 Tree
21
Search (Retrieval)
● Task : Search if there is a node with the given key, and output the item if so.
○ If the given key is not in the tree, we should be able to figure it out as well.60
20 70
10 40
30 50● Main Idea : At each node, decide which subtree to search further. Only 
3 cases:
○ [Case 1] If the search key = item  at the node, we found  it!
○ [Case 2] If the search key < item  at the node, the target must 
be in its left subtree  if exists.
○ [Case 3] If the search key > item  at the node, the target must 
be in its right subtree  if exists.
○ For Case 2 & 3, move to the corresponding subtree, then repeat 
the same testing.
○ Repeat until you reach at a leaf. If you still do not meet Case 1, 
we conclude the key is not in the tree .40 55
Found!
Not exists05 Tree
22
Search (Retrieval): Implementation
● Implementation based on recursive calls:
def search(root, key):
  if root is None:
    return None  # Not found
  elif key == root.item:
    return root  # Found
  elif key < root.item:
    return search(root.left, key)
  else:  # key > root.item
    return search(root.right, key)Base case (empty BST): Not found!
General case: case 1, 2, 305 Tree
23
Search (Retrieval): Time Complexity
● Time complexity  of search operation?
○ At each node, we compare two values once, and decide where to go. → O(1)
○ How many times?
● Thus, the worst time performance = tree height!
● In terms of N (the number of data points in the tree), what’s the asymptotic (Big O) complexity of tree search?Length from the root to the leaf!
If the tree is balanced  (close to full), the height 
gets closer to O(log N).
If the tree is unbalanced (close to linked list), the height 
gets closer to O(N).
Then, how the shape of a tree is determined? We will revisit this soon.05 Tree
[1]https://user.ceng.met u.edu.tr/~t can/ceng301_s1516/Schedule/week10.pdf[1] 
[1] 
24
Insertion
● Task : Insert a new key into the BST, preserving BST conditions.
○ We need to find the right location to put the new node.60
20 70
10 40
30 50● Main Idea : Insertion is basically a failed search . When we conclude the 
item does not exist, insert the new node right there!
○ [Case 1] If the search key = item  at the node, we found  it!
○ [Case 2] If the search key < item  at the node, the target must be 
in its left subtree  if exists.
○ [Case 3] If the search key > item  at the node, the target must be 
in its right subtree  if exists.
○ For Case 2 & 3, move to the corresponding subtree, then do the 
same testing.
○ Repeat until you reach at a leaf. Insert the new node there!55
5505 Tree
25
Insertion: Implementation
● Implementation based on recursive calls:
def insert(root, item):
  if root is None:
    new_node = TreeNode(item)
    return new_node
  elif key == root.item:
    # ERROR: already exists
  elif key < root.item:
    new_subtree = insert(root.left, item)
    root.left = new_subtree
    return root
  else:  # key > root.item
    new_subtree = insert(root.right, item)
    root.right = new_subtree
    return rootBase case: Create new node
General case: 3 ways05 Tree
26
Deletion
● Task : Delete a node with the given key, preserving BST conditions  after deletion.
○ After deletion of an intermediate node, the tree will be broken 
 .
● Main Idea :
○ [Case 1] If the node to delete is a leaf , simply remove it.
○ [Case 2] If the node to delete has a single child , the subtree will take it over.
○ [Case 3] If the node to delete has both children , elect the leftmost item in the right subtree as the new 
root.05 Tree
27
Deletion (Case 1)
● When the target node is a leaf , we can simply remove it.60
20 70
10 40
30 50● After deletion, the resulting tree
○ is still connected , and
○ still satisfies the BST conditions .
80
3505 Tree
28
Deletion (Case 2)
● When the target node has one child , the existing child takes the position of 
the target node, taking its descendents (subtree). 60
20 70
10 40
30 50● After deletion, the resulting tree
○ is broken ,
○ still satisfies the BST conditions.8080● After the right subtree takes over, the resulting tree
○ is no longer broken ,
○ still satisfies the BST conditions.
This slide is best seen with animations. 3505 Tree
29
Deletion (Case 3)
● When the target node has both children , we elect the target’s immediate successor (=left -most node in the 
right subtree) as the new root.
60
20 70
10 40
30 50● After deletion, the resulting tree is broken.
○ Cannot simply take one subtree as new root, since we have 
two.
80● To make the resulting tree satisfy BST conditions, we elect the 
immediate successor  of the deleted node. The resulting tree, however, 
is still broken !
○ Why immediate successor? With it, it’s guaranteed to satisfy the 
BST conditions!This slide is best seen with animations.
30
Similarly, we may nominate the immediate predecessor  (=right -most item in the left subtree.)35● The deleted immediate successor node may need to adopt its orphan 
right child (if any).
○ Here, it is guaranteed that no left child exists.3505 Tree
30
Deletion: Implementation
def delete(root, key):
  if root is None:
    return root
  if key < root.key:
    root.left = delete(root.left, key)
  elif key > root.key:
    root.right = delete(root.right, key)
  else:
  ... (to be continued)Locating the target
delete  function returns the subtree to 
replace the target node to be deleted.05 Tree
31
Deletion: Implementation
... (continuing)
  else:
    if root.left is None:
      new_root = root.right
      root = None
      return new_root
    elif root.right is None:
      new_root = root.left
      root = None
      return new_root
    else:
      im_su = get_immediate_successor (root)
      root.key = im_su.key
      root.right = delete(root.right, im_su.key)
  
    return rootCase 3: both childrenCase 1: no child if root.right  is also None
Case 2: single childdef get_immediate_successor (target):
    curr = target.right
    while curr.left is not None :
      curr = curr.left
    return curr
After this line, we now 
delete the node im_su . 05 Tree
32
Revisiting the shape of BST
● For a given data, how is the shape of BST determined?
○ Let’s try to insert “4, 7, 2, 3, 5, 1, 6”:
4
7 2
3 5 1
6○ Suppose the same data is given in a different 
order: “7, 6, 5, 4, 3, 2, 1”:
7
6
5
4
3
2
1Shape of the tree is determined by the 
order of insertion !
Unfortunately, we often cannot control 
the datastream itself. 
05 Tree
33
Balanced Trees
● We desire to make the tree more balanced  for faster operations.
● There are some special trees that guarantee balance  up to some level, but details of them are beyond of this 
course.
Red -black tree
: guarantees that the height is lower than 2 log( N+1).AVL tree
: guarantees that heights of the two child subtrees 
of any node differ by at most 1.05 Tree
[1]https://kostja.github.io/misc/2017/02/23/tarant ool -data -struct ures.html
[2]https://blog.naver.com/luex r/223479906039[1] [2] 
34
Tree Sort
● Inorder traversal  on a binary search tree lists the data in sorted order.
○ Due to the BST conditions, all values in the left subtree < root value < all values in the right subtree, at all 
nodes.
○ Inorder traversal visits nodes in the order of left - root - right!
r
TL TR
Inorder
Left - Root  - Right12
3● Time complexity?
○ We first need to insert all data into a BST.
→ O(log N) per each element × N of them = O(N log N)
(This assumes use one of the balanced trees!)
○ Then, inorder traversal: O(N)
← we visit one node at a time.
○ Overall, O(N log N) if the tree is balanced.
Otherwise, worst performance will be O(N2).05 Tree
35
Time Complexity
● Time complexity of Binary Search Tree operations?
Task Average -case Worst -case
Insertion
Retrieval
Deletion
TraversalO(log N)
O(log N)
O(log N)O(N)
O(N)
O(N)
= When the tree is significantly unbalanced.O(N) O(N)
When?05 Tree
36
37Applications of Binary Search Trees03
Problem 1
● Test if two binary trees are symmetric.
60
20 70
10 40
30 5060
20 70
10 40
30 5005 Tree
38
Problem 2
● Test if a binary tree is balanced.
○ A binary tree is balanced if the difference in the height of its left and right subtrees is at most 1 for all 
nodes in the tree.
60
20 70
10 40
30 5060
20 70
10 4005 Tree
39
Problem 3
05 Tree
40
Problem 305 Tree
41
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['Lecture 6.txt'] = """Lecture 6:
Graph & Search (BFS,DFS)
김수경
이화여자대학교 인공지능융합전공 소속© 2025 Upstage Co., Ltd.
1
2저작권 안내
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다 .
콘텐츠 일부 또는 전부를 복사 , 복제 , 판매 , 재판매 공개 , 공유 등을 할수없습니다 . 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다 . 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다 . 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education 의콘텐츠임을 알아볼 수있는 저작물을 작성 , 공개하는 행위
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트 /실습 수행 이외의 목적으로 사용하는 행위
3Graphs01
Definitions
● Graph G= (V, E), where
○ Vis a set of vertices (nodes), and
○ Eis the set of edges.
● Subgraph : a subset of a graph’s vertices and edges.
● Two vertices are adjacent if they are joined by an edge.
A
B
DC
EA
DC06 Graph & Search (BFS, DFS)
Graph Examples
06 Graph & Search (BFS, DFS)
[1]서울교통공사
[2] Google Map[1] [2] 
Graph Examples
06 Graph & Search (BFS, DFS)
[1] [2] 
[1]https://www.smrfoundation.org/2010/04/28/mapping -the-twitter -network -of-www2010 -with-nodexl/
[2] https://noureldien.com/research/videograph/index.html
Graph Examples
06 Graph & Search (BFS, DFS)
[1] [2] 
[1 https://www.nitrc.org/project/list_screenshots.php?group_id=504&screenshot_id=381
[2] https://www.researchgate.net/figure/Distinction -between -a-Graphical -Model -and-a-CAD -Model_fig1_361770871

Definitions
● Path : A sequence of connected edges 
● Cycle : A path whose starting vertex and ending vertex are the same
● Simple path : A path that contains no cycle
● Simple cycle : A cycle that contains no cycle in it
A
B
DC
EA
B
DC
ESimple pathSimple cycle06 Graph & Search (BFS, DFS)
Definitions
● Connected graph : Each pair of distinct vertices has a path between them
● Complete graph : Each pair of distinct vertices has an edge between them
Connected graph Disconnected graph Complete graph06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week14.pdf
Definitions
● Weighted graph vs. unweighted graph: whether edges have weights
● Directed graph vs. undirected graph: whether edges have direction
Weighted graph Directed graph06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week14.pdf
Definitions
● These are not allowed in (regular) graphs:
○ Multigraph : more than one edges allowed for a same pair of nodes.
○ Self edge : an edge starts from and arrives at the same node.
Multigraph Self edge
06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week14.pdf
Tree vs.Graph?
● Tree is a special case of graph, where
○ all nodes are connected , and
○ there is no cycle .
A
B
DC
EA
B
DC
E
Any node can be the root.06 Graph & Search (BFS, DFS)
Exercise
● Tree vs.Graph?
● Connected vs.disconnected?
● Cyclic vs.acyclic?
● Directed vs.undirected?
Graph
Connected
Cyclic
Directed
06 Graph & Search (BFS, DFS)
[1]서울교통공사[1] 
14Graph Representation02
Adjacency Matrix
● Adjacency matrix
○ A graph is represented by an N×Nmatrix (2D array) , where matrix[i][j] is 1 if there is an edge 
between vertex iand vertex j, and 0 otherwise.
○ In case of a directed graph, matrix[i][j] is 1 if there is an edge from vertex ito vertex j.
○ In case of a weighted graph, matrix[i][j] has the weight value, instead of 1.
● This is analogous to the array -based implementation of other data structures.
○ We use fixed size of memory (corresponding to N×N), regardless of how many edges we have.
○ (+) random access is done at O(1).
○ (-) inefficient use of memory if the graph is sparsely connected.06 Graph & Search (BFS, DFS)
Adjacency Matrix: Example
Directed graph06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Adjacency Matrix: Example
Weighted undirected graph
06 Graph & Search (BFS, DFS)
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf[1] 
Adjacency List
● Adjacency list
○ A graph is represented by Nlinked lists where list[i] is the list of vertices that is adjacent to vertex i.
○ In case of weighted graph, the list also contains the weight values.
● This is analogous to the reference -based implementation of other data structures.
○ For each node, we use variable size of memory, depending on the number of edges connected from/to it.
○ (+) efficient use of memory if the graph is sparsely connected.
○ (-) need linear search for an edge. (Not a big problem if the graph is sparse enough.)06 Graph & Search (BFS, DFS)
Adjacency List: Example06 Graph & Search (BFS, DFS)
Directed graph
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Adjacency List: Example
Weighted undirected graph06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Adjacency List: Implementation
class undirected_graph ():
def __init__ (self, nodes, edges):
self.v = nodes[:]
self.e = {}
for node in nodes:
self.e[node] = []
for (u, v) in edges:
self.e[v].append(u)
self.e[u].append(v)
v = ['a', 'b', 'c']
e = [('a', 'b'), ('b', 'c')]
graph = undirected_graph(v, e)
print(graph.e)
{'a': ['b'], 'b': ['a', 'c'], 'c': ['b']}● Can you modify this to
○ directed graph?
○ weighted graph?06 Graph & Search (BFS, DFS)
Google Interview Question
● Design a Graph class.
○ What is the graph for? What data to be stored?
○ How big will be the graph?
○ Is the graph expected to be sparse or dense ?
○ What operations are we going to use most frequently?
○ Is the node & edge likely static or dynamic ?06 Graph & Search (BFS, DFS)
23Graph Traversal03
Graph Traversal
● Goal: Visiting all nodes once in the graph.
○ E.g. , for searching a specific node
○ Caution: graphs may have cycles and may be disconnected . We still should visit all nodes, but should 
not visit the same node more than once, and finish once we visit all of them.
jk06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Depth First Search (DFS)
● Start from an arbitrary node.
● Visit any connected unvisited node from there.
● If no more node to visit, backtrack to the previous one, and keep going.
jk
This slide is best seen with animations.06 Graph & Search (BFS, DFS)
Depth First Search (DFS)
● To backtrack, we need to trace our footprints!
● What data structure would work best?
○ We backtrack to the most recently visited previous node!
○ Last -in, First -out: Stack would work nicely here!
a
b a b
c a b cNode visited Stack (bottom to top)
d a b c d
g a b c d g
e a b c d g e
(backtrack) a b c d g
f a b c d g f
(backtrack) a b c d g
(backtrack) a b c da
h a b c d h
(backtrack) a b c d
(backtrack) a b c
(backtrack) a b
(backtrack) a
i a i
(backtrack) a
(backtrack) (empty)06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Depth First Search (DFS)
def dfs(self):
unvisited = self.v.copy()
stack = Stack()
while not unvisited.is_empty():
visit(unvisited[0])  # visit origin
stack.push(unvisited[0])
del unvisited[0]
while not stack.is_empty():
curr = stack.peek()
if there remains an unvisited city from curr:
next = select an unvisited city from curr
visit(next)
stack.push(next)
delete next from unvisited
else:
stack.pop()  # backtrackingDo something when we 
visit the node.
(e.g., print, compare, …)
For each connected node 
fromcurr node (accessed 
by internal adjacency 
matrix or list ), check if it is 
in the unvisited .We need this loop to take care of 
disconnected nodes !06 Graph & Search (BFS, DFS)
Time Complexity of DFS
● At each step,
○ We visit a node x.
○ For the node x, we search the list of adjacent nodes.
○ If there is an unvisited adjacent node, move to there.
○ If not, backtrack to the previously visited node.
● How many such steps?
● In total:O(1)
O(|V|)
O(1)
O(1)With adj. matrix
O(|V|)
O(|V|2)With adj. list
Total number of search
= number of edges (|E|)
O(|V| + |E|)06 Graph & Search (BFS, DFS)
Breadth First Search (BFS)
● Start from an arbitrary node.
● Visit allconnected unvisited node from there.
● In the next step, repeat the same thing on those nodes. Keep going!
This slide is best seen with animations.
jk
1
234
5
6
78
106 Graph & Search (BFS, DFS)
Breadth First Search (BFS)
● We keep track of the order to process: ①, ②, ③, …
● What data structure would work best?
○ We process the waiting nodes in the order of our visit.
○ Fast -in, First -out: Queue would work nicely here!
a
a b f i
b f i c eNode visited Queue (front to back)
f i c e g
i c e g
c e g d
e g d
g d
d h
h (empty)06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Breadth First Search (BFS)
def bfs(self):
unvisited = self.v.copy()
queue = Queue()
while not unvisited.is_empty():
queue.enqueue(some unvisited node)
while not queue.is_empty():
curr = queue.dequeue()
visit(curr)
delete curr from unvisited
for city in all unvisited cities connected from curr:
queue.enqueue(city)Do something when we visit the node.
(e.g., print, compare, …)
For each connected node 
from curr node (accessed 
by internal adjacency 
matrix or list ), check if it is 
in the unvisited .We need this loop to take care 
of disconnected nodes !06 Graph & Search (BFS, DFS)
DFS vs.BFS
● DFS and BFS visit the nodes in different order.
○ BFS visits nodes closer to the origin first. With an unweighted graph, the path discovered by BFS is a 
shortest path from the origin to that node.
● Following the arrows, we build a tree.
○ Recall that the tree is a special graph, connected without a cycle.
DFS
BFSorigin06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Time Complexity of BFS
● At each step,
○ Dequeue a node from the queue and visit it (call it x).
○ From the node x, enque all unvisited adjacent nodes.
● How many such steps?
● In total:O(1)
O(|V|)With adj. matrix
O(|V|)
O(|V|2)With adj. list
Total number of search
= number of edges (|E|)
O(|V| + |E|)06 Graph & Search (BFS, DFS)
34Minimum Spanning Trees04
Spanning Trees
● Given an undirected connected graph G, find a tree as a subgraph of Gthat contains all of G’s vertices.
○ Recall that a Tree is a connected graph with no cycles, and it must contain |V| -1edges.
● For unweighted graphs, we may use DFS or BFS:
origin
 origin
DFS 
TreeBFS Tree06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Minimum Spanning Trees
● What about the graph is weighted ?
○ Each edge is no longer equal; they have different cost !
○ There may be multiple spanning trees.
→ We are interested in building a valid spanning tree with minimal cost .
Cost = 29 Cost = 3545
103
3
3
23
3
5
445
103
3
3
23
3
5
406 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Minimum Spanning Trees
● Main idea : let’s try a greedy approach (choose the option that looks like best at the current moment, not 
worrying about the future.)
○ Start with a given node selected only.
○ At each step, choose a least -cost edge connecting the visited region and the unvisited region .
○ Keep doing this, until all nodes are within the visited region.
● Prim’s algorithm is a rare case that a greedy algorithm guarantees global optimality.
● Starting from different initial node may result in different tree, but the minimum cost is always the same.06 Graph & Search (BFS, DFS)
Minimum Spanning Trees: Illustration
Cost = 2745
103
3
3
23
3
5
406 Graph & Search (BFS, DFS)06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf
Minimum Spanning Trees: Prim’s Algorithm
def prims_mst (graph, start):
visited = [start]
unvisited = graph.nodes.copy().remove(start)
mst = []
while not unvisited.is_empty():
e = least -cost edge from visited to unvisited
u = the node consisting of e from the unvisited side
visited.append(u)
unvisited.remove(u)
mst.append(e)
Time complexity? O(|V| • (|V|+|E|))
Note that this can be further improved by using Priority queue. 
This is beyond the scope of this course.06 Graph & Search (BFS, DFS)
40Topological Sorting05
Topological Sorting
● On a directed graph without cycles, list the nodes in “topological order”:
○ An order of vertices in which vertex xprecedes vertex yif there is an edge from xto y.
○ Usually, there are multiple topological orders for a directed graph.
06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf[1] 
Examples
06 Graph & Search (BFS, DFS)
[1] 
[1]https://harshpopculture.wordpress.com/2013/09/02/civilization -v-not-all-sequels -are-as-bad -as-duke -nukem -forever/
Topological Sorting
● Main idea : We should put a node without successors at the end of the output!
○ Choose a node without successors, put it at the end of the current list.
○ Detach the chosen node and all edges to it.
○ Recursively solve with the remaining graph, until no node remains.
● As we delete all edges to already chosen nodes, the next highest ones will become available to choose.06 Graph & Search (BFS, DFS)
Topological Sorting: Illustration
06 Graph & Search (BFS, DFS)
[1] 
[1]https://user.ceng.metu.edu.tr/~tcan/cen g301_s1516/Schedule/week14.pdf[1] 
Topological Sorting: Implementation
def topological_sort (nodes, edges):
output = []
curr_last = Set of all nodes with no incoming edge
while curr_last is not empty:
target = curr_last[0]
output.append(target)
del curr_last[0]
for each node m with an incoming edge e from target:
Remove e from the graph
if m has no other incoming edges:
curr_last.append(m)
if len(output) < len(nodes):
return error  # graph has at least one cycle
else:
return output
Time complexity? O(|V|+ |E|)O(|E|)
Up to |E| times!
Each edge can be removed up to once.Up to |V| times!
Each node can be selected up to once.
At this point, we have no more 
nodes at the last. If there is no 
cycle, we should be done now.06 Graph & Search (BFS, DFS)
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['Lecture 7.txt'] = """Lecture 7:
Priority Queue & Heap
김수경
이화여자대학교 인공지능융합전공 소속© 2025 Upstage Co., Ltd.
1
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의 지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한관리자에게 귀속되어 있습니다 .
콘텐츠일부또는전부를복사 , 복제 , 판매 , 재판매공개 , 공유등을할수없습니다 . 
유출될경우지식재산권 침해에대한책임을부담할수있습니다 . 
유출에해당하여 금지되는 행위의예시는다음과같습니다 . 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education 의콘텐츠임을 알아볼 수있는 저작물을 작성 , 공개하는 행위
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트 /실습 수행 이외의 목적으로 사용하는 행위
Queue: Recap
● Queue: 
First In First Out (FIFO)
○ Adding a new element ( enqueue )
○ Retrieving the oldest item ( peek )
○ Deleting an item ( dequeue )3enqueue1522
dequeue
119
07 Priority Queue & Heap
Priority Queue
● Each element consists of {key (priority), value (element)}
● Enqueue: Any order
● Dequeue: Delete by priority
● Example: Airplane boarding group
07 Priority Queue & Heap
[1]https://www.usatoday.com/story/todayinthesky/2013/09/30/airlines -promise -a-return -to-civility -for-a-fee/2894645/[1] 
Priority Queue
● Ordered Queue (for faster deletion)
● Enqueue: O(n)
● Dequeue: O(1)
Key
Value07 Priority Queue & Heap
[1]https://simplerize.com/data -structures/priority -queue[1] 
Priority Queue
● Unordered Queue (for faster insertion)
● Enqueue: O(1)
● Dequeue: O(n)
● Can we implement enqueue and dequeue in O(log(n)) ?
Key
Value07 Priority Queue & Heap
[1]https://simplerize.com/data -structures/priority -queue[1] 
7Heap01
Binary Heap
Min Heap Max Heap
•Heap -Order: key(v)≥key(parent (v))
•Complete Binary Tree
07 Priority Queue & Heap
[1]https://junior -datalist.tistory.com/347[1] 
Max -heap: Insertion 
● Insertion of a key (priority) k to the heap
● The insertion algorithm consists of 2 steps
○ Store k at the new last node
○ Restore the heap -order property  (heapify_up)07 Priority Queue & Heap
Max -heap: Insertion 
07 Priority Queue & Heap
[1]\\https://www.codingeek.com/data -structure/binary -heap -introduction -explanation -and-implementation/[1] 
Max -Heap: Deletion 
● Removal of the root key ( highest priority = maximum number ) from the heap
● The removal algorithm consists of 2 steps
○ Replace the root key with the key  of the last node.
○ Restore the heap -order property  ( Heapify -down )07 Priority Queue & Heap
Max -Heap: Deletion 
07 Priority Queue & Heap
[1]https://afteracademy.com/blog/heap -building -and-heap -sort/[1] 
Max Heap: Heap sort
● Build a Max -Heap :
○ Convert the array into a max -heap, ensuring the largest element is at the root.
○ Complexity: O(n) .
● Extract Maximum :
○ Swap the root (largest element) with the last element.
○ Reduce heap size by 1 and restore the max -heap property (heapify -down).
○ Repeat until all elements are sorted.
○ Complexity: O(nlogn).07 Priority Queue & Heap
Max Heap: Heap sort
07 Priority Queue & Heap
[1]https://www.geeksforgeeks.org/c/c -program -for-heap -sort/[1] 
Max Heap: Heap sort
07 Priority Queue & Heap
[1]https://www.geeksforgeeks.org/c/c -program -for-heap -sort/[1] 
Max Heap: Heap sort
07 Priority Queue & Heap
[1]https://www.geeksforgeeks.org/c/c -program -for-heap -sort/[1] 
Max Heap: Heap sort
07 Priority Queue & Heap
[1]https://www.geeksforgeeks.org/c/c -program -for-heap -sort/[1] 
Max Heap: Heap sort
07 Priority Queue & Heap
[1]https://www.geeksforgeeks.org/c/c -program -for-heap -sort/[1] 
Max Heap: Heap sort
07 Priority Queue & Heap
[1]https://www.geeksforgeeks.org/c/c -program -for-heap -sort/[1] 
Heap and Priority Queue
• We can use a heap to implement a priority queue
• We store a (key, element) item at each internal node
• We keep track of the position of the last node
• For simplicity, we show only the keys in the picture
07 Priority Queue & Heap
[1]https://nikolay.kirov.be/2025/CITB308/slides/ch07/ch07_2.html[1] 
Insertion 
● Insertion of a key (priority) k to the heap
● The insertion algorithm consists of 2 steps
○ Store k at the new last node
○ Restore the heap -order property 
(heapify_up : next slide)
07 Priority Queue & Heap
[1]https://nikolay.kirov.be/2025/CITB308/slides/ch07/ch07_2.html[1] 
Heapify -up
• After the insertion of a new key k, the heap -order property may be violated
• Algorithm heapify -uprestores the heap -order property by swapping kalong an upward path from the insertion 
node
• Heapify -up terminates when the key kreaches the root or a node whose parent has a key smaller than or equal 
to k
• Since a heap has height O(log n), heapify -up runs in O(log n)time
07 Priority Queue & Heap
[1]https://nikolay.kirov.be/2025/CITB308/slides/ch07/ch07_2.html[1] 
Insertion example 
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
[1]https://www.slideshare.net/slideshow/lec -8ds-algoheapspdf/251538564[1] 
Insertion example 
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
[1]https://www.slideshare.net/slideshow/lec -8ds-algoheapspdf/251538564[1] 
Insertion example 
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
[1]https://www.slideshare.net/slideshow/lec -8ds-algoheapspdf/251538564[1] 
Insertion example 
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
[1]https://www.slideshare.net/slideshow/lec -8ds-algoheapspdf/251538564[1] 
Insertion example 
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
[1]https://www.slideshare.net/slideshow/lec -8ds-algoheapspdf/251538564[1] 
Insertion example 
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
[1]https://www.slideshare.net/slideshow/lec -8ds-algoheapspdf/251538564[1] 
Insertion example 
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
[1]https://www.slideshare.net/slideshow/lec -8ds-algoheapspdf/251538564[1] 
Deletion 
● Removal of the root key (highest priority) from the heap
● The removal algorithm consists of 2 steps
○ Replace the root key with the key 
of the last node.
○ Restore the heap -order property 
(Heapify -down: next)
07 Priority Queue & Heap
[1] 
[1]https://nikolay.kirov.be/2025/CITB308/slides/ch07/ch07_2.html
Heapify -down
• After replacing the root key with the key k of the last node, the heap -order property may be violated
• Algorithm heapify -down restores the heap property by swapping key k with the child with the smallest key 
along a downward path from the root
• Heapify -down terminates when key k reaches a leaf or a node whose children have keys greater than or equal 
to k 
• Since a heap has height O(log n), heapify -down  runs in O(log n) time
[1]https://nikolay.kirov.be/2025/CITB308/slides/ch07/ch07_2.html07 Priority Queue & Heap
[1] 
Deletion Example
● left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● parent :
[child index -1] // 2• Deletion in Max(or Min) Heap always
happens at the root to remove Maximum (or Minimum) value
• Deleting it (or removing it) from root cause a hole which needs to be 
filled. 07 Priority Queue & Heap
Deletion Example
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
3107 Priority Queue & Heap
Deletion Example
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
3107 Priority Queue & Heap
Deletion Example
● Left child :
[parent index] * 2 + 1
● Right child :
[parent index] * 2 + 2
● Parent :
[child index -1] // 2
07 Priority Queue & Heap
Implementation (array)
07 Priority Queue & Heap
[1]https://velog.io/@wlgns2223/leetcode -215-Kth-Largest -Element -in-an-Array[1] 
Implementation (array)
07 Priority Queue & Heap
Heap -sort (Min heap)
O(nlog n) Sorting! Insert Remove
MinPQ-Sort 
Total
Heap Sort O(logn) O(logn) O(n logn)07 Priority Queue & Heap
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['Lecture 8.txt'] = """Lecture 8:
Recursion & Searching
김수경
이화여자대학교 인공지능융합전공 소속© 2025 Upstage Co., Ltd.
1
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의 지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한관리자에게 귀속되어 있습니다 .
콘텐츠일부또는전부를복사 , 복제 , 판매 , 재판매공개 , 공유등을할수없습니다 . 
유출될경우지식재산권 침해에대한책임을부담할수있습니다 . 
유출에해당하여 금지되는 행위의예시는다음과같습니다 . 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education 의콘텐츠임을 알아볼 수있는 저작물을 작성 , 공개하는 행위
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트 /실습 수행 이외의 목적으로 사용하는 행위
3Searching01
Searching Problem
Given a list of objects and a single target, locate it if it exists.
Example:
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Where is 4? → [6].
Where is 17? → It does not exist.
How to solve it?
What is the most efficient way?08 Recursion & Searching
Linear Search
● Let’s try the simplest algorithm: checking one by one!
○ Check [0]. If it contains the target value, return 0. Otherwise, move to the next.
○ Check [1]. If it contains the target value, return 1. Otherwise, move to the next.
○ …
○ Check [ N-1]. If it contains the target value, return N-1. Otherwise, return -1.
def linear_search (list, value):
for i in range(len(list)):
if list[i] == value:
return i
return -1Time complexity? O(N)
Can we do better?08 Recursion & Searching
Searching Problem
Now, let’s consider an additional condition:
Given a sorted list of objects and a single target, locate it if it exists.
Example:
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 2 4 5 6 10 15 21
Where is 4? → [4].
Where is 17? → It does not exist.
Can we use the linear search method to solve this version? Yes!
Can we solve it more efficiently?
08 Recursion & Searching
Analogy to Dictionary Search
● Suppose you are searching for a word in English dictionary.
● If you use the “linear search” method, how many words do you expect to see before you find the word?
N/2, where Nis the number of words in the dictionary!
● Do you really do this? Any better way?08 Recursion & Searching
[1]https://www.britannica.com/summary/dictionary[1] 

Binary Search
● Linear search does work for a sorted list, but does NOT take advantage of the fact that it is sorted.
● Main idea : Check what value is stored in the middle. If it is smaller than the target, we can ignore all values 
before this. Otherwise, we can ignore all values after this.
● For instance, target = 15:
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 2 4 5 6 10 15 21
15 should appear on the right side of this!
→ We can safely ignore all values on the left.08 Recursion & Searching
Binary Search
● In the next step, we repeat the same procedure with the reduced list:
Index 5 6 7 8 9
Value 5 6 10 15 21Again, 15 should appear on the right side of this!
→ We can safely ignore all values on the left.
● Repeat with the reduced list:
Index 8 9
Value 15 21Okay, we found it!08 Recursion & Searching
Binary Search
● What if we are searching a non -existent value? For instance, 14?
Index 8 9
Value 15 2114 should be on the left of this.
→ We can safely ignore all values on the right.
● Removing them gives now an empty list. We confirm that there is no 14.
Index
Value08 Recursion & Searching
Binary Search
def binary_search (list, value):
first = 0
last = len(list) -1
while first <= last:
mid = (first + last) // 2
if list[mid] == value:
return mid
elif list[mid] < value:
first = mid + 1
else:
last = mid -1
return -1Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 2 4 5 6 10 15 21
first last midExample: value = 7?
iter=1
iter=2
iter=3
iter=4
iter=508 Recursion & Searching
Time Complexity
● Linear search
○ Applicable to any list
○ Time complexity: O( N)
● Binary search
○ Applicable to a sorted list
○ Time complexity: O(log N)
08 Recursion & Searching
Additional Problems
● Does the binary search work when the list contains duplicates?
○ To make it return any of those duplicates?
○ To make it return the leftmost one?
○ To make it return the rightmost one?
● Find the first element greater than or equal to the query.08 Recursion & Searching
14Recursion02
Recursive Algorithm
● An algorithm that calls itself for subproblems .
● The subproblems are of exactly the same type as the original problem, with smaller scale .
● “Complex problems can be seen much simpler.”
● Examples:
○ Division in elementary school
○ Binary search
○ Sorting (selection sort, merge sort, …)
○ Tree traversal
08 Recursion & Searching
[1]
https://www.google.com/url?sa=i&url=https%3A%2F%2Fschool.jbedu.kr%2F_cmm%2FfileDownload%2Fclass%2Fjhwasan%2F2020%2FG02020602% 2F273057%2Fca81112587983642fbb5586a42845cb0&psig=AOvVaw3LT6c5Y1nA850MDX2_clu0
&ust=1763800053288000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLCR87DpgpEDFQAAAAAdAAAAABAE[1] 
Key Components in Recursive Algorithm
● Base case : the simplest case where the algorithm can trivially conclude without additional recursive call.
○ E.g. , empty list in searching, single element in sorting, …
○ Usually, this case is simply solved by O(1).
● General case : the algorithm may call one or more recursive call, to solve exactly the same problem in smaller 
scale .
○ Recursive call must be strictly smaller ; otherwise it may not finish infinitely.
○ Important! Make sure if the same thing is not repeatedly called.
● Keep in mind: your algorithm must finish with correct answer for all possible inputs . Then, make it as 
efficient as possible.08 Recursion & Searching
Binary Search: Recursive Version
def binary_search (list, value, first,last):
if first > last:
return -1
else:
mid = (first + last) // 2
if list[mid] == value:
return mid
elif list[mid] < value:
return binary_search (list, value, mid+1, last)
else:
return binary_search (list, value, first, mid -1)
binary_search(list, value, 0, len(list) -1)searchsearch
“Same problem of different size”
Time complexity? O(log N)Up to O(log N) recursive calls.
Each call takes O(1): computing mid, 
comparison with value, return output.08 Recursion & Searching
Reversing a String
Non -recursive version: Recursive version:● Print a string in reverse order.
○ E.g. , ACTGCC → CCGTCA
def reverse(str):
output = \"\"
for i in range(len(str)):
output += str[ -i-1]
return outputdef reverse(str):
if not str:
return str
else:
return str[ -1] + reverse(str[:-1])return reverse(str[1:]) + str[0]08 Recursion & Searching
Combination
● Combination: a selection of ritems from a set that has ndistinct members, such that the order of selection does 
not matter.
● Recursive definition:
○ C(n, r) = 1 if r= 0 or n
○ C(n, r) = 0 if r> n
○ C(n, r) = C( n -1, r-1) + C( n-1, r)
def comb(n, r):
if r == 0 or r == n:
return 1
elif r > n:
return 0
else:
return comb(n-1, r-1) + comb(n-1, r)This implementation is not efficient. 
Why?08 Recursion & Searching
Combination
def comb(n, r):
if r == 0 or r == n:
return 1
elif r > n:
return 0
else:
return comb(n-1, r-1) + comb(n-1, r)08 Recursion & Searching
[1]https://storm.cis.fordham.edu/~yli/documents/CISC2200Fall15/Recursive_7.pdf[1] 
Recursion Summary
● It provides a simpler way to interpret the problem.
● It becomes extremely inefficient if there’s duplicated computation.
● Make sure that your algorithm always meets the base case to terminate.08 Recursion & Searching
Problem 1 –Binary Search
08 Recursion & Searching
Problem 2 -Recursion
08 Recursion & Searching
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['Lecture 9.txt'] = """Lecture 9:
Sorting Algorithms
김수경
이화여자대학교 인공지능융합전공 소속© 2025 Upstage Co., Ltd.
1
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의 지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한관리자에게 귀속되어 있습니다 .
콘텐츠일부또는전부를복사 , 복제 , 판매 , 재판매공개 , 공유등을할수없습니다 . 
유출될경우지식재산권 침해에대한책임을부담할수있습니다 . 
유출에해당하여 금지되는 행위의예시는다음과같습니다 . 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education 의콘텐츠임을 알아볼 수있는 저작물을 작성 , 공개하는 행위
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트 /실습 수행 이외의 목적으로 사용하는 행위
Insertion Sort in Life
The Great Dalmuti09 Sorting Algorithms
[1]http://www.partyhatpotato.com/reviews/2017/7/great -dalmuti -review.html[1] 
3
4Insertion Sort01
Sorting Problem
● Input: a list of Nnumbers
● Output: permutation B[1, …, n] of A such that B[1] ≤ B[2] ≤ … ≤ B[n]
○ In other words, a rearranged list of items in the input, such that they monotonically increase (or 
decrease).
● Example:
○ Input:
○ Expected output:Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 2 4 5 6 10 15 2109 Sorting Algorithms
5
Why Sorting?
● Problems become easier once items are in sorted order:
○ Finding a median
○ Finding the closest pairs
○ Binary search
○ Identifying statistical outliers
● Various applications
○ Sorting a table by an attribute
○ Data compression: sorting finds duplicates.
609 Sorting Algorithms
[1]https://smart.dhgate.com/mastering -excel -sorting -step -by-step -techniques -to-organize -your -spreadsheet -like-a-pro/[1] 
(Human -like) Insertion Sort
● Main idea:
○ Start from an empty “sorted list” and a pile of items to sort.
○ For each item on the pile, put in the right position in the “sorted list”.
○ When there’s no item left in the pile, you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Index
ValuePile
Sorted 
list
709 Sorting Algorithms
(Human -like) Insertion Sort
● Main idea:
○ Start from an empty “sorted list” and a pile of items to sort.
○ For each item on the pile, put in the right position in the “sorted list”.
○ When there’s no item left in the pile, you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Index 0
Value -7Pile
Sorted 
list
809 Sorting Algorithms
(Human -like) Insertion Sort
● Main idea:
○ Start from an empty “sorted list” and a pile of items to sort.
○ For each item on the pile, put in the right position in the “sorted list”.
○ When there’s no item left in the pile, you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Index 0 1
Value -7 15Pile
Sorted 
list
909 Sorting Algorithms
(Human -like) Insertion Sort
● Main idea:
○ Start from an empty “sorted list” and a pile of items to sort.
○ For each item on the pile, put in the right position in the “sorted list”.
○ When there’s no item left in the pile, you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Index 0 1 2
Value -7 2 15Pile
Sorted 
list
1009 Sorting Algorithms
(Human -like) Insertion Sort
● Main idea:
○ Start from an empty “sorted list” and a pile of items to sort.
○ For each item on the pile, put in the right position in the “sorted list”.
○ When there’s no item left in the pile, you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Index 0 1 2 3 4 5 6 7 8
Value -7 -4 -1 2 4 5 6 10 15Pile
Sorted 
list
1109 Sorting Algorithms
Insertion Sort
● Let’s do this in-place , without using an additional list.
○ Start from an empty “sorted listregion ” and a pile the region of items to sort.
○ For each item on the pile in the unsorted region , put in the right position in the “sorted listregion ”.
○ When there’s no item left in the pile unsorted region , you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Sorted Unsorted
1209 Sorting Algorithms
Insertion Sort
● Let’s do this in-place , without using an additional list.
○ Start from an empty “sorted listregion ” and a pile the region of items to sort.
○ For each item on the pile in the unsorted region , put in the right position in the “sorted listregion ”.
○ When there’s no item left in the pile unsorted region , you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Sorted Unsorted
1309 Sorting Algorithms
Insertion Sort
● Let’s do this in-place , without using an additional list.
○ Start from an empty “sorted listregion ” and a pile the region of items to sort.
○ For each item on the pile in the unsorted region , put in the right position in the “sorted listregion ”.
○ When there’s no item left in the pile unsorted region , you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Sorted Unsorted
1409 Sorting Algorithms
Insertion Sort
● Let’s do this in-place , without using an additional list.
○ Start from an empty “sorted listregion ” and a pile the region of items to sort.
○ For each item on the pile in the unsorted region , put in the right position in the “sorted listregion ”.
○ When there’s no item left in the pile unsorted region , you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 2 15 6 -1 5 4 10 -4 21
Sorted Unsorted
1509 Sorting Algorithms
Insertion Sort
● Let’s do this in-place , without using an additional list.
○ Start from an empty “sorted listregion ” and a pile the region of items to sort.
○ For each item on the pile in the unsorted region , put in the right position in the “sorted listregion ”.
○ When there’s no item left in the pile unsorted region , you are done.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 2 6 15 -1 5 4 10 -4 21
Sorted Unsorted
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 2 4 5 6 10 15 21
Sorted
1609 Sorting Algorithms
Insertion Sort: Implementation
def insertion_sort (list):
for i in range(1, len(list)):
key = list[i]
j = i -1
while j >=0 and key < list[j]:
list[j+1] = list[j]
j -= 1
list[j+1] = key
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -1 2 5 6 15 4 10 -4 21
Sortedi
keyj
1709 Sorting Algorithms
Time Complexity
● At the i-th iteration, its inner loop (while) does:
○ Find the location to put the next item among         i items,
○ Shift all items on the right side by 1,
○ Put the target item at the found position.
● How many iterations?
● Overall complexity?
● If the input list is almost sorted, each iteration will be done by ≈O(1), so overall time complexity will be ≈O( N).? O(N)
O(N)
O(1)Complexity?
O(log N)if binary 
search used.
O(N)
O(N2)
1809 Sorting Algorithms
19Selection Sort02
Selection Sort
● Main idea: the opposite of insertion sort!
○ Instead of putting the next item in the right place,
○ Find the smallest item in the unsorted region, and
○ Swap it with the item in its right position.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Sorted UnsortedFind the smallest among unsorted ones.
The smallest is already in the target place 
2009 Sorting Algorithms
Selection Sort
● Main idea: the opposite of insertion sort!
○ Instead of putting the next item in the right place,
○ Find the smallest item in the unsorted region, and
○ Swap it with the item in its right position.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 15 2 6 -1 5 4 10 -4 21
Sorted UnsortedFind the smallest among unsorted ones.
Swap it with the one at the target position.
2109 Sorting Algorithms
Selection Sort
● Main idea: the opposite of insertion sort!
○ Instead of putting the next item in the right place,
○ Find the smallest item in the unsorted region, and
○ Swap it with the item in its right position.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 2 6 -1 5 4 10 15 21
Sorted UnsortedFind the smallest among unsorted ones.
Swap it with the one at the target position.
2209 Sorting Algorithms
Selection Sort
● Main idea: the opposite of insertion sort!
○ Instead of putting the next item in the right place,
○ Find the smallest item in the unsorted region, and
○ Swap it with the item in its right position.
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 6 2 5 4 10 15 21
Sorted UnsortedFind the smallest among unsorted ones.
Swap it with the one at the target position.
Repeat until there is no item left in the unsorted region!
2309 Sorting Algorithms
Selection Sort: Implementation
def selection_sort (list):
for i in range(len(list)):
smallest = i
for j in range(i+1, len(list)):
if list[j] < list[smallest]:
smallest = j
list[i], list[smallest] = list[smallest], list[i]
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 6 10 5 4 2 15 21
Sortedi
smallestswap
Q. Can you implement this with recursion?
2409 Sorting Algorithms
Time Complexity
● At the i-th iteration, its inner loop (for) does:
○ Find the smallest items among         N-i unsorted items,
○ Swap it with the item at the next position.
● How many iterations?
● Overall complexity?
● No benefit even though the input list is almost sorted.
○ When we find the next smallest item, we do not assume the remaining list is sorted.?O(N)
O(1)Complexity?
O(N)
O(N2)
2509 Sorting Algorithms
26Merge Sort03
Motivation
● Insertion sort and selection sort work but too slow.
○ Time complexity is O( N2).
○ Does not matter when handling small data, but we want to handle big data !
● Any better idea?
○ Divide and conquer!
2709 Sorting Algorithms
Merge Sort
● Main idea:
○ Divide the whole list into two sub -lists.
○ Sort the left and right sublists separately .
○ Merge the two sorted sublists into a single sorted one.
Index 0 1 2 3 4 5 6 7
Value 5 -2 0 10 -6 7 4 9
Index 0 1 2 3
Value -2 0 5 10Index 0 1 2 3
Value -6 4 7 9
Index 0 1 2 3 4 5 6 7
Value -6 -2 0 4 5 7 9 10Sort Sort
Merge
2809 Sorting Algorithms
Merge Sort
● Further breakdown: each sublist is also sorted in a similar way!
5 -2 0 10 -6 7 4 9
5 -2 0 10 -6 7 4 9
5 -2 0 10-6 74 9
5 -2 0 10-6 74 9Okay, dividing is easy!
Sorting each separately is also easy, as they have just a single item in the end.
2909 Sorting Algorithms
Merge Sort
● Further breakdown: each sublist is also sorted in a similar way!
-6 -2 0 4 6 7 9 10
-2 0 5 10 -6 4 7 9
-2 5 0 10-6 74 9
5 -2 0 10-6 7 4 9
What about merging?!
3009 Sorting Algorithms
Merge Sort
● At each step, the only non -trivial task is merging two sorted arrays into a single sorted array.
-6 -2 0 4 6 7 9 10
-2 0 5 10 -6 4 7 9
● First trial with brute force:
○ Concatenate the two list
○ Sort the entire list with insertion (or selection) sort.
○ Time complexity?
■ 1st split: 2 ×(N/2)2, 2st split: 4 ×(N/4)2, 3rd split: 8 ×(N/8)2, …
■ In total, O( N2). No benefit from directly sorting entire matrix at once.
3109 Sorting Algorithms
Merge Sort
● So, we need more efficient merging, taking advantage of the fact that the two sublists are already sorted .
-2 0 5 10 -6 4 7 9● The first (smallest) item must be either the smallest item in the left sublist or the smallest one in the right 
sublist.
-6
3209 Sorting Algorithms
Merge Sort
● Then, what about the next one?
-6
-2 0 5 10 -6 4 7 9● The second smallest item must be either the smallest item in the left sublist or the second smallest one in the 
right sublist (since -6 was already used).
-2
3309 Sorting Algorithms
Merge Sort
● In a similar way, we choose the smaller one between the smallest remaining items in each list at a time, until 
both lists are completely consumed.
-6 -2
-2 0 5 10 -6 4 7 90 4 5 7 9 10
Now, both sublists are all used!
3409 Sorting Algorithms
Merge Sort: Time Complexity
● Time complexity of this merging step?
○ At each time we fill the output, we
■ Compare two elements once → O(1)
■ Write the small one → O(1)
■ Move one pointer on the selected side → O(1)
○ How many times do we repeat this?
■ Same as the output list size!
■ 1st split: 2 ×(N/2), 2nd split: 4 ×(N/4), … → O(N)
-6 -2
-2 0 5 10 -6 4 7 90 4 5 7 9 10
3509 Sorting Algorithms
Merge Sort: Time Complexity
● How many steps do we have?
○ Same as the height of this tree: O(log N)
-6 -2 0 4 6 7 9 10
-2 0 5 10 -6 4 7 9
-2 5 0 10 -6 7 4 9
5 -2 0 10 -6 7 4 9So, overall time complexity is: O(Nlog N)
3609 Sorting Algorithms
Merge Sort: Implementation
def merge_sort (list):
if len(list) > 1:
mid = len(list) // 2 # round down
left = list[:mid]
right = list[mid:]
merge_sort (left)
merge_sort (right)
# TODO(students): merge left & right in the list
“else ” for this is the base case , where the recursive calls are done.
We skip it here, since there’s no action item in the base case.
3709 Sorting Algorithms
Merge Sort vs. Insertion Sort
● How different the speed is, between O(N2)vs. O(Nlog N)?
N NTime (sec)
3809 Sorting Algorithms
Can we do better?
● Insertion / Selection sort takes O(N2).
● Merge sort takes O(Nlog N).
● Can we do better?
What is the best possible time complexity for sorting problem?
Then, can we sort in O( N)?O(N), because we need O( N) to read the input list anyway.
Yes, if we have some additional conditions.
(It was proved that O( Nlog N) is the best for comparison -based sorting algorithms.)
3909 Sorting Algorithms
40Linear Time Sorting: O (n)04
Counting Sort
● A linear -time sorting algorithm under the condition that the input elements are always integers between 0 and 
k.
● Example:
4109 Sorting Algorithms
[1]https://eprints.upj.ac.id/id/eprint/9958/13/BAB%20III.pdf[1] 
Counting Sort
● Intuitive example: N= 7, k= 7
5725157[0] [1] [2] [3] [4] [5] [6] [7]
7 5 1
5
572
1 2 5 5 5 7 7Stable sort : the original 
order is preserved for 
items with the same key.
4209 Sorting Algorithms
Counting Sort
● Algorithm
○ Reading the entire input list, increase the number of occurrences of each key.
○ Take cumulative sum of this counts.
→ This is the ending index of each number in the sorted output.7 5 1 5 2 7 5
[0] [1] [2] [3] [4] [5] [6] [7]
0 1 1 0 0 3 0 2
[0] [1] [2] [3] [4] [5] [6] [7]
0 1 2 2 2 5 5 7
0:0 0:1 1:2 2:2 2:2 2:5 5:5 5:7
4309 Sorting Algorithms
Counting Sort
● Algorithm
○ Read the input list once again from backward ,
○ Subtract the target index by 1,
○ Put the element there, and move on.7 5 1 5 2 7 5
[0] [1] [2] [3] [4] [5] [6] [7]
0 1 2 2 2 5 5 7
0:1 1:2 2:2 2:2 2:5 5:5 5:7
[0] [1] [2] [3] [4] [5] [6]4
5 71
23
5Why backward?
→ For stable sort!
4409 Sorting Algorithms
6
Counting Sort: Implementation
def counting_sort (list):
output = [0] * (len(list))
count = [0] * (max(list) + 1)
for i in range(len(list)):
count[list[i]] += 1
for i in range(1, len(count)):
count[i] += count[i -1]
for i in range(len(list)):
j = len(list) -1 -i
count[list[j]] -= 1
index = count[list[j]]
output[index] = list[j]
return outputCount occurrences of each key.
Cumulative sum
Locate each element at the right position in 
the output.Time complexity?
O(N)
O(k)
O(N)
Overall, O(N+ k).
If k≤ N, counting sort runs in linear time on the input 
size ( N).
4509 Sorting Algorithms
Sorting in Reality
● What sorting algorithm is used in Python library?
○ Timsort (2002) : a hybrid sorting algorithm (merge sort + insertion sort)
■ A variant of merge sort (divide and conquer)
■ When a sublist becomes smaller than some threshold, it is sorted using insertion sort.
■ Insertion sort is faster than merge sort for a small list.
● If your data is small enough, insertion/selection sort may work okay.
● Otherwise, merge sort or quick sort is recommended.
● You may consider a linear -time sorting if your key is integer within a reasonable range. However, it may be hard 
to take advantage unless the dataset is really huge, and you implement efficiently.
4609 Sorting Algorithms
Problem  1
def selection_sort (list):
for i in range(len(list)):
smallest = i
for j in range(i+1, len(list)):
if list[j] < list[smallest]:
smallest = j
list[i], list[smallest] = list[smallest], list[i]
Index 0 1 2 3 4 5 6 7 8 9
Value -7 -4 -1 6 10 5 4 2 15 21
Sortedi
smallestswapQ. Can you implement this with selection sort with  recursion?
4709 Sorting Algorithms
Problem  2
def merge_sort (list):
if len(list) > 1:
mid = len(list) // 2
left = list[:mid]
right = list[mid:]
merge_sort (left)
merge_sort (right)
# TODO(students): merge left & right in the list
“else ” for this is the base case , where the recursive calls are done.
We skip it here, since there’s no action item in the base case.Q. Please implement merge sort. (# TODO section below)
4809 Sorting Algorithms
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['lecture01.txt'] = """Lecture 1: 
Basic of Algorithm & 
Computational Complexity 
김수경 
이화여자대학교 인공지능융합전공 소속 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위 
3 강사 소개 
김수경 
現 이화여자대학교  인공지능융합전공  소속 조교수 
관심 연구 분야
-Explainable AI (XAI) 
-NLP and Medical AI 
-AI for Science 
-RL based Optimization 

4 Algorithms & Complexity 
01
5 What is Algorithm? 01 Basic of Algorithm & Computational Complexity 
● Computational procedure  to solve a problem 
[1] https://blog.naver.com/sumr2002/220359932991 
[2] http://jokesandfun.de/infographic/the-cake-is-a-factﬂowchart/ 
[1] [2] 
6 Eﬃciency of an Algorithm 01 Basic of Algorithm & Computational Complexity 
Do you like fast/eﬃcient computer program, or slow one? 
Of course, we always expect our computers to do their jobs most eﬃciently !
[1] https://www.vecteezy.com/photo/20621853-stressed-and-overworked-businessman 
[2] https://stock.adobe.com/search?k=smashed+computer&asset_id=52541504 
[3] https://www.istockphoto.com/kr/%EC%82%AC%EC%A7%84/%EC%97%AC%EC%9E%90-%EC%BB%B4%ED%93%A8%ED%84%B0-gm118986833-12293508 
[2] [1] [3] 
7 Computation Complexity 01 Basic of Algorithm & Computational Complexity 
● Cost of algorithm = Sum of operation costs 
● Model of computation speciﬁes 
○ What operations  an algorithm is allowed to use 
○ Cost (time, space) of each operation 
● Execution costs 
○ Time complexity of a program: how much time ?
○ Space complexity of a program: how much memory ?
8 Measuring Time Complexity 01 Basic of Algorithm & Computational Complexity 
● Measure execution time  in seconds using a client program ( e.g., time module) 
○ (+) Easy to measure 
○ (+) Gives actual time 
○ (-) Large amounts of time might be required. 
○ (-) Results depend on lots of factors (machine, compiler, data…) 
● Count the number of operations in terms of input size  N
○ (+) Machine independent. 
○ (+) Gives algorithm’s scalability. 
○ (-) Tedious to compute… 
○ (-) Does not give actual time. 
● Fortunately, we care only about asymptotic behavior (with a very large N ‒ Big Data!) 
9 Elementary School Algorithm 01 Basic of Algorithm & Computational Complexity 
Example: Integer multiplication 
● Input: two N-digit numbers x, y
● Output: product of x and y
● Primitive operations allowed: 
○ Add 2 single-digit numbers 
○ Multiply 2 single-digit numbers 
5678 
×1234 
23
13
72
22
17034 
11356 
5678 
7006652 
10 Elementary School Algorithm 01 Basic of Algorithm & Computational Complexity 
Example: Integer multiplication 
● Input: two N-digit numbers x, y
● Output: product of x and y
● Primitive operations allowed: 
○ Add 2 single-digit numbers 
○ Multiply 2 single-digit numbers 5678 
×1234 
23
13
72
22
17034 
11356 
5678 
7006652 N multiplications 
(up to) N-1 additions For each row: 
N rows 
Total operations ≤ 3 N2In total, 
N(2N-1 ) operations 
(up to) N2 additions How many primitive operations used? 
11 Software Engineer’s Example 01 Basic of Algorithm & Computational Complexity 
def linear_search (list, value): 
  for i in range(len(list)): 
    if list[i] == value: 
      return i 
  return -1 
def selection_sort (list): 
  for i in range(len(list)): 
    smallest = i 
    for j in range(i+1, len(list)): 
      if list[j] < list[smallest]: 
        smallest = j 
    list[i], list[smallest] = list[smallest], 
list[i] Let’s denote len(list)  as N:
Operation Count 
== Operation Count 
smallest = i 
< 
smallest = j 
swap 1 to N N
(N2 - N)/2 
0 to (N2 - N)/2 
N
12 Big O Notation 
02
How to Characterize Time Complexity more formally  and simply ?
13 Simpliﬁcation of Time Complexity 01 Basic of Algorithm & Computational Complexity 
1. We care only about the worst-case  performance! 
 ← because we do not know what input data we will get in advance. 
Operation Count 
smallest = i N
< (N2 - N)/2 
smallest = j 0 to (N2 - N)/2 
swap N
14 Simpliﬁcation of Time Complexity 01 Basic of Algorithm & Computational Complexity 
2. Focus only on a single operation with the  highest order  of growth (=most expensive). 
● There may be multiple good choices. Then, just choose any of them. 
Operation Count 
smallest = i N
< (N2 - N)/2 
smallest = j (N2 - N)/2 
swap N
15 Simpliﬁcation of Time Complexity 01 Basic of Algorithm & Computational Complexity 
3. Remove lower order terms. 
← They do not really matter, since the higher order one dominates. 
Operation Count 
smallest = i ignored 
< ignored 
smallest = j (N2 - N)/2 
swap ignored 
16 Simpliﬁcation of Time Complexity 01 Basic of Algorithm & Computational Complexity 
4. Remove constants. 
← We have already thrown away information at step 2. At this stage, constants are not meaningful. 
Operation Count 
smallest = i ignored 
< ignored 
smallest = j (N2)/2
swap ignored Worst-case order of growth : N2
17 Formal Deﬁnition 01 Basic of Algorithm & Computational Complexity 
● If a function T (N) has its order of growth  less than or equal to f (N), we write this as T (N) ∈ O( f (N)), where O is 
called Big-O notation. 
● More mathematically, T (N) ∈ O( f (N)) means that there exists a positive constant c such that T (N)  ≤ c f (N) for all 
values of N greater than some positive N0 (i.e., large N).

18 Example 01 Basic of Algorithm & Computational Complexity 
● T (N) = N 2 + 5N 5
● T (N) ∈ O(N 5)?
○ That is, is there a positive constant c such that N 2 + 5N 5  ≤ cN 5 for large N?
○ Yes! 
■ N 2 + 5N 5 < N 5 + 5N 5 = 6N 5
■ With c = 6, it holds. 
● T (N) ∈ O( N 7)?
○ That is, is there a positive constant c such that N 2 + 5N 5  ≤ cN 7 for large N?
○ Yes! 
■ N 2 + 5N 5 < N 5 + 5N 5 = 6N 5 < 6N 7 
■ With c = 6, it holds. 

19 Example(cont’d) 01 Basic of Algorithm & Computational Complexity 
● T (N) = N 2 + 5N 5
● T (N) ∈ O(N 4)?
○ That is, is there a positive constant c such that N 2 + 5N 5  ≤ cN 4 for large N?
○ No 😕
■ Even if we set very large c, still for N > c, 5N 5 > N 5 > cN 4.
● We are usually interested in the tightest  order; in this example, O( N 5).

20 Exercise(cont’d) 01 Basic of Algorithm & Computational Complexity 
● T(N) = 2 N2 + 3N
● T(N) = 1/ N + 100 
● T(N) = 100cos( N) + 50 N2
● T(N) = log N + 2N
● T(N) = 2N + N2
O(N2)
O(1) 
O(N2)
O(N)
O(2N)
21 What is Important for Asymptotic Analysis? 01 Basic of Algorithm & Computational Complexity 
● Compare the two algorithms below: 
○ Algo1 requires 2N 2 operations, while 
○ Algo2 requires 500 N operations. 
○ Algo1 is faster than Algo2 for a small N, but becomes much slower for a very large N.
○ What is important? How fast function is growing !
● Order of growth: 
500 N
2N 2
22 Asymptotic Analysis 01 Basic of Algorithm & Computational Complexity 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['Untitled-checkpoint.ipynb.txt'] = """"""
    s.raw_texts['강의마무리_코랩 세션_Wrap Up 리포트.txt'] = """ 
 
 
[
자료구조와
 
알고리즘
]
 
코랩세션
 
Wrap
 
Up
 
리포트
 
작성팀:
 
6조
 
이영기
 
Wrap
 
Up
 
리포트
 
작성
 
내용
 
1)
 
논의
 
주제
 
a)
 
보라색으로
 
작성된
 
주제는
 
예시
 
주제로,
 
팀
 
내
 
논의하고
 
싶은
 
주제가
 
있다면
 
해당
 
주제로
 
논의해주세요!
 
2)
 
팀원별
 
핵심
 
아이디어
 
3)
 
논의
 
과정
 
4)
 
최종
 
논의
 
결과
 
및
 
회고
 
 
공통
 
예시
 
주제
 
(Day
 
01
 
-
 
Day
 
05)
 
Step
 
01.
 
Pseudo
 
code:
 
내
 
풀이를
 
10~20줄
 
내외로
 
요약(입력
 
출력,
 
핵심
 
로직,
 
예외
 
포함)
 
Step
 
02.
 
시간
 
공간
 
복잡도:
 
최선
 
평균
 
최악
 
중
 
무엇을
 
기준으로
 
말하는지
 
명시
 
Step
 
03.
 
효율성
 
주장:
 
“왜
 
이
 
방식이
 
합리적인가?”를
 
대안
 
1~2개와
 
비교로
 
설명
 
(반례
 
엣지케이스
 
포함)
 
 
 
Day
 
01
 
코랩
 
세션
 
 
1.
 
논의
 
주제
 
●
 
핵심
 
과제
:
 
정수
 
배열
 
nums
에서
 
합이
 
target
이
 
되는
 
두
 
숫자의
 
인덱스를
 
찾는
 
Two
 
Sum
 
문제
 
해결
 
●
 
주요
 
쟁점
:
  
배열
 
인덱스
 
기반
 
접근
 
방식
 
및
 
메모리
 
구조의
 
이해
 
○
 
브루트
 
포스
(
Brute
 
Force)
 
방식과
 
해시맵
(
Hash
 
Map)
 
방식의
 
메커니즘
 
차이
 
비교
 
○
 
데이터
 
크기
 
증가에
 
따른
 
시간복잡도
 
O(N^2)
 
vs
 
O(N)
의
 
실제적
 
영향력
 
파악
 
 
2.
 
팀원별
 
핵심
 
아이디어
 
●
 
브루트
 
포스
 
전략
 
(
아이디어
 
제안
):
 
○
 
모든
 
인덱스
 
쌍
 
(i,
 
j)
를
 
이중
 
반복문으로
 
직접
 
비교하여
 
합이
 
target
인
 
경우를
 
찾음
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
○
 
\"
자물쇠
 
번호를
 
풀기
 
위해
 
0000
부터
 
9999
까지
 
전부
 
대입하는
 
것
\"
과
 
같은
 
직관적인
 
방식
 
제안
 
●
 
해시맵
 
전략
 
(
아이디어
 
제안
):
 
○
 
리스트를
 
단
 
한
 
번
 
순회하며
,
 
target
 
-
 
현재값이
 
메모장
(
Dictionary)
에
 
있는지
 
확인
 
○
 
\"
입구에서
 
방명록을
 
확인하고
 
바로
 
목적지로
 
가는
 
것
\"
과
 
같은
 
효율적인
 
탐색
 
방식
 
제안
 
 
3.
 
논의
 
과정
 
●
 
Step
 
1.
 
브루트
 
포스
 
구현
 
및
 
한계점
 
인식
:
 
○
 
이중
 
for
문을
 
통해
 
인덱스
 
i
와
 
j
를
 
순회하며
 
정답을
 
찾는
 
코드를
 
작성함
 
○
 
전체
 
비교
 
방식은
 
입력값
 
N
 
에
 
대해
 
N
  
times
 
N
 
번의
 
연산이
 
필요하여
 
데이터가
 
10
배
 
늘면
 
연산은
 
100
배
 
늘어난다는
 
점을
 
분석함
 
●
 
Step
 
2.
 
해시맵을
 
통한
 
성능
 
개선
 
시도
:
 
○
 
enumerate
를
 
사용하여
 
인덱스와
 
값을
 
동시에
 
관리하고
,
 
한
 
번
 
본
 
숫자를
 
seen
 
딕셔너리에
 
저장하는
 
로직을
 
구축함
 
○
 
\"
타겟이
 
명확할
 
때
 
사용할
 
수
 
있는
 
최적의
 
솔루션
\"
이라는
 
인사이트를
 
도출함
 
●
 
Step
 
3.
 
알고리즘
 
효율성
 
비교
 
실험
:
 
○
 
데이터
 
개수가
 
100
만
 
개일
 
때
,
 
브루트
 
포스는
 
약
 
2.7
시간이
 
걸리지만
 
해시맵은
 
0.01
초
 
만에
 
끝난다는
 
수치적
 
차이를
 
시뮬레이션함
 
 
4.
 
최종
 
논의
 
결과
 
및
 
회고
 
●
 
최종
 
결과
:
 
○
 
시간복잡도
:
 
O(N^2)
 
에서
 
O(N)
 
으로
 
획기적으로
 
개선됨을
 
확인
 
○
 
트레이드
 
오프
(
Trade-off):
 
해시맵
 
방식은
 
시간
 
효율성이
 
뛰어나지만
,
 
추가적인
 
저장
 
공간
(
메모리
)
이
 
필요하다는
 
점을
 
명확히
 
함
 
●
 
회고
 
및
 
향후
 
과제
:
 
○
 
구현
 
난이도
:
 
브루트
 
포스가
 
구현은
 
쉽지만
,
 
대규모
 
데이터
 
처리
 
시
 
발생하는
   
비용
(
시간
)
  
이
 
곧
 
프로젝트의
 
성패와
 
직결됨을
 
깨달음
 
○
 
학습
 
성과
:
 
\"
이미
 
본
 
데이터를
 
기억하느냐
,
 
매번
 
새로
 
찾아
 
헤매느냐
\"
의
 
차이가
 
알고리즘
 
설계의
 
핵심임을
 
이해함
 
○
 
향후
 
다짐
:
 
단순히
 
루프를
 
돌리는
 
방식에서
 
벗어나
,
 
추가
 
메모리를
 
활용해
 
시간을
 
버는
 
해시맵과
 
같은
 
효율적인
 
사고를
 
체득하기로
 
함
 
 
 
Day
 
02
 
코랩
 
세션
 
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
1.
 
논의
 
주제
 
●
 
핵심
 
과제
:
 
스택
(
Stack)
 
자료구조를
 
활용하여
 
주어진
 
문자열
 
s
가
 
올바른
 
괄호
 
구성인지
 
판별하는
 
알고리즘
 
구현
 
●
 
주요
 
학습
 
포인트
:
 
○
 
스택의
 
LIFO(Last-In,
 
First-Out)
 
구조
 
및
 
push
 
pop
 
연산
 
원리
 
이해
 
○
 
문자열
 
내
 
괄호
 
패턴을
 
스택으로
 
검증하는
 
로직
 
설계
 
○
 
시간복잡도
 
O(N)
 
및
 
공간복잡도
 
O(N)
 
알고리즘의
 
분석과
 
효율성
 
검토
 
 
2.
 
팀원별
 
핵심
 
아이디어
 
●
 
스택
 
기반
 
매칭
 
아이디어
 
(
학생
 
제안
):
 
○
 
문자열을
 
왼쪽에서
 
오른쪽으로
 
순회하며
 
열린
 
괄호
((,
 
{,
 
[)
는
 
스택에
 
쌓고
(
push),
 
닫힌
 
괄호가
 
나오면
 
스택의
 
가장
 
위
(
top)
 
원소를
 
꺼내
(
pop)
 
짝이
 
맞는지
 
대조함
 
○
 
스택이
 
비어있는
 
상태에서
 
닫힌
 
괄호가
 
나오거나
,
 
꺼낸
 
원소와
 
짝이
 
맞지
 
않으면
 
즉시
 
False
를
 
반환함
 
●
 
데이터
 
구조
 
최적화
:
 
○
 
괄호의
 
짝을
 
매칭할
 
때
 
if-else
 
문
 
대신
   
딕셔너리
(
dict)
  
를
 
사용하여
 
코드
 
가독성과
 
확장성을
 
높임
 
●
 
예외
 
케이스
 
및
 
확장성
 
고려
:
 
○
 
단순히
 
괄호만
 
있는
 
문자열이
 
아니라
,
 
(3+4)
 
(2+5)
와
 
같이
 
숫자와
 
연산자가
 
포함된
 
수식에서도
 
괄호의
 
유효성을
 
검증할
 
수
 
있도록
 
설계
 
 
3.
 
논의
 
과정
 
●
 
Step
 
1.
 
문제
 
분석
 
및
 
엣지
 
케이스
 
도출
:
 
○
 
입력이
 
비어있거나
(\"\"),
 
열린
 
괄호만
 
있거나
(((((),
 
순서가
 
뒤섞인
 
경우
(([)])
 
등
 
다양한
 
실패
 
사례를
 
정의함
 
●
 
Step
 
2.
 
의사코드
(
Pseudocode)
 
설계
:
 
○
 
구현
 
전
 
\"
순회
 
→
 
열린
 
괄호
 
push
 
→
 
닫힌
 
괄호
 
pop
 
&
 
비교
 
→
 
최종
 
스택
 
확인
\"
으로
 
이어지는
 
단계별
 
로직을
 
자연어로
 
먼저
 
정립함
 
●
 
Step
 
3.
 
코드
 
구현
 
및
 
디버깅
:
 
○
 
처음
 
구현
 
시
 
발생할
 
수
 
있는
 
'
빈
 
스택에서의
 
pop
 
오류
'
를
 
방지하기
 
위해
 
if
 
not
 
stack:
 
return
 
False
와
 
같은
 
예외
 
처리를
 
선행하도록
 
로직을
 
보완함
 
○
 
숫자나
 
연산자
(+,
  
)
 
등
 
괄호
 
이외의
 
문자는
 
무시하고
 
넘어가는
 
else:
 
continue
 
로직을
 
추가하여
 
수식
 
지원
 
기능을
 
강화함
 
 
4.
 
최종
 
논의
 
결과
 
및
 
회고
 
●
 
최종
 
논의
 
결과
:
 
○
 
시간복잡도
:
 
문자열을
 
한
 
번만
 
순회하므로
 
O(N)
 
달성
 
○
 
공간복잡도
:
 
최악의
 
경우
 
모든
 
문자가
 
열린
 
괄호일
 
때
 
N
 
만큼
 
쌓이므로
 
O(N)
 
소요
 
○
 
도구의
 
적합성
:
 
괄호는
 
나중에
 
열린
 
것이
 
먼저
 
닫혀야
 
하므로
,
 
순서를
 
기억하지
 
못하는
 
해시테이블이나
 
선입선출인
 
큐보다
 
스택이
 
가장
 
적합한
 
도구임을
 
확인함
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
●
 
회고
:
 
○
 
단순한
 
문제
 
같지만
 
pop
 
연산
 
전
 
스택
 
상태를
 
확인하는
 
디테일이
 
프로그램의
 
안정성을
 
결정함을
 
체득함
 
○
 
이전
 
문제
(
Two
 
Sum)
에서
 
배운
 
해시맵과
 
이번
 
스택의
 
차이점을
 
비교하며
,
 
문제의
 
특성
(
순서가
 
중요한지
,
 
값이
 
중요한지
)
에
 
따라
 
올바른
 
자료구조를
 
선택하는
 
안목을
 
기르는
 
계기가
 
됨
 
 
왜
 
해시맵만으로는
 
어려울까요
?
 
(
논의
 
과정
)
 
제출하신
 
Day
 
2
 
미션
 
파일의
 
회고
 
내용과
 
일맥상통하는
 
부분입니다
.
 
●
 
순서
 
기억의
 
부재
:
 
해시맵은
 
\"
값이
 
어디에
 
있는가
\"
는
 
잘
 
찾지만
,
 
\"
어떤
 
순서로
 
들어왔는가
\"
를
 
자체적으로
 
관리하지
 
않습니다
.
 
●
 
복잡도
 
증가
:
 
위
 
코드처럼
 
인덱스를
 
일일이
 
관리하면
,
 
짝을
 
찾을
 
때마다
 
리스트를
 
뒤져야
 
하므로
 
시간복잡도가
 
O(N)
 
보다
 
나빠질
 
가능성이
 
큽니다
.
 
●
 
스택의
 
본질
:
 
결국
 
\"
가장
 
최근에
 
열린
 
괄호
\"
를
 
찾는
 
과정에서
 
indices[target_open].pop()
과
 
같은
 
연산을
 
쓰게
 
되는데
,
 
이는
 
해시맵을
 
스택의
 
저장소로만
 
쓰는
 
셈이
 
됩니다
.
 
 
최종
 
결론
 
및
 
회고
 
정리
 
●
 
팀원별
 
핵심
 
아이디어
:
 
해시맵은
 
괄호의
 
짝
 
정보를
 
저장하는
 
용도로는
 
매우
 
훌륭하지만
(
코드
 
가독성
 
향상
),
 
전체
 
로직을
 
담당하기엔
 
순서
 
제어
 
능력이
 
부족하다는
 
점을
 
확인했습니다
.
 
●
 
논의
 
과정
:
 
\"
이미
 
본
 
데이터를
 
기억하느냐
\"
라는
 
측면에서
 
해시맵과
 
스택은
 
닮았지만
,
 
괄호
 
문제는
   
'
가장
 
최근의
 
기억
'
  
이
 
중요하므로
 
LIFO(
후입선출
)
 
방식인
 
스택이
 
가장
 
경제적이라는
 
결론에
 
도달했습니다
.
 
●
 
최종
 
결과
:
 
괄호
 
검증
 
알고리즘에서
 
해시맵은
   
'
매핑
 
테이블
'
  
로서
 
스택을
 
보조할
 
때
 
가장
 
빛이
 
납니다
.
 
 
 
Day
 
03
 
코랩
 
세션
 
추가
 
예시
 
주제
 
:
 
DFS
와
 
BFS
의
 
차이를
 
정리하고,
 
이
 
미션
 
조건에서
 
어떤
 
탐색이
 
더
 
효율적인지
 
근거(복잡도
 
메모리
 
목표:
 
최단거리
 
등)로
 
선택해봅시다.
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
Step
 
01.
 
Pseudo
 
code
 
(BFS
 
)
 
●
 
입력
:
 
M
 
x
 
N
 
크기의
 
2
차원
 
문자열
 
배열
 
grid
 
('1':
 
육지
,
 
'0':
 
바다
)
 
●
 
출력
:
 
섬의
 
총
 
개수
 
count
 
(
정수
)
 
Python
 
#
 
1.
 
초기화
:
 
섬
 
개수
(
count)
 
=
 
0,
 
격자
 
크기
(
rows,
 
cols)
 
확인
 
#
 
2.
 
격자
 
순회
:
 
모든
 
칸
 
(r,
 
c)
를
 
하나씩
 
검사
 
#
 
3.
 
육지
 
발견
:
 
if
 
grid[r][c]
 
==
 
'1'
 
(
방문하지
 
않은
 
육지라면
)
 
  
#
 
3-1.
 
count
를
 
1
 
증가
 
  
#
 
3-2.
 
큐
(
Queue)
 
생성
 
및
 
시작
 
좌표
 
(r,
 
c)
 
삽입
 
  
#
 
3-3.
 
grid[r][c]
 
=
 
'0'
 
(
방문
 
표시
:
 
다시
 
안
 
오도록
 
바다로
 
변경
)
 
  
#
 
3-4.
 
BFS
 
탐색
 
시작
:
 
while
 
큐가
 
비어있지
 
않은
 
동안
 
    
#
 
a.
 
큐에서
 
현재
 
좌표
 
(curr_r,
 
curr_c)
 
추출
 
    
#
 
b.
 
상
,
 
하
,
 
좌
,
 
우
 
4
방향에
 
대해
 
다음
 
좌표
 
(nr,
 
nc)
 
계산
 
    
#
 
c.
 
유효성
 
검사
:
 
(nr,
 
nc)
가
 
격자
 
내에
 
있고
 
grid[nr][nc]
 
==
 
'1'
이면
 
      
#
 
-
 
큐에
 
(nr,
 
nc)
 
삽입
 
      
#
 
-
 
grid[nr][nc]
 
=
 
'0'
 
(
방문
 
표시
)
 
#
 
4.
 
결과
 
반환
:
 
최종
 
count
 
값
 
 
Step
 
02.
 
시간
 
공간
 
복잡도
 
(
최악의
 
경우
 
기준
)
 
●
 
시간
 
복잡도
:
 
O(m*n)
 
○
 
이유
:
 
모든
 
칸을
 
최대
 
한
 
번씩
 
방문합니다
.
 
육지인
 
칸은
 
큐에
 
들어갔다
 
나오며
 
4
방향을
 
검사하고
,
 
바다인
 
칸은
 
if
문
 
조건에서
 
바로
 
걸러지므로
 
전체
 
칸
 
수에
 
비례하는
 
연산만
 
수행합니다
.
 
●
 
공간
 
복잡도
:
 
O(m,n)
 
○
 
이유
:
 
큐에
 
저장되는
 
최대
 
좌표의
 
수는
 
격자의
 
너비나
 
높이
 
중
 
작은
 
값에
 
비례하여
 
쌓입니다
 
Step
 
03.
 
효율성
 
주장
 
이
 
방식이
 
합리적인
 
이유는
 
다른
 
대안들과
 
비교했을
 
때
 
안정성과
 
명확성이
 
높기
 
때문입니다
.
 
비
교
군
 
특징
 
및
 
한계점
 
효율성
 
판단
 
대
안
 
1:
 
재
귀
 
D
F
S
 
코드는
 
짧으나
 
섬이
 
매우
 
클
 
경우
(
예
:
 
수만
 
칸
)
 
Recursion
 
Error
 
발생
 
위험이
 
큼
.
 
BFS
 
승
:
 
대규모
 
데이터
 
처리
 
시
 
안정적임
.
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
대
안
 
2:
 
단
순
 
루
프
 
큐
 
스택
 
없이
 
매번
 
전체
 
격자를
 
다시
 
훑으며
 
연결성을
 
체크하면
 
중복
 
연산이
 
기하급수적으로
 
늘어남
.
 
BFS
 
승
:
 
한
 
번
 
방문한
 
노드를
 
즉시
 
지워
 
중복을
 
원천
 
차단함
.
 
●
 
 
반례
 
엣지케이스
 
대응
:
 
○
 
격자가
 
비어있는
 
경우
:
 
if
 
not
 
grid
 
조건으로
 
즉시
 
0
 
반환
.
 
○
 
전체가
 
육지인
 
경우
:
O(m*n)
 
내에
 
모든
 
칸을
 
0
으로
 
만들며
 
정상
 
종료
.
 
○
 
대각선
 
육지
:
 
4
방향
 
탐색
 
로직
(
nr,
 
nc
 
계산
)
을
 
통해
 
대각선은
 
별개의
 
섬으로
 
정확히
 
분리
 
처리
.
 
 
 
Day
 
04
 
코랩
 
세션
 
상황별
 
최적의
 
도구
 
선택
 
(Quick
 
Select,
 
Heap,
 
Binary
 
Search)
 
1.
 
퀵셀렉트
 
(Quick
 
Select)
 
●
 
핵심
 
원리
:
 
퀵
 
정렬의
 
원리를
 
이용하되
,
 
피벗
(
Pivot)
을
 
기준으로
 
찾고자
 
하는
 
값이
 
포함된
 
구역만
 
재귀적으로
 
파고듭니다
.
 
나머지
 
절반은
 
버립니다
.
 
●
 
목표
:
 
정렬되지
 
않은
 
배열에서
 
K
번째로
 
크거나
 
작은
 
값
 
찾기
.
 
●
 
시간
 
복잡도
:
 
평균
 
O(N)
 
,
 
최악
 
O(N^2)
 
.
 
●
 
논의
 
포인트
:
 
\"
전체를
 
정렬
(
 
O(N
 
log
 
N)
 
)
하지
 
않고도
 
특정
 
순위의
 
값을
 
찾을
 
수
 
있는
 
이유는
 
무엇인가
?\"
 
(
절반씩
 
버리는
 
분할
 
정복의
 
힘
)
 
 
2.
 
힙
 
(Heap
  
Priority
 
Queue)
 
●
 
핵심
 
원리
:
 
완전
 
이진
 
트리
 
구조를
 
유지하며
,
 
부모
 
노드가
 
자식
 
노드보다
 
항상
 
크거나
 
작은
 
상태를
 
유지합니다
.
 
●
 
목표
:
 
최댓값
 
또는
 
최솟값을
 
빠르게
 
추출하거나
,
 
실시간으로
 
우선순위를
 
관리하기
.
 
●
 
시간
 
복잡도
:
 
삽입
 
삭제
 
O(log
 
N)
 
,
 
K
 
번째
 
값
 
찾기
 
O(N
  
log
 
K)
 
.
 
●
 
논의
 
포인트
:
 
\"
데이터가
 
실시간으로
 
계속
 
추가되는
 
상황
(
Stream)
이라면
,
 
퀵셀렉트보다
 
힙이
 
유리한
 
이유는
 
무엇인가
?\"
 
(
유지보수
 
비용의
 
차이
)
 
 
3.
 
이진
 
탐색
 
(Binary
 
Search)
 
●
 
핵심
 
원리
:
 
이미
 
정렬된
 
데이터에서
 
중앙값을
 
기준으로
 
탐색
 
범위를
 
매
 
단계마다
 
절반씩
 
줄여나갑니다
.
 
●
 
목표
:
 
특정
 
값
(
Target)
의
 
**
위치
(
인덱스
)**
를
 
찾거나
 
존재
 
여부
 
확인하기
.
 
●
 
시간
 
복잡도
:
 
O(
 
log
 
N)
 
.
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
●
 
논의
 
포인트
:
 
\"
배열이
 
회전되어
 
있거나
(
Rotated)
 
일부만
 
정렬된
 
특이한
 
상황에서도
 
이진
 
탐색의
 
논리
(
절반
 
버리기
)
를
 
적용할
 
수
 
있는가
?\"
 
 
4.
 
[
비교
 
요약
]
 
알고리즘
 
선택
 
가이드
 
상황
 
추천
 
알고리즘
 
이유
 
정렬된
 
상태에서
 
특정
 
값
 
찾기
 
이진
 
탐색
 
가장
 
빠름
 
(
 
O(
 
log
 
N)
 
)
 
정렬
 
안
 
된
 
데이터에서
 
딱
 
하나
(
K
번째
)
 
찾기
 
퀵셀렉트
 
평균
 
성능이
 
가장
 
우수
 
(
 
O(N)
 
)
 
데이터가
 
계속
 
추가되면서
 
최댓값
 
유지
 
힙
 
(Heap)
 
동적
 
데이터
 
처리에
 
최적화
 
모든
 
데이터의
 
완벽한
 
순서가
 
필요할
 
때
 
병합
 
퀵
 
정렬
 
정렬
 
이후
 
이진
 
탐색
 
등
 
활용
 
가능
 
 
 
Day
 
05
 
코랩
 
세션
 
추가
 
예시
 
주제
 
-
 
(데일리미션)
 
각
 
정렬
 
알고리즘은
 
어떤
 
데이터
 
제약(거의
 
정렬됨,
 
안정성,
 
메모리,
 
최악
 
보장
 
등)에서
 
가장
 
적합한지
 
사례로
 
토론해보세요.
 
-
 
(심화미션)
 
최소힙
 
없이
 
같은
 
기능을
 
구현할
 
대안을
 
제시하고,
 
연산별
 
시간복잡도
 
관점에서
 
효율성이
 
어떻게
 
변하는지
 
비교해보세요.
 
주제
:
 
비교하지
 
않는
 
정렬
,
 
카운팅
 
정렬
 
(Counting
 
Sort)
 
1.
 
카운팅
 
정렬의
 
정의
 
●
 
비교
 
기반
 
정렬
O(N
 
log
 
N)
의
 
한계를
 
깨는
 
알고리즘
:
 
두
 
수를
 
비교해서
 
자리를
 
바꾸는
 
방식이
 
아니라
,
 
각
 
숫자의
 
출현
 
빈도를
 
세어서
 
위치를
 
바로
 
지정하는
 
방식입니다
.
 
●
 
시간
 
복잡도
:
 
O(N
 
+
 
K)
 
(
여기서
N
은
 
데이터
 
개수
,
 
K
는
 
데이터의
 
최대값
).
 
 
2.
 
핵심
 
3
단계
 
(
동작
 
원리
)
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
1.
 
Counting
 
(
세기
):
 
각
 
숫자가
 
몇
 
번
 
나왔는지
 
count
 
배열에
 
기록합니다
.
 
2.
 
Cumulative
 
Sum
 
(
누적합
):
 
각
 
숫자가
 
결과
 
배열에서
 
어디서
 
끝날지
 
**'
예약
 
번호
'**
를
 
매깁니다
.
 
3.
 
Placement
 
(
배치
):
 
원본
 
배열을
 
뒤에서부터
 
읽으며
,
 
예약
 
번호를
 
하나씩
 
깎으면서
(-=
 
1)
 
결과
 
배열에
 
배치합니다
.
 
Q1.
 
왜
 
뒤에서부터(역순으로)
 
채워넣나요?
 
●
 
답변:
 
데이터에
 
같은
 
숫자가
 
있을
 
때,
 
원래
 
순서를
 
유지하기
 
위해서입니다
 
(안정
 
정렬).
 
앞에서부터
 
채우면
 
원래
 
앞에
 
있던
 
숫자가
 
뒤로
 
갈
 
수
 
있습니다.
 
Q2.
 
max(list)
가
 
너무
 
크면
 
어떤
 
문제가
 
생기나요?
 
●
 
답변:
 
만약
 
숫자는
 
2개인데
 
최대값이
 
10억이라면,
 
count
 
배열의
 
크기가
 
10억이
 
되어
 
메모리
 
낭비가
 
심각해집니다.
 
이럴
 
때는
 
카운팅
 
정렬
 
대신
 
다른
 
정렬을
 
써야
 
합니다.
 
Q3.
 
카운팅
 
정렬을
 
쓸
 
수
 
없는
 
데이터
 
타입은?
 
●
 
답변:
 
소수(실수)
 
데이터.
 
배열의
 
인덱스는
 
정수여야
 
하므로
 
0.5
,
 
1.2
 
같은
 
값은
 
카운팅
 
정렬을
 
바로
 
적용할
 
수
 
없습니다.
 
5.
 
코랩
 
세션
 
논의
 
질문
 
(Discussion
 
Questions)
 
1.
 
메모리
 
효율성
:
 
\"
퀵셀렉트는
 
제자리
(
In-place)
에서
 
동작하여
 
메모리가
 
적게
 
드는데
,
 
합병
 
정렬이나
 
힙
 
생성과
 
비교했을
 
때
 
공간
 
복잡도
 
면에서
 
어떤
 
이점이
 
있을까
?\"
 
2.
 
안정성
:
 
\"
데이터가
 
거의
 
정렬되어
 
있는
 
최악의
 
경우
,
 
퀵셀렉트의
 
성능
 
저하
(
 
O(N^2)
 
)
를
 
어떻게
 
방지할
 
수
 
있을까
?\"
 
(
예
:
 
랜덤
 
피벗
 
선택
)
 
3.
 
실전
 
적용
:
 
\"
로그
 
분석
 
시스템에서
 
실시간으로
 
가장
 
에러가
 
많이
 
발생하는
 
상위
 
10
개
 
항목을
 
뽑아야
 
한다면
,
 
힙과
 
퀵셀렉트
 
중
 
무엇이
 
더
 
적합할까
?\"
 
Q1.
 
메모리
 
효율성
:
 
퀵셀렉트
 
vs
 
합병
 
정렬
 
vs
 
힙
 
●
 
답변
 
핵심
:
 
**\"
추가
 
공간을
 
사용하는가
(
In-place
 
여부
)\"**
가
 
포인트입니다
.
 
●
 
상세
 
설명
:
 
○
 
퀵셀렉트
:
 
원본
 
배열
 
안에서
 
요소들의
 
위치만
 
바꾸는
(
Swap)
 
In-place
 
알고리즘입니다
.
 
따라서
 
추가적인
 
메모리
 
공간이
 
거의
 
들지
 
않습니다
(
 
O(1)
 
).
 
○
 
합병
 
정렬
:
 
데이터를
 
쪼개서
 
담아둘
 
복사본
 
리스트가
 
반드시
 
필요합니다
.
 
그래서
 
데이터
 
양만큼의
 
추가
 
메모리
(
 
O(N)
 
)
가
 
소모됩니다
.
 
○
 
힙
:
 
기존
 
배열을
 
힙
 
구조로
 
재배치
(
heapify)
하면
 
O(1)
 
공간으로
 
가능하지만
,
 
보통
 
파이썬의
 
heapq
 
등을
 
사용해
 
새로운
 
리스트를
 
만들면
 
O(N)
 
공간이
 
필요합니다
.
 
●
 
결론
:
 
메모리가
 
극도로
 
제한된
 
환경
(
임베디드
 
등
)
에서는
 
퀵셀렉트가
 
가장
 
유리합니다
.
 
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
Q2.
 
퀵셀렉트의
 
최악의
 
경우
(
 
O(N^2)
 
)
 
방지
 
대책
 
●
 
답변
 
핵심
:
 
**\"
피벗
(
Pivot)
을
 
얼마나
 
영리하게
 
고르는가
\"**
가
 
해결책입니다
.
 
●
 
상세
 
설명
:
 
○
 
문제
 
상황
:
 
이미
 
정렬된
 
배열에서
 
맨
 
앞이나
 
맨
 
뒤를
 
피벗으로
 
고르면
,
 
한
 
쪽은
 
0
개
,
 
다른
 
쪽은
 
N-1
 
개로
 
나뉘어
 
속도가
 
급격히
 
느려집니다
.
 
○
 
해결책
 
1
 
(Random
 
Pivot):
 
피벗을
 
무작위로
 
고르면
 
최악의
 
상황을
 
만날
 
확률이
 
수학적으로
 
거의
 
0
에
 
수렴합니다
.
 
○
 
해결책
 
2
 
(Median-of-Three):
 
맨
 
앞
,
 
맨
 
뒤
,
 
중간값
 
중
 
\"
중간값
\"
을
 
피벗으로
 
선택하여
 
데이터를
 
최대한
 
균등하게
 
분할합니다
.
 
●
 
결론
:
 
실전에서는
 
랜덤
 
피벗만
 
사용해도
 
평균적으로
 
매우
 
안정적인
 
O(N)
 
성능을
 
얻을
 
수
 
있습니다
.
 
 
Q3.
 
실전
 
적용
:
 
실시간
 
상위
 
10
개
 
항목
 
추출
 
(
힙
 
vs
 
퀵셀렉트
)
 
●
 
답변
 
핵심
:
 
**\"
데이터가
 
정적인가
,
 
동적인가
\"**
를
 
따져야
 
합니다
.
 
●
 
상세
 
설명
:
 
○
 
퀵셀렉트
:
 
데이터가
 
이미
 
다
 
모여
 
있는
 
배치
(
Batch)
 
상황에서
 
유리합니다
.
 
한
 
번
 
실행해서
 
상위
 
10
개를
 
툭
 
뽑아내고
 
끝낼
 
때
 
가장
 
빠릅니다
.
 
○
 
힙
 
(Heap):
 
데이터가
 
초
 
단위로
 
계속
 
들어오는
 
스트리밍
(
Stream)
 
상황에서
 
유리합니다
.
 
■
 
크기가
 
10
인
 
'
최소
 
힙
(
Min-Heap)'
을
 
유지하면서
,
 
새로운
 
데이터가
 
들어올
 
때마다
 
힙의
 
최솟값과
 
비교해
 
교체하면
 
됩니다
.
 
■
 
이
 
방식은
 
전체
 
데이터를
 
다
 
저장할
 
필요
 
없이
 
항상
 
딱
 
10
개만
 
유지하면
 
되므로
 
메모리와
 
시간
 
면에서
 
훨씬
 
효율적입니다
.
 
●
 
결론
:
 
실시간
 
시스템이라면
 
**
힙
(
Heap)**
이
 
정답입니다
.
 
\"결국
 
절대적으로
 
우월한
 
알고리즘은
 
없습니다.
 
메모리가
 
중요한지(
In-place),
 
데이터가
 
실시간으로
 
들어오는지(
Stream),
 
혹은
 
**데이터의
 
범위가
 
한정적인지(
Counting)**
에
 
따라
 
우리가
 
가진
 
도구
 
상자에서
 
가장
 
적절한
 
도구를
 
꺼내
 
쓰는
 
능력이
 
중요합니다.\"
 
 
  
저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    return s

def print_summary():
    s = get_summary()
    print("Week:", s.week)
    print("Files count:", len(s.files))
    print("Tech stack:", s.tech_stack)