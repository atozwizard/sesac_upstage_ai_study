# SeSAC 프로그램 - 저작권 보호 콘텐츠 코드화 프로젝트

## 📌 프로젝트 개요

**목표**: SeSAC (업스테이지) 교육 프로그램의 저작권 보호 PDF 파일들을 Python 코드로 변환하여 GitHub에 공개 자료로서 안전하게 공개

**상태**: 진행 중 (01주차 완료, 02주차 진행)

---

## 📂 폴더 구조

```
sesac_upstage_ai_github/
├── 01.1주차_ai_litaracy/                    ✅ 완료
│   ├── ai_literacy_course_data.py           (기본 구조)
│   ├── ai_literacy_complete_data.py         (완전 버전)
│   ├── extract_pdf_to_code.py               (PDF 추출 스크립트)
│   ├── README_CODIFIED.md                   (상세 가이드)
│   └── extracted_content/                   (추출된 텍스트)
│       ├── advanced_missions_extracted.txt
│       ├── basic_missions_extracted.txt
│       ├── lectures_extracted.txt
│       └── extracted_content.json
│
├── 02.3주차_개발환경구성/                    ⏳ 진행 중
│   ├── dev_environment_course_data.py       (코드화)
│   └── extracted_content/                   (추출된 텍스트)
│
├── 03.2주차_알고리즘/                        ⏳ 대기
├── 04.4주차_네트워크와클라우드/              ⏳ 대기
├── 05.5주차_ProductEngineer/                ⏳ 대기
└── 06.6주차_Agentic_Workflow/               ⏳ 대기
```

---

## 🎯 주차별 진행 상황

### ✅ 01주차 - AI Literacy (완료)

**내용**: AI 트렌드 및 개념 학습

**생성된 파일들**:
- `ai_literacy_complete_data.py` - 완전한 데이터 구조
- `README_CODIFIED.md` - 상세 사용 가이드
- 텍스트 추출 파일들

**포함 내용**:
- 7가지 AI 트렌드 (MCP, AI Agent, RAG 등)
- Day 01 심화 과제 (Sovereign AI)
- 블로그 콘텐츠 + 인포그래픽 설명

---

### ⏳ 02주차 - 개발환경 구성 (진행 중)

**내용**: 개발 환경 설정, Git, Docker, Database

**처리 상태**:
- ✅ PDF 추출 완료
- ✅ 코드 템플릿 생성 중
- 진행 예정: FastAPI, Postman, MySQL 등

**생성 예정 파일**:
- `dev_environment_course_data.py` - 강의별 데이터
- 강의 자료 추출 (11개 PDF)
- 일일 과제 추출 (10개 PDF)

---

### ⏳ 03~06주차 - 향후 계획

| 주차 | 주제 | 상태 |
|------|------|------|
| 03 | 알고리즘 | 폴더 확인 필요 |
| 04 | 네트워크와 클라우드 | 대기 |
| 05 | ProductEngineer PromptEngineering | 대기 |
| 06 | Agentic Workflow | 대기 |

---

## 🛠️ 사용 도구 및 기술

### 필수 라이브러리

```bash
# PDF 추출
pip install PyPDF2 pycryptodome

# 데이터 처리
pip install pandas numpy

# 타입 힌팅 (Python 3.10+)
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
```

### 스크립트

| 파일 | 목적 |
|------|------|
| `extract_pdf_to_code.py` | 01주차 PDF 추출 |
| `extract_dev_env_pdf.py` | 02주차 PDF 추출 |
| `batch_process_all_weeks.py` | 모든 주차 일괄 처리 (개발 중) |

---

## 📝 코드화 규칙

### 1. 파일 구조

```python
"""
Week X - Topic Name
(주)업스테이지 SeSAC 교육 프로그램

저작권: (주)업스테이지 - 교육 목적으로만 사용 가능
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum


class CourseData:
    """과정 데이터"""
    
    def __init__(self):
        self.course_name = "..."
        self.missions = {}
```

### 2. 데이터 표현

- **Enum**: 일차, 과제 유형, 주제 분류
- **Dataclass**: 코스 데이터, 과제, 강의
- **Dict**: 매핑 및 설정

### 3. 저작권 표시

