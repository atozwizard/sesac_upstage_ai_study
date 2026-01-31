"""
Auto-generated module for 06.6주차_Product Engineer - Agentic Workflow
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
    name="06.6주차_Product Engineer - Agentic Workflow",
    lectures=[],
    missions=['01-AI Service and Agent Design.pdf', '02-Agentic AI.pdf', '03-Tool Calling Fundamentals.pdf', '04-MCP.pdf', '05-RAG and Agentic RAG.pdf', '06-Memory Management and Reflexion.pdf', 'Agents_Companion_v2.pdf', 'In Prospect and Retrospect Reflective Memory.pdf', 'Practice01_ai_service_agent_ipynb의_사본.ipynb', 'Practice02_agentic_workflow_ipynb의_사본.ipynb', 'Practice03_tool_calling_ipynb의_사본 (1).ipynb', 'Practice04_mcp_ipynb의_사본 (1).ipynb', '(EXT)_[SeSAC]_[Agentic_Workflow]_daily_mission_day1_기본과제_ipynb의_사본.ipynb', '(EXT)_[SeSAC]_[Agentic_Workflow]_daily_mission_day1_심화과제_ipynb의_사본.ipynb', '(EXT)_[SeSAC]_[Agentic_Workflow]_daily_mission_day2_기본과제_ipynb의_사본.ipynb', '(EXT)_[SeSAC]_[Agentic_Workflow]_daily_mission_day2_심화과제_ipynb의_사본.ipynb'],
    tech_stack=[]
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