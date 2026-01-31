from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class WeekSummary:
    week: str = ""
    files: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)
    raw_texts: Dict[str, str] = field(default_factory=dict)

def get_summary() -> WeekSummary:
    s = WeekSummary(week="03.3주차_개발환경구성")
    s.files = ['(EXT) [SeSAC] [개발환경 구성] 코랩 세션_Wrap Up 리포트 (template)의 사본.pdf', '00.project\\.idea\\.gitignore', '00.project\\.idea\\00.project.iml', '00.project\\.idea\\inspectionProfiles\\profiles_settings.xml', '00.project\\.idea\\misc.xml', '00.project\\.idea\\modules.xml', '00.project\\.idea\\workspace.xml', '00.project\\IDE_study\\.idea\\.gitignore', '00.project\\IDE_study\\.idea\\IDE_study.iml', '00.project\\IDE_study\\.idea\\inspectionProfiles\\profiles_settings.xml', '00.project\\IDE_study\\.idea\\misc.xml', '00.project\\IDE_study\\.idea\\modules.xml', '00.project\\IDE_study\\.idea\\workspace.xml', '00.project\\IDE_study\\__pycache__\\main.cpython-314.pyc', '00.project\\IDE_study\\int', '00.project\\IDE_study\\main.py', '00.project\\IDE_study\\pyproject.toml', '00.project\\IDE_study\\uv.lock', '00.project\\backend\\.gitignore', '00.project\\backend\\.idea\\.gitignore', '00.project\\backend\\.idea\\backend.iml', '00.project\\backend\\.idea\\inspectionProfiles\\profiles_settings.xml', '00.project\\backend\\.idea\\misc.xml', '00.project\\backend\\.idea\\modules.xml', '00.project\\backend\\.idea\\vcs.xml', '00.project\\backend\\.idea\\workspace.xml', '00.project\\backend\\.python-version', '00.project\\backend\\README.md', '00.project\\backend\\main.py', '00.project\\backend\\pyproject.toml', '00.project\\backend\\requirements.txt', '00.project\\backend\\uv.lock', '00.project\\day5\\.gitignore', '00.project\\day5\\.python-version', '00.project\\day5\\.vscode\\settings.json', '00.project\\day5\\README.md', '00.project\\day5\\__pycache__\\database.cpython-314.pyc', '00.project\\day5\\__pycache__\\main.cpython-314.pyc', '00.project\\day5\\__pycache__\\models.cpython-314.pyc', '00.project\\day5\\__pycache__\\repository.cpython-314.pyc', '00.project\\day5\\__pycache__\\service.cpython-314.pyc', '00.project\\day5\\database.py', '00.project\\day5\\logs\\server.log', '00.project\\day5\\main.py', '00.project\\day5\\models.py', '00.project\\day5\\pyproject.toml', '00.project\\day5\\repository.py', '00.project\\day5\\service.py', '00.project\\fake_llm_project\\.gitignore', '00.project\\fake_llm_project\\.idea\\.gitignore', '00.project\\fake_llm_project\\.idea\\fake_llm_project.iml', '00.project\\fake_llm_project\\.idea\\inspectionProfiles\\profiles_settings.xml', '00.project\\fake_llm_project\\.idea\\misc.xml', '00.project\\fake_llm_project\\.idea\\modules.xml', '00.project\\fake_llm_project\\.idea\\vcs.xml', '00.project\\fake_llm_project\\.idea\\workspace.xml', '00.project\\fake_llm_project\\.python-version', '00.project\\fake_llm_project\\__pycache__\\agent.cpython-314.pyc', '00.project\\fake_llm_project\\__pycache__\\tools.cpython-314.pyc', '00.project\\fake_llm_project\\agent.py', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\.gitignore', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\README.md', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\agent.py', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\atozwizard\\README.md', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\atozwizard\\자기소개입니다. txt', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\main.py', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\tools.py', '00.project\\fake_llm_project\\backup\\fake-llm-agent-fork\\workflow.py', '00.project\\fake_llm_project\\main.py', '00.project\\fake_llm_project\\pyproject.toml', '00.project\\fake_llm_project\\readme.md', '00.project\\fake_llm_project\\tools.py', '00.project\\fake_llm_project\\workflow.py', '00.project\\main.py', '00.project\\nqn4iwin-practice\\.gitignore', '00.project\\nqn4iwin-practice\\atozwizard\\readme.md', '00.project\\nqn4iwin-practice\\atozwizard\\try_news_crawling.py', '00.project\\nqn4iwin-practice\\practice1\\calculator.py', '00.project\\nqn4iwin-practice\\practice1\\main.py', '00.project\\nqn4iwin-practice\\readme.md', '00.project\\retry\\test.txt', '00.project\\upstage-infra-project\\upstage-infra-project\\.gitignore', '00.project\\upstage-infra-project\\upstage-infra-project\\__pycache__\\connection_pool.cpython-314.pyc', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\__init__.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\api\\__init__.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\api\\model\\role.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\api\\routes\\__init__.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\api\\routes\\cli_route.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\core\\connection_pool.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\core\\db.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\repository\\__init__.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\repository\\chat_repository.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\repository\\user_repository.py', '00.project\\upstage-infra-project\\upstage-infra-project\\app\\service\\__init__.py', '00.project\\upstage-infra-project\\upstage-infra-project\\infra\\mysql\\docker-compose.yml', '00.project\\upstage-infra-project\\upstage-infra-project\\infra\\sql\\1-create-users.ddl', '00.project\\upstage-infra-project\\upstage-infra-project\\infra\\sql\\2-crud-users.ddl', '00.project\\upstage-infra-project\\upstage-infra-project\\infra\\sql\\3-select-users.ddl', '00.project\\upstage-infra-project\\upstage-infra-project\\infra\\sql\\4-create-conversations.ddl', '00.project\\upstage-infra-project\\upstage-infra-project\\infra\\sql\\5-bulkinsert-conversations.ddl', '00.project\\upstage-infra-project\\upstage-infra-project\\infra\\sql\\6-index-conversations.ddl', '00.project\\upstage-infra-project\\upstage-infra-project\\main.py', '00.project\\upstage-infra-project\\upstage-infra-project\\pyproject.toml', '00.project\\upstage-infra-project\\upstage-infra-project\\uv.lock', '01.강의자료\\00 Development Environment Course Introduction.pdf', '01.강의자료\\01 Creating a Developer Friendly Computer Environment.pdf', '01.강의자료\\02-Python Development Environment.pptx', '01.강의자료\\03 Git Basics.pdf', '01.강의자료\\04 Git Advanced.pdf', '01.강의자료\\05 GitHub for Collaboration.pdf', '01.강의자료\\06 Project Management and GitHub.pdf', '01.강의자료\\07 Docker Infrastructure and MySQL.pdf', '01.강의자료\\08 Understanding Databases and MySQL.pdf', '01.강의자료\\09 Managing MySQL on a Server.pdf', '01.강의자료\\10 Maintainable Architecture.pdf', '01.강의자료\\SeSAC_CS with AI_Guide.pdf', '02.daily mission\\[SeSAC] [개발환경 구성] basic mission_day01_answer의 사본.pdf', '02.daily mission\\[SeSAC] [개발환경 구성] basic mission_day02_answer의 사본.pdf', '02.daily mission\\[SeSAC] [개발환경 구성] basic mission_day03_answer의 사본.pdf', '02.daily mission\\[SeSAC] [개발환경 구성] basic mission_day04_answer의 사본.pdf', '02.daily mission\\[SeSAC] [개발환경 구성] basic mission_day05_answer의 사본.pdf', '03.3주차_개발환경구성_module.py', '03.advanced mission\\[SeSAC] [개발환경 구성] advanced mission_day01_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [개발환경 구성] advanced mission_day02_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [개발환경 구성] advanced mission_day03_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [개발환경 구성] advanced mission_day04_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [개발환경 구성] advanced mission_day05_answer의 사본.pdf', 'README_GENERATED.md', 'README_TECHSTACK.md', 'README_TECHSTACK_DRAFT.md', '__pycache__\\03.3주차_개발환경구성_module.cpython-313.pyc', 'extracted_content\\(EXT) [SeSAC] [개발환경 구성] 코랩 세션_Wrap Up 리포트 (template)의 사본.txt', 'extracted_content\\00 Development Environment Course Introduction.txt', 'extracted_content\\01 Creating a Developer Friendly Computer Environment.txt', 'extracted_content\\03 Git Basics.txt', 'extracted_content\\04 Git Advanced.txt', 'extracted_content\\05 GitHub for Collaboration.txt', 'extracted_content\\06 Project Management and GitHub.txt', 'extracted_content\\07 Docker Infrastructure and MySQL.txt', 'extracted_content\\08 Understanding Databases and MySQL.txt', 'extracted_content\\09 Managing MySQL on a Server.txt', 'extracted_content\\10 Maintainable Architecture.txt', 'extracted_content\\SeSAC_CS with AI_Guide.txt', 'extracted_content\\[SeSAC] [개발환경 구성] advanced mission_day01_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] advanced mission_day02_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] advanced mission_day03_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] advanced mission_day04_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] advanced mission_day05_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] basic mission_day01_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] basic mission_day02_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] basic mission_day03_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] basic mission_day04_answer의 사본.txt', 'extracted_content\\[SeSAC] [개발환경 구성] basic mission_day05_answer의 사본.txt', 'extracted_content\\advanced_missions_extracted.txt', 'extracted_content\\daily_missions_extracted.txt', 'extracted_content\\extracted_content.json', 'extracted_content\\lectures_extracted.txt']
    s.tech_stack = []
    s.raw_texts = {}
    s.raw_texts['(EXT) [SeSAC] [개발환경 구성] 코랩 세션_Wrap Up 리포트 (template)의 사본.txt'] = """ 
 
 
[
개발환경
 
구성
]
 
코랩세션
 
Wrap
 
Up
 
리포트
 
작성팀:
 
6조
 
이영기
 
Wrap
 
Up
 
리포트
 
작성
 
내용
 
1)
 
논의
 
주제
 
a)
 
보라색으로
 
작성된
 
주제는
 
예시
 
주제로,
 
팀
 
내
 
논의하고
 
싶은
 
주제가
 
있다면
 
해당
 
주제로
 
논의해주세요!
 
2)
 
팀원별
 
핵심
 
아이디어
 
3)
 
논의
 
과정
 
4)
 
최종
 
논의
 
결과
 
및
 
회고
 
 
공통
 
예시
 
주제
 
(Day
 
01
 
-
 
Day
 
05)
 
 
Day
 
01
 
코랩
 
세션
 
 
오늘
 
하루
 
동안
 
겪은
 
파란만장한
 
과정은
 
단순한
 
설치기가
 
아니라,
 
**'개발
 
환경의
 
두
 
세계(
Linux
와
 
Windows)
를
 
넘나든
 
모험기'**와
 
같습니다
 
 
초기
 
환경
 
구축:
 
WSL2
와
 
Warp
 
터미널)
 
오늘의
 
시작은
 
리눅스
 
기반
 
개발
 
환경
 
구축이었습니다.
 
윈도우
 
내부에
 
**WSL2(Ubuntu)**
를
 
설치하고,
 
이를
 
시각적으로
 
제어하기
 
위해
 
Warp
 
터미널
을
 
연동했습니다.
 
●
 
작업
 
내용:
 
Ubuntu
 
환경에서
 
uv
를
 
사용해
 
가상환경(
.venv
)을
 
생성하고,
 
FastAPI
와
 
Loguru
 
등
 
필수
 
패키지를
 
설치했습니다.
 
●
 
연동:
 
파이참(
PyCharm)
의
 
인터프리터를
 
WSL
 
내부의
 
파이썬
 
경로로
 
지정하여
 
개발
 
준비를
 
마쳤습니다.
 
2.
 
발생한
 
문제:
 
환경
 
혼선과
 
경로
 
에러
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
실습
 
진행
 
중,
 
윈도우
 
실행
 
파일과
 
리눅스
 
파일
 
시스템
 
간의
 
경로
 
충돌이
 
발생했습니다.
 
●
 
에러
 
상황:
 
파이참에서
 
윈도우
 
경로에
 
설치된
 
uv.exe
를
 
사용하여
 
리눅스
 
파일
 
시스템(
\\\\wsl$\\home\\...
)
 
내부의
 
프로젝트를
 
제어하려
 
시도했습니다.
 
●
 
결과:
 
CreateProcess
 
error=267,
 
디렉터리
 
이름이
 
올바르지
 
않습니다
라는
 
시스템
 
에러가
 
발생했습니다.
 
이는
 
윈도우
 
바이너리가
 
리눅스
 
네이티브
 
경로를
 
직접
 
실행할
 
수
 
없기
 
때문에
 
발생하는
 
전형적인
 
경로
 
매핑
 
문제입니다.
 
3.
 
환경
 
전환:
 
CMD
와
 
D
드라이브로의
 
이전\\
 
복잡한
 
경로
 
문제를
 
해결하기
 
위해,
 
개발
 
환경을
 
리눅스(
WSL)
에서
 
윈도우(
CMD)
로
 
완전히
 
이전하기로
 
결정했습니다.
 
●
 
데이터
 
이동:
 
프로젝트
 
파일을
 
윈도우
 
파일
 
시스템인
 
D
드라이브로
 
옮겼습니다.
 
●
 
환경
 
재구축:
 
기존
 
리눅스용으로
 
생성되었던
 
.venv
 
폴더는
 
윈도우의
 
python.exe
와
 
호환되지
 
않으므로,
 
uv
 
venv
 
명령을
 
통해
 
윈도우용
 
가상환경으로
 
대체(
Replace)
했습니다.
 
●
 
패키지
 
재설치:
 
윈도우
 
환경에
 
맞춰
 
uv
 
add
 
loguru
 
uvicorn
 
fastapi
를
 
실행하여
 
의존성
 
라이브러리를
 
다시
 
구성했습니다.
 
4.
 
로직
 
구현
 
및
 
로깅
 
적용
 
 
환경
 
구축
 
후,
 
FastAPI
를
 
활용한
 
피보나치
 
수열
 
API
 
코드를
 
작성했습니다.
 
●
 
Loguru
 
적용:
 
표준
 
print
 
문
 
대신
 
loguru
 
라이브러리를
 
도입했습니다.
 
계산
 
시작과
 
끝은
 
logger.info
로,
 
반복문
 
내부의
 
변수
 
변화는
 
logger.debug
로
 
기록하도록
 
설계했습니다.
 
●
 
목적:
 
프로그램
 
실행
 
흐름을
 
가시화하고,
 
추후
 
디버깅
 
시
 
각
 
단계의
 
상태
 
값을
 
추적하기
 
위함입니다.
 
5.
 
최종
 
실행
 
및
 
검증
 
 
가상환경을
 
활성화(
.venv\\Scripts\\activate
)한
 
뒤,
 
서버
 
엔진인
 
Uvicorn
을
 
사용하여
 
API
 
서버를
 
구동했습니다.
 
●
 
명령어:
 
uvicorn
 
main:app
 
--reload
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
●
 
트러블슈팅:
 
명령어
 
끝에
 
불필요한
 
기호(
:
)가
 
포함되어
 
옵션
 
인식
 
에러가
 
발생했으나,
 
이를
 
수정하여
 
정상
 
구동을
 
확인했습니다.
 
●
 
최종
 
확인:
 
브라우저에서
 
http://127.0.0.1:8000/fib/10
에
 
접속하여
 
JSON
 
응답값(
{\"value\":
 
55}
)을
 
수신했으며,
 
터미널을
 
통해
 
실시간으로
 
출력되는
 
로깅
 
데이터의
 
무결성을
 
검증하며
 
세션을
 
종료했습니다.
 
 
:
 
\"결국
 
오늘
 
과정의
 
핵심은
 
OS
 
환경에
 
맞는
 
정확한
 
인터프리터
 
경로
 
설정
과
 
가상환경의
 
독립성
 
확보
였습니다.
 
환경이
 
충돌할
 
때는
 
에러가
 
발생한
 
지점의
 
파일
 
시스템
 
권한과
 
경로를
 
먼저
 
확인하는
 
것이
 
가장
 
빠른
 
해결책임을
 
확인했습니다.\"
 
 
 
Day
 
02
 
코랩
 
세션
 
 
 
소스트리를
 
버리고
 
안전을
 
선택하다
 
1.
 
내가
 
겪은
 
문제점
 
(Pain
 
Points)
 
●
 
도구의
 
번잡함:
 
파이참과
 
소스트리를
 
오가는
 
과정의
 
플리커가가
 
흐름을
 
끊음.
 
●
 
시각화의
 
역설:
 
소스트리의
 
시각화된
 
브랜치
 
그래프가
 
오히려
 
현재
 
상태를
 
파악하는
 
데
 
복잡하게
 
느껴져
 
방해가
 
됨.
 
●
 
데이터
 
유실:
 
강의를
 
따라가며
 
Stash
와
 
Branch
를
 
활용했으나,
 
커밋되지
 
않은
 
상태에서
 
조작하다
 
코드가
 
날아가는
 
경험을
 
함.
 
2.
 
깨달은
 
핵심
 
원칙
 
(Safe
 
Workﬂow)
 
\"Stash
는
 
믿지
 
마라,
 
오직
 
Commit
만이
 
나를
 
구원한다.\"
 
●
 
Revert
 
>
 
Stash:
 
임시
 
저장이
 
필요할
 
때도
 
일단
 
커밋을
 
하고,
 
나중에
 
Revert
로
 
되돌리는
 
것이
 
훨씬
 
안전함.
 
기록(
Log)
이
 
남기
 
때문에
 
절대
 
데이터가
 
영구적으로
 
사라지지
 
않음.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
●
 
Conﬂict
는
 
정면
 
돌파:
 
<<<<<<<
,
 
=======
,
 
>>>>>>>
 
기호를
 
직접
 
보고
 
내가
 
원하는
 
코드를
 
남기는
 
과정이
 
가장
 
확실한
 
병합
 
방법임.
 
 
3.
 
나만의
 
미니멀
 
개발
 
셋팅
 
(VS
 
Code
 
All-in-One)
 
여러
 
앱을
 
띄우는
 
대신
 
VS
 
Code
 
하나에
 
강력한
 
확장
 
프로그램을
 
붙여
 
'경량화'
 
성공.
 
●
 
Git
 
Graph:
 
소스트리
 
없이도
 
필요한
 
만큼의
 
그래프만
 
확인.
 
●
 
Thunder
 
Client:
 
포스트맨
 
없이
 
가볍게
 
API
 
테스트.
 
●
 
Terminal
 
(CMD/Git
 
Bash):
 
마우스
 
클릭보다
 
정확한
 
명령어
 
제어.
 
 
4.
 
실습
 
복습:
 
충돌(
Conﬂict)
 
해결
 
시나리오
 
사용자님이
 
직접
 
경험한
 
**\"가장
 
매끄럽지
 
않았던
 
그
 
지점\"**을
 
공략하는
 
법입니다.
 
1.
 
상황:
 
main
과
 
feature
 
브랜치가
 
같은
 
줄을
 
수정함.
 
2.
 
현상:
 
머지
 
시
 
>>>>>>>
 
기호
 
발생.
 
3.
 
해결
 
전략:
 
○
 
Accept
 
Current:
 
내
 
코드만
 
남기기
 
○
 
Accept
 
Incoming:
 
상대
 
코드만
 
남기기
 
○
 
Accept
 
Both:
 
둘
 
다
 
남기기
 
(위아래
 
순서
 
조정)
 
4.
 
마무리:
 
기호
 
삭제
 
후
 
Save
 
->
 
Add
 
->
 
Commit
.
 
 
 
Day
 
03
 
코랩
 
세션
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
오늘의
 
실습
 
히스토리
 
(Summary)
 
1단계:
 
로컬
 
파일
 
정리
 
및
 
첫
 
커밋
 
●
 
작업
 
내용:
 
atozwizard
 
폴더
 
내의
 
.txt
 
파일들을
 
backup
 
폴더로
 
옮기고,
 
fork
 
폴더로
 
이동시키는
 
등
 
로컬
 
환경을
 
정리했습니다.
 
●
 
핵심
 
이슈:
 
\"커밋을
 
했는데
 
싱크(
Sync)
도
 
눌러야
 
하나?\"
 
●
 
해결:
 
**커밋(로컬
 
저장)**과
 
**싱크/푸시(서버
 
전송)**의
 
차이를
 
이해하고,
 
싱크를
 
눌러
 
GitHub
 
서버에
 
반영했습니다.
 
2단계:
 
원격
 
저장소
 
클론(
Clone)
 
및
 
로컬
 
환경
 
구축
 
●
 
작업
 
내용:
 
다른
 
수강생의
 
리포지토리를
 
Fork
한
 
후,
 
VS
 
Code
 
터미널에서
 
git
 
clone
 
명령어를
 
사용하여
 
내
 
컴퓨터로
 
프로젝트
 
전체를
 
내려받았습니다.
 
●
 
핵심
 
이슈:
 
VS
 
Code
 
터미널과
 
GUI
를
 
활용한
 
로컬
 
작업
 
환경
 
세팅.
 
●
 
해결:
 
명령
 
팔레트(
Ctrl+Shift+P
)와
 
터미널을
 
병행하며
 
프로젝트
 
구조를
 
잡았습니다.
 
3단계:
 
브랜치(
Branch)
 
생성
 
및
 
작업
 
분리
 
●
 
작업
 
내용:
 
main
 
브랜치가
 
아닌
 
개인
 
작업용
 
브랜치
 
atozwizard
를
 
생성했습니다.
 
●
 
핵심
 
이슈:
 
git
 
branch
 
명령어로
 
현재
 
내가
 
어느
 
브랜치에
 
있는지
 
확인하는
 
법을
 
익혔습니다.
 
●
 
해결:
 
atozwizard
 
브랜치에서
 
README.md
 
파일을
 
최상위
 
경로(
Root)
에
 
생성하여
 
독립적인
 
작업
 
공간을
 
확보했습니다.
 
4단계:
 
추적(
Add)
과
 
스테이징의
 
이해
 
●
 
작업
 
내용:
 
새로
 
만든
 
파일을
 
커밋하기
 
전
 
단계를
 
수행했습니다.
 
●
 
핵심
 
이슈:
 
\"커밋
 
전
 
git
 
add
를
 
왜
 
굳이
 
해야
 
하는가?\"
 
●
 
해결:
 
깃이
 
파일을
 
추적하도록
 
만드는
 
'검문소(
Staging
 
Area)'
의
 
개념을
 
이해하고,
 
VS
 
Code
의
 
+
 
버튼으로
 
스테이징
 
후
 
커밋/푸시를
 
완료했습니다.
 
5단계:
 
Pull
 
Request(PR)
와
 
협업
 
프로세스
 
●
 
작업
 
내용:
 
내가
 
수정한
 
내용을
 
원본
 
저장소(상대방의
 
develop
 
브랜치)에
 
합쳐달라고
 
요청했습니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
●
 
핵심
 
이슈:
 
\"내
 
리포에는
 
파일이
 
있는데
 
왜
 
상대방
 
리포엔
 
안
 
보일까?\",
 
\"PR
이
 
바로
 
적용된
 
건가?\"
 
●
 
해결:
 
*
 
PR
은
 
**'제안'**일
 
뿐이며,
 
상대방이
 
Merge(
병합)
 
버튼을
 
눌러야
 
최종
 
반영된다는
 
점을
 
깨달았습니다.
 
○
 
Open(
초록색
)
과
 
Merged(
보라색
)
 
상태
 
아이콘의
 
차이를
 
통해
 
진행
 
상황을
 
확인했습니다.
 
 
 
Day
 
04
 
코랩
 
세션
 
v
 
기술
 
회고
 
및
 
정리
 
 
1.
 
uv
의
 
정체와
 
핵심
 
가치
 
정의
:
 
Rust
로
 
작성된
 
초고속
 
파이썬
 
패키지
 
및
 
프로젝트
 
관리자입니다
.
 
 
통합
 
관리
:
 
기존의
 
pyenv(
버전
 
관리
),
 
pip(
설치
),
 
venv(
가상환경
),
 
poetry(
의존성
 
관리
)
 
기능을
 
하나로
 
합쳤습니다
.
 
 
압도적
 
속도
:
 
기존
 
도구
 
대비
 
10~100
배
 
빠르며
,
 
캐싱
 
메커니즘을
 
통해
 
중복
 
설치를
 
방지하고
 
디스크
 
용량을
 
효율적으로
 
사용합니다
.
 
 
2.
 
프로젝트
 
시작
 
및
 
VS
 
Code
 
연동
 
 
초기화
:
 
uv
 
init
 
명령어로
 
pyproject.toml
과
 
가상환경
(.
venv)
을
 
동시에
 
생성하며
 
프로젝트를
 
시작했습니다
.
 
 
인터프리터
 
설정
:
 
VS
 
Code
에서
 
Select
 
Interpreter
 
메뉴를
 
통해
 
프로젝트
 
내부의
 
./venv/Scripts/python.exe
를
 
선택하여
 
연동했습니다
.
 
 
자동
 
인식
:
 
폴더
 
내에
 
.venv
가
 
있으면
 
VS
 
Code
가
 
이를
 
자동으로
 
감지하여
 
환경을
 
제안한다는
 
점을
 
확인했습니다
.
 
 
3.
 
주요
 
명령어
 
및
 
활용
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
패키지
 
추가
:
 
uv
 
add
 
[
패키지명
]
을
 
통해
 
가상환경
 
설치와
 
pyproject.toml
 
기록을
 
한
 
번에
 
처리했습니다
.
 
 
실행
:
 
uv
 
run
 
[
파일명
]
을
 
사용하면
 
가상환경
 
활성화
 
여부와
 
상관없이
 
안전하게
 
코드를
 
실행할
 
수
 
있음을
 
배웠습니다
.
 
 
기존
 
프로젝트
 
전환
:
 
uv
 
add
 
-r
 
requirements.txt
 
명령어로
 
기존의
 
의존성
 
목록을
 
uv
 
체계로
 
빠르게
 
가져오는
 
방법을
 
익혔습니다
.
 
 
4.
 
환경
 
관리
 
및
 
최적화
 
(C
드라이브
 
관리
)
 
 
로컬
 
가상환경
:
 
아나콘다와
 
달리
 
가상환경이
 
프로젝트
 
폴더
 
내부에
 
위치하여
,
 
프로젝트
 
삭제
 
시
 
관련
 
용량도
 
깔끔하게
 
정리되는
 
구조임을
 
이해했습니다
.
 
 
캐시
 
정리
:
 
uv
 
cache
 
clean
 
명령어를
 
통해
 
빌드
 
및
 
다운로드
 
캐시를
 
정리하여
 
C
드라이브
 
용량을
 
확보하는
 
법을
 
확인했습니다
.
 
 
Docker
와의
 
시너지
:
 
uv
를
 
Docker
 
빌드
 
과정에
 
포함하면
 
빌드
 
속도를
 
획기적으로
 
줄일
 
수
 
있으며
,
 
이는
 
곧
 
인프라
 
리소스
 
절약으로
 
이어진다는
 
점을
 
파악했습니다
.
 
 
5.
 
아나콘다
(
Conda)
와의
 
비교
 
 
경량화
:
 
무거운
 
아나콘다
 
시스템
 
전체를
 
유지할
 
필요
 
없이
,
 
프로젝트별로
 
꼭
 
필요한
 
파이썬
 
버전과
 
패키지만
 
가볍게
 
유지할
 
수
 
있다는
 
점이
 
큰
 
장점임을
 
느꼈습니다
.
 
 
재현성
:
 
uv.lock
 
파일을
 
통해
 
협업
 
시
 
팀원
 
모두가
 
동일한
 
환경을
 
100%
 
재현할
 
수
 
있다는
 
점에서
 
현대적인
 
협업
 
방식에
 
더
 
적합함
 
 
Day
 
05
 
코랩
 
세션
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
●
 
ORM
 
(Object-Relational
 
Mapping):
 
파이썬
 
객체와
 
DB
 
테이블을
 
연결하는
 
기술입니다
.
 
●
 
DB
 
드라이버
:
 
mysql-connector-python
을
 
설치하여
 
파이썬이
 
MySQL
과
 
대화할
 
수
 
있는
 
통로를
 
만들었습니다
.
 
●
 
계정
 
권한
 
문제
:
 
Access
 
denied
 
for
 
user
 
'tester'
 
에러를
 
통해
 
MySQL
 
계정
 
생성
 
및
 
권한
 
부여
(
GRANT
)
의
 
중요성을
 
배웠습니다
.
 
 
 
●
 
Create
 
(POST):
 
사용자의
 
입력을
 
받아
 
INSERT
 
INTO
 
문으로
 
데이터를
 
저장하고
,
 
%s
를
 
사용해
 
보안
(
SQL
 
Injection
 
방지
)
을
 
챙겼습니다
.
 
●
 
Read
 
(GET):
 
SELECT
 
id,
 
content,
 
created_at
 
FROM
 
todo
 
문으로
 
전체
 
목록을
 
불러와
 
리스트
 
형태로
 
반환했습니다
.
 
●
 
Delete
 
(DELETE):
 
WHERE
 
id
 
=
 
%s
 
조건을
 
사용하여
 
특정
 
데이터만
 
안전하게
 
삭제하는
 
법을
 
익혔습니다
.
 
 
 
오늘
 
마주친
 
에러들은
 
개발자라면
 
평생
 
마주칠
 
'
피가
 
되고
 
살이
 
되는
'
 
경험입니다
.
 
에러
 
코드
 
의미
 
해결책
 
404
 
Not
 
Found
 
주소를
 
못
 
찾음
 
URL
 
스펠링
(
todos
)
 
및
 
서버
 
실행
 
확인
 
500
 
Internal
 
Error
 
코드
 
내부
 
오류
 
터미널
 
로그
 
확인
 
후
 
SQL
 
오타
 
및
 
컬럼명
 
수정
 
1045
 
(Access
 
Denied)
 
DB
 
접속
 
거부
 
유저
 
생성
(
tester
)
 
및
 
비번
/
권한
 
설정
 
Git
 
[rejected]
 
로컬
-
원
격
 
불일치
 
pull
 
--rebase
로
 
동기화
 
후
 
다시
 
push
 
 
4.
 
개발
 
환경
 
도구
 
활용
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
●
 
Uvicorn:
 
--reload
 
옵션으로
 
코드를
 
수정할
 
때마다
 
서버가
 
자동
 
재시작되도록
 
설정했습니다
.
 
●
 
Thunder
 
Client:
 
Postman
 
대신
 
VS
 
Code
 
내부에서
 
바로
 
API
를
 
테스트하는
 
법을
 
익혔습니다
.
 
●
 
Swagger
 
UI
 
(
/docs
):
 
FastAPI
가
 
자동으로
 
만들어주는
 
문서로
 
브라우저에서
 
직접
 
테스트를
 
수행했습니다
.
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['00 Development Environment Course Introduction.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3강사소개
[1] 각주표기시, 해당이미지혹은자료에위첨자로[숫자] 표기후, 하단에링크기재 -없을경우삭제: Noto Sans KR, 6pt서영학
엔씨소프트(18.01~24.12)
• AI연구→ 백엔드서버개발자
• 24.01~24.12 : 플랫폼센터계정플랫폼개발팀
• 23.01~23.12 :금융플랫폼개발팀
• 금융플랫폼개발
• 18.01~22.12 : AI 서비스개발실서버팀
• KBO AI 플랫폼개발
부트캠프강사
• upstage 새싹프로젝트CS  part (26.01~)
• 멋쟁이사자처럼백엔드단기심화4기(25.03~06)기타
• 23, 24년실전코딩Testing강의,
22년실전코딩백엔드강의(충남대)
• 대학교알고리즘동아리회장
• elice 카이스트머신러닝부트캠프(AI) 
최우수상
• 16년ACM-ICPC대전본선
블로그및깃헙
• inspire12.tistory.com
• github.com/inspire12
400 -00
수업의목표
수업진행방식
5수업목표: 프로그램이돌아가는환경이해와사용
다양한서비스개발에필요한개발환경
1. 개발에필요한IDE와Python 개발환경
2. Git 과Github 을통해코드버전관리에서개발자와협업, 기획자와협업까지확장
3. 파이썬백엔드와외부시스템(mysql, network) 을사용하고연동해보기
6수업전체목차
개발환경과 협업
1. 개발환경카테고리
2. Python 실행환경
3. 코드버전관리: Git 
4. 기능/작업흐름: Branch
5. 개발자협업: Github 
6. 프로젝트관리: Github project인프라
7. 컨테이너: Docker 
8. DB: MySQL 기본
9. DB + Python 
10. 유지보수를고려한아키텍처
7상황, 실습위주로생각
각실습코드를 기록
git 기반실습코드기록
직접작업해볼수도
만약수업흐름을놓쳐도
따라올수있도록인프라
7. 컨테이너: Docker 
8. DB: MySQL 기본
9. DB + Python 
10. 실제프로젝트에서는? 

8영화, 인사이드아웃중
좋은경험핵심기억
학교에서회사로
학생에서개발자로
9핵심기억으로만들어지는머리속섬

10수업목표: 사고의확장
상황기반으로 필요성인지하고
도구를배우고카테고리를 이해한다
내앞의있는컴퓨터(로컬)에서실행되는것 →외부서버에서실행되는것의차이
혼자하는개발 → 여럿이하는개발
Know How →Know Where
수업에서다루는내용이넓고다양한편이다.
사용하는기술에서시작해큰카테고리를이해하는수업과정
11수업피드백
1. 더알고싶은부분
2. 수업의난이도
3. 수업질문
4. 진행방향에대한피드백
온라인강의
-실시간은현장조교님
-궁금한점/ 과제진행어려움 /수업난이도/ 기타상담등 slack, 오픈카톡방활용https://open.kakao.com/o/gz1Jiq3h
개념/진행
중요페이지실습해보기

12수업전준비할것들
설치해야할 것
1. pycharm ( community / ultimate: 학생이메일무료)
2. python 설치(3.12 버전) 
-pyenv 를 통해버전별로설정하는걸추천
3. 네트워크요청도구: Postman
4. 터미널앱: iterm(mac) / warp
-windows의경우 wsl 설정을통한shell 설정
-패키지설치도구(apt: linux, brew: mac , scoop: windows)
구글설문링크공유와퀴즈공유5. git설치
6. source tree 설치
7. dockerdesktop 설치
"""
    s.raw_texts['01 Creating a Developer Friendly Computer Environment.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3목표: 개발도구세팅개발하기쉬운컴퓨터환경만들기
목차
Pycharm (IDE) 사용법
Pycharm 디버깅과세팅방법
다양한개발도구소개
401 -01
목표
-파이썬서버기본환경을세팅할수있다
-도구의카테고리를이해하고각도구를사용한다사용도구
•통합개발환경(Pycharm community / ultimate)
•터미널(iterm / warp / zsh )
•API 요청도구(Postman)
•docker (docker desktop)
•mysql 도구(data grip)
5개발환경의중요성개발하기쉬운컴퓨터환경만들기
개발환경은 왜중요할까? (기술적)
-어디가문제가생겼는지어떻게확인하고로직을따라갈수있을까?
-필요할때바로적용하기위해, 문제를빠르게확인하게위해
-좋은도구는코드파악이나해석을도와주고문제점을파악하기쉽다
6개발환경의중요성개발하기쉬운컴퓨터환경만들기
개발환경은 왜중요할까? (환경적)
장인은도구를탓하지않는다? 장인은도구를만들어쓴다
개발을하게되면컴퓨터앞에서12시간이상앉아서고민하는시간
보는환경이편하지않고, 예쁘지않으면그시간이고역이다
모든자료구조, 서비스사용목적= 사용을쉽게하려고
개발환경구축= 컴퓨터리소스를쉽게사용하기위해서도구의종류(카테고리)
칼이필요하다 → 상황에맞는다양한칼존재
하나의칼을잘쓰게되면나머지배우기쉬워진다
7도구의종류개발하기쉬운컴퓨터환경만들기
개발환경의 종류
OS
-windows, mac, android, linux, browser
IDE
-pycharm , visual studio
Shell
-Bash, zsh, Powershell
터미널
-warp, iterm
AI 
-IDE + Claude Code언어
-python (3.12) , java, c, c++, rust, go lang, js 등등
Python 실행환경
-uv, pip
API 호출(curl)
-Postman , insomnia
docker 
-docker desktop
mysql 도구
-data grip
801 -02
목표
-파이썬서버기본환경을세팅할수있다
-shell 개념을이해한다
-가상환경venv를이해한다사용도구
•통합개발환경(Pycharm community / ultimate)
9IDE: Pycharm (파이참) 알아보기개발하기쉬운컴퓨터환경만들기
Pycharm 이란? 
jetbrains 에서만든통합개발환경(editor)
(Integration Development Environment)
https://www.jetbrains.com/pycharm/
실습은pycharm community 로진행
학생이라면pro 버전1년단위구독으로무료사용이가능합니다. (학교이메일필수)
https://www.jetbrains.com/ko-kr/academy/student-pack/다른ide가있지만pycharm 쓰는이유
-자동완성과코드보조기능
-디버깅이쉽다
-프로젝트생성시자동으로가상환경생성
(ide 는취향과선택의영역: vs code 를쓰셔도무방합니다)

10예) pycharm 내부적으로문제점을잡아준다개발하기쉬운컴퓨터환경만들기: 실습

11IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
Pycharm 작업폴더
추천: ~/Documents/workspace/upstage-project/ 폴더안에서작업
File → new Project 

12IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
Pycharm 으로간단한 Python 스크립트 실행해 보기
피보나치수열을출력하는프로그램을만들어보세요

13IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
피보나치수열을출력하는프로그램

14IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
ide 가인식하는python 실행환경확인(인터프리터) –project 생성때만든가상환경.venv

15IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
Break Point

16IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
F8 : 스텝오버
17IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
F8 : 스텝오버 * 5

18IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
F8 : 스텝오버

19IDE: Pycharm 주요단축키정리개발하기쉬운컴퓨터환경만들기: 실습
이름 단축키 
선언또는사용위치로이동  ctrl+ B 
선언또는사용위치로이동  ctrl+ alt + B  
전체검색  shift + shift  
뒤로(탐색)  ctrl+ alt + ←  
이름변경  ctrl+ F6 
코드완성  ctrl + spacebar  
구현으로이동  ctrl+클릭 
변수선언자동  ctrl + shift + v  
오른쪽분할에서열기  shift + enter (패키지에서파일클릭후)  이름 단축키 
최근파일목록  ctrl+ E 
맥은다른 시스템 명령어 때문에 겹쳐서 안될수도  (ctrl space)
-시스템환경설정 → 키보드 → 단축키 → 서비스 탭
단축키팝업설정
20pycharm 의자동완성기능개발하기쉬운컴퓨터환경만들기: 실습
ctrl + space

21IDE: Pycharm 기타세팅개발하기쉬운컴퓨터환경만들기: 실습
탭위치(취향)
-저는탭을따로안쓰고project view 를연동해서씁니다. 
-내가연곳을자동으로선택하도록하는설정

2201 -03
사용도구
•터미널(iterm / warp / zsh )
•API 요청도구(Postman)
•docker (docker desktop)
•mysql 도구(data grip)
•git 
23Shell: Bash / 터미널실행하기개발하기쉬운컴퓨터환경만들기: 실습
Mac vs Windows
mac 은기본세팅
wsl 리눅스설정이필요
CUI (Command UI)
환경에익숙해지기

24터미널도구: Warp 알아보기개발하기쉬운컴퓨터환경만들기
Warp 이란? 
최근인기있는터미널도구
https://www.warp.dev

25(심화/취향) 터미널창이쁘게꾸미기개발하기쉬운컴퓨터환경만들기
https://inspire12.tistory.com/344못생긴windows Powershell 예쁘고쓸만하게만들기
iterm + ohmyzsh
https://salmonpack.tistory.com/52

26(심화) pycharm 에서terminal 실행하기개발하기쉬운컴퓨터환경만들기: 실습
아래terminal 에서 작업하는 경우

27Docker 관리도구: Docker desktop 개발하기쉬운컴퓨터환경만들기
Docker 와인프라
docker / docker-compose
Docker Desktop 을통한설치

28DB 관리도구: Datagrip개발하기쉬운컴퓨터환경만들기
Datagrip 이란?
DB 에접속해서데이터를확인하는도구
동일UI로다양한DB 접근가능
https://www.jetbrains.com/ko-kr/datagrip/

29Git 설치개발하기쉬운컴퓨터환경만들기
https://git-scm.com/install/windows
mac : brew install git 
linux : sudo apt install git 
30Git 설치개발하기쉬운컴퓨터환경만들기

