from dataclasses import dataclass, field
from typing import List

@dataclass
class WeekSummary:
    week: str = ""
    lectures: List[str] = field(default_factory=list)
    missions: List[str] = field(default_factory=list)
    scripts: List[str] = field(default_factory=list)
    projects: List[str] = field(default_factory=list)
    notebooks: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)
    learning_summary: List[str] = field(default_factory=list)

def get_summary() -> WeekSummary:
    s = WeekSummary(week="02.2주차_알고리즘")
    s.lectures = ['강의마무리_코랩 세션_Wrap Up 리포트.pdf', '00.강의자료\\Lecture 10.pdf', '00.강의자료\\Lecture 2.pdf', '00.강의자료\\Lecture 3.pdf', '00.강의자료\\Lecture 4.pdf', '00.강의자료\\Lecture 5.pdf', '00.강의자료\\Lecture 6.pdf', '00.강의자료\\Lecture 7.pdf', '00.강의자료\\Lecture 8.pdf', '00.강의자료\\Lecture 9.pdf', '00.강의자료\\lecture01.pdf']
    s.missions = ['.ipynb_checkpoints\\ApplicationQuestion-checkpoint.ipynb', '.ipynb_checkpoints\\Day1_advanced_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Day1_daily_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Day2_advanced_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Day2_daily_mission(문제)-checkpoint.ipynb', '.ipynb_checkpoints\\Untitled-checkpoint.ipynb', '01.daily_mission\\Day1_daily_mission(문제)_leetcode001.ipynb', '01.daily_mission\\Day2_daily_mission(문제).ipynb', '01.daily_mission\\Day3_daily_mission(문제)_leetcode104.ipynb', '01.daily_mission\\Day4_daily_mission(문제)_leetcode215.ipynb', '01.daily_mission\\Day5_daily_mission(문제).ipynb', '02.advanced_mission\\Day1_advanced_mission(문제).ipynb', '02.advanced_mission\\Day2_advanced_mission(문제).ipynb', '02.advanced_mission\\Day3_advanced_mission(문제)_leetcode200.ipynb', '02.advanced_mission\\Day4_advanced_mission(문제).ipynb', '02.advanced_mission\\Day5_advanced_mission(문제)_leetcode-056.ipynb', '02.advanced_mission\\.ipynb_checkpoints\\Day4_advanced_mission(문제)-checkpoint.ipynb', '02.advanced_mission\\.ipynb_checkpoints\\Day5_advanced_mission(문제)_leetcode-056-checkpoint.ipynb', '01.daily_mission\\.ipynb_checkpoints\\Day4_daily_mission(문제)-checkpoint.ipynb', '01.daily_mission\\.ipynb_checkpoints\\Day4_daily_mission(문제)_leetcode215-checkpoint.ipynb', '01.daily_mission\\.ipynb_checkpoints\\Day5_daily_mission(문제)-checkpoint.ipynb']
    s.scripts = ['02.2주차_알고리즘_module.py', 'accomplicationQuestion_5-6.py', 'appicationQuestion9.py', 'applicationquestion10.py', 'ApplicationQuestions1-4.py', 'applicationQuestion_lec8.py', '자료구조와알고리즘.py', '.ipynb_checkpoints\\자료구조와알고리즘-checkpoint.py']
    s.projects = ['README_GENERATED.md', 'README_TECHSTACK.md', 'README_TECHSTACK_DRAFT.md', '__pycache__\\02.2주차_알고리즘_module.cpython-313.pyc']
    s.notebooks = ['extracted_content\\ApplicationQuestion-checkpoint.ipynb.txt', 'extracted_content\\Day1_advanced_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day1_advanced_mission(문제).ipynb.txt', 'extracted_content\\Day1_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day1_daily_mission(문제)_leetcode001.ipynb.txt', 'extracted_content\\Day2_advanced_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day2_advanced_mission(문제).ipynb.txt', 'extracted_content\\Day2_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day2_daily_mission(문제).ipynb.txt', 'extracted_content\\Day3_advanced_mission(문제)_leetcode200.ipynb.txt', 'extracted_content\\Day3_daily_mission(문제)_leetcode104.ipynb.txt', 'extracted_content\\Day4_advanced_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day4_advanced_mission(문제).ipynb.txt', 'extracted_content\\Day4_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day4_daily_mission(문제)_leetcode215-checkpoint.ipynb.txt', 'extracted_content\\Day4_daily_mission(문제)_leetcode215.ipynb.txt', 'extracted_content\\Day5_advanced_mission(문제)_leetcode-056-checkpoint.ipynb.txt', 'extracted_content\\Day5_advanced_mission(문제)_leetcode-056.ipynb.txt', 'extracted_content\\Day5_daily_mission(문제)-checkpoint.ipynb.txt', 'extracted_content\\Day5_daily_mission(문제).ipynb.txt', 'extracted_content\\extracted_content.json', 'extracted_content\\Lecture 10.txt', 'extracted_content\\Lecture 2.txt', 'extracted_content\\Lecture 3.txt', 'extracted_content\\Lecture 4.txt', 'extracted_content\\Lecture 5.txt', 'extracted_content\\Lecture 6.txt', 'extracted_content\\Lecture 7.txt', 'extracted_content\\Lecture 8.txt', 'extracted_content\\Lecture 9.txt', 'extracted_content\\lecture01.txt', 'extracted_content\\Untitled-checkpoint.ipynb.txt', 'extracted_content\\강의마무리_코랩 세션_Wrap Up 리포트.txt']
    s.tech_stack = []
    s.learning_summary = ['- 테스트 결과를 실행해 스크린샷 촬영 (제출 시 포함)', '- [ ] (과제용) 실행 결과를 캡처해 별도 제출 또는 첨부 준비를 했다.', '### ✅ 테스트 코드 (수정하지 말고, 위 함수를 구현한 뒤 실행해 보세요)', '### ✅ 테스트 코드 (수정하지 말고, 위 함수를 완성한 뒤 실행해 보세요)', '아래 셀을 실행해 예제 입력과 몇 가지 추가 케이스에 대해 결과를 확인해 보세요.', '###테스트코드', '## 🎯 학습 목표', '### ✅ 테스트 코드']
    return s

def print_summary():
    s = get_summary()
    print("Week:", s.week)
    print("Tech stack:", s.tech_stack)
    print("Learning summary:")
    for b in s.learning_summary:
        print(" -", b)