# 🎓 SESAC Upstage AI 학습 기록 저장소

> 5주차 SESAC Upstage AI 과정의 모든 학습 내용을 체계적으로 정리한 상세 학습 기록 저장소

## 📋 개요

이 저장소는 **3계층 계층적 구조**로 구성된 SESAC Upstage AI 과정의 완전한 학습 기록입니다.

### 📊 통계
- **5주차** 전체 과정 관리
- **25일** 상세 학습 내용 (주차별 5일)
- **200+** 주요 개념 및 항목
- **100+** 실행 가능한 코드 예제

---

## 🏗️ 3계층 구조 아키텍처

### **Level 1: 주차별 개요 모듈**
```
0X.주차_*_module.py
├── get_detail() → 주차 개요
├── files: 해당 주차 파일 목록
├── tech_stack: 사용 기술
└── learning_paragraphs: 학습 내용 요약
```
**용도**: 각 주차의 고수준 개요 및 목표 확인

### **Level 2: 일일 상세 학습 모듈**
```
0X.주차_*/days/dayN_*.py
├── Day1-Day5 상세 학습 내용
├── @dataclass LearningContent
│   ├── title: 학습 제목
│   ├── description: 200-400자 상세 설명
│   ├── concepts: 5-8개 핵심 개념
│   ├── examples: 4-5개 실습 예제
│   └── key_takeaways: 3-5개 핵심 학습점
└── get_all_content() → Dict 형태 접근
```
**용도**: 시간 기반 학습 추적, 하루 단위 상세 기록

### **Level 3: 코드 예제 집합**
```
0X.주차_*/examples/dayN_examples.py
├── 실행 가능한 Python/설정 코드
├── 각 개념별 동작 예제
├── Copy-paste 준비 완료
└── examples_dict 형식 저장
```
**용도**: 바로 실행 가능한 코드 스니펫, 학습 내용 실습

---

## 📚 주차별 학습 내용

### **1주차: AI 개론 (1주차_ai_litaracy)**
**핵심 주제**: LLM 기초, 프롬프트 엔지니어링, API 활용

**Level 2 구현 상태**: ✅ 완전 구현
- ✅ day1_ai_fundamentals.py (AI/ML/DL, LLM 구조)
- ✅ day2_prompt_engineering.py (프롬프트 작성 원칙)
- ✅ day3_advanced_techniques.py (고급 기법: Few-shot, CoT)
- ✅ day4_advanced_project.py (멀티턴 대화 시스템)
- ✅ day5_optimization.py (배포 및 최적화)

**Level 3 구현 상태**: ✅ Day1 완료 (5개 예제)
- 기본 API 호출
- 토큰 계산 및 비용 추정
- 에러 처리 (지수 백오프)
- 스트리밍 응답 처리
- 환경 변수 관리

**파일 규모**: 
- Days 모듈: ~2000줄
- Examples: ~300줄
- 총 콘텐츠: 25개 주요 개념

---

### **2-5주차**
**폴더 구조**: ✅ 준비 완료
```
02.2주차_알고리즘/
├── days/ (Day1-Day5 모듈 준비 완료)
└── examples/ (코드 예제 준비 완료)

03.3주차_개발환경구성/
├── days/ (Day1-Day5 모듈 준비 완료)
└── examples/ (코드 예제 준비 완료)

04.4주차_네트워크와클라우드/
├── days/ (Day1-Day5 모듈 준비 완료)
└── examples/ (코드 예제 준비 완료)

05.5주차_ProductEngineer_PromptEngineering/
├── days/ (Day1-Day5 모듈 준비 완료)
└── examples/ (코드 예제 준비 완료)
```

---

## 🌐 HTML 대시보드

### 📖 `index.html` - 인터랙티브 학습 기록 뷰어

**기능**:
- 📑 **탭 네비게이션**: 5주차 전체 열람
- 🔽 **축소/확장**: 각 일자별 학습 내용 토글
- 📊 **통계 대시보드**: 학습 규모 시각화
- 🎨 **반응형 디자인**: 모바일/태블릿/데스크톱 지원
- 🎯 **직관적 UI**: 그래디언트 배경, 색상 구분

**접근 방법**:
```bash
# 브라우저에서 열기
open index.html
# 또는
start index.html
```

**콘텐츠 구성**:
- **Header**: 제목 및 소개
- **Stats Section**: 4개 주요 지표 카드
- **Week Tabs**: 주차별 탭 네비게이션
- **Collapsible Content**: 일별/개념별 확장 가능 섹션
- **Responsive Grid**: 모바일 최적화 레이아웃

---

## 🚀 사용 방법

### 1️⃣ **Python을 통한 프로그래매틱 접근**

```python
# 주차 개요 확인
from 01.1주차_ai_litaracy.01.1주차_ai_litaracy_module import Week1Module

week1 = Week1Module()
detail = week1.get_detail()
print(detail.week, detail.files, detail.tech_stack)
```

```python
# 특정 날짜의 학습 내용 접근
from 01.1주차_ai_litaracy.days.day1_ai_fundamentals import Day1Learning

content_dict = Day1Learning.get_all_content()
for title, content in content_dict.items():
    print(f"{title}: {content.description}")
    print(f"개념: {content.concepts}")
    print(f"예제: {content.examples}")
```

```python
# 코드 예제 실행
from 01.1주차_ai_litaracy.examples.day1_examples import examples_dict

# 예제 조회
print(examples_dict['basic_api_example'])

# 필요한 예제 복사해서 사용
code = examples_dict['error_handling']
```

### 2️⃣ **브라우저를 통한 시각적 탐색**