31Git 설치개발하기쉬운컴퓨터환경만들기
프로젝트 폴더 내에서 우클릭 -추가 옵션 클릭
32API 테스트도구: Postman 알아보기개발하기쉬운컴퓨터환경만들기
데이터요청확인
HTTP 요청의 모든구성요소를 정확히 설정하고
테스트할 수있는환경을제공한다.
\"실제로사용자나 다른서비스가 우리서버에요청하는 방식그대로\" 요청을 재현
코드로만 확인하면
•요청 코드가 잘못된건지
•네트워크에 문제가 있는건지
•API 가 잘못된건지
알기 어렵다포스트맨 다운로드
[https://www.postman.com/downloads/
33HTTP API 만들기개발하기쉬운컴퓨터환경만들기

34diagram 그리기: excaildraw개발하기쉬운컴퓨터환경만들기
전체흐름과 순서파악, 아키텍처 설계그리기
https://excalidraw.com/

www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['03 Git Basics.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위
3오늘의목표: git 으로작업단위관리하기Git 
목차
git 설치와세팅
git 을사용하는이유
git init / add / commit
git commit 잘쓰는방법
source tree를통한시각화
4수업전설치및세팅Git 
준비사항
-Git 다운로드(일단default 값으로next)
-SourceTree 설치(계정skip)
-Github 계정생성
-Github API 키발급및등록
-예제코드: 
https://github.com/inspire12/fake-llm-agent

5Git 초기세팅(옵션)Git 
# 1. 사용자정보
git config --global user.name \"서영학\"
git config --global user.email \"your-email@example.com\"
# 2. 기본브랜치이름main으로
git config --global init.defaultBranch main
# 3. github token 키체인저장
git config --global credential.helper osxkeychain
# git config --global credential.helper manager-core
# 4. 색깔켜기(diff/log 보기편하게)
git config --global color.ui auto
# 5. 안전한줄바꿈설정(Mac/Linux 기준)
git config --global core.autocrlf input     # mac/Linux
git config --global core.autocrlf true      # Windows# 6. 에디터설정(VSCode 쓰면)
git config --global core.editor \"code --wait\"
# 7. pull 시rebase 대신merge (헷갈리면이게더무난)
git config --global pull.rebase false
# 8. log / diff 보기편하게pager 설정(뒤에추천도구delta 쓰면더좋음)
git config --global core.pager \"less -+F\"
코드링크
설정값저장위치
~/.gitconfig 파일에설정값적힘(global 설정)
.git/config (프로젝트별설정)
603 -01
왜다들Git Git 거릴까?
(로컬) 버전관리를위한Git
버전관리 → 프로젝트관리
7파일이름_최종_v3_최종최종.ppt  Git 
버전관리가 되지않으면..
-작업한파일을잃어버리기쉽다
-어떤파일이 최신인지 헷갈림
-내용이언제 어떻게바뀌었는지추적불가
-다른사람이수정하면 충돌발생& 해결불가
-이전버전으로되돌릴수없음
-협업자가파일을덮어쓰면복구불가
-파일이많아질수록관리어려움

8프로그래밍에선?Git 
파일이많아질수록 관리지옥
회사에선
-협업하는사람도많고
-작업하는파일도많아
-관리지옥

9Git 이란?Git 
Git은\"버전관리 도구\" = 프로젝트 전체성장기록, 타임머신
-Git은내가작성한파일이 어떻게변해왔는지 시간순서대로모두기록해준다.
-특정시점으로 되돌아갈수있다
-\"이부분 누가고쳤지?\" 도알수있다
Git 은버전관리 도구(VCS: Version Control System)

10Git 이란?Git 
Git은\"협업을위한표준도구\"
-개발자여러명이동시에작업해도 충돌을인지하고 안전하게합칠수있다
-어떤코드를언제작성했는지모두기록 되다
-다른사람의작업과내작업을 안전하게합칠수있다 .
-내코드가검토를(리뷰) 통해제품에나가는과정(배포와CI/CD)
1103 -02
12무슨프로젝트를진행할까?Git 
llm agent 기능만들기 (흉내내기)
요구사항
-사용자메시지입력처리
-기본응답생성
-Tool 실행결과반환
-오류처리
-로그출력
13무슨프로젝트를진행할까?Git 
일단기본프로젝트 진행
https://github.com/inspire12/fake-llm-agent/tree/start
내프로젝트
각파일만들고코드복사후세팅

14(실습) git 일단따라치기Git 
프로젝트 git 초기세팅/ 첫커밋하기
git init
git status 
git add main.py agent.py tools.py config.py 
git status 
git commit -m \"init: v1 기본LLM 에이전트\"
15git initGit 
git 저장소 초기화(세팅)
파이썬파일세팅후git 저장소생성
git init = 이폴더를Git이관리하도록만드는첫단계
git init 실행하면폴더안에.git이라는숨겨진디렉토리생긴다
.git 에Git이 메타데이터(변경사항)을저장
(코드추적-변경사항, 커밋-작업사항, 브랜치, 로그, 되돌리기정보등)
16git add Git 
Git 에변경을 커밋에 포함시키겠다고 체크하는단계
Git이변경사항을 추적할파일을지정하도록하는명령어
작업한변경을\"커밋후보영역\"에올림
커밋에포함할변경만선택적으로올림
17git 버전관리를위한코드추적Git 
코드변경추적
작업을하면
어떤코드의 변경사항을추적해야하는지 Git 에알려주는과정이필요하다
Git이코드를추적한다= 줄단위로\"어떤줄이추가·삭제·수정되었는지\"를기록
Git 은메타데이터(변경사항)을저장하는버전관리시스템
18git statusGit 
git 어떤파일을파일을추적하고 있는지 확인
Untracked → Git 모르는파일
Modiﬁed → 수정됨
Staged → add 완료
Clean → 변경없음

19.git 에특정파일이나폴더가들어가지않아야한다면?Git 
.gitignore
공유되면안되는파일은
ex) 
-API_KEY (비밀번호) 등
-ide (에디터) 사용하는파일.idea/* 
-개인개발환경설정파일 .venv/*
2003 -03
git 사용법
Commit 작성법
Commit 관리법
21변경이력= CommitGit 
git commit (커밋)
하나의commit 단위는기능이아니라목적
-하나의커밋은하나의의도를담는다
-제목은50자이내
-본문은왜수정했는지설명사용법
git add {파일명}
git commit
혹은
git commit -m \"커밋명\"
troubleshooting-
만약vi 에디터경험이없으시면
아래입력후vscode로수정
git config --global core.editor \"code --wait\"
22Commit 메시지작성방식Git 
git commit 작성형식
<type>(<optional scope>) : <subject>
<body -optional>
type: 변경의목적을나타내는키워드
scope (선택): 모듈/도메인/레이어(예: user, auth, api, core, docs 등)
subject: 한줄요약(명령형, 끝에마침표X)
body: 왜이변경을했는지, 중요한맥락/주의사항(필요할때만)
23(실습) 요구사항\"날씨기능추가\"Git 
일단따라치기
기능개발위해브랜치생성후기능추가및커밋
def get_weather (location ):
if location == \"서울\":
return \"맑음\"
return \"모름\"git switch -c feature/weather-tool
# 기능추가(코드로직추가)
# tools.py                              # agent.py
from tools import get_weather
class LlmAgent :
def handle(self, user, message ):
if \"날씨\" in message :
weather = get_weather( \"서울\")
return f\"{user}님, 서울날씨는 {weather }입니다.\"
return f\"{user}님, '{message }' 잘받았습니다.\"git add agent.py tools.py
git commit -m \"feat: 날씨기능추가\"

24변경이력은어떻게기록하면좋을까?Git 
git commit 작성원칙과전략
1. 하나의커밋 은하나의목적 만가져야한다(작고의미있게)
2.Subject(첫줄)는명령형+ 간결하게
3. 왜변경했는지기록하기(커밋메시지의본질)
Git commit 메시지의핵심은왜다.
코드는어떻게를보여주지만, 왜그렇게했는지는메시지가알려줌.
4. 한번에너무많은변경을커밋하지않기
파일20개이상바뀜. 500줄이상바뀜, 리팩토링+ 기능추가가섞여있음
→ 이런커밋은실제로리뷰불가능한커밋
25좋은commit 과나쁜commitGit 
나쁜Commit 예시
메시지예시
\"update\"
\"fix\"
\"수정\"
\"테스트\" / \"ㅋㅋ\" / \"임시\"
-어떤파일이, 왜, 어떻게바뀌었는지알수없다
-기능수정, 오타수정, 리팩토링이한커밋에섞여있다
-롤백할때어디까지되돌려야할지판단이어렵다좋은Commit 예시
메시지예시:
\"feat: add user login api\"
\"fix: handle null user in profile page\"
\"refactor: extract email validator from user service\"
\"chore: rename variable for clarity in auth controller\"
-커밋메시지만읽어도의도가파악된다
-기능/버그/리팩토링이분리되어있어롤백이쉽다
-한커밋이한가지목적만가진다
나쁜Commit은\"그순간은편하지만, 나중에모두에게빚이된다\"
좋은Commit은\"조금귀찮지만, 나와팀의시간을아껴준다\"
26하나의커밋은하나의목적만가져야하지만..Git 
현실적인 작업을 하며커밋을신경쓰기 어렵다
솔직히말하면, 좋은Commit 메시지작성은저도여전히어렵습니다
-기능개발중이라도수시로리팩토링이자연스럽게섞인다
-오타수정이나다른사람이짠코드의버그들이나잘못된컨벤센이보인다
-작업흐름이끊기는게싫어서커밋을미룬다
-처음시작할때전체설계를완전히이해하지못한상태에서작업할때가많다
-급한기능대응이나수정요청이중간에끼어든다
-팀의커밋문화에따라나도영향을받는다
-팀이커밋을지저분하게하면나도지저분해짐
27좋은커밋을쓰기위한실천팁Git 
현실적인 작업과정
리팩토링하거나오타고칠때 그순간바로커밋하지말고, 최소한기능개발이끝나기전에분리
기능개발중바꾼것들 섞였다고걱정하지말기-나중에분리하면됨
-git add -p 를활용해나중에라도분리하기
\"하나의commit 단위는기능이아니라목적\"이라고기억하기
28commit 전에넣을것들만지정하기Git 
git add -p 를통해commit 에넣을것만지정하기
git add -p
# y → 오타수정헝크만stage
# n → 디버깅코드hunk 건너뛰기
# s → 기능코드hunk를절반으로쪼개기
# e → 주석라인만골라서stage
hunk = Git이\"연속된변경라인을묶어서만든최소변경단위\"트러블슈팅)
git add –p (패치모드) 는git 이추적중인파일의
변경사항에서만가능하다
git add {file} 이후진행
29(실습) commit 전에넣을것들만지정하기Git 
실습순서
상황) 날씨응답문구변경중서버문제생겨debugging 용logging 코드추가필요해서추가
하나의파일에두개성향의수정이혼재된경우를가정
1. 같은파일수정후git add -p 로따로선택
2. 추가한코드따로커밋
-변경내역을고르는과정에서좋은코드에대한고민이생긴다
-커밋이구분되어있으면나중에작업을되돌리기쉽다

30(실습) commit 전에넣을것들만지정하기Git 
git add -p 를통해commit 에넣을것만지정하기
agent.py
-디버깅로깅작업
-날씨문구수정작업
두작업이혼재따로커밋을해보자
# 작업코드나눠서add 
git add -p agent.py
# print 부분은n
# prefix 부분은y
git commit -m \"feat: LLM 응답prefix 추가\"
git add agent.py
git commit -m \"feat: 디버깅코드추가\"
from tools import get_weather
class LlmAgent :
def handle(self, user, message ):
print(\"디버깅 중...\" )
if \"날씨\" in message :
weather = get_weather( \"서울\")
return f\"[LLM] {user}님, 서울 날씨는 {weather }입니다.\"
return f\"[LLM] {user}님, '{message }' 잘받았습니다.\"
3103 -04
Source tree 
변경사항을한눈에확인하며진행하기(직관성있게!)
32Git 이어려운이유Git
명령어도 중요하지만
상황과상황에맞는작업흐름이더중요✔상황이다양하고명령어연결과정이복잡
✔변경흐름이눈에안보임
✔추상적인개념이많다(meta data)
✔Git 개발자에게판단을요구
작업단위(커밋단위) 설계가필요
협업시규칙과충돌관리필요
✔되돌리는명령어가복잡
33Source treeGit 
\"Sourcetree: Git을 더쉽게, 더안전하게\"
Atlassian에서만든무료Git GUI 도구
시각적인diff 체크로변경내용을한눈에파악가능
hunk 단위, 라인단위로변경을클릭한번으로stage 가능
실수위험이줄어들고, commit 단위관리가쉬워짐
브랜치, merge, conflict도시각적으로표현되어부담이줄어듬

34Source treeGit 
https://www.sourcetreeapp.com
download & 설치
프로젝트세팅

35Source treeGit 
git add git status
git commit
36Source treeGit 
git log
git diff
git show
37참고사항Git 
vs code 익스텐션
-https://inpa.tistory.com/entry/VSCode- 💽-GIT-익스텐션-추천
git 명령어치트시트
-https://git-scm.com/cheat-sheet
-https://education.github.com/git-cheat-sheet-education.pdf
git 로드맵
-https://roadmap.sh/r/git--github-0ibs8
-https://maily.so/gitminam/posts/8do78n3prgq
38총정리Git 
git 은commit 을통한작업관리가 기본이자 핵심이다. 
-작업단위와 이력관리
-현실적인 작성법
git add -p / commit
-각명령어를 용도에 맞게사용하고
source tree
-git 도구를 통해더직관적으로 편하게git 을쓰자
-git 명령어를 알아야source tree도잘쓸수있다.
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['04 Git Advanced.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3오늘의목표: 작업되돌아가기Git 
목차
gitcheckout/switch를통한작업되돌아가기/이동하기
gitbranch를통한작업분리
merge협업과 conflict해결
404 –01
Git Branch 
merge / rebase
Git flow
5만약예전버전을사용해야한다면?Git 
현업에서 다양한 요구사항이 존재, 이전버전에서 작업을시작해야할 수도있다
‘무리한 요구를 하는 클라이언트 ’카카오톡 이모티콘
6만약예전버전을사용해야한다면?Git 
지금라이브 버전에 버그가 있어서 이전버전으로 서비스해야할 거같아요

7만약예전버전을사용해야한다면?Git 
하지만작업중에현실적으로
1. 커밋이 쌓이면 \"하던작업을 멈출수가없다\"
2. 예전버전과 지금버전사이의 변화등으로 현재작업이 영향이간다 (위험하다)
8git checkoutGit 
특정시점으로 코드를되돌릴때
-Git이저장한시점(commit)으로 이동
-이전커밋시점(snapshot) 이동가능
(잠깐) 다른작업으로 되돌릴 때현재작업이남아있을 때
만약커밋하지 않은파일이 있다면 되돌릴 때문제가 생길수있다

9git stashGit 
깃내부임시저장소
지금하던작업은미완성, commit하기엔너무지저분할때잠시옮겨놓는다
다른작업을해야하는데현재작업중인부분을커밋하기엔애매하고날리기도애매할때쓴다
checkout할때로컬에수정내용이남아있으면섞여서충돌날수있음
내부저장소에코드를잠시보관해남아있는변경이없는깨끗한상태로만들고 checkout하자

Source Tree 에서확인
10(실습) git stash 명령어, 사용법Git 
임시저장 하기
git stash 
메시지지정해서stash 생성
git stash save {메시지}
저장된변경목록보기
git stash list
가장최근저장된stash 보기
git stash show
다시꺼내오기stash 목록에서삭제
git stash pop
꺼내오지만목록에서는삭제하지않음
git stash apply
11git checkout 사용법정리Git 
git checkout
커밋해시로이동가능
git checkout <commit-hash>
브랜치이동
git checkout <브랜치>
새브랜치+ 이동
git checkout -b <브랜치>
파일되돌리기(옛날방식)
git checkout <커밋> --<파일>
12(실습) gitcheckoutGit 
코드를이전버전으로 되돌려보기
1. 두번째커밋hash값확인
2. gitcheckout(커밋hash값앞일부입력)
3. 코드변경과commitlog변경확인
Head 란? 
지금 작업 중인 곳 (현재 위치 )

13(실습) gitcheckoutGit 
코드를이전버전으로 되돌려보기
4. 실제코드로돌아가초기상태로변한코드를확인한다
이 때Detached HEAD 상태 발생
14(심화) Detached HEAD 란? Git 
HEAD는\"현재내가보고있는스냅샷\" 을가리키는데,
해시로체크아웃하면브랜치가아니라개별커밋을가리키게됩니다.
그래서\"Detached HEAD\"
→ \"브랜치에서떨어져있는상태\"
브랜치라는작업흐름내에서이동해야, 수정한내역을잃지않을수있다
이상태에서커밋하면브랜치와연결되지않아서
나중에찾기어려운고아커밋이생길수있어주의해야합니다.

1504 –02
git branch
16git branch Git 
작업흐름(줄기) / 작업에이름을붙인다
독립적으로 작업을 진행할 수있도록돕는작업흐름
마지막커밋을가리키는 포인터 (커밋흐름, 진행경로를 추적)
브랜치= 커밋흐름의 이름표
17Branch 없이개발하면생기는문제Git
브랜치가 없으면 되돌리기가 매우위험하다
•안정적으로 되돌릴 안전지점(safe point) 이없다.
•해시(hash) 기반으로 되돌리기는 어렵고실수하기 쉽다.
•잘못되면 작업물이 사라지거나 main을손상시킬 위험이크다.
18AI 시스템에서버전호환문제들Git
작업이많아지고 커밋이 많아질수록 생기는 문제점
AI 시스템에서 AI 모델별로적용할코드가다를수있다. 
실험이많아질수록 어떤버전 인지 알필요가있다
ex) 버전을가지고있어야하는 이유들
●현재서비스에 나가있는 모델+코드
●지금연구하고 있는모델+ 코드등버전별
●A/B테스트 등

19(실습) git checkout 과git branch Git 
코드를이전버전으로 되돌려보기
5. 추가작업을위해 branch 를생성
-hash 를통해이동하면 너무불편+ 추가작업위한바탕( branch)가필요하다
-Detached Head 해결
git branch develop

20git branch 이름은어떻게정해야할까?Git
브랜치이름기본규칙
1.형식: type/task-name(그룹형태)
a.복잡해지면area까지: type/ area/task-name (그룹형태)
2.단어는하이픈(-) 으로연결
3.공백, 대문자, 특수문자 ❌
4.이름만 보고 작업목적이 명확하게 보이도록
21git branch 이름은어떻게정해야할까?Git
브랜치종류(역할)에 따른prefix
feature —기능개발
-feature/user-profile
-feature/add-search-api
fix—버그수정
-fix/wrong-total-score
-fix/null-pointer-error
hotfix—운영긴급수정
-hotfix/payment-failure
refactor —구조개선
-refactor/split-preprocess-moduleexperiment —AI/ML 실험
-experiment/model-v2
-experiment/augmentation-test
docs—문서작업
-docs/update-api-spec
ci / infra —자동화& 인프라
-ci/add-github-actions
-infra/add-terraform-config
2204 –03
merge
conflict
23각자만든작업(branch)는어떻게합칠까?Git
gitmerge
두브랜치의작업내용을하나로합치는과정
gitconflict
두브랜치가같은파일의같은부분(hunk) 을수정했을때
Git은두개의코드가같은줄에있을때\"어느쪽이맞는지\" 결정불가
→ 개발자에게선택권을넘김
24Conflict 해결과정Git
Conflict는 \"오류\"가 아니다. Git이개발자에게 선택권을 넘긴것이다.
1. 두코드중어떤부분을살릴지결정
-내버전만살릴수도있음
-상대버전만살릴수도있음
-둘을합쳐새로운버전을만들수도있음
2. 충돌표시(<<<<<<<, =======, >>>>>>>) 제거
3. 수정된파일저장
4. 다시stage( gitadd) → commit(Merge커밋) 
25(실습) Conflict 파일Git
A 브랜치(현재) –B 브랜치(합칠 브랜치)
<<<<<<< HEAD
return f\"{user} 님,  '{message}' 를 잘 받았습니다 .\"
=======
return f\"{user} 님, 서울 날씨는 '{message}' 잘 받았습니다 .\"
>>>>>>> lecture/conflict-b
git switch start
git pull
uv sync
26(실습) git merge 와conflict 실습Git
git merge 와conflict
1. lecture/conflict-a branch 생성후agent.py 파일return 바꾸고커밋
2. lecture/conflict-b branch 생성후agent.py 파일return 바꾸고커밋
(1,2) 같은파일을
3. lecture/conflict-a 브랜치에lecture/conflict-b 브랜치를merge
4. conflict 발생
3. feature/embedding-service 에서develop 로합쳐보기

27(실습) git merge 와conflict 실습Git
git merge 와conflict
4. merge 실패conflict 상황

28Conflict 을줄이는방법Git
잦은Git conflict는 생산성과 코드안정성에 직접적으로 영향
작은단위로자주커밋하고자주푸시(Push/Pull) 하기
-Conflict의가장큰원인은 오래떨어져있던두타임라인이갑자기만날때 생김.
일정한merge 흐름
-브랜치의역할을나누고merge 하는브랜치를고정
기능단위로브랜치를짧게유지하기
-작업이길어질것같으면기능을분리
-브랜치는 3~5일안에 merge가목표
파일단위충돌위험을줄이기위한코드구조화(Clean code)
-Conflict는\"같은 파일의 같은 줄 \"이 바뀌어야 난다 .
→ 파일을 분리하면 conflict가 줄어든다 . 
29Conflict 을줄이는방법Git
잦은Git conflict는 생산성과 코드안정성에 직접적으로 영향
main/develop브랜치를더럽히지않기
-팀의중심브랜치(main/develop)가깨끗하면충돌도줄어듦.
-직접main에push금지
-PR 기반merge강제
-PR 템플릿으로커밋기준통일
merge전에미리차이(diff) 확인
-merge전에다음을통해conflict가능성을예측
컨벤션통일
-Prettier/ Black / ESLint등\"자동포매터\" 도입
-Conflict를많이만드는원인중하나는 줄바꿈, 들여쓰기, 공백, 포매팅차이
3004 -04
git flow
31Git branch 전략적으로사용하는방법Git
일관된 merge 흐름의필요성
conflict 는생산성을해친다= 개발자의의사결정을계속물어보게된다
역할과개발환경에맞는 일관된merge 흐름이필요하다
회사개발환경(사내개발환경/ 테스트환경/ 라이브환경)
32Git branch 전략Git flow Git
단순한브랜치전략을넘어개발의흐름을깔끔하게정리

33main  / develop 브랜치Git
배포하는 브랜치: main 
실제배포된 코드(production)
tag를통해실제배포된 버전들을 관리(정기/비정기인지)
메인배포인지 아니면서브배포인지
작업을합치는브랜치: develop
개발자들의 작업들을 합치는공간(중간단계개발통합) 
feature 브랜치들

34각자작업을진행하는브랜치Git
feature/, feat/
해야할작업이생김→ 이슈등록
develop 에서이슈에 대한feature 브랜치작성
이슈들에 대한처리

35QA, 테스트, 릴리즈직전작업Git
release
정기배포: QA, 문서화, 버그수정, 릴리즈노트
develop에서기능완료후분기
작업완료후main + develop 에머지+ Git Tag 추가
develop 에서바로main 으로가는게아니라중간단계에서
다듬는다.
개발초기단계, 라이브가없는단계에선굳이필요없습니다.

36(비정기) 배포하는브랜치: hotfix Git
main 에서바로분기해서 긴급수정브랜치
1. develop 에배포하면안될것들이있을경우
2. 운영중버그발견해서즉시수정필요
이럴때
main에서분기해서작업
완료후main + develop 모두병합
기존의작업을cherry pick 등으로
코드를(커밋)을가져다사용

37총정리Git 
Git작업흐름과되돌리기
branch필요성과 사용법/사례
-gitbranch각역할
merge/ conflict
-conflict해결법
-conflict를줄이는방법
Gitflow전략
-Gitflow를통한merge전략과 배포
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['05 GitHub for Collaboration.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3오늘의목표: Git 에서Github 확장Git 
목차
Git 에서Github으로확장,Github이해
github권한과github세팅
git clone, push, pull 등git과github기본기능다루기
fork, pull request,  코드리뷰, issue 등github기능다루기
405 -01
Git과Github 
Github 계정
Git repository 
Git remote 
Github push 
5혼자개발 → 여럿이하는개발( 회사)Github
개발자with 개발자
하나의프로젝트를같이개발하는순간어떤문제가생길까? 
다른사람의코드를어떻게가져올까?
•다른사람이만든코드를어떻게가져올까?
•내가만든코드를어떻게공유할까?
6개발자끼리코드를공유할중앙저장소(온라인) 필요Github
Github 이란?
로컬Git이연결되는온라인저장소
코드협업을위한 플랫폼(저장소에서기능이추가됨)
Git 저장소 를온라인에서관리
GitHub는세계최대 오픈소스 플랫폼
백업· 공유· 리뷰· 자동화제공
Git = 도구, GitHub = 서비스
팀개발의중심
오픈소스: 공개된협업프로젝트

7Git != Github Github
Git과Github 다르다, 둘간관계
Git = 버전관리도구(로컬)
GitHub = Git 저장소를호스팅하는온라인서비스
Git 없이는GitHub를사용할수없음
GitHub는협업· 리뷰· 공유· 자동화제공
Github 말고도 GitLab, Bitbucket 등다른서비스도존재

8Github 에서사용하는용어들Github
주요용어
✔remote = 원격저장소 주소
•\"어디로보낼까? 어디에서 가져올까?\"를 remote를통해판단
✔origin = 기본remote 이름
✔(Code) Repository(repo): 코드저장소= Github
✔Push / Pull: 업로드 / 다운로드
✔Fork: 다른저장소 내계정으로 복사(권한문제해결)
upstream = 원본저장소remote 이름
✔Pull Request(PR): 변경요청
✔Issue: 작업/버그 기록
✔Code Review: 변경검토과정

9Github 에서사용하는용어들Github
Git -Github 연결하는 용어
✔저장소 가져오기 → clone
GitHub 프로젝트를 내컴퓨터로 내려받는 명령
✔원격주소등록→ remote add
GitHub와연결하기 위해내Git에게
\"이주소가 GitHub 저장소야\" 라고지정
✔GitHub 에서프로젝트 복사→ fork
clone이“내컴퓨터로 복사”라면, fork는GitHub 계정으로 복사

10Push / PullGithub
원격저장소와 코드상태를 맞추는 작업
push = 내컴퓨터→ GitHub로코드를올린다
pull = GitHub → 내컴퓨터로코드를받아온다
push는업로드 , pull은다운로드+ merge 기능을동시에포함.
push 전에pull 을통해원격저장소와동기화를하고진행해야한다
실제현업/ 협업에서가장많이사용하는기능
11(실습) Github 계정생성하고저장소에내코드올리기Github
실습순서
github 사이트에서
1. Github 가입
2. Repository 생성
내프로젝트에서
3. git remote 설정
4. 코드push << 인증에러
5. api key 발급및로컬에등록
6. 코드push (main 브랜치)
7. branch push 실습
8. clone 으로올린프로젝트 코드받아보기
12(실습) Github 계정생성하고저장소에내코드올리기Github
실습진행
github 사이트에서
1. Github 가입 github.com →signup 
2. Repository 생성
GitHub에로그인→ New Repository 클릭→ 이름입력후Create
내프로젝트(llm agent)에서
3. git remote 설정
git remote add origingithub.com/{username}/fake-llm-agent
git remote -v # remote 확인
4. git push -u origin

13(실습)Github사용을위한key 발급받기Github
Github을 쓰기위해key 발급을해야한다
https://github.com/settings/tokens
note: 토큰이름등록
expiration: 30일
select scop: repo 선택
맨아래generation token

14Github 사용을위한key 저장하기Github
Github을 쓰기위해key 저장후사용
윈도우
git config --global credential.helpermanager-core
mac
git config --global credential.helperosxkeychain
15(실습) Github 계정생성하고저장소에내코드올리기Github
실습진행
6. 코드push(main 브랜치)
git push -u origin
7. branch push 실습
git checkout -b feature/login
git push -u origin feature/login
8. clone 으로올린프로젝트코드받아보기
git clone github.com/{username}/fake-llm-agent
1605 -02
repository 권한과 fork
Pull Request 
Review
오픈소스기여
17남의Repository(오픈소스)를수정하고싶어.. 하지만Github
Push 가거절되는이유= 내저장소가 아니니까
GitHub의대부분의저장소는내가직접push할수없다. (권한이없기때문)
권한(permission) 때문.  upstream(원본저장소)은관리자(Maintainer) 외에는push 허용X
그래서내버전으로개발을하고, 개발내용을공유하려면
-권한을요청해서받거나
-저장소를내계정으로복사(fork) 해야한다
아무나직접push하면프로젝트전체가피해를볼수있다.
→ PR을통해요청에대한 논의/검증단계를거쳐승인후merge 하는것이안전하다
18남의Repository(오픈소스)를수정하고싶어.. 하지만Github
https://opensource.guide/leadership-and-governance/오픈소스의 코드를 관리하는 사람들
-Contributor: PR로기여(push 권한없음)
-Committer: 특정브랜치에push 가능
-Maintainer: 프로젝트관리및merge 권한

19내수정을오픈소스에반영하고싶어Github
https://opensource.guide/leadership-and-governance/오픈소스의 코드를 관리하는 사람들
1. 나도오픈소스관리권한을받는다
2. 내가오픈소스를만든다
--현실적으로어렵다
3. 내가만든변경사항을보여주고, 의견을나누고, 승인되면, 상대가가져가반영한다
20Pull Request (PR)Github
원본프로젝트에 내가만든기능을 추가하고 싶어
pull (당겨가는걸) request(요청)
내가만든거너가당겨가서니프로젝트에넣을래? 
코드리뷰과정을통해PR에대해논의(리뷰)
리뷰어가추가로고쳐달라고요청할수있다. or 반려할수있다.
프로젝트담당자(메인테이너)의승인(Approve) 이후merge →코드에반영이된다
→ 배포후제품에반영
21(실습) githubpull requestGithub
실습순서
강사repo
1. 예제프로젝트github.com/inspire12/fake-llm-agent fork 
수강생repo
2. fork 로받은프로젝트github.com/ {자신의깃헙주소} /fake-llm-agent  확인
3. fork 로받은프로젝트 clone
Trouble shooting)
-이미clone 받은프로젝트가있으니 backup 폴더 를만들고
-backup 폴더에서clone 하자
22(실습) github pull requestGithub
실습순서
수강생repo
4. fork 코드에서수정작업(main 브랜치)
-아이디로폴더를하나만들고그안에자기소개.md  
-자기소개/ 이력서등을간단하게업로드
5. add, commit 후푸시
commit 명ex)
docs: {username} 자기소개입니다
6 push 후내코드가fork 된내repo 에반영되었는지 확인
23(실습) github pull requestGithub
실습순서
7. pull request 요청
-PR 이요청되면자연스럽게요청을받는쪽에PR 이생긴다
강사repo
8. 강사와코드리뷰후코드수정
-강사와간단한인사말진행후
9. merge 후코드적용확인
24(실습) github pull request Github
실습진행
fork 를한새프로젝트
받아서진행

25(실습) github pull request Github
실습진행
push 는main branch 

26(실습) github pull request Github
실습진행
PR

27Code ReviewGithub
프로젝트에 반영전충분한 논의/검증이 필요하다
•다른개발자가작성한코드를검토하는과정
•코드품질향상목적
•버그예방
•일관성유지
•팀커뮤니케이션강화
28(실습) pull request 내용기반으로Code Review 하기Github
실습진행
PR 날리기

29Code ReviewGithub
Single Comment (단일코멘트)
•PR의특정코드줄이나특정라인에남기는 임시메모/ 가벼운피드백 .
•Review로제출되지않음
•PR 작성자에게요청사항으로잡히지않음
•승인/변경요청같은상태변화없음
•해당댓글은리뷰프로세스를마무리하지않아도됨

30Code ReviewGithub
Code Review (Review)
•여러코멘트를묶어서하나의\"리뷰\"로제출됨
•Review 버튼을눌러야함
•Reviewer가어떤조치를요청하는지명확히전달됨
•PR에\"Approved / Request Changes / Comment\" 상태가기록됨
•팀프로세스에서공식적인승인절차로사용
 Comment: 의견남기고끝
Approve: \"이PR 합쳐도됩니다\"
Request Changes: \"이대로는Merge 불가, 수정필요\"
31Code Review 후변경사항반영하기Github
코드리뷰로 수정사항을받은후
PR 이올라간상태에서해당브랜치에
코드를수정해커밋이쌓이면PR에도자동으로쌓인다

32총정리Github
Github을통한협업
github개념 익히기
-저장소, 권한이슈
githubrepo 코드공유/ 사용하기
-clone, push, pull
github실제 협업해보기
-fork, pull request, Code Review
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['06 Project Management and GitHub.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3오늘의목표: 프로젝트를관리이해Github 
목차
프로젝트를만드는사람들
issue 와pull request
프로젝트관리도구이해
406 -01
혼자개발 → 여럿이하는개발( 회사)
버전관리 → 프로젝트관리
5혼자개발 → 여럿이하는개발( 회사)
https://yozm.wishket.com/magazine/detail/1455/기획자→ 개발자
지난시간에는개발자와개발자끼리의협업이라면
회사에는같이프로젝트를만드는다양한사람들이존재
프로그래밍을하기전에
무엇을만들지, 왜만들지, 언제까지만들지먼저정리되어야한다.Github 

6혼자개발 → 여럿이하는개발( 회사)Github 
개발자와 함께일하는사람들
•기획자(PO/Product Manager)
•디자이너
•QA
•사업팀
•때때로… CEO, 회사에서 개발자는 무엇을 코딩하게 될까
•기획자가새로운기능요구사항을올림
•디자이너가화면을업데이트함
•개발자A는백엔드API 개발
•개발자B는프론트화면개발
•QA는테스트일정조율
•PO는우선순위조정
706 -02
•해야할일, 일의할당
•Issue = Ticket
8프로젝트관리의시작은항상Issue다.Github 
Issue는\"해야할일\"을정의하는 가장단위
프로젝트는결국해야할일들의집합이다.
그러나\"무엇을해야하는지\"가명확하지않으면
개발은엉뚱한방향으로흘러간다.
Issue는해야할일을정의하고추적하는첫출발점이다.
9Issue가없다면?Github 
Issue 는일의중심
할일이말로만전달되고사라짐
우선순위가불명확
역할분담이애매해지고책임도흐려짐
어떤기능이완료됐는지, 어떤문제가열려있는지추적불가

10(실습) issue 등록해보기Github 
이슈만들어보기
만약상단바에code 다음에issue가보이지않는다면settings > features 에서 issue 활성화

11(실습) issue 등록해보기Github 
issue 특징

12(실습) issue 등록해보기Github 
이슈만들어보기
만약상단바에code 다음에issue가보이지않는다면settings > features 에서 issue 활성화

13Issue / PR 같이볼사람언급해보기Github 
@ 을통해유저언급해보기

14보냈던Pull Request에Issue 언급해보기Github 
#{이슈번호/PR번호}  ISSUE 단위로실제작업연동(PR) 
•PR과이슈는둘다# 으로호출가능

1506 -03
Github project
16프로젝트관리도구가없이일을하는경우Github 
기획자–개발자 협업의 혼란
•기능요청이슬랙·카톡·노션에흩어져있음
•누가어떤작업을하는지파악불가
•일정·우선순위가정리되지않음
•개발자는“무엇부터해야하나?”를매일질문
•기획자와개발자가서로다른정보로일함
기획과 개발정보가 한곳에 정리되지 않는다는 것
•코드보다커뮤니케이션으로시간을많이쓰게된다.
17프로젝트관리도구의기본기능Github 
작업정의/ 작업분해
\"우리가무엇을해야하는지목록을만드는것\"
큰기능을작은단위로쪼개기
모든팀원이이해할수있는형태로문서화
작업누락방지
진행상황/ 상태시각화
To Do → In Progress → Review → Done
작업흐름을한눈에확인
병목·지연구간즉시파악우선순위(Priority)와 일정(Milestone) 관리
어떤작업이더중요한지정의
스프린트/ 마일스톤/ 데드라인
리스크조기감지
18AI 와프로젝트관리도구의궁합Github 
https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/AI 에효율적인 업무지시
AI는정리된정보를기반 으로할때가장잘작동함:
-Issue에요약된요구사항
-Project 보드의작업상태
-우선순위, 마감일, 작업히스토리
-담당자와PR의연결관계
AI 코드리뷰, AI 코딩 등앞으로이런task 정의가더
중요해질것
19AI 와프로젝트관리도구의궁합Github 
https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/AI 코드리뷰서비스
코파일럿 / 코드레빗등등

20프로젝트관리도구종류Github 
통일된작업흐름을 도와주는 Tools
Jira, Notion, Trello, Linear 등등
Jira: 기업용대형프로젝트에강함
Notion: 문서기반의유연한협업
Trello: 간단한칸반방식
Linear: 빠른스타트업중심도구

21Github project 란?Github 
github project 의장점
•코드, 이슈, PR, 일정이 모두GitHub 안에서하나의흐름으로 이어진다.
•PR이나 Issue 연동
•+ 무료
실제강의만들때제작조교님과작업한프로젝트관리(github project) 

22github 알림Github 
github 에서 일어나는일들을알려준다
github 알림, 이메일등을설정한알림을받아볼수있다

23(실습) github project 생성하기Github 
github project 생성하기
1. https://github.com/users/{username}/projects
접속후create 
2. Kanban 선택
3. project 이름과우리가작업한repository 입력후Create Project
4. issue 생성
5. 담당자할당
6. PR 올리기

24(실습) github project 생성하기Github 
github project 생성하기
1. https://github.com/users/{username}/projects
접속후create 
2. Kanban 선택

25(실습) github project 생성하기Github 
github project 생성하기
3. project 이름과우리가작업한repository 입력후Create Project
개발진행과정을한눈에확인할수있다

26(실습) 기존issue 와github project 연동Github 
기존issue에서
project 오른쪽 톱니바퀴 클릭후

27총정리Github
Github 을통한프로젝트 관리
프로젝트 관리도구필요성
-프로젝트를 만드는사람들과 협업하는 방법
작업단위issue 
-issue 를통해문제제기와작업할당, PR 연동
github project 
-Kanban 보드 등을통해작업한눈에보기
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['07 Docker Infrastructure and MySQL.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3목표: Docker는편리하다Docker
목차
Docker 필요성
Docker 구성요소
Docker 사용법및실습
docker-compose 로mysql 켜기프로젝트 : https://github.com/inspire12/upstage-infra-project.git
4언어레벨에서문제 → 인프라수준에서문제Docker 
대부분문제는언어밖에서 발생한다
OS가서로다르다
Windows / macOS / Linux 환경차이로 동일코드가다르게동작함.
시스템 패키지가 다르다
libssl, libxml 등OS 레벨라이브러리 버전이 달라충돌발생.
외부서비스환경이다르다
MySQL, Redis가로컬에는 없거나, 버전/설정이 서버와 다름.
서버와 로컬의 OS 차이
서버(Ubuntu)와로컬(macOS)의 동작방식차이때문에문제재현이 어려움.
venv는“언어의존성”만 맞춰줄뿐,
실제문제는OS·시스템라이브러리·외부 서비스처럼 인프라레벨에서 발생한다.
507 -01
607 -01
Docker 란?

7(심화) 입문자가Docker 까지굳이알아야하나Docker 
왜내컴퓨터에선 안되는거야
입문자는환경문제로가장많이고생한다.
-설치과정도오래걸리고나중에처리도어려움
DB, 캐시, 메시지큐같은인프라를안전하게체험할수있다.
-초보자의성장속도를크게올려주는도구다.
팀프로젝트를하면환경차이가문제를만든다.
-Docker는개발환경을통일해개발을더쉽게만든다.

8Docker 이야기할것과이야기하지않을것Docker 
이야기할 것
다른사람의 세팅을가져다쓴다
(외부의존성, 인프라구성요소)
Docker 설치
Docker 이미지/ 컨테이너
-Docker 실행흐름
접속을위한Docker 네트워크
-host.internal.network
docker-compose 인프라구성
-mysql 실행해보기이야기하지 않을것
Dockerfile 작성
-내앱을컨테이너화
Docker 내부구조
-Docker overlay 구조
-namespace, cgroup 
-런타임구조
실제운영배포전략
-kubernetes, ci/cd
컨테이너네트워크심화
9Docker 이미지와컨테이너Docker 
설계도= 이미지, 실행환경 = 컨테이너, 실행= 애플리케이션
-이미지: 실행가능한앱의정적인 설계도(변하지않음)
-컨테이너: 이미지를메모리에띄운 실행인스턴스 (변할수있음)
이미지= 레시피, 컨테이너= 그걸로만든요리
10(심화) DockerfileDocker 
docker 이미지 생성을 위한명세서
애플리케이션 실행에 필요한 환경 구성 절차를
코드로 적어 놓은 설정 파일
개발자마다 환경이 달라도 항상 동일한 실행 환경을 만들 수 있음
서버와 로컬이 달라서 생기는 “동작 안 함 ” 문제를 근본적으로 해결
계층(Layer) 기반빌드→ 캐싱, 빠른재사용
Docker 실행흐름
•Dockerfile → docker build → docker 이미지생성
•docker 이미지→ docker run → 컨테이너생성및실행
11(실습) Docker desktop 설치Docker 
Docker 설치
https://docs.docker.com/desktop/setup/install/windows-install

12(실습) Docker desktop 설치Docker 

13(실습) Docker desktop 설치Docker 
docker --version
docker 명령어시Cannot connect 가뜬다면docker desktop 실행이안된상태
docker 자체적으로리소스를가져가는게많아서평소에는꺼놓고필요할때사용하는걸권장(로그인시켜지는옵션해제)
1407 -02
15Docker 아키텍처Docker 
Docker 구성요소와 명령어이어생각
Docker 이미지
실행가능한앱의\"설계도\" 또는\"템플릿\"
Docker 컨테이너
이미지가실제로실행된\"격리된박스\"
Dockerfile
설계도를만드는설명서
Docker Hub
이미지를올리고내려받는GitHub 같은저장소
Docker 데몬
Docker 컨테이너를관리하는\"운영체제속관리자\"
Docker CLI
Docker를제어하는\"터미널명령어\"
16Docker 명령어패턴Docker 
docker <대상> <행동> [옵션]
✔대상(Resource)
image
container
volume
network
system
(추가: plugin, context 등)✔행동(Action)
ls (목록조회)
rm (삭제)
prune (사용되지않는리소스정리)
inspect (정보조회)
logs (로그조회)
create / run / stop …✔docker 초창기구조화되기전패턴
docker ps
docker rm
docker rmi
docker images
docker run
예전명령어도정상동작
옵션확인
docker <대상> <행동> --help
17Docker 기본명령어정리Docker 
컨테이너 상태체크/ 컨테이너 생성/ 실행
✔Container 상태체크
docker container ls 
docker ps 
docker ps -a
✔Container 생성/ 실행/ 삭제
docker run / docker start
docker stop / docker rm 
✔docker 로그, 분석
docker log / docker inspect
✔docker hub (github 같은외부저장소)
docker pull / docker push✔Container 실행
docker run 
-d(백그라운드) 
--rm(컨테이너종료시컨테이너도삭제) 
--name (컨테이너이름지정)
✔Container 내부들어가보기
docker exec –it {pod 이름} bash
https://hub.docker.com

18nginx 란? (엔진엑스)Docker 
가벼운웹서버
웹서버, 역방향프록시, 로드밸런서, 캐시서버, HTTP 캐싱등
다양한기능을수행하는고성능오픈소스소프트웨어
비동기이벤트기반구조를사용하여적은자원으로
높은동시성(다수의연결동시처리)을제공하며, 특히대규모트래픽을처리하는데강점
실습에선
누군가브라우저로요청하면
HTML 와같은정적파일을그대로돌려주는역할
19(실습)Docker 기본명령어Docker 
웹서버nginx 이미지를 받아서사용해보자
1. nginx docker 이미지를받는다
2. nginx docker 이미지를컨테이너로띄워본다
3. nginx 접속확인
4. 컨테이너상태를확인
5. 컨테이너정보를확인
6. 컨테이너로그확인
6-1 컨테이너로그지속적으로확인
7. 컨테이너내부들어가보기
8. 컨테이너종료및삭제
20(실습) 이미지받고실행해보기Docker 
실습과정
1. nginx docker 이미지를받는다
docker image pull nginx
2. nginx docker 이미지를컨테이너로띄워본다// 만약8080 포트가있다면8081 등으로수정
docker container run -d   --name my-nginx   -p 8080:80nginx
3. nginx 를브라우저로접속확인해본다
localhost:8080
만약8080 port 로프로그램이켜있다면
-p 앞값을다른포트로ex) 18080:80

21(실습) 실행중인컨테이너확인하기Docker 
실습과정
4. 실행중인컨테이너확인하기
docker container ls
5. (심화) 컨테이너상세정보확인하기
docker container inspect my-nginx
6. 컨테이너로그확인
6-1. 컨테이너로그확인지속적으로확인(-f 옵션) 하면서브라우저접속해보기
→ 로그가들어오는것확인하기

22(실습) 실행중인컨테이너확인하기Docker 
실습과정
7. 컨테이너내부들어가보기
docker exec -it my-nginx bash
8. 컨테이너중지및삭제
docker container stop my-nginx
docker container rm my-nginx
8-1 이미지확인및삭제
docker image ls
docker image rm nginx
9. 삭제됐는지확인
docker container ls // docker ps 
docker image ls // docker images

23Docker 다른리소스Docker 
✔Docker Network
격리된컨테이너끼리혹은시스템과통신하기위한리소스
컨테이너는기본적으로서로분리된공간에서돌아가기때문에(자동연결되지않음)
이를연결할네트워크가필요
•포트매핑 -p 8080:80 
•컨테이너안에서호스트를가리키는주소 host.docker.internal 
✔Docker Volume
데이터는컨테이너밖에저장하기위한리소스
기본적으로수명이짧은실행환경이라서, 지우면데이터도같이사라진다. 
만약데이터가중요하다면데이터는컨테이너바깥에따로저장
2407 -03
Docker 복잡하고반복적인설정/명령어관리
25docker run 의단점Docker 
올릴docker 컨테이너가 너무많아+ 명령어옵션이너무많아
실제개발환경에서는보통컨테이너가1개가아니라여러개가필요
•웹서버(nginx 또는node 서버)
•데이터베이스(MySQL)
•캐시서버(Redis)
•메시지큐(Kafka)
•백엔드API 서버
컨테이너하나당매번docker run 명령으로직접쳐야하는것들
•이미지 이름
•포트 매핑
•환경변수
•볼륨
•네트워크 설정
26docker-compose 란?  Docker 
https://dev.to/waji97/docker-compose-management-1d84\"docker-compose.yml \" 파일로 컨테이너 설정을관리한다
여러개의docker run 설정을하나의파일(docker-compose.yml)로
관리해서한번에실행·정리할수있게해주는도구
•팀전체환경을하나의파일에서관리할수있어서공유가편함
•up / down 

#version: '3.8'         # docker-compose 의 버전 정의
services :    # 서비스(컨테이너) 정의
서비스이름 :        # 서비스 이름 (임의로 지정 가능 )
image: 이미지명
container_name : 컨테이너이름 (선택사항)
ports:
-\"호스트포트:컨테이너포트\"
volumes :
-\"호스트경로:컨테이너내부경로\"
environment :
환경변수명 : 값
networks :
-네트워크명
networks :    # 사용할 네트워크 정의
네트워크명 :
driver: bridge (기본값)
volumes :      # 사용할 볼륨 정의
볼륨명:
driver: local (기본값)
27docker-compose.yml 파일Docker 
https://dev.to/waji97/docker-compose-management-1d84services: 컨테이너 정의들
images: 무슨이미지를컨테이너로띄울지
container_name: 이름을직접지정
ports: docker network 와로컬네트워크의포트연결
8080:80
앞이내컴퓨터포트뒤가docker 컨테이너내포트
3306:3306
port는같지만두네트워크는다른곳
#version: '3.8'         # docker-compose 의 버전 정의
services :    # 서비스(컨테이너) 정의
서비스이름 :        # 서비스 이름 (임의로 지정 가능 )
image: 이미지명
container_name : 컨테이너이름 (선택사항)
ports:
-\"호스트포트:컨테이너포트\"
volumes :
-\"호스트경로:컨테이너내부경로\"
environment :
환경변수명 : 값
networks :
-네트워크명
networks :    # 사용할 네트워크 정의
네트워크명 :
driver: bridge (기본값)
volumes :      # 사용할 볼륨 정의
볼륨명:
driver: local (기본값)
28docker-compose.yml 파일Docker 
https://dev.to/waji97/docker-compose-management-1d84services: 컨테이너 정의들
volumes: 호스트와컨테이너간디렉토리공유
environment: 컨테이너환경변수설정(DB 초기설정등)
restart: 재시작정책(no, always, unless-stopped 등)
depends_on: 의존관계명시(기동순서기준, 의존성보장X)
29(실습) docker-compose 로mysql 실행해보기Docker 
실습순서
1. infra/mysql/docker-compose.yml 파일
2. docker-compose 실행
3. docker-compose 안에정의된서비스컨테이너확인
4. 실행된서비스접속
5. 실행된서비스로그확인
30(실습) docker-compose 로mysql 실행해보기Docker 
docker-compose.yml 예시파일

31(실습) docker-compose 로mysql 실행해보기Docker 
실습과정
1.infra/mysql/docker-compose.yml 파일
2. docker-compose 실행
docker-compose -d  up  
3. 실행된서비스컨테이너확인
docker-compose ps
4. 브라우저로접속
localhost:8080
4. 실행된서비스접속
docker-compose exec mysql bash
5. 실행된서비스로그확인 // mysql 자체log 가안찍히는버전
docker-compose  logs

3207 -04
docker network 
host.docker.internal
mysql 접속
33mysql 접속클라이언트Docker 
adminer
docker-compose 파일내에adminer 포함
웹기반간단한mysql 관리툴
접속정보도
docker-compose.yml 에적혀있음

34Trouble shooting) 이미MySQL 이깔려있다면?Docker
port 가겹쳐서오류가날수있다. 
services:
mysql:
image: mysql:8.0
ports:
-\"3306:3306\"
environment :
-MYSQL_ROOT_PASSWORD=password
-MYSQL_DATABASE=llmagent
-MYSQL_USER=tester
-MYSQL_PASSWORD=tester
adminer :
image: adminer
restart: always
ports:
-\"8081:8080\"ports: 
앞부분을
塪塪塧塭 → 塪塪塧塮 로
변경
35mysql 접속클라이언트Docker 
datagrip 으로접속하기
https://www.jetbrains.com/ko-kr/datagrip/

36docker compose 에두개이상서비스를띄운상황Docker 
Docker Network
패키지= 격리
docker 내부에있으면다소통될까?
도커컨테이너내부
로컬컴퓨터의네트워크
Port 포워딩
도커컨테이너내부로컬컴퓨터네트워크연결
host.docker.internal
도커내부에서로컬네트워크를가리키는예약어

37docker 쓰면인프라추가/ 삭제가깔끔하다Docker
docker 쓰는장점= 편하다
-인프라설정이어떻게작동하는지 테스트하기 좋다
만약수동설치였다면? 
-mysql 은컴퓨터 켜졌을 때자동으로 켜져서(백그라운드) 노트북의 리소스를 점유하고 있었을 수도
-설정이나 파일잘못건드렸다가 맨날메모리참조오류떠서고통받고있을수도
-삭제를해도설정파일이나 환경변수가 남아있어서 다음에 또설치했을 때문제가생길수도..
38docker 이미지/리소스삭제Docker
docker rm / rmi / prune 
docker ps -a
docker {컨테이너 id} rm 
docker images
docker {docker image 명} rmi 
# prune: 사용되지 않는(unused) 이미지자동정리
docker image prune  
docker image prune --filter \"dangling=true\"
docker system prune -a -f
39총정리Docker 
Docker 로인프라 설치를 대체
docker 아키텍처이해
docker 명령어
Docker-compose 로docker를더쉽게
docker-compose up /  down 
docker-compose 를통한인프라(외부의존성) 세팅
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['08 Understanding Databases and MySQL.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3목표: MySQL 사용익히기DB
목차
Docker 필요성과구성요소
docker-compose 로mysql 실행및접속
DDL 실습
DML 실습
Select 심화프로젝트 : https://github.com/inspire12/upstage-infra-project.git
408 -01
DB 개념
RDBMS와MySQL
query, table
5DB(데이터베이스)의필요성DB 
데이터가 관리가 되지않으면? 
데이터파일관리지옥
여러사람이 접근하는 데이터충돌
검색, 저장속도저하
백업/복원 어려움
6DB(데이터베이스)란?DB 
데이터를 구조적으로 저장·관리하는 시스템
데이터를 안전하게 저장하는 곳
빠르게찾기위한 도구
여러사용자가 동시에사 용가능
서비스의 기억저장소역할
7Excel과유사한DBDB 
https://yozm.wishket.com/magazine/detail/1721/DB 용어
데이터베이스 : 하나의\"DB\"는여러개의테이블을포함
테이블: 데이터를넣는큰표(시트)
-스키마: 테이블설계도
컬럼: 표의열, 속성
로우(row): 한줄의데이터
PK(Primary Key): 각줄을구분하는고유ID

8DB 의종류DB 
목적에따라다양한 DB
RDB (관계형데이터베이스)
•MySQL, PostgreSQL
•표(테이블)로구성, SQL사용
NoSQL, Document DB
•MongoDB 등, 문서형태
캐시DB (key-value)
•Redis
Graph DB

9SQL이란?: Structured Query LanguageDB 
DB에게무엇을 할지말해주는 '구조화된 쿼리=질의 언어'
RDBMS조작표준언어, 선언형 언어
'어떻게'가 아니라 '무엇을' 조회하거나 수정하고 싶은지를 선언적으로 표현합니다.
기본문법구조
동사(명령어) + 대상(table, column) + 조건
•SELECT: 조회
•INSERT: 추가
•UPDATE: 수정
•DELETE: 삭제
10SQL 의종류DB 
DDL: 데이터베이스의 \"구조\"를 정의하거나 변경하는 SQL 명령어
집을짓거나리모델링(설계도제작)
•Createdatabase / table / index
•Drop database / table / index
DML: 데이터베이스의 \"데이터\"를 추가, 조회, 수정, 삭제하는 SQL 명령어
•가구나물건을집안에넣거나빼는작업
•SELECT
•INSERT (Save) table
•UPDATE table
•DELETE table
DCL: 권한
TCL: 트랜잭션
11MySQL
RDBMS
query, table
Datagrip 으로DB 연결08 -02
12MySQLDB 
https://www.oracle.com/kr/mysql/what-is-mysql/MySQL 란?
데이터저장및관리에 사용되는 오픈소스관계형데이터베이스 관리시스템(RDBMS)입니다.
안정성, 성능, 확장성, 사용편의성 을 갖춘MySQL는개발자들에게 널리사용되는 중입니다
MySQL를 배워놓으면 PostgreSQL 이나Oracle 도빠르게습득
13MySQL 일단시작해보자DB 
Docker-compose 를통한MySQL 실행
git clone https://github.com/inspire12/upstage-infra-project.git
git fetch --all
git switch start
프로젝트내
infra/mysql/docker-compose.yml
cd infra/mysql
docker-compose up -d 

14docker-compose 파일에서접속정보확인하기DB 
MySQL 란?
host:  localhost
port: 3306
user: tester
password: tester
database: llmagentservices:
mysql:
image: mysql:8.0
ports:
-\"3306:3306\"
environment :
-MYSQL_ROOT_PASSWORD=password
-MYSQL_DATABASE=llmagent
-MYSQL_USER=tester
-MYSQL_PASSWORD=tester
adminer :
image: adminer
restart: always
ports:
-\"8081:8080\"
15datagrip 으로연결해보기DB 
datasource > 접속정보 입력

1608 -03
Data Definition Language
create database
create table
column 타입
primary key, auto increment
17요구사항: 프로젝트에유저기능을붙여보자DB 
User 데이터 저장할 테이블 설계
일단개인정보, 인증관련 생각없이진행
•User 가리키는id 는저장시자동생성
•name 필요
•가입날짜자동생성https://github.com/inspire12/upstage-infra-project
git switch feature/sql
git pull
infra/sql  
파일 참조 부탁드립니다
18database, table DB 
데이터를 저장할 틀이우선필요하다
CREATE DATABASE db명;
데이터베이스틀을만드는가장기본문법
CREATE TABLE 테이블명(컬럼정의…);
•테이블이름+ 컬럼목록을괄호안에선언합니다.
테이블을수정하는문법으로, ADD/MODIFY/DROP을활용
•ALTER TABLE 테이블명ADD 컬럼명타입;
•ALTER TABLE 테이블명MODIFY 컬럼명타입;
•ALTER TABLE 테이블명DROP 컬럼명;
아예구조자체를삭제합니다.
•DROP DATABASE db명;
•DROP TABLE 테이블명;
19database, table DB 
데이터베이스 생성및사용지정
테이블생성및사용지정
20Table 생성시고려할것들DB 
PK, 데이터선택
pk 설정필수
auto increment id 사용
데이터타입선택주의
default 값설정
not null 제약
unique 제약
index 생성기준pk 설정 필수 / auto increment id 사용
모든 테이블의 고유 식별자 , 반드시 있어야 성능 우위 , 일반적으로 정수
형Auto Increment 를 사용
21Table 생성시고려할것들DB 
데이터타입선택
타입을잘못선택하면인덱스효율이나빠지고, 불필요한저장공간을사용하고, 조회성능이떨어진다
•숫자데이터는 INT를기본으로쓰고, 사용자수나로그가매우많아질가능성이있으면 BIGINT
•문자는varchar(허용문자길이), 길이를정할수있으면길이지정, 성능과저장공간측면에서중요
•매우긴텍스트(예: 프롬프트, AI agent 로그)는 TEXT타입
•Boolean 값은MySQL에서는실제boolean 타입이tinyint(1)로처리
•날짜/시간정보는 DATETIME 이나TIMESTAMP 사용해야검색·정렬이정확
•가격, 포인트, 금액처럼계산정확도가필요한데이터는 DECIMAL
22Table 생성시고려할것들DB 
default 값설정
값이주어지지않았을때의기본값을지정해데이터일관성
not null 제약
비어있으면안되는중요한컬럼에반드시적용
unique 제약
이메일처럼중복되면안되는컬럼
index 생성기준
검색성능과직결, where 절에자주쓰는컬럼에만선택적으로설정추가옵션
2308 -04
Data Manipulation Language
CRUD 
-Insert
-Read (Select)
-Update
-Delete
24InsertDB 
새로운행(row)을테이블에 삽입
INSERT INTO 테이블명 (컬럼1, 컬럼2)
VALUES (값1, 값2);INSERT INTO users (name, email)
VALUES ('kim', 'kim@naver.com');
INSERT INTO users (name, email)
VALUES ('kim', 'kim@upstage.ai'),
('seo', 'seo@upstage.ai'),
('kim', 'kim12@upstage.ai');한 번에 여러 줄을 넣을 수도 있다
25SelectDB 
어떤데이터를 가져올지 선언하는 문법
SELECT 컬럼1, 컬럼2
FROM 테이블명
WHERE 조건SELECT id, name
FROM users
WHERE name = 'kim';
SELECT * FROM users
WHERE id >= 3;
SELECT * FROM users
WHERE age >= 20 AND age <= 30;
SELECT * FROM users
WHERE NOT (name = 'kim);
26UpdateDB 
기존데이터 수정
UPDATE 테이블명
SET 컬럼= 값
WHERE 조건;UPDATE users
SET name = 'lee'
WHERE id = 1;
SELECT * form 
WHERE id = 1;
UPDATE users SET name = 'lee' 
WHERE id = 1;조건(where)을 반드시 사용해야 안전
select 를 먼저 하고 변경하는 식으로 진행
27DeleteDB 
WHERE 조건없이delete 하면테이블전체데이터 삭제됨(주의)
DELETE FROM 테이블명
WHERE 조건;DELETE FROM users
WHERE id = 1;
조건(where)을 반드시 사용해야 안전
select 를 먼저 하고 변경하는 식으로 진행
SELECT * FROM users
WHERE id = 1;
DELETE FROM users
WHERE id = 1;
2808 -05
29범위검색DB 
기간/ prefix
기간검색(date)
부분검색 (prefix)SELECT * FROM users
WHERE created_at BETWEEN '2025-11-01' AND '2026-02-28';
SELECT *
FROM conversations
ORDER BY created_at DESC;
30비교조건DB 
정렬/ 개수제한
ORDER BY 컬럼ASC|DESC;
LIMIT 개수;SELECT *
FROM conversations
ORDER BY created_at DESC;
SELECT *
FROM conversations
ORDER BY created_at DESC
LIMIT 3;
3108 -06
인덱스
트랜잭션
32요구사항: 유저대화를저장해보자DB 
대화(conversations) 데이터 저장할 테이블 설계
1.어떤유저가 물어봤는지
2.최신대화를 알고싶다https://github.com/inspire12/upstage-infra-project
infra/sql  
안 쿼리 파일 참조

33DB(데이터베이스)란?DB 
데이터를 구조적으로 저장·관리하는 시스템
데이터를 안전하게 저장하는 곳
여러사용자가 동시에사 용가능
서비스의 기억저장소역할빠르게찾기위한 도구인덱스
34인덱스DB 
데이터를 빠르게 찾기위한정렬된 목차생성
검색속도를 위한목차생성
where 조건(검색) 컬럼에적용
insert update 시인덱스도 같이수정하게 된다

35인덱스사용법DB 
추가/ 제거/ 테이블생산시추가
CREATE INDEX 인덱스명
ON 테이블명 (컬럼1, 컬럼2, ...);
DROP INDEX 인덱스명CREATE INDEX idx_user_created
ON conversations (user_id, created_at);
DROP INDEX idx_user_created
ON conversations;

36(심화)정렬이되어있으면왜검색이빠르지? DB 
이진검색
기존탐색은 전체를 한번확인해야한다 O(n)
정렬이되면반으로 나누면서 검색할수있다O(log 2N)
MySQL은 기본적으론 PK 기준으로 정렬되며 저장
PK (Auto Increment) 를통한검색이 가장빠름
만약Auto Increment가아니라랜덤,분산값을 쓰면insert 속도가느릴수있다
(들어갈 위치를 매번찾게된다면)

37큰대화데이터에서인덱스유무로속도비교DB 
실습순서
1. conversations 인덱스제거
2. 큰데이터 입력 (속도가 오래걸릴수있어서 주의)
3. select 확인(+성능)
4. conversations 인덱스추가
5. select 확인(+성능)
38큰대화데이터에서인덱스유무로속도비교DB 
실습순서
1. conversations 인덱스제거
2. 큰데이터 입력(테스트를 위해프로시저 이용)
3. select 확인(+성능)
4. conversations 인덱스추가
5. select 확인(+성능)

39못다한DB 개념들DB 
알아야할 DB 개념
집계함수
mysql 함수
트랜잭션
조인
서브쿼리
실행계획
격리수준
등등
40총정리DB 
MySQL 사용법
DDL: 저장구조를정의하는 SQL
DML: 데이터조작을요청하는SQL
MySQL 에서CRUD 
Select 추가사용방법
검색성능을 위한index 
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['09 Managing MySQL on a Server.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3목표: Python으로DB 데이터를다루고서버로확장Python 서버와DB
목차
Python에서MySQL 다루기
커넥션풀
안전한저장을위한트랜잭션
409 -01
python 
MySQL 
Connection
5왜프로그램으로DB를다뤄야할까?Python 서버와DB 
사람이직접DB를사용하면?
사람이직접DB에들어가서
INSERT 하고SELECT 하는방식은
수동, 반복, 느림, 오류이라는문제
6왜프로그램으로DB를다뤄야할까?Python 서버와DB 
프로그래밍의장점= 반복, 데이터처리
데이터자동처리–대화저장, 로그기록, 통계계산을 코드로 자동화
대량데이터 처리가능–수천~수만 건을빠르게 처리
동시에여러요청처리–서비스환경에서 필수
반복되는 로직자동화–매번SQL을수동으로 칠필요없음
서비스내부로직과 연결가능–예: AI Agent의대화내역저장

7Python -DB 연결과정Python 서버와DB 
Python DB 연결과정과 용어
DB 드라이버(pymysql 등)
python 과mysql 연결통역기역할
connection
Python ↔ MySQL 서버사이통로
생성비용높음
cursor
SQL을보내고결과를받는도구(작업자)
8Python -DB 연결과정Python 서버와DB 
Python DB 연결과정과 용어
execute
문자열sql 실행
파라미터바인딩사용(%s)
fetchone / fetchall
select 결과조회
commit
데이터조작시(insert/update/delete) 반영
rollback
오류시되돌리기
close
커넥션/커서종료, 자원반환

9(실습) Python -DB 연결과정Python 서버와DB 
실습순서
Python이 MySQL과 대화하려면 드라이버가 필요
1.uv add pymysql로 설치
○uv add cryptography 도설치
○ .env 파일생성후db_user / db_password 입력
2.pymysql.connect(...)로 MySQL 서버에 연결(Connection)
3.conn.cursor()로 커서(Cursor) 생성
4.cursor.execute(\"SQL...\")로 쿼리실행
5.fetchone(), fetchall()로결과가져오기
6.Cursor 반납
7.마지막에 conn.close()로연결 종료
10DB 연결테스트Python 서버와DB 
import pymysql
def connection ():
conn = pymysql.connect(
host=\"localhost\" ,
port=3306,
user=\"tester\",
password =\"tester\",
database =\"llmagent\" ,
charset=\"utf8mb4\" ,
)
try:
with conn.cursor() as cursor:
cursor.execute( \"SELECT 1\" )
row = cursor.fetchone()
print(row)
finally:
conn.close()
if __name__ == '__main__' :
connection()git switch feature/crud/cr
git pull
uv sync
혹시 프로젝트 실행 시
RuntimeError: 'cryptography' package is required for 
sha256_password or caching_sha2_password auth 
methods ..
에러 발생시
uv add cryptography    실행해주세요
.env 파일 생성

1109 -02
python 
MySQL 
Connection
12실습을하기전팁Python 서버와DB 
브랜치별 실습코드분리
Sourcetree 에서전체작업을확인가능
fix/uvadd .. 
의존성초반추가..

13유저등록: Create = InsertPython 서버와DB 
실습과정def create_user (name: str, email: str):
conn = pymysql.connect(
host=\"localhost\" ,
port=3306,
user=\"root\",
password =\"password\" ,
database =\"llmagent\" ,
charset=\"utf8mb4\" ,
cursorclass =pymysql.cursors.DictCursor,
)
try:
with conn.cursor() as cursor:
sql = \"\"\"
INSERT INTO users (name, email)
VALUES (%s, %s) \\
\"\"\"
cursor.execute( sql, (name, email))
conn.commit()
finally:
conn.close()결과
git switch feature/crud/cr
git pull
uv sync
14유저등록: Read = SelectPython 서버와DB 
실습과정 결과def get_user_by_email (email: str):
conn = pymysql.connect(
host=\"localhost\" ,
port=3306,
user=\"root\",
password =\"password\" ,
database =\"llmagent\" ,
charset=\"utf8mb4\" ,
cursorclass =pymysql.cursors.DictCursor,
)
try:
with conn.cursor() as cursor:
sql = \"\"\"
SELECT id, name, email, created_at
FROM users
WHERE email = %s \\
\"\"\"
cursor.execute( sql, (email,))
return cursor.fetchone()
finally:
conn.close()
select 는
commit 필요없다
15잠깐! conn 부분이이렇게매번반복되잖아? Python 서버와DB 
요청마다 conn을새로만드는 방식은 매우비효율적
1.TCP 연결
1.MySQL 인증과정(user/password)
1.세션초기화
1.버퍼준비
매연결마다 반복
16connection poolPython 서버와DB 
connection 을미리만들고재사용하면 효율적이지 않을까?
프로그램 시작시conn 5 ~ 10개정도미리만들어둠
요청이 들어오면 풀에서 하나꺼내주고
작업완료되면 다시풀로돌려보냄(반납)
•conn 생성비용절감
•DB 서버부하감소
•병렬요청가능(멀티스레드/멀티 워커)
•안정적인 서비스 운영가능
17(실습) connection pool 개발Python 서버와DB 
실습순서
1. connection pool 클래스 생성
-순차적connection 배분을 위해queue 를생성
-connection pool 생성단계에서 정해진개수만큼connection 을만들고 저장
2. connection pool 생성시db 연결정보 전달
3. 연결요청시커넥션을 순차적으로 전달
-만약연결이 끊겼으면 재연결
5. connection으로db 작업수행후반환
18(실습) connection pool 개발Python 서버와DB 
실습과정
import pymysql
from queue import Queue
class PymysqlConnectionPool :
def __init__(self, maxsize =5, **db_params ):
self._pool = Queue( maxsize )
self._db_params = db_params
for _ in range(maxsize ):
self._pool.put( self._create_conn())
def _create_conn (self):
return pymysql.connect(
charset=\"utf8mb4\" ,
cursorclass =pymysql.cursors.DictCursor,
**self._db_params,
)def get_conn (self):
# 큐에서커넥션하나가져옴(없으면대기)
conn = self._pool.get()
# 혹시끊겨있으면재연결
try:
conn.ping(reconnect =True)
except Exception :
conn = self._create_conn()
return conn
def release_connection (self, conn):
# 풀에커넥션되돌려놓기
self._pool.put( conn)
def close_all (self):
# 프로그램종료시풀안의모든커넥션정리
while not self._pool.empty():
conn = self._pool.get()
conn.close()git switch feature/crud/connectionpool
git pull
uv sync
100 번을했을때
커넥션이유지가되나?

19(실습) connection pool 개발후반영Python 서버와DB 
실습과정
 실제데이터오는지확인
없다면저장했는지확인
20(실습) 유저등록: UpdatePython 서버와DB 
실습과정
결과
git switch feature/crud/ud
git pull
uv sync
main.py
1
 슬라이드 20
1  이 부분 텍스트가 강의 녹화시 강의자님께 가릴 것 같습니다 !
Gio Paik, 2025-12-10
21(실습) 유저등록: DeletePython 서버와DB 
실습과정
 main.py
결과

22(실습) 유저대화도마찬가지CRUDPython 서버와DB 
실습과정 :대화저장/ 최근대화목록조회git switch feature/crud/conversation
git pull
uv sync

2309 -03
데이터정합성을위한트랜잭션
원자성
24요구사항: 유저질문과에이전트응답을동시에저장해주세요Python 서버와DB 
두가지쿼리가 동시에 일어나는 경우
ex) 유저질문, 에이전트 응답이 쌍인데, 한쪽이저장이 안될경우ai 품질이상발견
한쪽이저장안되면차라리둘다저장안되게 해주세요
한쪽이 실패했을때둘다실패
25트랜잭션이란? Python 서버와DB 
https://rebro.kr/162DB의작업단위
여러작업을 하나의 단위로 묶는기능
Atomicity(원자성) —모두성공하거나(None) 모두실패
Consistency(일관성) —데이터무결성유지
Isolation(격리성) —다른트랜잭션 간간섭제거
Durability(지속성) —commit 후영구반영됨
26(실습) 두요청저장Python 서버와DB 
실습과정
둘다성공한경우
둘다저장됐는지 확인git switch feature/crud/transaction
git pull
uv sync
27두요청저장실패Python 서버와DB 
실습과정
한쪽만성공한 경우
둘다실패되는지 확인

28총정리Python 서버와DB 
Python 에서DB 연결과정
Connection Pool 의필요성
Transaction과 원자성Python 에서SQL 실행
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['10 Maintainable Architecture.txt'] = """SPEAKER
서영학© 2025 Upstage Co., Ltd.
2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위
3목표: 역할별로레이어를나누고DB를편하게쓰자계층형아키텍처와ORM
목차
역할별로나눈계층형아키텍처소개
mysql table과model의괴리: ORM
SQLAlchemy 사용법
4현상황진단계층형아키텍처
main.py 에모든로직이몰려있다
main.py 가너무비대해진다
•수정이 어렵다
•테스트 어렵다
•역할이 모호하다

510 -01
-역할에맞는레이어분리
-api layer -service layer -repository layer 책임분리
6현상황진단계층형아키텍처
https://www.codeit.kr/tutorials/194/mvc-pattern-and-layered-architecturemain.py 에로직을 역할별로생각
•실행하는 부분(요청받는부분)
•DB 연결만들기
•SQL 실행
•비즈니스 로직처리
•응답생성
7계층형(레이어드) 아키텍처구조계층형아키텍처
route / service / repository 구조로 책임을 분리
route
•요청받기
•입력검증
•service 호출
service
•비즈니스 로직
•트랜잭션 제어
•repository 호출repository
•db 접근
•sql 실행
•데이터 반환
core
•db 연결
•설정
8(실습) 레이어드아키텍처구조로변경계층형아키텍처
실습순서
1. 패키지구조먼저
2. main.py 에있는db 관련소스
(connection, connection_pool) core 로이전
3. main.py 안에있는db 쿼리호출repository chat/user로구분해서이동
4. main.py main 실행부분route/cli_routes.py 로이동
5. cli_routes.py 에서실행할service 파일chat/user 로구분해서생성
6. main 지우고cli_routes.py 를통해작업실행

9(실습) layer = 계층, 우선패키지구조부터잡자계층형아키텍처
실습과정
1. 패키지 구조먼저
app 폴더안에묶은이유
-애플리케이션코드를한곳
-프로젝트의실제동작로직(개발자가만든)이들어가는영역
•api (라우트)
•service (비즈니스로직)
•repository (DB 처리)
•core (환경, 설정)
•models (데이터구조)
git switch feature/layered/start
git pull
uv sync
10(실습) 레이어드아키텍처구조로변경계층형아키텍처
실습과정
2. main.py 에있는db 관련소스(connection, connection_pool) core 로이전
3. main.py 안에있는db 쿼리호출repository chat/user로구분해서 이동
git switch feature/layered/refactor
git pull
uv sync
11(실습) 레이어드아키텍처구조로변경계층형아키텍처
실습과정
4. main.py main 실행부분 route/cli_routes.py 로이동
5. cli_routes.py 에서실행할 service 파일chat/user 로구분해서 생성
6. main 지우고cli_routes.py 를통해작업실행
git switch feature/layered/complete
git pull
uv sync
12역할을분리하고계층화하여복잡도를낮춘다.계층형아키텍처
한레이어는 한가지책임에만 집중하게 하자
변경영향최소화: DB가바뀌어도 Service 로직은 그대로
테스트용이: Service를DB 없이도 단위테스트가능
읽기쉬운흐름: \"요청→ 서비스→ 저장소\"로 생각하기 쉬움
역할을분리하고 계층화하여 복잡도를 낮춘다.
안전성과 유지보수성을 높이기 위한설계철학기반.
각계층간명확한 책임분리(Separation of Concerns) 지향

1310 -02
table 과model
14코드에SQL 를그대로쓴다면? ORM
raw sql 반복증가
repository 복잡증가
필드추가시sql 수정 필요
유지보수비용증가
서비스성장대비어려움
table 을코드와매핑해볼수있을까?

15ORM 이란?ORM
객체지향프로그래밍 언어의객체와
관계형데이터베이스의 테이블을 자동으로 연결(Mapping)해주는 기술
SQL 대신객체중심의코드로데이터조작
코드의변경→ DB 변경스트레스최소화
16ORM이제공하는핵심기능ORM
ORM 을쓰면좋은점들
객체와테이블의매핑: 클래스↔ 테이블, 객체필드↔ 테이블컬럼연결자동화
CRUD 기능자동화: 생성(Create), 읽기(Read), 수정(Update), 삭제(Delete) 작업을객체중심으로제공
영속성관리(Persistence Context): 객체의상태(생성, 수정, 삭제)를추적하고DB에자동동기화
트랜잭션관리: 데이터의일관성보장(Transaction commit, rollback 자동관리)
객체지향쿼리지원: JPQL(자바), Django ORM(Python) 등객체중심의쿼리제공
17SQLAlchemy 이란?ORM
python 기반ORM 도구
개발자가SQL 쿼리문을직접작성하는대신, 파이썬객체지향코드를사용하여데이터베이스와상호작용
할수있도록도와준다
ORM 기능외에도, 파이썬코드로SQL 표현식을구성하고실행할수있는저수준(low-level) 기능을제공
다양한데이터베이스시스템(SQLite, PostgreSQL, MySQL, Oracle, Microsoft SQL Server 등)을지원
Session객체를통해데이터베이스연결을관리하고트랜잭션을효율적으로제어
18SQLAlchemy 구성요소: Engine ORM
Engine
데이터베이스와의실제연결을담당하는객체
커넥션풀관리
DB URL 기반생성
모든ORM 동작의출발점
19SQLAlchemy 구성요소: Session ORM
Session
ORM 작업단위(트랜잭션포함)
add / commit / rollback / query 실행
DB 연결을추상화한고수준API
20SQLAlchemy 구성요소: Base ModelORM
Base Model
ORM 테이블매핑의부모클래스
Column, Integer, String 등SQLAlchemy 타입정의
클래스= 테이블구조표현
21SQLAlchemy: ORM MappingORM
db 테이블→ 객체클래스 매핑

22SQLAlchemy 에서Model을통해쿼리요청하기ORM
CRUD
ORM에서 CRUD는SQL을직접쓰는대신Python 객체를추가·조회·수정·삭제하는방식
insert: session.add(model)
select: session.query(Model).filter().first() / all()
update: 객체수정후commit
delete: session.delete(instance) 후commit
23INSERTORM
INSERT
session = SessionLocal()
user = User(name=\"kim\", email=\"kim@test.com\")
session.add(user)
session.commit()        # 실제INSERT 발생
session.refresh(user)   # DB가생성한PK(id) 등최신값적용
24SELECTORM
SELECT
session = SessionLocal()
# 단일조회
user = session.query(User).filter(User.email == \"kim@test.com\").first()
# 여러개조회
users = session.query(User).all()
# 특정조건조회
users = session.query(User).filter(User.name == \"kim\").all()
25UPDATEORM
UPDATE
user = session.query(User).filter(User.id == 1).first()
user.name = \"lee\"     # 객체필드수정
session.commit()      # UPDATE SQL 자동실행
26DELETEORM
DELETE
user = session.query(User).filter(User.id == 1).first()
session.delete(user)
session.commit()
27(실습) sqlalchemy 로기존query를orm 으로변경ORM
실습순서
1. sqlalchemy 설치
2. sqlalchemy 연결, 기존connection 객체를sql_alchemy 객체로변경
3. user, conversation 테이블모델매핑
4. user, conversation  query 수정
5. serializer 를통해응답값수정

28(실습) sqlalchemy 로기존query를orm 으로변경ORM
실습순서
1. sqlalchemy 설치
uv add sqlalchemy
2. sqlalchemy 연결, 기존connection 객체를sql_alchemy 객체로변경(app/core/db.py)
3. user, conversation 테이블모델매핑
app/models/base.py
app/models/user.py
git switch feature/orm/conn
git pull
uv sync
29(실습) sqlalchemy 로기존query를orm 으로변경ORM
실습순서
4. user, conversation  query 수정git switch feature/orm/query
git pull
uv sync
app/repository/user_repository.py
305. serializer 를통해응답값수정ORM
실습과정
기존응답
json 형태( map/dict ) 로바꾸기위한라이브러리설치
uv add sqlalchemy-serializer
table 모델코드에반영
결과
git switch feature/orm/serializer
git pull
git sync
31총정리계층형아키텍처와ORM
역할에따라코드를 layer로나눌수있다
Route, Service, Repository
ORM 필요성과 SQLAlchemy 통해ORM 구현하기
Table과Model 연결(Mapping)
Model 을통해SQL 쿼리요청하기
ORM 은Repository의책임
32Complete
33개발환경수업총정리개발환경
개발환경개선
혼자하는 개발에서 여럿이
git commit, branch 
github
issue -pr -code review -mergeIDE, 개발도구들
uv, pyproject.toml외부의존성 다루기
docker 구성요소사용법
docker-compose
DB 을통한데이터 관리
SQL 사용법, Where 최적화
DB 연결관리앞으로 개발 속도 + 공부 속도를 높여줄 개발 환경 개선
유지보수를 위한리팩토링
코드책임에따른리팩토링
테이블과 객체 관계 ORM 
www.upstage.ai © 2025 Upstage Co., Ltd.

"""
    s.raw_texts['[SeSAC] [개발환경 구성] advanced mission_day01_answer의 사본.txt'] = """step
 
1.
 
피보나치
 
함수에
 
브레이크
 
포인트
 
찍기
 
 
 
 
Day
 
01
 
답안지
 
작성자:
 
이영기기
 
Step
 
1.
 
피보나치
 
함수에
 
브레이크
 
포인트
 
찍기
 
브레이크
 
포인트를
 
찍은
 
화면을
 
캡쳐하여
 
첨부해주세요.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
step
 
2.Evaluate
 
Expression
으로
 
직접
 
값
 
확인하기
 
 
 
 
 
Day
 
05
 
답안지
 
작성자:
 
이영기
 
Step
 
2.
 
Evaluate
 
Expression
으로
 
직접
 
값
 
확인하기
 
Evaluate
 
Expression
 
기능을
 
활용하여
 
값을
 
확인한
 
화면을
 
캡쳐하여
 
첨부합니다.
 
evaluate
 
expression
 
 
 
 
 
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
variables
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
watch
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] advanced mission_day02_answer의 사본.txt'] = """step
 
1.
 
git
 
log
를
 
통해
 
Head
 
Commit
 
파악하기
 
 
 
 
Day
 
02
 
답안지
 
작성자:
 
이영기
 
step
 
1.
 
git
 
log
를
 
통해
 
Head
 
Commit
 
파악하기
 
질문
 
답변하기
 
01.
 
HEAD
는
 
무엇을
 
가리키고
 
있나요?
 
main
 
02.
 
HEAD
 
이전
 
커밋으로
 
되돌아가면
 
어떤
 
변화가
 
발생할까요?
 
하던
 
내용이
 
날아갈
 
수
 
있다
 
03.
협업
 
환경에서
 
reset
 
대신
 
revert
가
 
필요한
 
이유는
 
무엇일까요?
 
모든
 
것을
 
커밋
,
 
기록시키니까
 
백업이
 
가능해진다
.
 
stash
에
 
임시저장하는
 
것보다
 
확실함
.
 
강의내용
 
따라가다가
 
여러번
 
날렸음
.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
step
 
2.
 
원하는
 
commit
을
 
git
 
revert
를
 
이용하여
 
롤백하기
 
 
 
 
 
Day
 
05
 
답안지
 
작성자:
 
이영기)
 
Step
 
2.
 
원하는
 
commit
을
 
git
 
revert
를
 
이용하여
 
롤백하기
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
 
지금까지
 
수행한
 
내용을
 
git
 
log
를
 
통해
 
스크린샷
 
캡처로
 
첨부하고,
 
 
https://github.com/atozwizard/fake_llm_project
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] advanced mission_day03_answer의 사본.txt'] = """Step
 
1.
 
조장
 
저장소
 
Fork
 
하기
 
 
 
 
Day
 
03
 
답안지
 
작성자:
 
이영기)
 
Step
 
1.
 
조장
 
저장소
 
Fork
 
하기
 
 
조장의
 
저장소를
 
Fork
후
 
캡처하여
 
Github
 
Repository
 
주소와함께
 
제출합니다..
 
https://github.com/atozwizard/nqn4iwin-practice
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
Step
 
2.Pull
 
Request
 
생성하기
 
 
 
 
Day
 
03
 
답안지
 
작성자:
 
이영기
 
Step
 
1.
 
Pull
 
Request
 
생성하기
 
변경사항을
 
작성
 
후
 
커밋합니다.
 
 
그
 
후
 
PR
을
 
생성하고
 
캡쳐하여
 
Github
 
Repository
 
주소와
 
함께
 
제출해주세요
 
https://github.com/nqn4iwin/practice/pull/3/commits/d18ea3d8e652aea40ea7be6f180cd32be
be82208
 
 
 
 
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] advanced mission_day04_answer의 사본.txt'] = """ 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
SQL
문제
 
해결하기
 
user_id
 
name
 
age
 
role
 
created_at
 
1
 
Kim
 
28
 
USER
 
2023-01-10
 
2
 
Lee
 
35
 
ADMIN
 
2022-11-30
 
3
 
Park
 
22
 
USER
 
2024-03-15
 
4
 
Choi
 
41
 
USER
 
2021-07-21
 
아래
 
조건을
 
만족하는
 
사용자의
 
 
이름(
name)
과
 
나이(
age)
 
조회하는
 
SQL
 
문을
 
작성하세요.
 
 
조회
 
조건
 
1.
 
나이가
 
30세
 
이상인
 
사용자
 
2.
 
역할(
role)
이
 
USER
인
 
사용자
 
3.
 
가입일(
created_at)
이
 
2022년
 
이후인
 
사용자
 
셀렉트
 
프롬
 
에이지>=30
 
셀렉트
 
프롬
 
롤
 
=
 
user
 
셀렉트
 
프롬
 
가입일
 
yyyy>=2022
 
SELECT
 
name,
 
age
 
FROM
 
users
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
WHERE
 
age
  
>=
 
30
 
AND
 
role
 
=
 
ʻUSER’
 
AND
 
created_at
 
>=
 
’2022-01-01’;
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] advanced mission_day05_answer의 사본.txt'] = """step
 
1.
 
3-Layered
 
Architecture
로
 
리팩토링
 
 
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
3-Layered
 
Architecture
로
 
리팩토링
 
3
 
Layered
 
Architeture
로
 
리펙토링한
 
프로젝트를
 
Github
에
 
올리고,
 
 
Repository
 
주소를
 
첨부해주세요
 
 
https://github.com/atozwizard/atozwizard.git
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
step
 
2.
 
SQLAlchemy
를
 
이용한
 
DB
 
접근
 
리팩토링
 
 
 
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
SQLAlchemy
를
 
이용한
 
DB
 
접근
 
리팩토링
 
SQL
 
Alchemy
로
 
리펙토링한
 
프로젝트를
 
Github
에
 
올리고,
 
 
Repository
 
주소를
 
첨부해주세요
 
https://github.com/atozwizard/atozwizard/tree/develop
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] basic mission_day01_answer의 사본.txt'] = """step
 
1.
 
UV
로
 
Fast
 
API
 
라이브러리
 
추가하기
 
 
 
 
Day
 
01
 
답안지
 
작성자:
 
이영기기
 
Step
 
1.
 
UV
로
 
Fast
 
API
 
라이브러리
 
추가하기
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
step
 
2.
 
Postman
으로
 
Get
 
요청을
 
통해
 
피보나치
 
함수
 
호출하기
 
 
 
 
 
Day
 
01
 
답안지
 
작성자:이영기기
 
Step
 
2.
 
Postman
으로
 
Get
 
요청을
 
통해
 
피보나치
 
함수
 
호출하기
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] basic mission_day02_answer의 사본.txt'] = """ 
 
 
Day
 
02
 
답안지
 
작성자:
 
이영기
 
Step
 
1.
 
마크다운
 
및
 
다양한
 
사이트를
 
이용하여
 
Github
 
ReadMe
 
꾸미기
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
Github
 
Repository
주소와,
 
ReadMe
 
스크린샷을
 
첨부합니다.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] basic mission_day03_answer의 사본.txt'] = """step
 
1.
 
저장소
 
클론
 
및
 
깃
 
브랜치
 
생성
 
 
 
 
Day
 
03
 
답안지
 
작성자:이영기
 
Step
 
1.
 
저장소
 
클론
 
및
 
깃
 
브랜치
 
생성
 
git
 
branch
를
 
이용하여
 
현재
 
어떤
 
브랜치들이
 
나열되어있는지
 
스크린샷으로
 
찍어
 
첨부합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
step
 
2.
 
Github
에서
 
PR
 
생성
 
및
 
Merge
 
 
 
 
 
Day
 
03
 
답안지
 
작성자:
 
이영기
 
Step
 
2.
 
Github
에서
 
PR
 
생성
 
및
 
Merge
 
https://github.com/atozwizard/fake-llm-agent-fork/tree/atozwizard
 
Github
에서
 
PR
이
 
생성되어있는
 
모습을
 
스크린샷으로
 
찍어
 
첨부
 
후,
 
MERGE
 
합니다.
 
git
 
repository
 
주소도
 
같이
 
첨부합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] basic mission_day04_answer의 사본.txt'] = """step
 
1.
 
Docker
로
 
MySQL
 
컨테이너
 
실행하기
 
 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
Docker
로
 
MySQL
 
컨테이너
 
실행하기
 
Docker
로
 
Mysql
를
 
실행하고,
 
docker
 
ps
 
명령어를
 
통해
 
 
Mysql
가
 
실행되고있는
 
모습을
 
캡처하여
 
첨부합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
step
 
2.
 
DataGrip
 
설치
 
및
 
MySQL
에
 
연결하기
 
 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
DataGrip
 
설치
 
및
 
MySQL
에
 
연결하기
 
Datagrip
을
 
설치하고,
 
MySQL
과
 
연결한
 
화면을
 
캡쳐하여
 
첨부합니다.
 
 
 
 

"""
    s.raw_texts['[SeSAC] [개발환경 구성] basic mission_day05_answer의 사본.txt'] = """step
 
1.
 
빈칸에
 
적절한
 
쿼리문
 
작성하기
 
 
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
빈칸에
 
적절한
 
쿼리문
 
작성하기
 
https://github.com/atozwizard/atozwizard
 
주어진
 
코드의
 
빈칸에
 
적절한
 
쿼리문을
 
작성
 
후
 
GitHub
에
 
올려
 
Repository
 
주소를
 
제출합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

 
step
 
2.
 
Postman
으로
 
정상동작
 
확인하기
 
 
 
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.Postman
으로
 
정상동작
 
확인하기
 
Postman
으로
 
API
요청
 
테스트를
 
통해
 
Todo
 
리스트
 
조회
 
및
 
삽입
 
결과를
 
캡쳐하여
 
첨부합니다.
 
또한
 
DB
에
 
데이터가
 
정상적으로
 
삽입되었는지
 
확인
 
후
 
결과를
 
캡쳐하여
 
첨부합니다.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 

"""
    s.raw_texts['advanced_missions_extracted.txt'] = """============================================================
ADVANCED_MISSIONS
============================================================


────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] advanced mission_day01_answer의 사본.pdf
문자 수: 1142
────────────────────────────────────────────────────────────

step
 
1.
 
피보나치
 
함수에
 
브레이크
 
포인트
 
찍기
  
 
 
Day
 
01
 
답안지
 
작성자:
 
이영기기
 
Step
 
1.
 
피보나치
 
함수에
 
브레이크
 
포인트
 
찍기
 
브레이크
 
포인트를
 
찍은
 
화면을
 
캡쳐하여
 
첨부해주세요.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
step
 
2.Evaluate
 
Expression
으로
 
직접
 
값
 
확인하기
 
  
 
 
Day
 
05
 
답안지
 
작성자:
 
이영기
 
Step
 
2.
 
Evaluate
 
Expression
으로
 
직접
 
값
 
확인하기
 
Evaluate
 
Expression
 
기능을
 
활용하여
 
값을
 
확인한
 
화면을
 
캡쳐하여
 
첨부합니다.
 
evaluate
 
expression
 
 
 
 
 
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
variables
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
watch
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] advanced mission_day02_answer의 사본.pdf
문자 수: 1241
────────────────────────────────────────────────────────────

step
 
1.
 
git
 
log
를
 
통해
 
Head
 
Commit
 
파악하기
  
 
 
Day
 
02
 
답안지
 
작성자:
 
이영기
 
step
 
1.
 
git
 
log
를
 
통해
 
Head
 
Commit
 
파악하기
 
질문
 
답변하기
 
01.
 
HEAD
는
 
무엇을
 
가리키고
 
있나요?
 
main
 
02.
 
HEAD
 
이전
 
커밋으로
 
되돌아가면
 
어떤
 
변화가
 
발생할까요?
 
하던
 
내용이
 
날아갈
 
수
 
있다
 
03.
협업
 
환경에서
 
reset
 
대신
 
revert
가
 
필요한
 
이유는
 
무엇일까요?
 
모든
 
것을
 
커밋
,
 
기록시키니까
 
백업이
 
가능해진다
.
 
stash
에
 
임시저장하는
 
것보다
 
확실함
.
 
강의내용
 
따라가다가
 
여러번
 
날렸음
.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
step
 
2.
 
원하는
 
commit
을
 
git
 
revert
를
 
이용하여
 
롤백하기
 
  
 
 
Day
 
05
 
답안지
 
작성자:
 
이영기)
 
Step
 
2.
 
원하는
 
commit
을
 
git
 
revert
를
 
이용하여
 
롤백하기
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
 
지금까지
 
수행한
 
내용을
 
git
 
log
를
 
통해
 
스크린샷
 
캡처로
 
첨부하고,
 
 
https://github.com/atozwizard/fake_llm_project
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] advanced mission_day03_answer의 사본.pdf
문자 수: 709
────────────────────────────────────────────────────────────

Step
 
1.
 
조장
 
저장소
 
Fork
 
하기
  
 
 
Day
 
03
 
답안지
 
작성자:
 
이영기)
 
Step
 
1.
 
조장
 
저장소
 
Fork
 
하기
 
 
조장의
 
저장소를
 
Fork
후
 
캡처하여
 
Github
 
Repository
 
주소와함께
 
제출합니다..
 
https://github.com/atozwizard/nqn4iwin-practice
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
Step
 
2.Pull
 
Request
 
생성하기
 
  
 
Day
 
03
 
답안지
 
작성자:
 
이영기
 
Step
 
1.
 
Pull
 
Request
 
생성하기
 
변경사항을
 
작성
 
후
 
커밋합니다.
 
 
그
 
후
 
PR
을
 
생성하고
 
캡쳐하여
 
Github
 
Repository
 
주소와
 
함께
 
제출해주세요
 
https://github.com/nqn4iwin/practice/pull/3/commits/d18ea3d8e652aea40ea7be6f180cd32be
be82208
 
  
 
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] advanced mission_day04_answer의 사본.pdf
문자 수: 1010
────────────────────────────────────────────────────────────

 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
SQL
문제
 
해결하기
 
user_id
 
name
 
age
 
role
 
created_at
 
1
 
Kim
 
28
 
USER
 
2023-01-10
 
2
 
Lee
 
35
 
ADMIN
 
2022-11-30
 
3
 
Park
 
22
 
USER
 
2024-03-15
 
4
 
Choi
 
41
 
USER
 
2021-07-21
 
아래
 
조건을
 
만족하는
 
사용자의
 
 
이름(
name)
과
 
나이(
age)
 
조회하는
 
SQL
 
문을
 
작성하세요.
 
 
조회
 
조건
 
1.
 
나이가
 
30세
 
이상인
 
사용자
 
2.
 
역할(
role)
이
 
USER
인
 
사용자
 
3.
 
가입일(
created_at)
이
 
2022년
 
이후인
 
사용자
 
셀렉트
 
프롬
 
에이지>=30
 
셀렉트
 
프롬
 
롤
 
=
 
user
 
셀렉트
 
프롬
 
가입일
 
yyyy>=2022
 
SELECT
 
name,
 
age
 
FROM
 
users
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
WHERE
 
age
  
>=
 
30
 
AND
 
role
 
=
 
ʻUSER’
 
AND
 
created_at
 
>=
 
’2022-01-01’;
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] advanced mission_day05_answer의 사본.pdf
문자 수: 905
────────────────────────────────────────────────────────────

step
 
1.
 
3-Layered
 
Architecture
로
 
리팩토링
  
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
3-Layered
 
Architecture
로
 
리팩토링
 
3
 
Layered
 
Architeture
로
 
리펙토링한
 
프로젝트를
 
Github
에
 
올리고,
 
 
Repository
 
주소를
 
첨부해주세요
 
 
https://github.com/atozwizard/atozwizard.git
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
step
 
2.
 
SQLAlchemy
를
 
이용한
 
DB
 
접근
 
리팩토링
 
  
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
SQLAlchemy
를
 
이용한
 
DB
 
접근
 
리팩토링
 
SQL
 
Alchemy
로
 
리펙토링한
 
프로젝트를
 
Github
에
 
올리고,
 
 
Repository
 
주소를
 
첨부해주세요
 
https://github.com/atozwizard/atozwizard/tree/develop
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 


"""
    s.raw_texts['daily_missions_extracted.txt'] = """============================================================
DAILY_MISSIONS
============================================================


────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] basic mission_day01_answer의 사본.pdf
문자 수: 999
────────────────────────────────────────────────────────────

step
 
1.
 
UV
로
 
Fast
 
API
 
라이브러리
 
추가하기
  
 
 
Day
 
01
 
답안지
 
작성자:
 
이영기기
 
Step
 
1.
 
UV
로
 
Fast
 
API
 
라이브러리
 
추가하기
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
step
 
2.
 
Postman
으로
 
Get
 
요청을
 
통해
 
피보나치
 
함수
 
호출하기
 
  
 
 
Day
 
01
 
답안지
 
작성자:이영기기
 
Step
 
2.
 
Postman
으로
 
Get
 
요청을
 
통해
 
피보나치
 
함수
 
호출하기
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] basic mission_day02_answer의 사본.pdf
문자 수: 688
────────────────────────────────────────────────────────────

 
 
 
Day
 
02
 
답안지
 
작성자:
 
이영기
 
Step
 
1.
 
마크다운
 
및
 
다양한
 
사이트를
 
이용하여
 
Github
 
ReadMe
 
꾸미기
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
Github
 
Repository
주소와,
 
ReadMe
 
스크린샷을
 
첨부합니다.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] basic mission_day03_answer의 사본.pdf
문자 수: 1744
────────────────────────────────────────────────────────────

step
 
1.
 
저장소
 
클론
 
및
 
깃
 
브랜치
 
생성
  
 
 
Day
 
03
 
답안지
 
작성자:이영기
 
Step
 
1.
 
저장소
 
클론
 
및
 
깃
 
브랜치
 
생성
 
git
 
branch
를
 
이용하여
 
현재
 
어떤
 
브랜치들이
 
나열되어있는지
 
스크린샷으로
 
찍어
 
첨부합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
step
 
2.
 
Github
에서
 
PR
 
생성
 
및
 
Merge
 
  
 
 
Day
 
03
 
답안지
 
작성자:
 
이영기
 
Step
 
2.
 
Github
에서
 
PR
 
생성
 
및
 
Merge
 
https://github.com/atozwizard/fake-llm-agent-fork/tree/atozwizard
 
Github
에서
 
PR
이
 
생성되어있는
 
모습을
 
스크린샷으로
 
찍어
 
첨부
 
후,
 
MERGE
 
합니다.
 
git
 
repository
 
주소도
 
같이
 
첨부합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] basic mission_day04_answer의 사본.pdf
문자 수: 781
────────────────────────────────────────────────────────────

step
 
1.
 
Docker
로
 
MySQL
 
컨테이너
 
실행하기
  
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
Docker
로
 
MySQL
 
컨테이너
 
실행하기
 
Docker
로
 
Mysql
를
 
실행하고,
 
docker
 
ps
 
명령어를
 
통해
 
 
Mysql
가
 
실행되고있는
 
모습을
 
캡처하여
 
첨부합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
step
 
2.
 
DataGrip
 
설치
 
및
 
MySQL
에
 
연결하기
 
  
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
DataGrip
 
설치
 
및
 
MySQL
에
 
연결하기
 
Datagrip
을
 
설치하고,
 
MySQL
과
 
연결한
 
화면을
 
캡쳐하여
 
첨부합니다.
 
 
 
 



────────────────────────────────────────────────────────────
파일: [SeSAC] [개발환경 구성] basic mission_day05_answer의 사본.pdf
문자 수: 854
────────────────────────────────────────────────────────────

step
 
1.
 
빈칸에
 
적절한
 
쿼리문
 
작성하기
  
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
빈칸에
 
적절한
 
쿼리문
 
작성하기
 
https://github.com/atozwizard/atozwizard
 
주어진
 
코드의
 
빈칸에
 
적절한
 
쿼리문을
 
작성
 
후
 
GitHub
에
 
올려
 
Repository
 
주소를
 
제출합니다.
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 
 
step
 
2.
 
Postman
으로
 
정상동작
 
확인하기
 
  
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.Postman
으로
 
정상동작
 
확인하기
 
Postman
으로
 
API
요청
 
테스트를
 
통해
 
Todo
 
리스트
 
조회
 
및
 
삽입
 
결과를
 
캡쳐하여
 
첨부합니다.
 
또한
 
DB
에
 
데이터가
 
정상적으로
 
삽입되었는지
 
확인
 
후
 
결과를
 
캡쳐하여
 
첨부합니다.
 
 
*저작권
 
주의
 
(주)업스테이지가
 
제공하는
 
모든
 
교육
 
콘텐츠의
 
지식재산권은
 
운영
 
주체인
 
(주)업스테이지에게
 
귀속되어
 
있습니다.
 
콘텐츠
 
일부
 
또는
 
전부를
 
복사,
 
복제,
 
판매,
 
재판매
 
공개,
 
공유
 
등을
 
할
 
수
 
없습니다.
 


"""
    s.raw_texts['lectures_extracted.txt'] = """============================================================
LECTURES
============================================================


────────────────────────────────────────────────────────────
파일: 00 Development Environment Course Introduction.pdf
문자 수: 2177
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3강사소개
[1] 각주표기시, 해당이미지혹은자료에위첨자로[숫자] 표기후, 하단에링크기재 -없을경우삭제: Noto Sans KR, 6pt서영학
엔씨소프트(18.01~24.12)
• AI연구→ 백엔드서버개발자
• 24.01~24.12 : 플랫폼센터계정플랫폼개발팀
• 23.01~23.12 :금융플랫폼개발팀
• 금융플랫폼개발
• 18.01~22.12 : AI 서비스개발실서버팀
• KBO AI 플랫폼개발
부트캠프강사
• upstage 새싹프로젝트CS  part (26.01~)
• 멋쟁이사자처럼백엔드단기심화4기(25.03~06)기타
• 23, 24년실전코딩Testing강의,
22년실전코딩백엔드강의(충남대)
• 대학교알고리즘동아리회장
• elice 카이스트머신러닝부트캠프(AI) 
최우수상
• 16년ACM-ICPC대전본선
블로그및깃헙
• inspire12.tistory.com
• github.com/inspire12400 -00
수업의목표
수업진행방식5수업목표: 프로그램이돌아가는환경이해와사용
다양한서비스개발에필요한개발환경
1. 개발에필요한IDE와Python 개발환경
2. Git 과Github 을통해코드버전관리에서개발자와협업, 기획자와협업까지확장
3. 파이썬백엔드와외부시스템(mysql, network) 을사용하고연동해보기6수업전체목차
개발환경과 협업
1. 개발환경카테고리
2. Python 실행환경
3. 코드버전관리: Git 
4. 기능/작업흐름: Branch
5. 개발자협업: Github 
6. 프로젝트관리: Github project인프라
7. 컨테이너: Docker 
8. DB: MySQL 기본
9. DB + Python 
10. 유지보수를고려한아키텍처7상황, 실습위주로생각
각실습코드를 기록
git 기반실습코드기록
직접작업해볼수도
만약수업흐름을놓쳐도
따라올수있도록인프라
7. 컨테이너: Docker 
8. DB: MySQL 기본
9. DB + Python 
10. 실제프로젝트에서는? 
8영화, 인사이드아웃중
좋은경험핵심기억
학교에서회사로
학생에서개발자로9핵심기억으로만들어지는머리속섬
10수업목표: 사고의확장
상황기반으로 필요성인지하고
도구를배우고카테고리를 이해한다
내앞의있는컴퓨터(로컬)에서실행되는것 →외부서버에서실행되는것의차이
혼자하는개발 → 여럿이하는개발
Know How →Know Where
수업에서다루는내용이넓고다양한편이다.
사용하는기술에서시작해큰카테고리를이해하는수업과정11수업피드백
1. 더알고싶은부분
2. 수업의난이도
3. 수업질문
4. 진행방향에대한피드백
온라인강의
-실시간은현장조교님
-궁금한점/ 과제진행어려움 /수업난이도/ 기타상담등 slack, 오픈카톡방활용https://open.kakao.com/o/gz1Jiq3h
개념/진행
중요페이지실습해보기
12수업전준비할것들
설치해야할 것
1. pycharm ( community / ultimate: 학생이메일무료)
2. python 설치(3.12 버전) 
-pyenv 를 통해버전별로설정하는걸추천
3. 네트워크요청도구: Postman
4. 터미널앱: iterm(mac) / warp
-windows의경우 wsl 설정을통한shell 설정
-패키지설치도구(apt: linux, brew: mac , scoop: windows)
구글설문링크공유와퀴즈공유5. git설치
6. source tree 설치
7. dockerdesktop 설치


────────────────────────────────────────────────────────────
파일: 01 Creating a Developer Friendly Computer Environment.pdf
문자 수: 4428
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3목표: 개발도구세팅개발하기쉬운컴퓨터환경만들기
목차
Pycharm (IDE) 사용법
Pycharm 디버깅과세팅방법
다양한개발도구소개401 -01
목표
-파이썬서버기본환경을세팅할수있다
-도구의카테고리를이해하고각도구를사용한다사용도구
•통합개발환경(Pycharm community / ultimate)
•터미널(iterm / warp / zsh )
•API 요청도구(Postman)
•docker (docker desktop)
•mysql 도구(data grip)5개발환경의중요성개발하기쉬운컴퓨터환경만들기
개발환경은 왜중요할까? (기술적)
-어디가문제가생겼는지어떻게확인하고로직을따라갈수있을까?
-필요할때바로적용하기위해, 문제를빠르게확인하게위해
-좋은도구는코드파악이나해석을도와주고문제점을파악하기쉽다6개발환경의중요성개발하기쉬운컴퓨터환경만들기
개발환경은 왜중요할까? (환경적)
장인은도구를탓하지않는다? 장인은도구를만들어쓴다
개발을하게되면컴퓨터앞에서12시간이상앉아서고민하는시간
보는환경이편하지않고, 예쁘지않으면그시간이고역이다
모든자료구조, 서비스사용목적= 사용을쉽게하려고
개발환경구축= 컴퓨터리소스를쉽게사용하기위해서도구의종류(카테고리)
칼이필요하다 → 상황에맞는다양한칼존재
하나의칼을잘쓰게되면나머지배우기쉬워진다7도구의종류개발하기쉬운컴퓨터환경만들기
개발환경의 종류
OS
-windows, mac, android, linux, browser
IDE
-pycharm , visual studio
Shell
-Bash, zsh, Powershell
터미널
-warp, iterm
AI 
-IDE + Claude Code언어
-python (3.12) , java, c, c++, rust, go lang, js 등등
Python 실행환경
-uv, pip
API 호출(curl)
-Postman , insomnia
docker 
-docker desktop
mysql 도구
-data grip801 -02
목표
-파이썬서버기본환경을세팅할수있다
-shell 개념을이해한다
-가상환경venv를이해한다사용도구
•통합개발환경(Pycharm community / ultimate)9IDE: Pycharm (파이참) 알아보기개발하기쉬운컴퓨터환경만들기
Pycharm 이란? 
jetbrains 에서만든통합개발환경(editor)
(Integration Development Environment)
https://www.jetbrains.com/pycharm/
실습은pycharm community 로진행
학생이라면pro 버전1년단위구독으로무료사용이가능합니다. (학교이메일필수)
https://www.jetbrains.com/ko-kr/academy/student-pack/다른ide가있지만pycharm 쓰는이유
-자동완성과코드보조기능
-디버깅이쉽다
-프로젝트생성시자동으로가상환경생성
(ide 는취향과선택의영역: vs code 를쓰셔도무방합니다)
10예) pycharm 내부적으로문제점을잡아준다개발하기쉬운컴퓨터환경만들기: 실습
11IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
Pycharm 작업폴더
추천: ~/Documents/workspace/upstage-project/ 폴더안에서작업
File → new Project 
12IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
Pycharm 으로간단한 Python 스크립트 실행해 보기
피보나치수열을출력하는프로그램을만들어보세요
13IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
피보나치수열을출력하는프로그램
14IDE: Pycharm (파이참) 실행해보기개발하기쉬운컴퓨터환경만들기: 실습
ide 가인식하는python 실행환경확인(인터프리터) –project 생성때만든가상환경.venv
15IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
Break Point
16IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
F8 : 스텝오버17IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
F8 : 스텝오버 * 5
18IDE: Pycharm 디버깅해보기개발하기쉬운컴퓨터환경만들기: 실습
F8 : 스텝오버
19IDE: Pycharm 주요단축키정리개발하기쉬운컴퓨터환경만들기: 실습
이름 단축키 
선언또는사용위치로이동  ctrl+ B 
선언또는사용위치로이동  ctrl+ alt + B  
전체검색  shift + shift  
뒤로(탐색)  ctrl+ alt + ←  
이름변경  ctrl+ F6 
코드완성  ctrl + spacebar  
구현으로이동  ctrl+클릭 
변수선언자동  ctrl + shift + v  
오른쪽분할에서열기  shift + enter (패키지에서파일클릭후)  이름 단축키 
최근파일목록  ctrl+ E 
맥은다른 시스템 명령어 때문에 겹쳐서 안될수도  (ctrl space)
-시스템환경설정 → 키보드 → 단축키 → 서비스 탭
단축키팝업설정20pycharm 의자동완성기능개발하기쉬운컴퓨터환경만들기: 실습
ctrl + space
21IDE: Pycharm 기타세팅개발하기쉬운컴퓨터환경만들기: 실습
탭위치(취향)
-저는탭을따로안쓰고project view 를연동해서씁니다. 
-내가연곳을자동으로선택하도록하는설정
2201 -03
사용도구
•터미널(iterm / warp / zsh )
•API 요청도구(Postman)
•docker (docker desktop)
•mysql 도구(data grip)
•git 23Shell: Bash / 터미널실행하기개발하기쉬운컴퓨터환경만들기: 실습
Mac vs Windows
mac 은기본세팅
wsl 리눅스설정이필요
CUI (Command UI)
환경에익숙해지기
24터미널도구: Warp 알아보기개발하기쉬운컴퓨터환경만들기
Warp 이란? 
최근인기있는터미널도구
https://www.warp.dev
25(심화/취향) 터미널창이쁘게꾸미기개발하기쉬운컴퓨터환경만들기
https://inspire12.tistory.com/344못생긴windows Powershell 예쁘고쓸만하게만들기
iterm + ohmyzsh
https://salmonpack.tistory.com/52
26(심화) pycharm 에서terminal 실행하기개발하기쉬운컴퓨터환경만들기: 실습
아래terminal 에서 작업하는 경우
27Docker 관리도구: Docker desktop 개발하기쉬운컴퓨터환경만들기
Docker 와인프라
docker / docker-compose
Docker Desktop 을통한설치
28DB 관리도구: Datagrip개발하기쉬운컴퓨터환경만들기
Datagrip 이란?
DB 에접속해서데이터를확인하는도구
동일UI로다양한DB 접근가능
https://www.jetbrains.com/ko-kr/datagrip/
29Git 설치개발하기쉬운컴퓨터환경만들기
https://git-scm.com/install/windows
mac : brew install git 
linux : sudo apt install git 30Git 설치개발하기쉬운컴퓨터환경만들기
31Git 설치개발하기쉬운컴퓨터환경만들기
프로젝트 폴더 내에서 우클릭 -추가 옵션 클릭32API 테스트도구: Postman 알아보기개발하기쉬운컴퓨터환경만들기
데이터요청확인
HTTP 요청의 모든구성요소를 정확히 설정하고
테스트할 수있는환경을제공한다.
\"실제로사용자나 다른서비스가 우리서버에요청하는 방식그대로\" 요청을 재현
코드로만 확인하면
•요청 코드가 잘못된건지
•네트워크에 문제가 있는건지
•API 가 잘못된건지
알기 어렵다포스트맨 다운로드
[https://www.postman.com/downloads/33HTTP API 만들기개발하기쉬운컴퓨터환경만들기
34diagram 그리기: excaildraw개발하기쉬운컴퓨터환경만들기
전체흐름과 순서파악, 아키텍처 설계그리기
https://excalidraw.com/
www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 03 Git Basics.pdf
문자 수: 7331
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위3오늘의목표: git 으로작업단위관리하기Git 
목차
git 설치와세팅
git 을사용하는이유
git init / add / commit
git commit 잘쓰는방법
source tree를통한시각화4수업전설치및세팅Git 
준비사항
-Git 다운로드(일단default 값으로next)
-SourceTree 설치(계정skip)
-Github 계정생성
-Github API 키발급및등록
-예제코드: 
https://github.com/inspire12/fake-llm-agent
5Git 초기세팅(옵션)Git 
# 1. 사용자정보
git config --global user.name \"서영학\"
git config --global user.email \"your-email@example.com\"
# 2. 기본브랜치이름main으로
git config --global init.defaultBranch main
# 3. github token 키체인저장
git config --global credential.helper osxkeychain
# git config --global credential.helper manager-core
# 4. 색깔켜기(diff/log 보기편하게)
git config --global color.ui auto
# 5. 안전한줄바꿈설정(Mac/Linux 기준)
git config --global core.autocrlf input     # mac/Linux
git config --global core.autocrlf true      # Windows# 6. 에디터설정(VSCode 쓰면)
git config --global core.editor \"code --wait\"
# 7. pull 시rebase 대신merge (헷갈리면이게더무난)
git config --global pull.rebase false
# 8. log / diff 보기편하게pager 설정(뒤에추천도구delta 쓰면더좋음)
git config --global core.pager \"less -+F\"
코드링크
설정값저장위치
~/.gitconfig 파일에설정값적힘(global 설정)
.git/config (프로젝트별설정)603 -01
왜다들Git Git 거릴까?
(로컬) 버전관리를위한Git
버전관리 → 프로젝트관리7파일이름_최종_v3_최종최종.ppt  Git 
버전관리가 되지않으면..
-작업한파일을잃어버리기쉽다
-어떤파일이 최신인지 헷갈림
-내용이언제 어떻게바뀌었는지추적불가
-다른사람이수정하면 충돌발생& 해결불가
-이전버전으로되돌릴수없음
-협업자가파일을덮어쓰면복구불가
-파일이많아질수록관리어려움
8프로그래밍에선?Git 
파일이많아질수록 관리지옥
회사에선
-협업하는사람도많고
-작업하는파일도많아
-관리지옥
9Git 이란?Git 
Git은\"버전관리 도구\" = 프로젝트 전체성장기록, 타임머신
-Git은내가작성한파일이 어떻게변해왔는지 시간순서대로모두기록해준다.
-특정시점으로 되돌아갈수있다
-\"이부분 누가고쳤지?\" 도알수있다
Git 은버전관리 도구(VCS: Version Control System)
10Git 이란?Git 
Git은\"협업을위한표준도구\"
-개발자여러명이동시에작업해도 충돌을인지하고 안전하게합칠수있다
-어떤코드를언제작성했는지모두기록 되다
-다른사람의작업과내작업을 안전하게합칠수있다 .
-내코드가검토를(리뷰) 통해제품에나가는과정(배포와CI/CD)1103 -0212무슨프로젝트를진행할까?Git 
llm agent 기능만들기 (흉내내기)
요구사항
-사용자메시지입력처리
-기본응답생성
-Tool 실행결과반환
-오류처리
-로그출력13무슨프로젝트를진행할까?Git 
일단기본프로젝트 진행
https://github.com/inspire12/fake-llm-agent/tree/start
내프로젝트
각파일만들고코드복사후세팅
14(실습) git 일단따라치기Git 
프로젝트 git 초기세팅/ 첫커밋하기
git init
git status 
git add main.py agent.py tools.py config.py 
git status 
git commit -m \"init: v1 기본LLM 에이전트\"15git initGit 
git 저장소 초기화(세팅)
파이썬파일세팅후git 저장소생성
git init = 이폴더를Git이관리하도록만드는첫단계
git init 실행하면폴더안에.git이라는숨겨진디렉토리생긴다
.git 에Git이 메타데이터(변경사항)을저장
(코드추적-변경사항, 커밋-작업사항, 브랜치, 로그, 되돌리기정보등)16git add Git 
Git 에변경을 커밋에 포함시키겠다고 체크하는단계
Git이변경사항을 추적할파일을지정하도록하는명령어
작업한변경을\"커밋후보영역\"에올림
커밋에포함할변경만선택적으로올림17git 버전관리를위한코드추적Git 
코드변경추적
작업을하면
어떤코드의 변경사항을추적해야하는지 Git 에알려주는과정이필요하다
Git이코드를추적한다= 줄단위로\"어떤줄이추가·삭제·수정되었는지\"를기록
Git 은메타데이터(변경사항)을저장하는버전관리시스템18git statusGit 
git 어떤파일을파일을추적하고 있는지 확인
Untracked → Git 모르는파일
Modiﬁed → 수정됨
Staged → add 완료
Clean → 변경없음
19.git 에특정파일이나폴더가들어가지않아야한다면?Git 
.gitignore
공유되면안되는파일은
ex) 
-API_KEY (비밀번호) 등
-ide (에디터) 사용하는파일.idea/* 
-개인개발환경설정파일 .venv/*2003 -03
git 사용법
Commit 작성법
Commit 관리법21변경이력= CommitGit 
git commit (커밋)
하나의commit 단위는기능이아니라목적
-하나의커밋은하나의의도를담는다
-제목은50자이내
-본문은왜수정했는지설명사용법
git add {파일명}
git commit
혹은
git commit -m \"커밋명\"
troubleshooting-
만약vi 에디터경험이없으시면
아래입력후vscode로수정
git config --global core.editor \"code --wait\"22Commit 메시지작성방식Git 
git commit 작성형식
<type>(<optional scope>) : <subject>
<body -optional>
type: 변경의목적을나타내는키워드
scope (선택): 모듈/도메인/레이어(예: user, auth, api, core, docs 등)
subject: 한줄요약(명령형, 끝에마침표X)
body: 왜이변경을했는지, 중요한맥락/주의사항(필요할때만)23(실습) 요구사항\"날씨기능추가\"Git 
일단따라치기
기능개발위해브랜치생성후기능추가및커밋
def get_weather (location ):
if location == \"서울\":
return \"맑음\"
return \"모름\"git switch -c feature/weather-tool
# 기능추가(코드로직추가)
# tools.py                              # agent.py
from tools import get_weather
class LlmAgent :
def handle(self, user, message ):
if \"날씨\" in message :
weather = get_weather( \"서울\")
return f\"{user}님, 서울날씨는 {weather }입니다.\"
return f\"{user}님, '{message }' 잘받았습니다.\"git add agent.py tools.py
git commit -m \"feat: 날씨기능추가\"
24변경이력은어떻게기록하면좋을까?Git 
git commit 작성원칙과전략
1. 하나의커밋 은하나의목적 만가져야한다(작고의미있게)
2.Subject(첫줄)는명령형+ 간결하게
3. 왜변경했는지기록하기(커밋메시지의본질)
Git commit 메시지의핵심은왜다.
코드는어떻게를보여주지만, 왜그렇게했는지는메시지가알려줌.
4. 한번에너무많은변경을커밋하지않기
파일20개이상바뀜. 500줄이상바뀜, 리팩토링+ 기능추가가섞여있음
→ 이런커밋은실제로리뷰불가능한커밋25좋은commit 과나쁜commitGit 
나쁜Commit 예시
메시지예시
\"update\"
\"fix\"
\"수정\"
\"테스트\" / \"ㅋㅋ\" / \"임시\"
-어떤파일이, 왜, 어떻게바뀌었는지알수없다
-기능수정, 오타수정, 리팩토링이한커밋에섞여있다
-롤백할때어디까지되돌려야할지판단이어렵다좋은Commit 예시
메시지예시:
\"feat: add user login api\"
\"fix: handle null user in profile page\"
\"refactor: extract email validator from user service\"
\"chore: rename variable for clarity in auth controller\"
-커밋메시지만읽어도의도가파악된다
-기능/버그/리팩토링이분리되어있어롤백이쉽다
-한커밋이한가지목적만가진다
나쁜Commit은\"그순간은편하지만, 나중에모두에게빚이된다\"
좋은Commit은\"조금귀찮지만, 나와팀의시간을아껴준다\"26하나의커밋은하나의목적만가져야하지만..Git 
현실적인 작업을 하며커밋을신경쓰기 어렵다
솔직히말하면, 좋은Commit 메시지작성은저도여전히어렵습니다
-기능개발중이라도수시로리팩토링이자연스럽게섞인다
-오타수정이나다른사람이짠코드의버그들이나잘못된컨벤센이보인다
-작업흐름이끊기는게싫어서커밋을미룬다
-처음시작할때전체설계를완전히이해하지못한상태에서작업할때가많다
-급한기능대응이나수정요청이중간에끼어든다
-팀의커밋문화에따라나도영향을받는다
-팀이커밋을지저분하게하면나도지저분해짐27좋은커밋을쓰기위한실천팁Git 
현실적인 작업과정
리팩토링하거나오타고칠때 그순간바로커밋하지말고, 최소한기능개발이끝나기전에분리
기능개발중바꾼것들 섞였다고걱정하지말기-나중에분리하면됨
-git add -p 를활용해나중에라도분리하기
\"하나의commit 단위는기능이아니라목적\"이라고기억하기28commit 전에넣을것들만지정하기Git 
git add -p 를통해commit 에넣을것만지정하기
git add -p
# y → 오타수정헝크만stage
# n → 디버깅코드hunk 건너뛰기
# s → 기능코드hunk를절반으로쪼개기
# e → 주석라인만골라서stage
hunk = Git이\"연속된변경라인을묶어서만든최소변경단위\"트러블슈팅)
git add –p (패치모드) 는git 이추적중인파일의
변경사항에서만가능하다
git add {file} 이후진행29(실습) commit 전에넣을것들만지정하기Git 
실습순서
상황) 날씨응답문구변경중서버문제생겨debugging 용logging 코드추가필요해서추가
하나의파일에두개성향의수정이혼재된경우를가정
1. 같은파일수정후git add -p 로따로선택
2. 추가한코드따로커밋
-변경내역을고르는과정에서좋은코드에대한고민이생긴다
-커밋이구분되어있으면나중에작업을되돌리기쉽다
30(실습) commit 전에넣을것들만지정하기Git 
git add -p 를통해commit 에넣을것만지정하기
agent.py
-디버깅로깅작업
-날씨문구수정작업
두작업이혼재따로커밋을해보자
# 작업코드나눠서add 
git add -p agent.py
# print 부분은n
# prefix 부분은y
git commit -m \"feat: LLM 응답prefix 추가\"
git add agent.py
git commit -m \"feat: 디버깅코드추가\"
from tools import get_weather
class LlmAgent :
def handle(self, user, message ):
print(\"디버깅 중...\" )
if \"날씨\" in message :
weather = get_weather( \"서울\")
return f\"[LLM] {user}님, 서울 날씨는 {weather }입니다.\"
return f\"[LLM] {user}님, '{message }' 잘받았습니다.\"3103 -04
Source tree 
변경사항을한눈에확인하며진행하기(직관성있게!)32Git 이어려운이유Git
명령어도 중요하지만
상황과상황에맞는작업흐름이더중요✔상황이다양하고명령어연결과정이복잡
✔변경흐름이눈에안보임
✔추상적인개념이많다(meta data)
✔Git 개발자에게판단을요구
작업단위(커밋단위) 설계가필요
협업시규칙과충돌관리필요
✔되돌리는명령어가복잡33Source treeGit 
\"Sourcetree: Git을 더쉽게, 더안전하게\"
Atlassian에서만든무료Git GUI 도구
시각적인diff 체크로변경내용을한눈에파악가능
hunk 단위, 라인단위로변경을클릭한번으로stage 가능
실수위험이줄어들고, commit 단위관리가쉬워짐
브랜치, merge, conflict도시각적으로표현되어부담이줄어듬
34Source treeGit 
https://www.sourcetreeapp.com
download & 설치
프로젝트세팅
35Source treeGit 
git add git status
git commit36Source treeGit 
git log
git diff
git show37참고사항Git 
vs code 익스텐션
-https://inpa.tistory.com/entry/VSCode- 💽-GIT-익스텐션-추천
git 명령어치트시트
-https://git-scm.com/cheat-sheet
-https://education.github.com/git-cheat-sheet-education.pdf
git 로드맵
-https://roadmap.sh/r/git--github-0ibs8
-https://maily.so/gitminam/posts/8do78n3prgq38총정리Git 
git 은commit 을통한작업관리가 기본이자 핵심이다. 
-작업단위와 이력관리
-현실적인 작성법
git add -p / commit
-각명령어를 용도에 맞게사용하고
source tree
-git 도구를 통해더직관적으로 편하게git 을쓰자
-git 명령어를 알아야source tree도잘쓸수있다.www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 04 Git Advanced.pdf
문자 수: 5822
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3오늘의목표: 작업되돌아가기Git 
목차
gitcheckout/switch를통한작업되돌아가기/이동하기
gitbranch를통한작업분리
merge협업과 conflict해결404 –01
Git Branch 
merge / rebase
Git flow5만약예전버전을사용해야한다면?Git 
현업에서 다양한 요구사항이 존재, 이전버전에서 작업을시작해야할 수도있다
‘무리한 요구를 하는 클라이언트 ’카카오톡 이모티콘6만약예전버전을사용해야한다면?Git 
지금라이브 버전에 버그가 있어서 이전버전으로 서비스해야할 거같아요
7만약예전버전을사용해야한다면?Git 
하지만작업중에현실적으로
1. 커밋이 쌓이면 \"하던작업을 멈출수가없다\"
2. 예전버전과 지금버전사이의 변화등으로 현재작업이 영향이간다 (위험하다)8git checkoutGit 
특정시점으로 코드를되돌릴때
-Git이저장한시점(commit)으로 이동
-이전커밋시점(snapshot) 이동가능
(잠깐) 다른작업으로 되돌릴 때현재작업이남아있을 때
만약커밋하지 않은파일이 있다면 되돌릴 때문제가 생길수있다
9git stashGit 
깃내부임시저장소
지금하던작업은미완성, commit하기엔너무지저분할때잠시옮겨놓는다
다른작업을해야하는데현재작업중인부분을커밋하기엔애매하고날리기도애매할때쓴다
checkout할때로컬에수정내용이남아있으면섞여서충돌날수있음
내부저장소에코드를잠시보관해남아있는변경이없는깨끗한상태로만들고 checkout하자
Source Tree 에서확인
10(실습) git stash 명령어, 사용법Git 
임시저장 하기
git stash 
메시지지정해서stash 생성
git stash save {메시지}
저장된변경목록보기
git stash list
가장최근저장된stash 보기
git stash show
다시꺼내오기stash 목록에서삭제
git stash pop
꺼내오지만목록에서는삭제하지않음
git stash apply11git checkout 사용법정리Git 
git checkout
커밋해시로이동가능
git checkout <commit-hash>
브랜치이동
git checkout <브랜치>
새브랜치+ 이동
git checkout -b <브랜치>
파일되돌리기(옛날방식)
git checkout <커밋> --<파일>12(실습) gitcheckoutGit 
코드를이전버전으로 되돌려보기
1. 두번째커밋hash값확인
2. gitcheckout(커밋hash값앞일부입력)
3. 코드변경과commitlog변경확인
Head 란? 
지금 작업 중인 곳 (현재 위치 )
13(실습) gitcheckoutGit 
코드를이전버전으로 되돌려보기
4. 실제코드로돌아가초기상태로변한코드를확인한다
이 때Detached HEAD 상태 발생14(심화) Detached HEAD 란? Git 
HEAD는\"현재내가보고있는스냅샷\" 을가리키는데,
해시로체크아웃하면브랜치가아니라개별커밋을가리키게됩니다.
그래서\"Detached HEAD\"
→ \"브랜치에서떨어져있는상태\"
브랜치라는작업흐름내에서이동해야, 수정한내역을잃지않을수있다
이상태에서커밋하면브랜치와연결되지않아서
나중에찾기어려운고아커밋이생길수있어주의해야합니다.
1504 –02
git branch16git branch Git 
작업흐름(줄기) / 작업에이름을붙인다
독립적으로 작업을 진행할 수있도록돕는작업흐름
마지막커밋을가리키는 포인터 (커밋흐름, 진행경로를 추적)
브랜치= 커밋흐름의 이름표17Branch 없이개발하면생기는문제Git
브랜치가 없으면 되돌리기가 매우위험하다
•안정적으로 되돌릴 안전지점(safe point) 이없다.
•해시(hash) 기반으로 되돌리기는 어렵고실수하기 쉽다.
•잘못되면 작업물이 사라지거나 main을손상시킬 위험이크다.18AI 시스템에서버전호환문제들Git
작업이많아지고 커밋이 많아질수록 생기는 문제점
AI 시스템에서 AI 모델별로적용할코드가다를수있다. 
실험이많아질수록 어떤버전 인지 알필요가있다
ex) 버전을가지고있어야하는 이유들
●현재서비스에 나가있는 모델+코드
●지금연구하고 있는모델+ 코드등버전별
●A/B테스트 등
19(실습) git checkout 과git branch Git 
코드를이전버전으로 되돌려보기
5. 추가작업을위해 branch 를생성
-hash 를통해이동하면 너무불편+ 추가작업위한바탕( branch)가필요하다
-Detached Head 해결
git branch develop
20git branch 이름은어떻게정해야할까?Git
브랜치이름기본규칙
1.형식: type/task-name(그룹형태)
a.복잡해지면area까지: type/ area/task-name (그룹형태)
2.단어는하이픈(-) 으로연결
3.공백, 대문자, 특수문자 ❌
4.이름만 보고 작업목적이 명확하게 보이도록21git branch 이름은어떻게정해야할까?Git
브랜치종류(역할)에 따른prefix
feature —기능개발
-feature/user-profile
-feature/add-search-api
fix—버그수정
-fix/wrong-total-score
-fix/null-pointer-error
hotfix—운영긴급수정
-hotfix/payment-failure
refactor —구조개선
-refactor/split-preprocess-moduleexperiment —AI/ML 실험
-experiment/model-v2
-experiment/augmentation-test
docs—문서작업
-docs/update-api-spec
ci / infra —자동화& 인프라
-ci/add-github-actions
-infra/add-terraform-config2204 –03
merge
conflict23각자만든작업(branch)는어떻게합칠까?Git
gitmerge
두브랜치의작업내용을하나로합치는과정
gitconflict
두브랜치가같은파일의같은부분(hunk) 을수정했을때
Git은두개의코드가같은줄에있을때\"어느쪽이맞는지\" 결정불가
→ 개발자에게선택권을넘김24Conflict 해결과정Git
Conflict는 \"오류\"가 아니다. Git이개발자에게 선택권을 넘긴것이다.
1. 두코드중어떤부분을살릴지결정
-내버전만살릴수도있음
-상대버전만살릴수도있음
-둘을합쳐새로운버전을만들수도있음
2. 충돌표시(<<<<<<<, =======, >>>>>>>) 제거
3. 수정된파일저장
4. 다시stage( gitadd) → commit(Merge커밋) 25(실습) Conflict 파일Git
A 브랜치(현재) –B 브랜치(합칠 브랜치)
<<<<<<< HEAD
return f\"{user} 님,  '{message}' 를 잘 받았습니다 .\"
=======
return f\"{user} 님, 서울 날씨는 '{message}' 잘 받았습니다 .\"
>>>>>>> lecture/conflict-b
git switch start
git pull
uv sync26(실습) git merge 와conflict 실습Git
git merge 와conflict
1. lecture/conflict-a branch 생성후agent.py 파일return 바꾸고커밋
2. lecture/conflict-b branch 생성후agent.py 파일return 바꾸고커밋
(1,2) 같은파일을
3. lecture/conflict-a 브랜치에lecture/conflict-b 브랜치를merge
4. conflict 발생
3. feature/embedding-service 에서develop 로합쳐보기
27(실습) git merge 와conflict 실습Git
git merge 와conflict
4. merge 실패conflict 상황
28Conflict 을줄이는방법Git
잦은Git conflict는 생산성과 코드안정성에 직접적으로 영향
작은단위로자주커밋하고자주푸시(Push/Pull) 하기
-Conflict의가장큰원인은 오래떨어져있던두타임라인이갑자기만날때 생김.
일정한merge 흐름
-브랜치의역할을나누고merge 하는브랜치를고정
기능단위로브랜치를짧게유지하기
-작업이길어질것같으면기능을분리
-브랜치는 3~5일안에 merge가목표
파일단위충돌위험을줄이기위한코드구조화(Clean code)
-Conflict는\"같은 파일의 같은 줄 \"이 바뀌어야 난다 .
→ 파일을 분리하면 conflict가 줄어든다 . 29Conflict 을줄이는방법Git
잦은Git conflict는 생산성과 코드안정성에 직접적으로 영향
main/develop브랜치를더럽히지않기
-팀의중심브랜치(main/develop)가깨끗하면충돌도줄어듦.
-직접main에push금지
-PR 기반merge강제
-PR 템플릿으로커밋기준통일
merge전에미리차이(diff) 확인
-merge전에다음을통해conflict가능성을예측
컨벤션통일
-Prettier/ Black / ESLint등\"자동포매터\" 도입
-Conflict를많이만드는원인중하나는 줄바꿈, 들여쓰기, 공백, 포매팅차이3004 -04
git flow31Git branch 전략적으로사용하는방법Git
일관된 merge 흐름의필요성
conflict 는생산성을해친다= 개발자의의사결정을계속물어보게된다
역할과개발환경에맞는 일관된merge 흐름이필요하다
회사개발환경(사내개발환경/ 테스트환경/ 라이브환경)32Git branch 전략Git flow Git
단순한브랜치전략을넘어개발의흐름을깔끔하게정리
33main  / develop 브랜치Git
배포하는 브랜치: main 
실제배포된 코드(production)
tag를통해실제배포된 버전들을 관리(정기/비정기인지)
메인배포인지 아니면서브배포인지
작업을합치는브랜치: develop
개발자들의 작업들을 합치는공간(중간단계개발통합) 
feature 브랜치들
34각자작업을진행하는브랜치Git
feature/, feat/
해야할작업이생김→ 이슈등록
develop 에서이슈에 대한feature 브랜치작성
이슈들에 대한처리
35QA, 테스트, 릴리즈직전작업Git
release
정기배포: QA, 문서화, 버그수정, 릴리즈노트
develop에서기능완료후분기
작업완료후main + develop 에머지+ Git Tag 추가
develop 에서바로main 으로가는게아니라중간단계에서
다듬는다.
개발초기단계, 라이브가없는단계에선굳이필요없습니다.
36(비정기) 배포하는브랜치: hotfix Git
main 에서바로분기해서 긴급수정브랜치
1. develop 에배포하면안될것들이있을경우
2. 운영중버그발견해서즉시수정필요
이럴때
main에서분기해서작업
완료후main + develop 모두병합
기존의작업을cherry pick 등으로
코드를(커밋)을가져다사용
37총정리Git 
Git작업흐름과되돌리기
branch필요성과 사용법/사례
-gitbranch각역할
merge/ conflict
-conflict해결법
-conflict를줄이는방법
Gitflow전략
-Gitflow를통한merge전략과 배포www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 05 GitHub for Collaboration.pdf
문자 수: 5526
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3오늘의목표: Git 에서Github 확장Git 
목차
Git 에서Github으로확장,Github이해
github권한과github세팅
git clone, push, pull 등git과github기본기능다루기
fork, pull request,  코드리뷰, issue 등github기능다루기405 -01
Git과Github 
Github 계정
Git repository 
Git remote 
Github push 5혼자개발 → 여럿이하는개발( 회사)Github
개발자with 개발자
하나의프로젝트를같이개발하는순간어떤문제가생길까? 
다른사람의코드를어떻게가져올까?
•다른사람이만든코드를어떻게가져올까?
•내가만든코드를어떻게공유할까?6개발자끼리코드를공유할중앙저장소(온라인) 필요Github
Github 이란?
로컬Git이연결되는온라인저장소
코드협업을위한 플랫폼(저장소에서기능이추가됨)
Git 저장소 를온라인에서관리
GitHub는세계최대 오픈소스 플랫폼
백업· 공유· 리뷰· 자동화제공
Git = 도구, GitHub = 서비스
팀개발의중심
오픈소스: 공개된협업프로젝트
7Git != Github Github
Git과Github 다르다, 둘간관계
Git = 버전관리도구(로컬)
GitHub = Git 저장소를호스팅하는온라인서비스
Git 없이는GitHub를사용할수없음
GitHub는협업· 리뷰· 공유· 자동화제공
Github 말고도 GitLab, Bitbucket 등다른서비스도존재
8Github 에서사용하는용어들Github
주요용어
✔remote = 원격저장소 주소
•\"어디로보낼까? 어디에서 가져올까?\"를 remote를통해판단
✔origin = 기본remote 이름
✔(Code) Repository(repo): 코드저장소= Github
✔Push / Pull: 업로드 / 다운로드
✔Fork: 다른저장소 내계정으로 복사(권한문제해결)
upstream = 원본저장소remote 이름
✔Pull Request(PR): 변경요청
✔Issue: 작업/버그 기록
✔Code Review: 변경검토과정
9Github 에서사용하는용어들Github
Git -Github 연결하는 용어
✔저장소 가져오기 → clone
GitHub 프로젝트를 내컴퓨터로 내려받는 명령
✔원격주소등록→ remote add
GitHub와연결하기 위해내Git에게
\"이주소가 GitHub 저장소야\" 라고지정
✔GitHub 에서프로젝트 복사→ fork
clone이“내컴퓨터로 복사”라면, fork는GitHub 계정으로 복사
10Push / PullGithub
원격저장소와 코드상태를 맞추는 작업
push = 내컴퓨터→ GitHub로코드를올린다
pull = GitHub → 내컴퓨터로코드를받아온다
push는업로드 , pull은다운로드+ merge 기능을동시에포함.
push 전에pull 을통해원격저장소와동기화를하고진행해야한다
실제현업/ 협업에서가장많이사용하는기능11(실습) Github 계정생성하고저장소에내코드올리기Github
실습순서
github 사이트에서
1. Github 가입
2. Repository 생성
내프로젝트에서
3. git remote 설정
4. 코드push << 인증에러
5. api key 발급및로컬에등록
6. 코드push (main 브랜치)
7. branch push 실습
8. clone 으로올린프로젝트 코드받아보기12(실습) Github 계정생성하고저장소에내코드올리기Github
실습진행
github 사이트에서
1. Github 가입 github.com →signup 
2. Repository 생성
GitHub에로그인→ New Repository 클릭→ 이름입력후Create
내프로젝트(llm agent)에서
3. git remote 설정
git remote add origingithub.com/{username}/fake-llm-agent
git remote -v # remote 확인
4. git push -u origin
13(실습)Github사용을위한key 발급받기Github
Github을 쓰기위해key 발급을해야한다
https://github.com/settings/tokens
note: 토큰이름등록
expiration: 30일
select scop: repo 선택
맨아래generation token
14Github 사용을위한key 저장하기Github
Github을 쓰기위해key 저장후사용
윈도우
git config --global credential.helpermanager-core
mac
git config --global credential.helperosxkeychain15(실습) Github 계정생성하고저장소에내코드올리기Github
실습진행
6. 코드push(main 브랜치)
git push -u origin
7. branch push 실습
git checkout -b feature/login
git push -u origin feature/login
8. clone 으로올린프로젝트코드받아보기
git clone github.com/{username}/fake-llm-agent1605 -02
repository 권한과 fork
Pull Request 
Review
오픈소스기여17남의Repository(오픈소스)를수정하고싶어.. 하지만Github
Push 가거절되는이유= 내저장소가 아니니까
GitHub의대부분의저장소는내가직접push할수없다. (권한이없기때문)
권한(permission) 때문.  upstream(원본저장소)은관리자(Maintainer) 외에는push 허용X
그래서내버전으로개발을하고, 개발내용을공유하려면
-권한을요청해서받거나
-저장소를내계정으로복사(fork) 해야한다
아무나직접push하면프로젝트전체가피해를볼수있다.
→ PR을통해요청에대한 논의/검증단계를거쳐승인후merge 하는것이안전하다18남의Repository(오픈소스)를수정하고싶어.. 하지만Github
https://opensource.guide/leadership-and-governance/오픈소스의 코드를 관리하는 사람들
-Contributor: PR로기여(push 권한없음)
-Committer: 특정브랜치에push 가능
-Maintainer: 프로젝트관리및merge 권한
19내수정을오픈소스에반영하고싶어Github
https://opensource.guide/leadership-and-governance/오픈소스의 코드를 관리하는 사람들
1. 나도오픈소스관리권한을받는다
2. 내가오픈소스를만든다
--현실적으로어렵다
3. 내가만든변경사항을보여주고, 의견을나누고, 승인되면, 상대가가져가반영한다20Pull Request (PR)Github
원본프로젝트에 내가만든기능을 추가하고 싶어
pull (당겨가는걸) request(요청)
내가만든거너가당겨가서니프로젝트에넣을래? 
코드리뷰과정을통해PR에대해논의(리뷰)
리뷰어가추가로고쳐달라고요청할수있다. or 반려할수있다.
프로젝트담당자(메인테이너)의승인(Approve) 이후merge →코드에반영이된다
→ 배포후제품에반영21(실습) githubpull requestGithub
실습순서
강사repo
1. 예제프로젝트github.com/inspire12/fake-llm-agent fork 
수강생repo
2. fork 로받은프로젝트github.com/ {자신의깃헙주소} /fake-llm-agent  확인
3. fork 로받은프로젝트 clone
Trouble shooting)
-이미clone 받은프로젝트가있으니 backup 폴더 를만들고
-backup 폴더에서clone 하자22(실습) github pull requestGithub
실습순서
수강생repo
4. fork 코드에서수정작업(main 브랜치)
-아이디로폴더를하나만들고그안에자기소개.md  
-자기소개/ 이력서등을간단하게업로드
5. add, commit 후푸시
commit 명ex)
docs: {username} 자기소개입니다
6 push 후내코드가fork 된내repo 에반영되었는지 확인23(실습) github pull requestGithub
실습순서
7. pull request 요청
-PR 이요청되면자연스럽게요청을받는쪽에PR 이생긴다
강사repo
8. 강사와코드리뷰후코드수정
-강사와간단한인사말진행후
9. merge 후코드적용확인24(실습) github pull request Github
실습진행
fork 를한새프로젝트
받아서진행
25(실습) github pull request Github
실습진행
push 는main branch 
26(실습) github pull request Github
실습진행
PR
27Code ReviewGithub
프로젝트에 반영전충분한 논의/검증이 필요하다
•다른개발자가작성한코드를검토하는과정
•코드품질향상목적
•버그예방
•일관성유지
•팀커뮤니케이션강화28(실습) pull request 내용기반으로Code Review 하기Github
실습진행
PR 날리기
29Code ReviewGithub
Single Comment (단일코멘트)
•PR의특정코드줄이나특정라인에남기는 임시메모/ 가벼운피드백 .
•Review로제출되지않음
•PR 작성자에게요청사항으로잡히지않음
•승인/변경요청같은상태변화없음
•해당댓글은리뷰프로세스를마무리하지않아도됨
30Code ReviewGithub
Code Review (Review)
•여러코멘트를묶어서하나의\"리뷰\"로제출됨
•Review 버튼을눌러야함
•Reviewer가어떤조치를요청하는지명확히전달됨
•PR에\"Approved / Request Changes / Comment\" 상태가기록됨
•팀프로세스에서공식적인승인절차로사용
 Comment: 의견남기고끝
Approve: \"이PR 합쳐도됩니다\"
Request Changes: \"이대로는Merge 불가, 수정필요\"31Code Review 후변경사항반영하기Github
코드리뷰로 수정사항을받은후
PR 이올라간상태에서해당브랜치에
코드를수정해커밋이쌓이면PR에도자동으로쌓인다
32총정리Github
Github을통한협업
github개념 익히기
-저장소, 권한이슈
githubrepo 코드공유/ 사용하기
-clone, push, pull
github실제 협업해보기
-fork, pull request, Code Reviewwww.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 06 Project Management and GitHub.pdf
문자 수: 3556
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3오늘의목표: 프로젝트를관리이해Github 
목차
프로젝트를만드는사람들
issue 와pull request
프로젝트관리도구이해406 -01
혼자개발 → 여럿이하는개발( 회사)
버전관리 → 프로젝트관리5혼자개발 → 여럿이하는개발( 회사)
https://yozm.wishket.com/magazine/detail/1455/기획자→ 개발자
지난시간에는개발자와개발자끼리의협업이라면
회사에는같이프로젝트를만드는다양한사람들이존재
프로그래밍을하기전에
무엇을만들지, 왜만들지, 언제까지만들지먼저정리되어야한다.Github 
6혼자개발 → 여럿이하는개발( 회사)Github 
개발자와 함께일하는사람들
•기획자(PO/Product Manager)
•디자이너
•QA
•사업팀
•때때로… CEO, 회사에서 개발자는 무엇을 코딩하게 될까
•기획자가새로운기능요구사항을올림
•디자이너가화면을업데이트함
•개발자A는백엔드API 개발
•개발자B는프론트화면개발
•QA는테스트일정조율
•PO는우선순위조정706 -02
•해야할일, 일의할당
•Issue = Ticket8프로젝트관리의시작은항상Issue다.Github 
Issue는\"해야할일\"을정의하는 가장단위
프로젝트는결국해야할일들의집합이다.
그러나\"무엇을해야하는지\"가명확하지않으면
개발은엉뚱한방향으로흘러간다.
Issue는해야할일을정의하고추적하는첫출발점이다.9Issue가없다면?Github 
Issue 는일의중심
할일이말로만전달되고사라짐
우선순위가불명확
역할분담이애매해지고책임도흐려짐
어떤기능이완료됐는지, 어떤문제가열려있는지추적불가
10(실습) issue 등록해보기Github 
이슈만들어보기
만약상단바에code 다음에issue가보이지않는다면settings > features 에서 issue 활성화
11(실습) issue 등록해보기Github 
issue 특징
12(실습) issue 등록해보기Github 
이슈만들어보기
만약상단바에code 다음에issue가보이지않는다면settings > features 에서 issue 활성화
13Issue / PR 같이볼사람언급해보기Github 
@ 을통해유저언급해보기
14보냈던Pull Request에Issue 언급해보기Github 
#{이슈번호/PR번호}  ISSUE 단위로실제작업연동(PR) 
•PR과이슈는둘다# 으로호출가능
1506 -03
Github project16프로젝트관리도구가없이일을하는경우Github 
기획자–개발자 협업의 혼란
•기능요청이슬랙·카톡·노션에흩어져있음
•누가어떤작업을하는지파악불가
•일정·우선순위가정리되지않음
•개발자는“무엇부터해야하나?”를매일질문
•기획자와개발자가서로다른정보로일함
기획과 개발정보가 한곳에 정리되지 않는다는 것
•코드보다커뮤니케이션으로시간을많이쓰게된다.17프로젝트관리도구의기본기능Github 
작업정의/ 작업분해
\"우리가무엇을해야하는지목록을만드는것\"
큰기능을작은단위로쪼개기
모든팀원이이해할수있는형태로문서화
작업누락방지
진행상황/ 상태시각화
To Do → In Progress → Review → Done
작업흐름을한눈에확인
병목·지연구간즉시파악우선순위(Priority)와 일정(Milestone) 관리
어떤작업이더중요한지정의
스프린트/ 마일스톤/ 데드라인
리스크조기감지18AI 와프로젝트관리도구의궁합Github 
https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/AI 에효율적인 업무지시
AI는정리된정보를기반 으로할때가장잘작동함:
-Issue에요약된요구사항
-Project 보드의작업상태
-우선순위, 마감일, 작업히스토리
-담당자와PR의연결관계
AI 코드리뷰, AI 코딩 등앞으로이런task 정의가더
중요해질것19AI 와프로젝트관리도구의궁합Github 
https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/AI 코드리뷰서비스
코파일럿 / 코드레빗등등
20프로젝트관리도구종류Github 
통일된작업흐름을 도와주는 Tools
Jira, Notion, Trello, Linear 등등
Jira: 기업용대형프로젝트에강함
Notion: 문서기반의유연한협업
Trello: 간단한칸반방식
Linear: 빠른스타트업중심도구
21Github project 란?Github 
github project 의장점
•코드, 이슈, PR, 일정이 모두GitHub 안에서하나의흐름으로 이어진다.
•PR이나 Issue 연동
•+ 무료
실제강의만들때제작조교님과작업한프로젝트관리(github project) 
22github 알림Github 
github 에서 일어나는일들을알려준다
github 알림, 이메일등을설정한알림을받아볼수있다
23(실습) github project 생성하기Github 
github project 생성하기
1. https://github.com/users/{username}/projects
접속후create 
2. Kanban 선택
3. project 이름과우리가작업한repository 입력후Create Project
4. issue 생성
5. 담당자할당
6. PR 올리기
24(실습) github project 생성하기Github 
github project 생성하기
1. https://github.com/users/{username}/projects
접속후create 
2. Kanban 선택
25(실습) github project 생성하기Github 
github project 생성하기
3. project 이름과우리가작업한repository 입력후Create Project
개발진행과정을한눈에확인할수있다
26(실습) 기존issue 와github project 연동Github 
기존issue에서
project 오른쪽 톱니바퀴 클릭후
27총정리Github
Github 을통한프로젝트 관리
프로젝트 관리도구필요성
-프로젝트를 만드는사람들과 협업하는 방법
작업단위issue 
-issue 를통해문제제기와작업할당, PR 연동
github project 
-Kanban 보드 등을통해작업한눈에보기www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 07 Docker Infrastructure and MySQL.pdf
문자 수: 8242
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3목표: Docker는편리하다Docker
목차
Docker 필요성
Docker 구성요소
Docker 사용법및실습
docker-compose 로mysql 켜기프로젝트 : https://github.com/inspire12/upstage-infra-project.git4언어레벨에서문제 → 인프라수준에서문제Docker 
대부분문제는언어밖에서 발생한다
OS가서로다르다
Windows / macOS / Linux 환경차이로 동일코드가다르게동작함.
시스템 패키지가 다르다
libssl, libxml 등OS 레벨라이브러리 버전이 달라충돌발생.
외부서비스환경이다르다
MySQL, Redis가로컬에는 없거나, 버전/설정이 서버와 다름.
서버와 로컬의 OS 차이
서버(Ubuntu)와로컬(macOS)의 동작방식차이때문에문제재현이 어려움.
venv는“언어의존성”만 맞춰줄뿐,
실제문제는OS·시스템라이브러리·외부 서비스처럼 인프라레벨에서 발생한다.507 -01607 -01
Docker 란?
7(심화) 입문자가Docker 까지굳이알아야하나Docker 
왜내컴퓨터에선 안되는거야
입문자는환경문제로가장많이고생한다.
-설치과정도오래걸리고나중에처리도어려움
DB, 캐시, 메시지큐같은인프라를안전하게체험할수있다.
-초보자의성장속도를크게올려주는도구다.
팀프로젝트를하면환경차이가문제를만든다.
-Docker는개발환경을통일해개발을더쉽게만든다.
8Docker 이야기할것과이야기하지않을것Docker 
이야기할 것
다른사람의 세팅을가져다쓴다
(외부의존성, 인프라구성요소)
Docker 설치
Docker 이미지/ 컨테이너
-Docker 실행흐름
접속을위한Docker 네트워크
-host.internal.network
docker-compose 인프라구성
-mysql 실행해보기이야기하지 않을것
Dockerfile 작성
-내앱을컨테이너화
Docker 내부구조
-Docker overlay 구조
-namespace, cgroup 
-런타임구조
실제운영배포전략
-kubernetes, ci/cd
컨테이너네트워크심화9Docker 이미지와컨테이너Docker 
설계도= 이미지, 실행환경 = 컨테이너, 실행= 애플리케이션
-이미지: 실행가능한앱의정적인 설계도(변하지않음)
-컨테이너: 이미지를메모리에띄운 실행인스턴스 (변할수있음)
이미지= 레시피, 컨테이너= 그걸로만든요리10(심화) DockerfileDocker 
docker 이미지 생성을 위한명세서
애플리케이션 실행에 필요한 환경 구성 절차를
코드로 적어 놓은 설정 파일
개발자마다 환경이 달라도 항상 동일한 실행 환경을 만들 수 있음
서버와 로컬이 달라서 생기는 “동작 안 함 ” 문제를 근본적으로 해결
계층(Layer) 기반빌드→ 캐싱, 빠른재사용
Docker 실행흐름
•Dockerfile → docker build → docker 이미지생성
•docker 이미지→ docker run → 컨테이너생성및실행11(실습) Docker desktop 설치Docker 
Docker 설치
https://docs.docker.com/desktop/setup/install/windows-install
12(실습) Docker desktop 설치Docker 
13(실습) Docker desktop 설치Docker 
docker --version
docker 명령어시Cannot connect 가뜬다면docker desktop 실행이안된상태
docker 자체적으로리소스를가져가는게많아서평소에는꺼놓고필요할때사용하는걸권장(로그인시켜지는옵션해제)1407 -0215Docker 아키텍처Docker 
Docker 구성요소와 명령어이어생각
Docker 이미지
실행가능한앱의\"설계도\" 또는\"템플릿\"
Docker 컨테이너
이미지가실제로실행된\"격리된박스\"
Dockerfile
설계도를만드는설명서
Docker Hub
이미지를올리고내려받는GitHub 같은저장소
Docker 데몬
Docker 컨테이너를관리하는\"운영체제속관리자\"
Docker CLI
Docker를제어하는\"터미널명령어\"16Docker 명령어패턴Docker 
docker <대상> <행동> [옵션]
✔대상(Resource)
image
container
volume
network
system
(추가: plugin, context 등)✔행동(Action)
ls (목록조회)
rm (삭제)
prune (사용되지않는리소스정리)
inspect (정보조회)
logs (로그조회)
create / run / stop …✔docker 초창기구조화되기전패턴
docker ps
docker rm
docker rmi
docker images
docker run
예전명령어도정상동작
옵션확인
docker <대상> <행동> --help17Docker 기본명령어정리Docker 
컨테이너 상태체크/ 컨테이너 생성/ 실행
✔Container 상태체크
docker container ls 
docker ps 
docker ps -a
✔Container 생성/ 실행/ 삭제
docker run / docker start
docker stop / docker rm 
✔docker 로그, 분석
docker log / docker inspect
✔docker hub (github 같은외부저장소)
docker pull / docker push✔Container 실행
docker run 
-d(백그라운드) 
--rm(컨테이너종료시컨테이너도삭제) 
--name (컨테이너이름지정)
✔Container 내부들어가보기
docker exec –it {pod 이름} bash
https://hub.docker.com
18nginx 란? (엔진엑스)Docker 
가벼운웹서버
웹서버, 역방향프록시, 로드밸런서, 캐시서버, HTTP 캐싱등
다양한기능을수행하는고성능오픈소스소프트웨어
비동기이벤트기반구조를사용하여적은자원으로
높은동시성(다수의연결동시처리)을제공하며, 특히대규모트래픽을처리하는데강점
실습에선
누군가브라우저로요청하면
HTML 와같은정적파일을그대로돌려주는역할19(실습)Docker 기본명령어Docker 
웹서버nginx 이미지를 받아서사용해보자
1. nginx docker 이미지를받는다
2. nginx docker 이미지를컨테이너로띄워본다
3. nginx 접속확인
4. 컨테이너상태를확인
5. 컨테이너정보를확인
6. 컨테이너로그확인
6-1 컨테이너로그지속적으로확인
7. 컨테이너내부들어가보기
8. 컨테이너종료및삭제20(실습) 이미지받고실행해보기Docker 
실습과정
1. nginx docker 이미지를받는다
docker image pull nginx
2. nginx docker 이미지를컨테이너로띄워본다// 만약8080 포트가있다면8081 등으로수정
docker container run -d   --name my-nginx   -p 8080:80nginx
3. nginx 를브라우저로접속확인해본다
localhost:8080
만약8080 port 로프로그램이켜있다면
-p 앞값을다른포트로ex) 18080:80
21(실습) 실행중인컨테이너확인하기Docker 
실습과정
4. 실행중인컨테이너확인하기
docker container ls
5. (심화) 컨테이너상세정보확인하기
docker container inspect my-nginx
6. 컨테이너로그확인
6-1. 컨테이너로그확인지속적으로확인(-f 옵션) 하면서브라우저접속해보기
→ 로그가들어오는것확인하기
22(실습) 실행중인컨테이너확인하기Docker 
실습과정
7. 컨테이너내부들어가보기
docker exec -it my-nginx bash
8. 컨테이너중지및삭제
docker container stop my-nginx
docker container rm my-nginx
8-1 이미지확인및삭제
docker image ls
docker image rm nginx
9. 삭제됐는지확인
docker container ls // docker ps 
docker image ls // docker images
23Docker 다른리소스Docker 
✔Docker Network
격리된컨테이너끼리혹은시스템과통신하기위한리소스
컨테이너는기본적으로서로분리된공간에서돌아가기때문에(자동연결되지않음)
이를연결할네트워크가필요
•포트매핑 -p 8080:80 
•컨테이너안에서호스트를가리키는주소 host.docker.internal 
✔Docker Volume
데이터는컨테이너밖에저장하기위한리소스
기본적으로수명이짧은실행환경이라서, 지우면데이터도같이사라진다. 
만약데이터가중요하다면데이터는컨테이너바깥에따로저장2407 -03
Docker 복잡하고반복적인설정/명령어관리25docker run 의단점Docker 
올릴docker 컨테이너가 너무많아+ 명령어옵션이너무많아
실제개발환경에서는보통컨테이너가1개가아니라여러개가필요
•웹서버(nginx 또는node 서버)
•데이터베이스(MySQL)
•캐시서버(Redis)
•메시지큐(Kafka)
•백엔드API 서버
컨테이너하나당매번docker run 명령으로직접쳐야하는것들
•이미지 이름
•포트 매핑
•환경변수
•볼륨
•네트워크 설정26docker-compose 란?  Docker 
https://dev.to/waji97/docker-compose-management-1d84\"docker-compose.yml \" 파일로 컨테이너 설정을관리한다
여러개의docker run 설정을하나의파일(docker-compose.yml)로
관리해서한번에실행·정리할수있게해주는도구
•팀전체환경을하나의파일에서관리할수있어서공유가편함
•up / down 
#version: '3.8'         # docker-compose 의 버전 정의
services :    # 서비스(컨테이너) 정의
서비스이름 :        # 서비스 이름 (임의로 지정 가능 )
image: 이미지명
container_name : 컨테이너이름 (선택사항)
ports:
-\"호스트포트:컨테이너포트\"
volumes :
-\"호스트경로:컨테이너내부경로\"
environment :
환경변수명 : 값
networks :
-네트워크명
networks :    # 사용할 네트워크 정의
네트워크명 :
driver: bridge (기본값)
volumes :      # 사용할 볼륨 정의
볼륨명:
driver: local (기본값)
27docker-compose.yml 파일Docker 
https://dev.to/waji97/docker-compose-management-1d84services: 컨테이너 정의들
images: 무슨이미지를컨테이너로띄울지
container_name: 이름을직접지정
ports: docker network 와로컬네트워크의포트연결
8080:80
앞이내컴퓨터포트뒤가docker 컨테이너내포트
3306:3306
port는같지만두네트워크는다른곳#version: '3.8'         # docker-compose 의 버전 정의
services :    # 서비스(컨테이너) 정의
서비스이름 :        # 서비스 이름 (임의로 지정 가능 )
image: 이미지명
container_name : 컨테이너이름 (선택사항)
ports:
-\"호스트포트:컨테이너포트\"
volumes :
-\"호스트경로:컨테이너내부경로\"
environment :
환경변수명 : 값
networks :
-네트워크명
networks :    # 사용할 네트워크 정의
네트워크명 :
driver: bridge (기본값)
volumes :      # 사용할 볼륨 정의
볼륨명:
driver: local (기본값)
28docker-compose.yml 파일Docker 
https://dev.to/waji97/docker-compose-management-1d84services: 컨테이너 정의들
volumes: 호스트와컨테이너간디렉토리공유
environment: 컨테이너환경변수설정(DB 초기설정등)
restart: 재시작정책(no, always, unless-stopped 등)
depends_on: 의존관계명시(기동순서기준, 의존성보장X)29(실습) docker-compose 로mysql 실행해보기Docker 
실습순서
1. infra/mysql/docker-compose.yml 파일
2. docker-compose 실행
3. docker-compose 안에정의된서비스컨테이너확인
4. 실행된서비스접속
5. 실행된서비스로그확인30(실습) docker-compose 로mysql 실행해보기Docker 
docker-compose.yml 예시파일
31(실습) docker-compose 로mysql 실행해보기Docker 
실습과정
1.infra/mysql/docker-compose.yml 파일
2. docker-compose 실행
docker-compose -d  up  
3. 실행된서비스컨테이너확인
docker-compose ps
4. 브라우저로접속
localhost:8080
4. 실행된서비스접속
docker-compose exec mysql bash
5. 실행된서비스로그확인 // mysql 자체log 가안찍히는버전
docker-compose  logs
3207 -04
docker network 
host.docker.internal
mysql 접속33mysql 접속클라이언트Docker 
adminer
docker-compose 파일내에adminer 포함
웹기반간단한mysql 관리툴
접속정보도
docker-compose.yml 에적혀있음
34Trouble shooting) 이미MySQL 이깔려있다면?Docker
port 가겹쳐서오류가날수있다. 
services:
mysql:
image: mysql:8.0
ports:
-\"3306:3306\"
environment :
-MYSQL_ROOT_PASSWORD=password
-MYSQL_DATABASE=llmagent
-MYSQL_USER=tester
-MYSQL_PASSWORD=tester
adminer :
image: adminer
restart: always
ports:
-\"8081:8080\"ports: 
앞부분을
塪塪塧塭 → 塪塪塧塮 로
변경35mysql 접속클라이언트Docker 
datagrip 으로접속하기
https://www.jetbrains.com/ko-kr/datagrip/
36docker compose 에두개이상서비스를띄운상황Docker 
Docker Network
패키지= 격리
docker 내부에있으면다소통될까?
도커컨테이너내부
로컬컴퓨터의네트워크
Port 포워딩
도커컨테이너내부로컬컴퓨터네트워크연결
host.docker.internal
도커내부에서로컬네트워크를가리키는예약어
37docker 쓰면인프라추가/ 삭제가깔끔하다Docker
docker 쓰는장점= 편하다
-인프라설정이어떻게작동하는지 테스트하기 좋다
만약수동설치였다면? 
-mysql 은컴퓨터 켜졌을 때자동으로 켜져서(백그라운드) 노트북의 리소스를 점유하고 있었을 수도
-설정이나 파일잘못건드렸다가 맨날메모리참조오류떠서고통받고있을수도
-삭제를해도설정파일이나 환경변수가 남아있어서 다음에 또설치했을 때문제가생길수도..38docker 이미지/리소스삭제Docker
docker rm / rmi / prune 
docker ps -a
docker {컨테이너 id} rm 
docker images
docker {docker image 명} rmi 
# prune: 사용되지 않는(unused) 이미지자동정리
docker image prune  
docker image prune --filter \"dangling=true\"
docker system prune -a -f39총정리Docker 
Docker 로인프라 설치를 대체
docker 아키텍처이해
docker 명령어
Docker-compose 로docker를더쉽게
docker-compose up /  down 
docker-compose 를통한인프라(외부의존성) 세팅www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 08 Understanding Databases and MySQL.pdf
문자 수: 6597
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3목표: MySQL 사용익히기DB
목차
Docker 필요성과구성요소
docker-compose 로mysql 실행및접속
DDL 실습
DML 실습
Select 심화프로젝트 : https://github.com/inspire12/upstage-infra-project.git408 -01
DB 개념
RDBMS와MySQL
query, table5DB(데이터베이스)의필요성DB 
데이터가 관리가 되지않으면? 
데이터파일관리지옥
여러사람이 접근하는 데이터충돌
검색, 저장속도저하
백업/복원 어려움6DB(데이터베이스)란?DB 
데이터를 구조적으로 저장·관리하는 시스템
데이터를 안전하게 저장하는 곳
빠르게찾기위한 도구
여러사용자가 동시에사 용가능
서비스의 기억저장소역할7Excel과유사한DBDB 
https://yozm.wishket.com/magazine/detail/1721/DB 용어
데이터베이스 : 하나의\"DB\"는여러개의테이블을포함
테이블: 데이터를넣는큰표(시트)
-스키마: 테이블설계도
컬럼: 표의열, 속성
로우(row): 한줄의데이터
PK(Primary Key): 각줄을구분하는고유ID
8DB 의종류DB 
목적에따라다양한 DB
RDB (관계형데이터베이스)
•MySQL, PostgreSQL
•표(테이블)로구성, SQL사용
NoSQL, Document DB
•MongoDB 등, 문서형태
캐시DB (key-value)
•Redis
Graph DB
9SQL이란?: Structured Query LanguageDB 
DB에게무엇을 할지말해주는 '구조화된 쿼리=질의 언어'
RDBMS조작표준언어, 선언형 언어
'어떻게'가 아니라 '무엇을' 조회하거나 수정하고 싶은지를 선언적으로 표현합니다.
기본문법구조
동사(명령어) + 대상(table, column) + 조건
•SELECT: 조회
•INSERT: 추가
•UPDATE: 수정
•DELETE: 삭제10SQL 의종류DB 
DDL: 데이터베이스의 \"구조\"를 정의하거나 변경하는 SQL 명령어
집을짓거나리모델링(설계도제작)
•Createdatabase / table / index
•Drop database / table / index
DML: 데이터베이스의 \"데이터\"를 추가, 조회, 수정, 삭제하는 SQL 명령어
•가구나물건을집안에넣거나빼는작업
•SELECT
•INSERT (Save) table
•UPDATE table
•DELETE table
DCL: 권한
TCL: 트랜잭션11MySQL
RDBMS
query, table
Datagrip 으로DB 연결08 -0212MySQLDB 
https://www.oracle.com/kr/mysql/what-is-mysql/MySQL 란?
데이터저장및관리에 사용되는 오픈소스관계형데이터베이스 관리시스템(RDBMS)입니다.
안정성, 성능, 확장성, 사용편의성 을 갖춘MySQL는개발자들에게 널리사용되는 중입니다
MySQL를 배워놓으면 PostgreSQL 이나Oracle 도빠르게습득13MySQL 일단시작해보자DB 
Docker-compose 를통한MySQL 실행
git clone https://github.com/inspire12/upstage-infra-project.git
git fetch --all
git switch start
프로젝트내
infra/mysql/docker-compose.yml
cd infra/mysql
docker-compose up -d 
14docker-compose 파일에서접속정보확인하기DB 
MySQL 란?
host:  localhost
port: 3306
user: tester
password: tester
database: llmagentservices:
mysql:
image: mysql:8.0
ports:
-\"3306:3306\"
environment :
-MYSQL_ROOT_PASSWORD=password
-MYSQL_DATABASE=llmagent
-MYSQL_USER=tester
-MYSQL_PASSWORD=tester
adminer :
image: adminer
restart: always
ports:
-\"8081:8080\"15datagrip 으로연결해보기DB 
datasource > 접속정보 입력
1608 -03
Data Definition Language
create database
create table
column 타입
primary key, auto increment17요구사항: 프로젝트에유저기능을붙여보자DB 
User 데이터 저장할 테이블 설계
일단개인정보, 인증관련 생각없이진행
•User 가리키는id 는저장시자동생성
•name 필요
•가입날짜자동생성https://github.com/inspire12/upstage-infra-project
git switch feature/sql
git pull
infra/sql  
파일 참조 부탁드립니다18database, table DB 
데이터를 저장할 틀이우선필요하다
CREATE DATABASE db명;
데이터베이스틀을만드는가장기본문법
CREATE TABLE 테이블명(컬럼정의…);
•테이블이름+ 컬럼목록을괄호안에선언합니다.
테이블을수정하는문법으로, ADD/MODIFY/DROP을활용
•ALTER TABLE 테이블명ADD 컬럼명타입;
•ALTER TABLE 테이블명MODIFY 컬럼명타입;
•ALTER TABLE 테이블명DROP 컬럼명;
아예구조자체를삭제합니다.
•DROP DATABASE db명;
•DROP TABLE 테이블명;19database, table DB 
데이터베이스 생성및사용지정
테이블생성및사용지정20Table 생성시고려할것들DB 
PK, 데이터선택
pk 설정필수
auto increment id 사용
데이터타입선택주의
default 값설정
not null 제약
unique 제약
index 생성기준pk 설정 필수 / auto increment id 사용
모든 테이블의 고유 식별자 , 반드시 있어야 성능 우위 , 일반적으로 정수
형Auto Increment 를 사용21Table 생성시고려할것들DB 
데이터타입선택
타입을잘못선택하면인덱스효율이나빠지고, 불필요한저장공간을사용하고, 조회성능이떨어진다
•숫자데이터는 INT를기본으로쓰고, 사용자수나로그가매우많아질가능성이있으면 BIGINT
•문자는varchar(허용문자길이), 길이를정할수있으면길이지정, 성능과저장공간측면에서중요
•매우긴텍스트(예: 프롬프트, AI agent 로그)는 TEXT타입
•Boolean 값은MySQL에서는실제boolean 타입이tinyint(1)로처리
•날짜/시간정보는 DATETIME 이나TIMESTAMP 사용해야검색·정렬이정확
•가격, 포인트, 금액처럼계산정확도가필요한데이터는 DECIMAL22Table 생성시고려할것들DB 
default 값설정
값이주어지지않았을때의기본값을지정해데이터일관성
not null 제약
비어있으면안되는중요한컬럼에반드시적용
unique 제약
이메일처럼중복되면안되는컬럼
index 생성기준
검색성능과직결, where 절에자주쓰는컬럼에만선택적으로설정추가옵션2308 -04
Data Manipulation Language
CRUD 
-Insert
-Read (Select)
-Update
-Delete24InsertDB 
새로운행(row)을테이블에 삽입
INSERT INTO 테이블명 (컬럼1, 컬럼2)
VALUES (값1, 값2);INSERT INTO users (name, email)
VALUES ('kim', 'kim@naver.com');
INSERT INTO users (name, email)
VALUES ('kim', 'kim@upstage.ai'),
('seo', 'seo@upstage.ai'),
('kim', 'kim12@upstage.ai');한 번에 여러 줄을 넣을 수도 있다25SelectDB 
어떤데이터를 가져올지 선언하는 문법
SELECT 컬럼1, 컬럼2
FROM 테이블명
WHERE 조건SELECT id, name
FROM users
WHERE name = 'kim';
SELECT * FROM users
WHERE id >= 3;
SELECT * FROM users
WHERE age >= 20 AND age <= 30;
SELECT * FROM users
WHERE NOT (name = 'kim);26UpdateDB 
기존데이터 수정
UPDATE 테이블명
SET 컬럼= 값
WHERE 조건;UPDATE users
SET name = 'lee'
WHERE id = 1;
SELECT * form 
WHERE id = 1;
UPDATE users SET name = 'lee' 
WHERE id = 1;조건(where)을 반드시 사용해야 안전
select 를 먼저 하고 변경하는 식으로 진행27DeleteDB 
WHERE 조건없이delete 하면테이블전체데이터 삭제됨(주의)
DELETE FROM 테이블명
WHERE 조건;DELETE FROM users
WHERE id = 1;
조건(where)을 반드시 사용해야 안전
select 를 먼저 하고 변경하는 식으로 진행
SELECT * FROM users
WHERE id = 1;
DELETE FROM users
WHERE id = 1;2808 -0529범위검색DB 
기간/ prefix
기간검색(date)
부분검색 (prefix)SELECT * FROM users
WHERE created_at BETWEEN '2025-11-01' AND '2026-02-28';
SELECT *
FROM conversations
ORDER BY created_at DESC;30비교조건DB 
정렬/ 개수제한
ORDER BY 컬럼ASC|DESC;
LIMIT 개수;SELECT *
FROM conversations
ORDER BY created_at DESC;
SELECT *
FROM conversations
ORDER BY created_at DESC
LIMIT 3;3108 -06
인덱스
트랜잭션32요구사항: 유저대화를저장해보자DB 
대화(conversations) 데이터 저장할 테이블 설계
1.어떤유저가 물어봤는지
2.최신대화를 알고싶다https://github.com/inspire12/upstage-infra-project
infra/sql  
안 쿼리 파일 참조
33DB(데이터베이스)란?DB 
데이터를 구조적으로 저장·관리하는 시스템
데이터를 안전하게 저장하는 곳
여러사용자가 동시에사 용가능
서비스의 기억저장소역할빠르게찾기위한 도구인덱스34인덱스DB 
데이터를 빠르게 찾기위한정렬된 목차생성
검색속도를 위한목차생성
where 조건(검색) 컬럼에적용
insert update 시인덱스도 같이수정하게 된다
35인덱스사용법DB 
추가/ 제거/ 테이블생산시추가
CREATE INDEX 인덱스명
ON 테이블명 (컬럼1, 컬럼2, ...);
DROP INDEX 인덱스명CREATE INDEX idx_user_created
ON conversations (user_id, created_at);
DROP INDEX idx_user_created
ON conversations;
36(심화)정렬이되어있으면왜검색이빠르지? DB 
이진검색
기존탐색은 전체를 한번확인해야한다 O(n)
정렬이되면반으로 나누면서 검색할수있다O(log 2N)
MySQL은 기본적으론 PK 기준으로 정렬되며 저장
PK (Auto Increment) 를통한검색이 가장빠름
만약Auto Increment가아니라랜덤,분산값을 쓰면insert 속도가느릴수있다
(들어갈 위치를 매번찾게된다면)
37큰대화데이터에서인덱스유무로속도비교DB 
실습순서
1. conversations 인덱스제거
2. 큰데이터 입력 (속도가 오래걸릴수있어서 주의)
3. select 확인(+성능)
4. conversations 인덱스추가
5. select 확인(+성능)38큰대화데이터에서인덱스유무로속도비교DB 
실습순서
1. conversations 인덱스제거
2. 큰데이터 입력(테스트를 위해프로시저 이용)
3. select 확인(+성능)
4. conversations 인덱스추가
5. select 확인(+성능)
39못다한DB 개념들DB 
알아야할 DB 개념
집계함수
mysql 함수
트랜잭션
조인
서브쿼리
실행계획
격리수준
등등40총정리DB 
MySQL 사용법
DDL: 저장구조를정의하는 SQL
DML: 데이터조작을요청하는SQL
MySQL 에서CRUD 
Select 추가사용방법
검색성능을 위한index www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 09 Managing MySQL on a Server.pdf
문자 수: 5692
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3목표: Python으로DB 데이터를다루고서버로확장Python 서버와DB
목차
Python에서MySQL 다루기
커넥션풀
안전한저장을위한트랜잭션409 -01
python 
MySQL 
Connection5왜프로그램으로DB를다뤄야할까?Python 서버와DB 
사람이직접DB를사용하면?
사람이직접DB에들어가서
INSERT 하고SELECT 하는방식은
수동, 반복, 느림, 오류이라는문제6왜프로그램으로DB를다뤄야할까?Python 서버와DB 
프로그래밍의장점= 반복, 데이터처리
데이터자동처리–대화저장, 로그기록, 통계계산을 코드로 자동화
대량데이터 처리가능–수천~수만 건을빠르게 처리
동시에여러요청처리–서비스환경에서 필수
반복되는 로직자동화–매번SQL을수동으로 칠필요없음
서비스내부로직과 연결가능–예: AI Agent의대화내역저장
7Python -DB 연결과정Python 서버와DB 
Python DB 연결과정과 용어
DB 드라이버(pymysql 등)
python 과mysql 연결통역기역할
connection
Python ↔ MySQL 서버사이통로
생성비용높음
cursor
SQL을보내고결과를받는도구(작업자)8Python -DB 연결과정Python 서버와DB 
Python DB 연결과정과 용어
execute
문자열sql 실행
파라미터바인딩사용(%s)
fetchone / fetchall
select 결과조회
commit
데이터조작시(insert/update/delete) 반영
rollback
오류시되돌리기
close
커넥션/커서종료, 자원반환
9(실습) Python -DB 연결과정Python 서버와DB 
실습순서
Python이 MySQL과 대화하려면 드라이버가 필요
1.uv add pymysql로 설치
○uv add cryptography 도설치
○ .env 파일생성후db_user / db_password 입력
2.pymysql.connect(...)로 MySQL 서버에 연결(Connection)
3.conn.cursor()로 커서(Cursor) 생성
4.cursor.execute(\"SQL...\")로 쿼리실행
5.fetchone(), fetchall()로결과가져오기
6.Cursor 반납
7.마지막에 conn.close()로연결 종료10DB 연결테스트Python 서버와DB 
import pymysql
def connection ():
conn = pymysql.connect(
host=\"localhost\" ,
port=3306,
user=\"tester\",
password =\"tester\",
database =\"llmagent\" ,
charset=\"utf8mb4\" ,
)
try:
with conn.cursor() as cursor:
cursor.execute( \"SELECT 1\" )
row = cursor.fetchone()
print(row)
finally:
conn.close()
if __name__ == '__main__' :
connection()git switch feature/crud/cr
git pull
uv sync
혹시 프로젝트 실행 시
RuntimeError: 'cryptography' package is required for 
sha256_password or caching_sha2_password auth 
methods ..
에러 발생시
uv add cryptography    실행해주세요
.env 파일 생성
1109 -02
python 
MySQL 
Connection12실습을하기전팁Python 서버와DB 
브랜치별 실습코드분리
Sourcetree 에서전체작업을확인가능
fix/uvadd .. 
의존성초반추가..
13유저등록: Create = InsertPython 서버와DB 
실습과정def create_user (name: str, email: str):
conn = pymysql.connect(
host=\"localhost\" ,
port=3306,
user=\"root\",
password =\"password\" ,
database =\"llmagent\" ,
charset=\"utf8mb4\" ,
cursorclass =pymysql.cursors.DictCursor,
)
try:
with conn.cursor() as cursor:
sql = \"\"\"
INSERT INTO users (name, email)
VALUES (%s, %s) \\
\"\"\"
cursor.execute( sql, (name, email))
conn.commit()
finally:
conn.close()결과
git switch feature/crud/cr
git pull
uv sync14유저등록: Read = SelectPython 서버와DB 
실습과정 결과def get_user_by_email (email: str):
conn = pymysql.connect(
host=\"localhost\" ,
port=3306,
user=\"root\",
password =\"password\" ,
database =\"llmagent\" ,
charset=\"utf8mb4\" ,
cursorclass =pymysql.cursors.DictCursor,
)
try:
with conn.cursor() as cursor:
sql = \"\"\"
SELECT id, name, email, created_at
FROM users
WHERE email = %s \\
\"\"\"
cursor.execute( sql, (email,))
return cursor.fetchone()
finally:
conn.close()
select 는
commit 필요없다15잠깐! conn 부분이이렇게매번반복되잖아? Python 서버와DB 
요청마다 conn을새로만드는 방식은 매우비효율적
1.TCP 연결
1.MySQL 인증과정(user/password)
1.세션초기화
1.버퍼준비
매연결마다 반복16connection poolPython 서버와DB 
connection 을미리만들고재사용하면 효율적이지 않을까?
프로그램 시작시conn 5 ~ 10개정도미리만들어둠
요청이 들어오면 풀에서 하나꺼내주고
작업완료되면 다시풀로돌려보냄(반납)
•conn 생성비용절감
•DB 서버부하감소
•병렬요청가능(멀티스레드/멀티 워커)
•안정적인 서비스 운영가능17(실습) connection pool 개발Python 서버와DB 
실습순서
1. connection pool 클래스 생성
-순차적connection 배분을 위해queue 를생성
-connection pool 생성단계에서 정해진개수만큼connection 을만들고 저장
2. connection pool 생성시db 연결정보 전달
3. 연결요청시커넥션을 순차적으로 전달
-만약연결이 끊겼으면 재연결
5. connection으로db 작업수행후반환18(실습) connection pool 개발Python 서버와DB 
실습과정
import pymysql
from queue import Queue
class PymysqlConnectionPool :
def __init__(self, maxsize =5, **db_params ):
self._pool = Queue( maxsize )
self._db_params = db_params
for _ in range(maxsize ):
self._pool.put( self._create_conn())
def _create_conn (self):
return pymysql.connect(
charset=\"utf8mb4\" ,
cursorclass =pymysql.cursors.DictCursor,
**self._db_params,
)def get_conn (self):
# 큐에서커넥션하나가져옴(없으면대기)
conn = self._pool.get()
# 혹시끊겨있으면재연결
try:
conn.ping(reconnect =True)
except Exception :
conn = self._create_conn()
return conn
def release_connection (self, conn):
# 풀에커넥션되돌려놓기
self._pool.put( conn)
def close_all (self):
# 프로그램종료시풀안의모든커넥션정리
while not self._pool.empty():
conn = self._pool.get()
conn.close()git switch feature/crud/connectionpool
git pull
uv sync
100 번을했을때
커넥션이유지가되나?
19(실습) connection pool 개발후반영Python 서버와DB 
실습과정
 실제데이터오는지확인
없다면저장했는지확인20(실습) 유저등록: UpdatePython 서버와DB 
실습과정
결과
git switch feature/crud/ud
git pull
uv sync
main.py
1 슬라이드 20
1  이 부분 텍스트가 강의 녹화시 강의자님께 가릴 것 같습니다 !
Gio Paik, 2025-12-1021(실습) 유저등록: DeletePython 서버와DB 
실습과정
 main.py
결과
22(실습) 유저대화도마찬가지CRUDPython 서버와DB 
실습과정 :대화저장/ 최근대화목록조회git switch feature/crud/conversation
git pull
uv sync
2309 -03
데이터정합성을위한트랜잭션
원자성24요구사항: 유저질문과에이전트응답을동시에저장해주세요Python 서버와DB 
두가지쿼리가 동시에 일어나는 경우
ex) 유저질문, 에이전트 응답이 쌍인데, 한쪽이저장이 안될경우ai 품질이상발견
한쪽이저장안되면차라리둘다저장안되게 해주세요
한쪽이 실패했을때둘다실패25트랜잭션이란? Python 서버와DB 
https://rebro.kr/162DB의작업단위
여러작업을 하나의 단위로 묶는기능
Atomicity(원자성) —모두성공하거나(None) 모두실패
Consistency(일관성) —데이터무결성유지
Isolation(격리성) —다른트랜잭션 간간섭제거
Durability(지속성) —commit 후영구반영됨26(실습) 두요청저장Python 서버와DB 
실습과정
둘다성공한경우
둘다저장됐는지 확인git switch feature/crud/transaction
git pull
uv sync27두요청저장실패Python 서버와DB 
실습과정
한쪽만성공한 경우
둘다실패되는지 확인
28총정리Python 서버와DB 
Python 에서DB 연결과정
Connection Pool 의필요성
Transaction과 원자성Python 에서SQL 실행www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: 10 Maintainable Architecture.pdf
문자 수: 5616
────────────────────────────────────────────────────────────

SPEAKER
서영학© 2025 Upstage Co., Ltd.2저작권안내
(주)업스테이지가 제공하는 모든교육콘텐츠의지식재산권은
운영주체인 (주)업스테이지 또는해당저작물의 적법한 관리자에게 귀속되어 있습니다.
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할수없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수있는 저작물을 작성, 공개하는 행위
● 제공된 데이터의 일부 혹은전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위3목표: 역할별로레이어를나누고DB를편하게쓰자계층형아키텍처와ORM
목차
역할별로나눈계층형아키텍처소개
mysql table과model의괴리: ORM
SQLAlchemy 사용법4현상황진단계층형아키텍처
main.py 에모든로직이몰려있다
main.py 가너무비대해진다
•수정이 어렵다
•테스트 어렵다
•역할이 모호하다
510 -01
-역할에맞는레이어분리
-api layer -service layer -repository layer 책임분리6현상황진단계층형아키텍처
https://www.codeit.kr/tutorials/194/mvc-pattern-and-layered-architecturemain.py 에로직을 역할별로생각
•실행하는 부분(요청받는부분)
•DB 연결만들기
•SQL 실행
•비즈니스 로직처리
•응답생성7계층형(레이어드) 아키텍처구조계층형아키텍처
route / service / repository 구조로 책임을 분리
route
•요청받기
•입력검증
•service 호출
service
•비즈니스 로직
•트랜잭션 제어
•repository 호출repository
•db 접근
•sql 실행
•데이터 반환
core
•db 연결
•설정8(실습) 레이어드아키텍처구조로변경계층형아키텍처
실습순서
1. 패키지구조먼저
2. main.py 에있는db 관련소스
(connection, connection_pool) core 로이전
3. main.py 안에있는db 쿼리호출repository chat/user로구분해서이동
4. main.py main 실행부분route/cli_routes.py 로이동
5. cli_routes.py 에서실행할service 파일chat/user 로구분해서생성
6. main 지우고cli_routes.py 를통해작업실행
9(실습) layer = 계층, 우선패키지구조부터잡자계층형아키텍처
실습과정
1. 패키지 구조먼저
app 폴더안에묶은이유
-애플리케이션코드를한곳
-프로젝트의실제동작로직(개발자가만든)이들어가는영역
•api (라우트)
•service (비즈니스로직)
•repository (DB 처리)
•core (환경, 설정)
•models (데이터구조)
git switch feature/layered/start
git pull
uv sync10(실습) 레이어드아키텍처구조로변경계층형아키텍처
실습과정
2. main.py 에있는db 관련소스(connection, connection_pool) core 로이전
3. main.py 안에있는db 쿼리호출repository chat/user로구분해서 이동
git switch feature/layered/refactor
git pull
uv sync11(실습) 레이어드아키텍처구조로변경계층형아키텍처
실습과정
4. main.py main 실행부분 route/cli_routes.py 로이동
5. cli_routes.py 에서실행할 service 파일chat/user 로구분해서 생성
6. main 지우고cli_routes.py 를통해작업실행
git switch feature/layered/complete
git pull
uv sync12역할을분리하고계층화하여복잡도를낮춘다.계층형아키텍처
한레이어는 한가지책임에만 집중하게 하자
변경영향최소화: DB가바뀌어도 Service 로직은 그대로
테스트용이: Service를DB 없이도 단위테스트가능
읽기쉬운흐름: \"요청→ 서비스→ 저장소\"로 생각하기 쉬움
역할을분리하고 계층화하여 복잡도를 낮춘다.
안전성과 유지보수성을 높이기 위한설계철학기반.
각계층간명확한 책임분리(Separation of Concerns) 지향
1310 -02
table 과model14코드에SQL 를그대로쓴다면? ORM
raw sql 반복증가
repository 복잡증가
필드추가시sql 수정 필요
유지보수비용증가
서비스성장대비어려움
table 을코드와매핑해볼수있을까?
15ORM 이란?ORM
객체지향프로그래밍 언어의객체와
관계형데이터베이스의 테이블을 자동으로 연결(Mapping)해주는 기술
SQL 대신객체중심의코드로데이터조작
코드의변경→ DB 변경스트레스최소화16ORM이제공하는핵심기능ORM
ORM 을쓰면좋은점들
객체와테이블의매핑: 클래스↔ 테이블, 객체필드↔ 테이블컬럼연결자동화
CRUD 기능자동화: 생성(Create), 읽기(Read), 수정(Update), 삭제(Delete) 작업을객체중심으로제공
영속성관리(Persistence Context): 객체의상태(생성, 수정, 삭제)를추적하고DB에자동동기화
트랜잭션관리: 데이터의일관성보장(Transaction commit, rollback 자동관리)
객체지향쿼리지원: JPQL(자바), Django ORM(Python) 등객체중심의쿼리제공17SQLAlchemy 이란?ORM
python 기반ORM 도구
개발자가SQL 쿼리문을직접작성하는대신, 파이썬객체지향코드를사용하여데이터베이스와상호작용
할수있도록도와준다
ORM 기능외에도, 파이썬코드로SQL 표현식을구성하고실행할수있는저수준(low-level) 기능을제공
다양한데이터베이스시스템(SQLite, PostgreSQL, MySQL, Oracle, Microsoft SQL Server 등)을지원
Session객체를통해데이터베이스연결을관리하고트랜잭션을효율적으로제어18SQLAlchemy 구성요소: Engine ORM
Engine
데이터베이스와의실제연결을담당하는객체
커넥션풀관리
DB URL 기반생성
모든ORM 동작의출발점19SQLAlchemy 구성요소: Session ORM
Session
ORM 작업단위(트랜잭션포함)
add / commit / rollback / query 실행
DB 연결을추상화한고수준API20SQLAlchemy 구성요소: Base ModelORM
Base Model
ORM 테이블매핑의부모클래스
Column, Integer, String 등SQLAlchemy 타입정의
클래스= 테이블구조표현21SQLAlchemy: ORM MappingORM
db 테이블→ 객체클래스 매핑
22SQLAlchemy 에서Model을통해쿼리요청하기ORM
CRUD
ORM에서 CRUD는SQL을직접쓰는대신Python 객체를추가·조회·수정·삭제하는방식
insert: session.add(model)
select: session.query(Model).filter().first() / all()
update: 객체수정후commit
delete: session.delete(instance) 후commit23INSERTORM
INSERT
session = SessionLocal()
user = User(name=\"kim\", email=\"kim@test.com\")
session.add(user)
session.commit()        # 실제INSERT 발생
session.refresh(user)   # DB가생성한PK(id) 등최신값적용24SELECTORM
SELECT
session = SessionLocal()
# 단일조회
user = session.query(User).filter(User.email == \"kim@test.com\").first()
# 여러개조회
users = session.query(User).all()
# 특정조건조회
users = session.query(User).filter(User.name == \"kim\").all()25UPDATEORM
UPDATE
user = session.query(User).filter(User.id == 1).first()
user.name = \"lee\"     # 객체필드수정
session.commit()      # UPDATE SQL 자동실행26DELETEORM
DELETE
user = session.query(User).filter(User.id == 1).first()
session.delete(user)
session.commit()27(실습) sqlalchemy 로기존query를orm 으로변경ORM
실습순서
1. sqlalchemy 설치
2. sqlalchemy 연결, 기존connection 객체를sql_alchemy 객체로변경
3. user, conversation 테이블모델매핑
4. user, conversation  query 수정
5. serializer 를통해응답값수정
28(실습) sqlalchemy 로기존query를orm 으로변경ORM
실습순서
1. sqlalchemy 설치
uv add sqlalchemy
2. sqlalchemy 연결, 기존connection 객체를sql_alchemy 객체로변경(app/core/db.py)
3. user, conversation 테이블모델매핑
app/models/base.py
app/models/user.py
git switch feature/orm/conn
git pull
uv sync29(실습) sqlalchemy 로기존query를orm 으로변경ORM
실습순서
4. user, conversation  query 수정git switch feature/orm/query
git pull
uv sync
app/repository/user_repository.py305. serializer 를통해응답값수정ORM
실습과정
기존응답
json 형태( map/dict ) 로바꾸기위한라이브러리설치
uv add sqlalchemy-serializer
table 모델코드에반영
결과
git switch feature/orm/serializer
git pull
git sync31총정리계층형아키텍처와ORM
역할에따라코드를 layer로나눌수있다
Route, Service, Repository
ORM 필요성과 SQLAlchemy 통해ORM 구현하기
Table과Model 연결(Mapping)
Model 을통해SQL 쿼리요청하기
ORM 은Repository의책임32Complete33개발환경수업총정리개발환경
개발환경개선
혼자하는 개발에서 여럿이
git commit, branch 
github
issue -pr -code review -mergeIDE, 개발도구들
uv, pyproject.toml외부의존성 다루기
docker 구성요소사용법
docker-compose
DB 을통한데이터 관리
SQL 사용법, Where 최적화
DB 연결관리앞으로 개발 속도 + 공부 속도를 높여줄 개발 환경 개선
유지보수를 위한리팩토링
코드책임에따른리팩토링
테이블과 객체 관계 ORM www.upstage.ai © 2025 Upstage Co., Ltd.



────────────────────────────────────────────────────────────
파일: SeSAC_CS with AI_Guide.pdf
문자 수: 0
────────────────────────────────────────────────────────────



"""
    s.raw_texts['SeSAC_CS with AI_Guide.txt'] = """"""
    return s

def print_summary():
    s = get_summary()
    print("Week:", s.week)
    print("Files count:", len(s.files))
    print("Tech stack:", s.tech_stack)