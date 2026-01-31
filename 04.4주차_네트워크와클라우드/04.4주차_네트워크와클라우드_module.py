"""
Auto-generated module for 04.4주차_네트워크와클라우드
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
    name="04.4주차_네트워크와클라우드",
    lectures=[],
    missions=['(EXT) [SeSAC] [네트워크와 클라우드] 코랩 세션_Wrap Up 리포트 (template)의 사본.pdf', '00 Course Introduction.pptx.pdf', '01 Understanding Web Communication and HTTP.pdf', '02 Network Fundamental Knowledge.pdf', '03 Getting Started with Cloud Computing.pdf', '04 Managing Cloud Servers.pdf', '05 Web Server User Service 1.pdf', '06 Web Server User Service 2.pdf', '07 Cloud Deployment Automation 1.pdf', '09 Getting Started with Cloud Exploring AWS Components.pdf', '1-08 Cloud Deployment Automation 2.pdf', '1-Why Cloud Computing Is Essential for AI Agent.pdf', '2-10 Network and AI.pdf', 'Why CI_CD Is Essential  for AI Agent.pdf', 'Why Operational and AI Infrastructure Integration Is Essential for AI Agent (1).pdf', 'Why Operational and AI Infrastructure Integration Is Essential for AI Agent.pdf', 'Why Web Server Development Is Essential for AI Agent.pdf', '[SeSAC] [네트워크와 클라우드] basic mission_day01_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] basic mission_day02_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] basic mission_day03_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] basic mission_day04_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] advanced mission_day01_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] advanced mission_day02_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] advanced mission_day03_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] advanced mission_day04_answer의 사본.pdf', '[SeSAC] [네트워크와 클라우드] advanced mission_day05_answer의 사본.pdf'],
    tech_stack=['aws', 'fastapi', 'git', 'github']
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