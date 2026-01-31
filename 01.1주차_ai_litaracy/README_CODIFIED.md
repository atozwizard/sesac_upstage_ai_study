# AI Literacy Course - Codified Version

## 📋 개요

SeSAC AI Literacy 프로그램의 저작권 보호 PDF 파일들을 Python 코드로 변환했습니다.

**작성자**: 이영기  
**변환 날짜**: 2026-01-31  
**원본**: (주)업스테이지 교육 콘텐츠  

---

## 📂 생성된 파일

### 1. PDF 추출 파일
```
extracted_content/
├── advanced_missions_extracted.txt    (심화 과제 텍스트)
├── basic_missions_extracted.txt       (기본 과제 텍스트)
├── lectures_extracted.txt              (강의 자료 텍스트)
├── extracted_content.json             (JSON 요약)
└── extract_pdf_to_code.py             (추출 스크립트)
```

### 2. 코드화 파일
```
ai_literacy_course_data.py             (기본 구조)
ai_literacy_complete_data.py           (완전 버전)
README_CODIFIED.md                     (이 파일)
```

---

## 🔧 사용 방법

### 기본 사용법

```python
from ai_literacy_complete_data import (
    create_course_repository,
    AILiteracyCourseRepository,
    MissionType
)

# 저장소 생성
repo = create_course_repository()

# 과정 요약 조회
summary = repo.get_course_summary()
print(summary)

# Day 01 심화 과제 조회
mission = repo.get_mission(1, MissionType.ADVANCED)
print(mission.content_proposal.selected_trend)
```

### 트렌드 정보 조회

```python
from ai_literacy_complete_data import BasicMissionContent

# MCP 트렌드 정보
mcp_trend = BasicMissionContent.AI_TRENDS_DATA.get("MCP")
print(mcp_trend.core_concept)
print(mcp_trend.practical_examples)
```

### 미션 데이터 접근

```python
from ai_literacy_complete_data import AdvancedMissionContent

# Day 01 심화 과제 데이터
day01_data = AdvancedMissionContent.DAY01_SOVEREIGN_AI

# 블로그 콘텐츠
blog = day01_data["blog_content"]
print(f"제목: {blog.title}")
print(f"글자 수: {blog.get_word_count()}")

# 인포그래픽 콘텐츠
infographic = day01_data["infographic_content"]
print(f"도구: {infographic.tools_used}")
```

---

## 📊 데이터 구조

### 클래스 다이어그램

```
AILiteracyCourseRepository
├── basic_missions: Dict[int, Mission]
├── advanced_missions: Dict[int, Mission]
└── Methods
    ├── get_mission()
    ├── get_all_ai_trends()
    ├── get_course_summary()
    └── get_mission_statistics()

Mission
├── day: int
├── step: str
├── mission_type: MissionType
├── author: str
├── content_proposal: ContentProposal
├── blog_content: BlogContent
├── infographic_content: InfographicContent
└── submission_date: str

ContentProposal
├── selected_trend: str
├── selection_reasoning: SelectionReasoning
├── selected_formats: List[ContentType]
├── format_suitability: str
├── expected_difficulties: List[str]
├── solutions: List[str]
└── preparation_items: List[str]

AITrendDefinition
├── name: str
├── core_concept: str
├── practical_examples: List[str]
├── related_companies: List[str]
└── distinction: str (optional)
```

---

## 🎓 AI 트렌드

### 1. MCP (Model Context Protocol)
- **핵심 개념**: AI가 외부 도구나 데이터에 접근할 수 있게 도와주는 공통된 연결 방식
- **실생활 활용**: GPT, Gemini가 Canva, Suno 등의 도구에 접근
- **관련 기업**: Notion, Figma, Microsoft

### 2. AI Agent
- **핵심 개념**: 사용자의 목표를 이해하고 스스로 계획을 세우며 자율적으로 행동
- **실생활 활용**: 영화 추천 자동화, 의료 진단 보조
- **특징**: 어시스턴트와 달리 자율적 판단과 행동 수행

### 3. Sovereign AI
- **핵심 개념**: 국가가 AI의 모든 인프라(모델, 서버, 네트워크, 전력)를 직접 갖춤
- **실생활 활용**: 정부 데이터 접근 제어, 회사 인트라넷 관리
- **국가 사례**: 중국(AI 2030), 일본(정책 우선 투자), 인도(민관 협력)

### 4. RAG (Retrieval-Augmented Generation)
- 외부 데이터 소스에서 정보를 검색한 후 LLM이 응답 생성

