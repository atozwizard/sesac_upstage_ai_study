"""
Auto-generated module for 05.5주차_ProductEngineer_PromptEngineering
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
    name="05.5주차_ProductEngineer_PromptEngineering",
    lectures=[],
    missions=['(EXT) [SeSAC] [Prompt Engineering] 코랩 세션_Wrap Up 리포트 (template)의 사본.pdf', '[SeSAC] Lv3 Product Engineering 타운홀 미팅.pdf', '02-Basic_Prompting.pptx.pdf', '03-Advanced LLM Prompting Strategies_1.pdf', '09-Related_Works_Trends.pptx.pdf', '1-01-Introduction.pptx.pdf', '1-08-Prompt-Based LLM Security Vulnerabilities and Safety Validation.pdf', '10-Agentic_AI_Summary.pptx.pdf', '2-04-Advanced LLM Prompting Strategies_2.pdf', 'Chain-of-Thought Prompting Elicits Reasoning.pdf', 'Exploring Agentic Workflows_ A Deep Dive into AI-Enhanced Productivity.pdf', 'FaithfulRAG Fact-Level Conflict Modeling for Context-Faithful.pdf', 'Large Language Models are Better Reasoners with Self-Verification.pdf', 'Prompt Engineering_07_Advanced RAG_2.pdf', 'Prompting Large Vision-Language Models for Compositional Reasoning.pdf', 'Red Teaming Language Models with Language Models.pdf', '[Daily_Mission]_(Day1_기본_심화)_Prompt_Engineering을_적용하여_MMLU_풀이하기(문제)_ipynb의_사본 (1).ipynb', '[Daily_Mission]_(Day2_기본_심화)_LLM_고급_프롬프팅_기법(문제)_ipynb의_사본.ipynb', '[Daily_Mission]_(Day4_기본)_RAG_Knowledge_Conflict(문제)_ipynb의_사본.ipynb', '[Daily_Mission]_(Day4_심화)_Prompt_Guardrails(문제)_ipynb의_사본.ipynb', '[Daily_Mission]_(Day4_심화)_Prompt_Guardrails(정답).ipynb', '[Daily_Mission]_(Day5_기본)_Visual–Text_Embedding_Alignment_이해하기(문제)_ipynb의_사본.ipynb', '[Daily_Mission]_(Day5_심화)_Tool_selector_만들기(문제).ipynb', '[Daily_Mission]_(Day5_심화)_Tool_selector_만들기(정답)_ipynb의_사본.ipynb'],
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