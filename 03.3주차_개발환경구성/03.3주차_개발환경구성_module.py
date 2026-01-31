"""
Auto-generated module for 03.3주차_개발환경구성
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class WeekSummary:
    name: str
    lectures: List[str] = field(default_factory=list)
    missions: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)


summary = WeekSummary(
    name="03.3주차_개발환경구성",
    lectures=[],
    missions=['(EXT) [SeSAC] [개발환경 구성] 코랩 세션_Wrap Up 리포트 (template)의 사본.pdf', '00 Development Environment Course Introduction.pdf', '01 Creating a Developer Friendly Computer Environment.pdf', '03 Git Basics.pdf', '04 Git Advanced.pdf', '05 GitHub for Collaboration.pdf', '06 Project Management and GitHub.pdf', '07 Docker Infrastructure and MySQL.pdf', '08 Understanding Databases and MySQL.pdf', '09 Managing MySQL on a Server.pdf', '10 Maintainable Architecture.pdf', 'SeSAC_CS with AI_Guide.pdf', '[SeSAC] [개발환경 구성] basic mission_day01_answer의 사본.pdf', '[SeSAC] [개발환경 구성] basic mission_day02_answer의 사본.pdf', '[SeSAC] [개발환경 구성] basic mission_day03_answer의 사본.pdf', '[SeSAC] [개발환경 구성] basic mission_day04_answer의 사본.pdf', '[SeSAC] [개발환경 구성] basic mission_day05_answer의 사본.pdf', '[SeSAC] [개발환경 구성] advanced mission_day01_answer의 사본.pdf', '[SeSAC] [개발환경 구성] advanced mission_day02_answer의 사본.pdf', '[SeSAC] [개발환경 구성] advanced mission_day03_answer의 사본.pdf', '[SeSAC] [개발환경 구성] advanced mission_day04_answer의 사본.pdf', '[SeSAC] [개발환경 구성] advanced mission_day05_answer의 사본.pdf'],
    tech_stack=['docker', 'git', 'github', 'mysql', 'postman', 'sql']
)



def print_summary():
    print("Week: ", summary.name)
    print("Lectures:")
    for l in summary.lectures:
        print("  - " + l)
    print("Missions:")
    for m in summary.missions:
        print("  - " + m)
    print("Tech stack detected:", summary.tech_stack)