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

def get_summary() -> WeekSummary:
    s = WeekSummary(week="01.1주차_ai_litaracy")
    s.lectures = ['01.강의자료\\01-Understanding of AI.pdf', '01.강의자료\\02-Understanding the Working Principles of AI.pdf', '01.강의자료\\03-Ability to converse with AI.pdf', '01.강의자료\\04-Explore AI application cases by industry.pdf', '01.강의자료\\05-AI ethics and social change.pdf', '02.advanced mission\\(EXT) [SeSAC] [AI Literacy] advanced mission_day01_answer_sheet의 사본.pdf', '02.advanced mission\\(EXT) [SeSAC] [AI Literacy] advanced mission_day02_answer_sheet의 사본.pdf', '02.advanced mission\\(EXT) [SeSAC] [AI Literacy] advanced mission_day03_answer_sheet의 사본.pdf', '02.advanced mission\\(EXT) [SeSAC] [AI Literacy] advanced mission_day04_answer_sheet의 사본.pdf', '02.advanced mission\\day5_심화_ai정체성선언문_이영기.pdf', '03.basic mission\\(EXT) [SeSAC] [AI Literacy] basic mission_day01_answer_sheet의 사본.pdf', '03.basic mission\\(EXT) [SeSAC] [AI Literacy] basic mission_day02_answer_sheet의 사본.pdf', '03.basic mission\\(EXT) [SeSAC] [AI Literacy] basic mission_day03_answer_sheet의 사본.pdf', '03.basic mission\\(EXT) [SeSAC] [AI Literacy] basic mission_day05_answer_sheet의 사본.pdf', '03.basic mission\\day4_산업리서치_이영기.pdf', '03.basic mission\\day5_발표자료_이영기.pdf']
    s.missions = []
    s.scripts = []
    s.projects = ['README_TECHSTACK.md', 'README_TECHSTACK_DRAFT.md', 'extracted_content\\extracted_content.json']
    s.notebooks = ['extracted_content\\advanced_missions_extracted.txt', 'extracted_content\\basic_missions_extracted.txt', 'extracted_content\\lectures_extracted.txt']
    s.tech_stack = []
    return s

def print_summary():
    s = get_summary()
    print("Week:", s.week)
    print("Tech stack:", s.tech_stack)
    print("Lectures:
", "
".join(s.lectures))
