"""
Day 3: 고급 프롬프트 기법
======================

Few-shot Learning, Chain-of-Thought, 다국어 지원, 구조화된 출력, 에러 처리
"""

from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class LearningContent:
    title: str
    description: str
    concepts: List[str] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)
    key_takeaways: List[str] = field(default_factory=list)


class Day3Learning:
    """Day 3: 고급 프롬프트 기법"""
    
    fewshot = LearningContent(
        title="3.1 Few-Shot Learning",
        description="여러 예제를 통해 모델이 패턴을 학습하도록 유도하는 기법",
        concepts=["예제 선택", "예제 순서", "다양성", "쏘트 예제 기법"],
        examples=["감정분석", "개체명인식", "질문응답", "분류 작업"],
        key_takeaways=["3-5개 예제가 적당", "다양한 케이스 포함", "명확한 형식"]
    )
    
    cot = LearningContent(
        title="3.2 Chain-of-Thought (CoT)",
        description="모델이 단계별로 추론하도록 유도하여 정확도 향상",
        concepts=["중간 단계", "검증", "자기 일관성", "다단계 추론"],
        examples=["수학 문제", "논리 문제", "복잡한 질문", "계획 수립"],
        key_takeaways=["'단계별' 강조", "검증 단계 포함", "틀린 추론 교정"]
    )
    
    multilingual = LearningContent(
        title="3.3 다국어 지원",
        description="언어별 특성을 고려한 프롬프트 작성",
        concepts=["언어별 토큰화", "문맥 차이", "문법 구조", "번역 품질"],
        examples=["한영 번역", "한중 번역", "다언어 분류", "언어 감지"],
        key_takeaways=["명확한 언어 지정", "문화적 맥락", "검증 필수"]
    )
    
    structured = LearningContent(
        title="3.4 구조화된 출력",
        description="JSON, CSV 등 특정 형식으로 출력하도록 강제",
        concepts=["JSON 스키마", "마크다운", "테이블", "형식 검증"],
        examples=["데이터 추출", "API 응답", "레포트 생성", "데이터 변환"],
        key_takeaways=["형식 예제 명시", "필드 설명", "검증 로직"]
    )
    
    error_handling = LearningContent(
        title="3.5 에러 처리 및 검증",
        description="모델 응답의 오류를 감지하고 처리하는 기법",
        concepts=["응답 검증", "재시도 로직", "사용자 확인", "폴백 옵션"],
        examples=["입력 검증", "출력 검증", "신뢰도 점수", "오류 복구"],
        key_takeaways=["입력 검증 필수", "재시도 전략", "사용자 피드백"]
    )
    
    @staticmethod
    def get_all_content() -> Dict[str, LearningContent]:
        return {
            "fewshot": Day3Learning.fewshot,
            "cot": Day3Learning.cot,
            "multilingual": Day3Learning.multilingual,
            "structured": Day3Learning.structured,
            "error_handling": Day3Learning.error_handling,
        }
