"""
Day 4: 심화 프로젝트 - 멀티턴 대화 시스템
=======================================

대화 기록 관리, 컨텍스트 유지, 동적 프롬프트, 응답 검증, 비용 최적화
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


class Day4Learning:
    """Day 4: 심화 프로젝트"""
    
    memory_management = LearningContent(
        title="4.1 대화 기록 및 메모리 관리",
        description="대화 이력을 효율적으로 관리하여 컨텍스트 유지",
        concepts=["슬라이딩 윈도우", "요약 기법", "우선순위", "토큰 최적화"],
        examples=["긴 대화 처리", "요약 생성", "중요 정보 추출", "메모리 제한"],
        key_takeaways=["메모리 용량 제한 설정", "자동 요약", "우선순위 기반 선별"]
    )
    
    context_preservation = LearningContent(
        title="4.2 컨텍스트 유지 전략",
        description="여러 턴의 대화에서 일관된 이해 유지",
        concepts=["사용자 의도", "개체 참조", "문맥 일관성", "상태 관리"],
        examples=["지속적인 주제", "참조 해결", "개인화", "논리 검증"],
        key_takeaways=["명확한 참조", "의도 파악", "일관성 유지"]
    )
    
    dynamic_prompts = LearningContent(
        title="4.3 동적 프롬프트 구성",
        description="사용자 입력과 대화 상황에 따라 프롬프트 동적 생성",
        concepts=["조건부 로직", "변수 삽입", "컨텍스트 추가", "프롬프트 빌더"],
        examples=["사용자별 커스터마이징", "도메인 특화", "동적 예제", "적응형 프롬프트"],
        key_takeaways=["유연한 템플릿", "데이터 바인딩", "조건 처리"]
    )
    
    validation_retry = LearningContent(
        title="4.4 응답 검증 및 재시도 로직",
        description="모델 응답을 검증하고 오류 시 자동으로 재시도",
        concepts=["응답 검증", "오류 감지", "재시도 전략", "폴백 메커니즘"],
        examples=["형식 검증", "의미 검증", "신뢰도 점수", "사용자 확인"],
        key_takeaways=["자동 재시도", "점진적 백오프", "사용자 개입 옵션"]
    )
    
    cost_optimization = LearningContent(
        title="4.5 비용 최적화",
        description="API 사용량을 모니터링하고 비용을 최소화",
        concepts=["토큰 계산", "모델 선택", "캐싱", "배치 처리"],
        examples=["저비용 모델 선택", "컨텍스트 압축", "응답 재사용", "사용량 추적"],
        key_takeaways=["토큰 효율성", "모델 비교", "사용량 모니터링"]
    )
    
    @staticmethod
    def get_all_content() -> Dict[str, LearningContent]:
        return {
            "memory_management": Day4Learning.memory_management,
            "context_preservation": Day4Learning.context_preservation,
            "dynamic_prompts": Day4Learning.dynamic_prompts,
            "validation_retry": Day4Learning.validation_retry,
            "cost_optimization": Day4Learning.cost_optimization,
        }
