"""
Day 5: 최적화 및 배포
===================

프롬프트 성능 측정, A/B 테스트, 최적화 전략, 에러 분석, 프로덕션 배포
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


class Day5Learning:
    """Day 5: 최적화 및 배포"""
    
    performance_metrics = LearningContent(
        title="5.1 프롬프트 성능 측정 지표",
        description="프롬프트 품질을 객관적으로 평가하는 지표",
        concepts=["정확도", "완전성", "명확성", "응답 시간", "사용자 만족도"],
        examples=["분류 정확도", "생성 품질 점수", "사용자 피드백", "자동 평가"],
        key_takeaways=["정성적 + 정량적 평가", "다양한 지표 조합", "벤치마크 설정"]
    )
    
    ab_testing = LearningContent(
        title="5.2 A/B 테스트",
        description="프롬프트 변형 간의 성능을 통계적으로 비교",
        concepts=["실험 설계", "표본 크기", "통계 검정", "유의성"],
        examples=["프롬프트 A vs B", "파라미터 비교", "모델 비교", "길이 최적화"],
        key_takeaways=["충분한 표본 크기", "무작위화", "한 변수씩만 테스트"]
    )
    
    error_analysis = LearningContent(
        title="5.3 에러 케이스 분석",
        description="실패 사례에서 배우고 개선점 도출",
        concepts=["에러 분류", "근본 원인 분석", "패턴 감지", "가설 검증"],
        examples=["실패 사례 수집", "분류 및 분석", "개선책 도출", "재테스트"],
        key_takeaways=["체계적 분석", "반복 개선", "문서화"]
    )
    
    optimization_strategy = LearningContent(
        title="5.4 최적화 전략",
        description="프롬프트를 단계적으로 개선하는 전략",
        concepts=["점진적 개선", "파레토 원칙", "성능 한계", "비용-성능 트레이드오프"],
        examples=["기본값에서 시작", "우선순위 개선", "신규 기법 실험", "최종 검증"],
        key_takeaways=["한 번에 하나씩 개선", "효과 측정", "중단 지점 결정"]
    )
    
    production_deployment = LearningContent(
        title="5.5 프로덕션 배포",
        description="최적화된 프롬프트를 실제 서비스에 배포",
        concepts=["버전 관리", "A/B 롤아웃", "모니터링", "롤백", "문서화"],
        examples=["점진적 배포", "실시간 모니터링", "문제 감지 및 해결", "사후 분석"],
        key_takeaways=["단계적 배포", "지속적 모니터링", "빠른 롤백 준비"]
    )
    
    @staticmethod
    def get_all_content() -> Dict[str, LearningContent]:
        return {
            "performance_metrics": Day5Learning.performance_metrics,
            "ab_testing": Day5Learning.ab_testing,
            "error_analysis": Day5Learning.error_analysis,
            "optimization_strategy": Day5Learning.optimization_strategy,
            "production_deployment": Day5Learning.production_deployment,
        }