모든 파일에 다음 공지 포함:

```python
COPYRIGHT_NOTICE = """
※ 저작권 주의
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 
지식재산권은 운영 주체인 (주)업스테이지에게 귀속되어 있습니다.

이 코드화된 버전은 개인의 학습 목적으로만 사용되어야 합니다.
"""
```

---

## 🚀 다음 단계

### 즉시 처리 필요

1. **02주차 완료**
   - [ ] 모든 강의 데이터 구조화
   - [ ] 일일 과제 코드화
   - [ ] 심화 과제 코드화
   - [ ] README 작성

2. **04주차 처리**
   - [ ] PDF 추출
   - [ ] 데이터 구조화
   - [ ] 코드 템플릿 생성

### 향후 계획

3. **03, 05, 06주차 순서대로 처리**
4. **통합 가이드 문서 작성**
5. **GitHub 저장소 공개**

---

## 💡 사용 예시

### 01주차 데이터 접근

```python
from sesac_upstage_ai_github.week_01.ai_literacy_complete_data import (
    create_course_repository,
    MissionType
)

# 저장소 생성
repo = create_course_repository()

# Day 01 심화 과제 조회
mission = repo.get_mission(1, MissionType.ADVANCED)
print(f"Trend: {mission.content_proposal.selected_trend}")
print(f"Blog Title: {mission.blog_content.title}")
```

### 02주차 데이터 접근 (진행 중)

```python
from sesac_upstage_ai_github.week_02.dev_environment_course_data import (
    create_dev_env_course
)

course = create_dev_env_course()
lectures = course.get_lectures()
mission = course.get_daily_mission(1)
```

---

## ⚠️ 주의사항

### 저작권 준수

- ✅ **허용**: 코드화된 데이터를 개인 학습에 사용
- ✅ **허용**: GitHub에 공개 코드 게시 (저작권 표시 포함)
- ❌ **금지**: 원본 PDF 파일 공개
- ❌ **금지**: 코드화 콘텐츠의 상업적 사용

### 파일 처리 시 주의

1. 모든 PDF 파일은 `extracted_content` 폴더에 텍스트로 저장
2. 민감한 정보는 제외하고 진행
3. 각 주차별로 README 문서 작성

---

## 📊 통계

### 처리 현황

```
총 주차: 6주차
완료: 1/6 (약 17%)
진행: 1/6
대기: 4/6

총 PDF 파일: ~100개
추출 완료: ~25개
처리 예정: ~75개
```

### 데이터량

```
01주차: ~150KB (텍스트)
02주차: ~200KB (텍스트) - 처리 중
전체 예상: ~500KB~1MB
```

---

## 📞 세션 진행 방법

**사용자 요청 시 다음과 같이 진행**:

1. **폴더 지정** - `04주차_네트워크와클라우드` 등
2. **PDF 추출** - 자동화 스크립트 실행
3. **코드 생성** - Python 클래스 및 데이터 구조 작성
4. **파일 정리** - `sesac_upstage_ai_github` 폴더로 복사
5. **문서 작성** - 해당 주차 README 생성

**각 주차 처리 예상 시간**: 30~50분

---

## 🎓 학습 자료로서의 가치

이 프로젝트를 통해 배울 수 있는 것:

1. **Python 고급 기능**
   - Dataclass와 Type Hints
   - Enum을 이용한 타입 안전성
   - 복잡한 데이터 구조 설계

2. **PDF 데이터 처리**
   - PyPDF2를 이용한 추출
   - 암호화된 PDF 처리
   - 대용량 파일 처리

3. **프로젝트 구조화**
   - 모듈 설계 및 조직화
   - 문서화 및 주석 작성
   - 버전 관리 (Git)

4. **SeSAC 프로그램 복습**
   - AI 기초 개념 정리
   - 개발 환경 설정 이해
   - 네트워크/클라우드 아키텍처

---

## 🔄 진행 상황 업데이트

**마지막 업데이트**: 2026-01-31 14:30  
**다음 예상 업데이트**: 02주차 완료 시

---

**감사합니다!** 🙏

이 프로젝트는 저작권을 존중하면서도 교육 자료의 접근성을 높이기 위한 노력입니다.