### 5. Physical AI
- AI가 로봇이나 물리적 시스템을 통해 실제 세계에서 작동

### 6. A2A (Agent to Agent)
- 여러 AI Agent들이 서로 협력하여 복잡한 작업 수행

### 7. 소형 언어 모델
- 경량이지만 실용적인 성능을 제공하는 LLM

---

## 📝 Day 01 심화 과제: Sovereign AI

### 과제 정보
- **저자**: 이영기
- **선택 트렌드**: Sovereign AI
- **선택 형식**: 블로그 글 + 인포그래픽
- **제출 날짜**: 2024-01-15

### 선택 이유
1. **참신함**: 폐쇄성과 개방성의 공존이 특이함
2. **관심도**: 대중의 이해도를 높일 수 있는 주제
3. **관점**: 국가안보적 관점에서 중요성 강조
4. **접근**: 브런치 글과 인포그래픽으로 표현
5. **효율성**: AI 툴 사용으로 빠른 제작 가능

### 평가 기준
| 기준 | 점수 | 내용 |
|------|------|------|
| 관심도 | 5점 | 폐쇄성과 개방성의 공존 |
| 대중 이해도 | 높음 | 국가안보 관점 이해 용이 |
| 실생활 예시 | 높음 | 인트라넷, 정부24 등 |
| 콘텐츠 형식 | 블로그 + 인포 | 복합 형식 사용 |
| 제작 자신감 | 높음 | 기본 미션 기반 가능 |

### 블로그 콘텐츠

**제목**: "AI 시대의 주권: 디지털 식민주의와 소버린 AI"

**도입 (200자)**
```
누가 AI를 통제하는가?
```

**본론 (600자)**
- 디지털 식민주의 개념
- AI의 완전한 자주권: 모델 + 서버 + 네트워크 + 전력
- 국가별 사례: 중국, 일본, 인도

**결론 (200자)**
- AI 주권은 고립이 아닌 연결된 자립
- 개방형 주권 AI의 미래

**참고 자료**
- [기술 주권](https://www.technologyreview.kr/...)
- [소버린 AI란](https://banjjakpro.com/...)
- [국가 과학기술 계획](https://nsp.nanet.go.kr/...)

### 인포그래픽 콘텐츠

**제목**: 국가안보를 위한 소버린 AI의 필요성

**필수 요소 체크리스트**
- [x] 핵심 개념 (3줄 요약)
- [x] 작동 원리 (다이어그램)
- [x] 장점 3가지: 국가 안보 강화, 데이터 독립성, 기술 주권
- [x] 단점 2가지: 높은 비용, 기술 격차
- [x] 활용 기업: 중국, 일본, 인도
- [x] 미래 전망: 개방형 주권 AI 시대

**디자인**
- **색상**: 파랑 계열 (국가 안보 이미지)
- **구조**: 상단(개념) - 중단(사례) - 하단(전망)
- **강조**: 국가별 투자 규모 비교

---

## ⚠️ 저작권 공지

```
※ 저작권 주의
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은
운영 주체인 (주)업스테이지에게 귀속되어 있습니다.

콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매,
공개, 공유 등을 할 수 없습니다.

이 코드화된 버전은 개인의 학습 목적으로만 사용되어야 합니다.
```

---

## 🚀 확장 가능성

이 구조는 다음과 같이 확장할 수 있습니다:

```python
# 새로운 미션 추가
mission = Mission(
    day=2,
    step="Step 1",
    mission_type=MissionType.BASIC,
    author="이영기",
    content_proposal=new_proposal
)

# 데이터베이스 저장
# -> SQLAlchemy를 사용하여 데이터 영속화

# API 서버
# -> FastAPI를 사용하여 REST API 제공

# 웹 애플리케이션
# -> 웹 대시보드로 과제 추적 및 관리
```

---

## 📖 학습 목표

이 코드를 통해 다음을 학습할 수 있습니다:

1. **AI 트렌드 이해**: 현재 AI 기술 동향을 구조적으로 파악
2. **파이썬 데이터 구조**: Dataclass, Enum, 타입 힌팅 실습
3. **객체 지향 설계**: 리포지토리 패턴, 엔티티 설계
4. **교육 콘텐츠 관리**: 과제 시스템 구축의 기초

---

## 📞 문의

이 코드화된 버전에 대한 질문이나 개선 제안이 있으시면
학습 환경에서 직접 수정 및 확장할 수 있습니다.

---

**마지막 업데이트**: 2026-01-31  
**버전**: 1.0  
**상태**: 완성됨
