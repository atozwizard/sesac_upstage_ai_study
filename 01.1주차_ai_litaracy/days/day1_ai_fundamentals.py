"""
Day 1: AI와 LLM 기초 이해
========================

AI(Artificial Intelligence), Machine Learning, Deep Learning의 개념과 차이, 
LLM의 동작 원리, 토큰과 컨텍스트 윈도우 이해
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class LearningContent:
    """학습 내용 구조"""
    title: str
    description: str
    concepts: List[str] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)
    key_takeaways: List[str] = field(default_factory=list)


class Day1Learning:
    """Day 1: AI와 LLM 기초 이해"""
    
    # ============ Section 1: AI의 개념 ============
    ai_concepts = LearningContent(
        title="1.1 AI vs Machine Learning vs Deep Learning",
        description="""
        AI(인공지능): 인간의 지능을 모방하는 프로그램
        - 광의: 규칙 기반 전문가 시스템도 AI
        - 협의: 데이터로부터 학습하는 시스템
        
        Machine Learning: 명시적 프로그래밍 없이 데이터로부터 학습
        - Supervised Learning (지도학습): 레이블된 데이터로 학습
        - Unsupervised Learning (비지도학습): 패턴 발견
        - Reinforcement Learning (강화학습): 보상으로부터 학습
        
        Deep Learning: 다층 신경망을 이용한 기계학습
        - 특징 추출을 자동으로 수행
        - 이미지, 텍스트, 음성 처리에 강함
        """,
        concepts=[
            "AI의 정의와 역사",
            "Machine Learning의 3가지 학습 방식",
            "Neural Networks의 기초",
            "Deep Learning의 등장 배경",
            "LLM (Large Language Models)의 개념"
        ],
        examples=[
            "예1: 이메일 스팸 필터 (Supervised ML)",
            "예2: 추천 시스템 (Collaborative Filtering)",
            "예3: 이미지 분류 (Deep Learning)",
            "예4: ChatGPT (LLM)"
        ],
        key_takeaways=[
            "AI는 광의의 개념, ML은 AI의 부분집합",
            "DL은 ML의 특수한 형태",
            "LLM은 transformer 아키텍처 기반의 DL 모델"
        ]
    )
    
    # ============ Section 2: LLM의 동작 원리 ============
    llm_architecture = LearningContent(
        title="1.2 LLM의 동작 원리",
        description="""
        LLM (Large Language Model): 대규모 텍스트 데이터로 학습된 신경망
        
        학습 과정:
        1. Pre-training: 대규모 텍스트 코퍼스로 미리 학습
           - Unsupervised Learning
           - 다음 토큰 예측 (Causal Language Modeling)
        
        2. Fine-tuning: 특정 작업에 맞게 추가 학습
           - Supervised Learning
           - Instruction tuning, RLHF (Reinforcement Learning from Human Feedback)
        
        3. In-context Learning: 프롬프트를 통한 적응
           - Few-shot examples
           - 재학습 없이 새로운 작업 수행
        
        Transformer 아키텍처:
        - Attention 메커니즘: 입력 간의 상관관계 학습
        - Self-Attention: 입력 시퀀스 내부의 관계 파악
        - Multi-head Attention: 여러 관점에서 동시에 학습
        """,
        concepts=[
            "Transformer 아키텍처의 구조",
            "Attention 메커니즘의 원리",
            "Self-Attention과 Cross-Attention",
            "Positional Encoding (위치 정보 인코딩)",
            "Feed-forward Networks",
            "Normalization과 Residual Connections"
        ],
        examples=[
            "예1: GPT 시리즈의 진화 (GPT-2 → GPT-3 → GPT-4)",
            "예2: BERT vs GPT의 차이점",
            "예3: Attention 시각화 예제",
            "예4: 토큰 예측 시뮬레이션"
        ],
        key_takeaways=[
            "LLM의 핵심은 Attention 메커니즘",
            "Pre-training과 Fine-tuning의 중요성",
            "프롬프트가 모델의 성능을 좌우",
            "더 큰 모델, 더 많은 데이터 = 더 나은 성능"
        ]
    )
    
    # ============ Section 3: 토큰과 컨텍스트 윈도우 ============
    tokenization = LearningContent(
        title="1.3 토큰(Token)과 컨텍스트 윈도우",
        description="""
        토큰 (Token): LLM이 이해하는 최소 단위
        - 단어, 부분 단어, 심볼 등으로 분할
        - 각 토큰은 고유한 정수 ID로 매핑
        - 1 토큰 ≈ 0.75 단어 (평균)
        
        토큰화 방식:
        1. Word Tokenization: 전체 단어 단위 (어휘 크기 큼)
        2. Subword Tokenization: BPE, WordPiece (효율적)
        3. Character Tokenization: 문자 단위 (드물게 사용)
        
        컨텍스트 윈도우 (Context Window):
        - 모델이 한 번에 처리할 수 있는 최대 토큰 수
        - GPT-4: 8K, 32K, 128K 버전
        - Claude: 100K, 200K 토큰
        - 더 긴 컨텍스트 = 더 많은 정보 처리 가능
        
        토큰 계산:
        - Input tokens: 입력 프롬프트의 토큰 수
        - Output tokens: 생성된 응답의 토큰 수
        - API 비용 = (input_tokens × input_price) + (output_tokens × output_price)
        """,
        concepts=[
            "토큰화 알고리즘 (BPE, WordPiece, SentencePiece)",
            "토큰과 단어의 관계",
            "컨텍스트 윈도우의 제한",
            "롱 컨텍스트 처리 기술",
            "토큰 효율성 최적화"
        ],
        examples=[
            "예1: 같은 문장의 다양한 토큰화 결과",
            "예2: 다국어 토큰화의 차이",
            "예3: 컨텍스트 윈도우 제한 사례",
            "예4: 토큰 수 추정 계산"
        ],
        key_takeaways=[
            "프롬프트 최적화는 토큰 효율성 고려 필수",
            "컨텍스트 윈도우는 장문 처리의 핵심 제약",
            "토큰 수를 정확히 계산하면 비용 예측 가능",
            "언어마다 토큰화 효율이 다름"
        ]
    )
    
    # ============ Section 4: OpenAI API 설정 ============
    api_setup = LearningContent(
        title="1.4 OpenAI API 가입 및 설정",
        description="""
        OpenAI API 시작하기:
        
        1단계: 계정 생성
        - https://platform.openai.com 방문
        - 이메일로 가입
        - 이메일 인증
        
        2단계: API 키 생성
        - Settings → API keys 이동
        - "Create new secret key" 클릭
        - 키 복사 및 안전하게 보관
        
        3단계: 초기 크레딧 확인
        - 신규 가입자: $5 무료 크레딧 (3개월 유효)
        - Usage 페이지에서 실시간 사용량 확인
        
        4단계: API 키 설정
        - 환경변수로 설정: OPENAI_API_KEY
        - Python에서 로드: os.getenv("OPENAI_API_KEY")
        - 절대 코드에 직접 삽입하지 말 것!
        
        5단계: 요금 제한 설정
        - Usage limits 설정으로 예상치 못한 비용 방지
        - 조직 레벨의 비용 관리
        """,
        concepts=[
            "OpenAI 계정 및 조직 관리",
            "API 키 보안 관리",
            "사용료 모니터링",
            "요금 제한 설정",
            "API 에러 처리"
        ],
        examples=[
            "예1: .env 파일을 이용한 안전한 키 관리",
            "예2: 환경 변수 로드 방법",
            "예3: 첫 API 호출 코드",
            "예4: 비용 추적 대시보드"
        ],
        key_takeaways=[
            "API 키는 절대 공개하면 안 됨",
            "환경변수를 통한 키 관리가 필수",
            "사용량을 정기적으로 확인할 것",
            "요금 제한을 설정하여 과도한 비용 방지"
        ]
    )
    
    # ============ Section 5: 첫 API 호출 ============
    first_call = LearningContent(
        title="1.5 첫 번째 ChatGPT API 호출",
        description="""
        기본 API 호출 구조:
        
        1. 필요한 라이브러리 임포트
        2. API 키 설정
        3. 메시지 구성 (system, user)
        4. API 호출
        5. 응답 파싱 및 출력
        
        Chat Completion API:
        - Model: 사용할 모델 선택 (gpt-4, gpt-3.5-turbo 등)
        - Messages: 대화 이력
        - Temperature: 응답의 창의성 (0~2)
        - Max_tokens: 최대 생성 토큰 수
        
        응답 구조:
        - choices[0]['message']['content']: 실제 응답 텍스트
        - usage: 사용한 토큰 수
        - model: 실제 사용된 모델
        - finish_reason: 생성 종료 이유
        """,
        concepts=[
            "Chat Completion API의 기본 구조",
            "메시지 역할 (system, user, assistant)",
            "주요 파라미터와 의미",
            "응답 구조 해석",
            "에러 처리 및 재시도"
        ],
        examples=[
            "예1: 간단한 질문-답변",
            "예2: 시스템 프롬프트 활용",
            "예3: 다중 턴 대화",
            "예4: 토큰 사용량 추적"
        ],
        key_takeaways=[
            "system 역할이 모델의 동작 방식을 결정",
            "Temperature는 응답의 일관성과 창의성의 트레이드오프",
            "API 응답에는 사용량 정보 포함",
            "에러 처리는 프로덕션 환경에서 필수"
        ]
    )
    
    @staticmethod
    def get_all_content() -> Dict[str, LearningContent]:
        """모든 학습 내용 반환"""
        return {
            "ai_concepts": Day1Learning.ai_concepts,
            "llm_architecture": Day1Learning.llm_architecture,
            "tokenization": Day1Learning.tokenization,
            "api_setup": Day1Learning.api_setup,
            "first_call": Day1Learning.first_call,
        }
    
    @staticmethod
    def print_summary():
        """학습 내용 요약 출력"""
        print("=" * 60)
        print("Day 1: AI와 LLM 기초 이해")
        print("=" * 60)
        
        for section_name, content in Day1Learning.get_all_content().items():
            print(f"\n📌 {content.title}")
            print(f"개념: {', '.join(content.concepts[:3])}...")
            print(f"주요 학습: {', '.join(content.key_takeaways[:2])}...")