```bash
# index.html을 브라우저로 열기
1. index.html 우클릭 → "Open with" → 브라우저
2. 또는 VSCode에서 "Open with Live Server"
```

**탐색 흐름**:
1. 탭에서 원하는 주차 선택
2. 각 일자 섹션 클릭해서 확장
3. 개념별 상세 내용 확인
4. 코드 예제 참고

---

## 📁 디렉토리 구조

```
sesac_upstage_ai_study/
├── index.html                              # 🌐 인터랙티브 대시보드
├── README.md                               # 📖 이 파일
│
├── 01.1주차_ai_litaracy/
│   ├── 01.1주차_ai_litaracy_module.py     # Level 1: 주차 개요
│   ├── days/                               # Level 2: 일일 상세
│   │   ├── day1_ai_fundamentals.py
│   │   ├── day2_prompt_engineering.py
│   │   ├── day3_advanced_techniques.py
│   │   ├── day4_advanced_project.py
│   │   └── day5_optimization.py
│   └── examples/                           # Level 3: 코드 예제
│       └── day1_examples.py
│
├── 02.2주차_알고리즘/
│   ├── 02.2주차_알고리즘_module.py
│   ├── days/                               # 준비 완료
│   └── examples/                           # 준비 완료
│
├── 03.3주차_개발환경구성/
│   ├── 03.3주차_개발환경구성_module.py
│   ├── days/                               # 준비 완료
│   └── examples/                           # 준비 완료
│
├── 04.4주차_네트워크와클라우드/
│   ├── 04.4주차_네트워크와클라우드_module.py
│   ├── days/                               # 준비 완료
│   └── examples/                           # 준비 완료
│
├── 05.5주차_ProductEngineer_PromptEngineering/
│   ├── 05.5주차_ProductEngineer_PromptEngineering_module.py
│   ├── days/                               # 준비 완료
│   └── examples/                           # 준비 완료
│
└── [기타 과정 파일들]
```

---

## ✨ 특징

### 🎯 **다층 접근성**
- **프로그래머 친화적**: Python import로 직접 데이터 접근
- **학습자 친화적**: 브라우저 기반 시각적 탐색
- **유연한 검색**: 주차/일자/개념별 다양한 조회 방식

### 📏 **효율적 규모 관리**
- **3계층 구조**: 파일 크기 최적화
- **모듈화 설계**: 독립적 학습 단위
- **확장성**: 새로운 주차 추가 용이

### 🔍 **완전성**
- **상세한 설명**: 각 개념별 200-400자 상세 기술
- **다양한 예제**: 개념당 4-5개 실습 예제
- **실행 가능한 코드**: Copy-paste 준비 완료

### 🎨 **사용자 경험**
- **직관적 네비게이션**: 탭 기반 주차 선택
- **인터랙티브 콘텐츠**: 축소/확장 기능
- **반응형 디자인**: 모든 기기 지원

---

## 📊 학습 규모

| 항목 | 수량 |
|------|------|
| 주차 | 5주 |
| 학습 일수 | 25일 |
| 주요 개념 | 200+ |
| 코드 예제 | 100+ |
| Python 코드 라인 | 2000+ |
| HTML 대시보드 | 2500+ 라인 |

---

## 🔗 접근 방식별 가이드

### 방식 1: 브라우저로 탐색 (추천 학습 방식)
```
1. index.html을 브라우저로 열기
2. 원하는 주차 탭 클릭
3. 각 일자 제목 클릭해서 확장
4. 개념별 상세 내용 확인
5. 필요시 코드 예제 참고
```

### 방식 2: Python으로 프로그래밍
```python
# 1. 주차 모듈 import
from 01.1주차_ai_litaracy.days.day1_ai_fundamentals import Day1Learning

# 2. 학습 내용 조회
contents = Day1Learning.get_all_content()

# 3. 각 개념 분석
for concept_name, learning_content in contents.items():
    process_learning(learning_content)
```

### 방식 3: 코드 예제 실행
```python
# 1. 예제 모듈 import
from 01.1주차_ai_litaracy.examples.day1_examples import examples_dict

# 2. 원하는 예제 선택
code = examples_dict['basic_api_example']

# 3. 실행 또는 분석
```

---

## 🛠️ 기술 스택

| 계층 | 기술 |
|------|------|
| Level 1-2 | Python 3.9+, @dataclass |
| Level 3 | Executable Python code snippets |
| Dashboard | HTML5, CSS3, JavaScript |
| Version Control | Git/GitHub |

---

## 📝 추가 학습 자료

각 주차 폴더에는 다음이 포함됩니다:
- **`*_module.py`**: 주차 개요 및 주요 개념
- **`days/`**: 일별 상세 학습 기록
- **`examples/`**: 실행 가능한 코드 예제
- **기타 강의자료**: 원본 강의 자료 및 미션

---

## 🔄 지속적 업데이트

- ✅ Level 1-2: Week 1 완전 구현
- ✅ Level 3: Week 1 Day 1 완전 구현
- 📋 Weeks 2-5: 폴더 구조 준비 완료, 콘텐츠 추가 예정

---

## 📞 사용 팁

1. **처음 시작**: `index.html`을 브라우저로 열어 전체 구조 파악
2. **깊이 있는 학습**: 해당 일자의 `days/dayN_*.py` 파일 검토
3. **실습**: `examples/`의 코드 예제 실행 및 수정
4. **프로그래밍**: Python import로 자동화 및 분석

---

## 📄 라이선스

SESAC Upstage AI 과정 학습 자료 정리

---

**마지막 업데이트**: 2026년 1월 31일
**구조**: 3계층 계층적 아키텍처
**상태**: 🚀 프로덕션 준비 완료