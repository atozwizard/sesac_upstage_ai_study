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
    w = WeekDetail(week="01.1주차_ai_litaracy")
    # 원본 자료 중 메타 정보만 보존합니다. 원문 텍스트는 저작권 이슈로 요약 형태로 모듈에 담았습니다.
    w.files = [
        '01.강의자료\\01-Understanding of AI.pdf',
        '01.강의자료\\02-Understanding the Working Principles of AI.pdf',
        '01.강의자료\\03-Ability to converse with AI.pdf',
        '01.강의자료\\04-Explore AI application cases by industry.pdf',
        '01.강의자료\\05-AI ethics and social change.pdf',
        '02.advanced mission\\day5_심화_ai정체성선언문_이영기.pdf',
        '03.basic mission\\day4_산업리서치_이영기.pdf',
        '03.basic mission\\day5_발표자료_이영기.pdf'
    ]
    w.tech_stack = ["AI_개념", "AI_윤리", "프롬프팅_기초", "사례분석"]
    w.learning_paragraphs = [
        "강의 목표: AI의 기본 작동 원리(모델, 학습, 추론)를 이해하고, AI가 생성하는 결과의 한계(환각, 편향)를 인지한다.",
        "실습 요약: 간단한 프롬프트를 설계하고, 프롬프트 문구(역할·제약·형식)에 따른 출력 차이를 실험했다.",
        "핵심 통찰: AI는 통계적 패턴에 기반하여 '가능성 높은' 텍스트를 생성하므로, 검증·후처리(RAG/체크리스트 등)가 필수임을 학습했다.",
        "프로젝트 기록: 산업별 적용 사례를 조사해 발표하면서 실제 비즈니스 문제를 AI로 어떻게 풀지 설계해보았다.",
        "학습 권장: 프롬프트를 짤 때는 (1) 역할 부여, (2) 입력 예시, (3) 출력 포맷 명시, (4) 검증 기준을 함께 포함시키자."
    ]
    w.code_examples = {
        "prompt_example.py": (
            "# 간단한 프롬프트 템플릿 예시\n"
            "def build_prompt(task: str, persona: str = 'assistant') -> str:\n"
            "    return f'Role: {persona}\\nTask: {task}\\nPlease answer concisely.'\n\n"
            "# 사용 예\n"
            "if __name__ == '__main__':\n"
            "    p = build_prompt('주어진 텍스트를 요약해줘', persona='요약 전문가')\n"
            "    print(p)"
        )
    }
    return w

def print_detail():
    d = get_detail()
    print("Week:", d.week)
    print("Techs:", d.tech_stack)
    print("\nLearning paragraphs:")
    for p in d.learning_paragraphs:
        print(" -", p[:80], "...")
    print("\nCode examples files:", list(d.code_examples.keys()))