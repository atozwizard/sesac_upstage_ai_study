from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class WeekSummary:
    week: str = ""
    files: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)
    raw_texts: Dict[str, str] = field(default_factory=dict)

def get_summary() -> WeekSummary:
    s = WeekSummary(week="04.4주차_네트워크와클라우드")
    s.files = ['(EXT) [SeSAC] [네트워크와 클라우드] 코랩 세션_Wrap Up 리포트 (template)의 사본.pdf', '00.project\\upstage-keypair.pem', '00.project\\upstage-network-lecture\\.env', '00.project\\upstage-network-lecture\\.env.example', '00.project\\upstage-network-lecture\\.github\\ISSUE_TEMPLATE\\lecture_sample.yml', '00.project\\upstage-network-lecture\\.github\\workflows\\deploy.yml', '00.project\\upstage-network-lecture\\.gitignore', '00.project\\upstage-network-lecture\\.pytest_cache\\.gitignore', '00.project\\upstage-network-lecture\\.pytest_cache\\CACHEDIR.TAG', '00.project\\upstage-network-lecture\\.pytest_cache\\README.md', '00.project\\upstage-network-lecture\\.pytest_cache\\v\\cache\\lastfailed', '00.project\\upstage-network-lecture\\.pytest_cache\\v\\cache\\nodeids', '00.project\\upstage-network-lecture\\.python-version', '00.project\\upstage-network-lecture\\README.md', '00.project\\upstage-network-lecture\\__pycache__\\main.cpython-312.pyc', '00.project\\upstage-network-lecture\\__pycache__\\test_todo.cpython-313-pytest-8.4.2.pyc', '00.project\\upstage-network-lecture\\app\\__init__.py', '00.project\\upstage-network-lecture\\app\\__pycache__\\__init__.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\__pycache__\\deps.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\__pycache__\\exceptions.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\__pycache__\\logging.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\api\\route\\__pycache__\\user_routers.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\api\\route\\user_routers.py', '00.project\\upstage-network-lecture\\app\\core\\__pycache__\\db.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\core\\db.py', '00.project\\upstage-network-lecture\\app\\exceptions.py', '00.project\\upstage-network-lecture\\app\\models\\__pycache__\\__init__.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\models\\entities\\__init__.py', '00.project\\upstage-network-lecture\\app\\models\\entities\\__pycache__\\__init__.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\models\\entities\\__pycache__\\base.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\models\\entities\\__pycache__\\users.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\models\\entities\\base.py', '00.project\\upstage-network-lecture\\app\\models\\entities\\conversation.py', '00.project\\upstage-network-lecture\\app\\models\\entities\\role.py', '00.project\\upstage-network-lecture\\app\\models\\entities\\users.py', '00.project\\upstage-network-lecture\\app\\models\\schemas\\__pycache__\\__init__.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\models\\schemas\\__pycache__\\user.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\repository\\__pycache__\\user_repo.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\repository\\user_repo.py', '00.project\\upstage-network-lecture\\app\\service\\__pycache__\\user_service.cpython-312.pyc', '00.project\\upstage-network-lecture\\app\\service\\user_service.py', '00.project\\upstage-network-lecture\\docker-compose.yml', '00.project\\upstage-network-lecture\\infra\\mysql\\docker-compose.yml', '00.project\\upstage-network-lecture\\infra\\sql\\1-create-users.ddl', '00.project\\upstage-network-lecture\\infra\\sql\\2-crud-users.ddl', '00.project\\upstage-network-lecture\\infra\\sql\\3-select-users.ddl', '00.project\\upstage-network-lecture\\infra\\sql\\4-create-conversations.ddl', '00.project\\upstage-network-lecture\\infra\\sql\\5-bulkinsert-conversations.ddl', '00.project\\upstage-network-lecture\\infra\\sql\\6-index-conversations.ddl', '00.project\\upstage-network-lecture\\logs\\app.log', '00.project\\upstage-network-lecture\\main.py', '00.project\\upstage-network-lecture\\pyproject.toml', '00.project\\upstage-network-lecture\\services\\__init__.py', '00.project\\upstage-network-lecture\\services\\ai_agent.py', '00.project\\upstage-network-lecture\\template\\__init__.py', '00.project\\upstage-network-lecture\\test_todo.py', '00.project\\upstage-network-lecture\\uv.lock', '01.강의자료\\00 Course Introduction.pptx.pdf', '01.강의자료\\01 Understanding Web Communication and HTTP.pdf', '01.강의자료\\02 Network Fundamental Knowledge.pdf', '01.강의자료\\03 Getting Started with Cloud Computing.pdf', '01.강의자료\\04 Managing Cloud Servers.pdf', '01.강의자료\\05 Web Server User Service 1.pdf', '01.강의자료\\06 Web Server User Service 2.pdf', '01.강의자료\\07 Cloud Deployment Automation 1.pdf', '01.강의자료\\09 Getting Started with Cloud Exploring AWS Components.pdf', '01.강의자료\\1-08 Cloud Deployment Automation 2.pdf', '01.강의자료\\1-Why Cloud Computing Is Essential for AI Agent.pdf', '01.강의자료\\2-10 Network and AI.pdf', '01.강의자료\\Why CI_CD Is Essential  for AI Agent.pdf', '01.강의자료\\Why Operational and AI Infrastructure Integration Is Essential for AI Agent (1).pdf', '01.강의자료\\Why Operational and AI Infrastructure Integration Is Essential for AI Agent.pdf', '01.강의자료\\Why Web Server Development Is Essential for AI Agent.pdf', '02.daily mission\\[SeSAC] [네트워크와 클라우드] basic mission_day01_answer의 사본.pdf', '02.daily mission\\[SeSAC] [네트워크와 클라우드] basic mission_day02_answer의 사본.pdf', '02.daily mission\\[SeSAC] [네트워크와 클라우드] basic mission_day03_answer의 사본.pdf', '02.daily mission\\[SeSAC] [네트워크와 클라우드] basic mission_day04_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [네트워크와 클라우드] advanced mission_day01_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [네트워크와 클라우드] advanced mission_day02_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [네트워크와 클라우드] advanced mission_day03_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [네트워크와 클라우드] advanced mission_day04_answer의 사본.pdf', '03.advanced mission\\[SeSAC] [네트워크와 클라우드] advanced mission_day05_answer의 사본.pdf', '04.4주차_네트워크와클라우드_module.py', 'README_GENERATED.md', 'README_TECHSTACK.md', 'README_TECHSTACK_DRAFT.md', '__pycache__\\04.4주차_네트워크와클라우드_module.cpython-313.pyc', 'extracted_content\\(EXT) [SeSAC] [네트워크와 클라우드] 코랩 세션_Wrap Up 리포트 (template)의 사본.txt', 'extracted_content\\00 Course Introduction.pptx.txt', 'extracted_content\\01 Understanding Web Communication and HTTP.txt', 'extracted_content\\02 Network Fundamental Knowledge.txt', 'extracted_content\\03 Getting Started with Cloud Computing.txt', 'extracted_content\\04 Managing Cloud Servers.txt', 'extracted_content\\05 Web Server User Service 1.txt', 'extracted_content\\06 Web Server User Service 2.txt', 'extracted_content\\07 Cloud Deployment Automation 1.txt', 'extracted_content\\09 Getting Started with Cloud Exploring AWS Components.txt', 'extracted_content\\1-08 Cloud Deployment Automation 2.txt', 'extracted_content\\1-Why Cloud Computing Is Essential for AI Agent.txt', 'extracted_content\\2-10 Network and AI.txt', 'extracted_content\\Why CI_CD Is Essential  for AI Agent.txt', 'extracted_content\\Why Operational and AI Infrastructure Integration Is Essential for AI Agent (1).txt', 'extracted_content\\Why Operational and AI Infrastructure Integration Is Essential for AI Agent.txt', 'extracted_content\\Why Web Server Development Is Essential for AI Agent.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] advanced mission_day01_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] advanced mission_day02_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] advanced mission_day03_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] advanced mission_day04_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] advanced mission_day05_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] basic mission_day01_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] basic mission_day02_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] basic mission_day03_answer의 사본.txt', 'extracted_content\\[SeSAC] [네트워크와 클라우드] basic mission_day04_answer의 사본.txt', 'extracted_content\\extracted_content.json']
    s.tech_stack = []
    s.raw_texts = {}
    s.raw_texts['(EXT) [SeSAC] [네트워크와 클라우드] 코랩 세션_Wrap Up 리포트 (template)의 사본.txt'] = """ 
 
 
[
네트워크와
 
클라우드
]
 
코랩세션
 
Wrap
 
Up
 
리포트
 
작성팀:
 
(6조
 
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
 
 
포트
 
포워딩
 
개념
 
포트
 
포워딩
 
테이블은
 
외부
 
포트와
 
내부
 
포트를
 
1
대
1
로
 
매핑
 
포트
 
번호가
 
반드시
 
동일할
 
필요는
 
없으며
,
 
테이블
 
설정에
 
따라
 
다르게
 
매핑
 
가능
 
(
예
:
 
외부
 
1024
 
→
 
내부
 
1025)
 
내부에서
 
SSH
를
 
22
번
 
포트에
 
띄워도
 
보안을
 
위해
 
외부에는
 
다른
 
포트로
 
노출
 
가능
 
같은
 
IP
의
 
같은
 
포트에는
 
여러
 
연결이
 
동시에
 
불가능함
 
(
주소
 
하나당
 
하나의
 
연결
)
 
공인
 
IP
와
 
사설
 
IP
 
개념
 
정리
 
공인
 
IP
는
 
전세계적으로
 
사용하는
 
주소로
,
 
아파트의
 
공식
 
주소에
 
비유됨
 
사설
 
IP
는
 
아파트
 
내부의
 
동호수와
 
같이
 
내부에서만
 
구분
 
가능한
 
주소
 
외부에서
 
접근하려면
 
공인
 
IP
를
 
알아야
 
내부로
 
들어올
 
수
 
있음
 
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
 

 
 
라우터의
 
개념
 
확장
 
라우터는
 
특정
 
물리
 
장치만을
 
의미하는
 
것이
 
아니라
,
 
들어온
 
요청을
 
목적지로
 
분배하는
 
역할
 
자체를
 
의미
 
공인
 
IP
를
 
사설
 
IP
로
 
변환하는
 
것뿐만
 
아니라
,
 
사설
 
IP
를
 
더
 
세분화하는
 
것도
 
라우팅
 
네트워크는
 
트리가
 
아닌
 
그래프
 
구조로
,
 
라우터는
 
상하
 
관계가
 
아닌
 
노드
 
간
 
분배
 
역할
 
라우팅
 
테이블을
 
통해
 
들어온
 
요청을
 
어디로
 
보낼지
 
결정
 
파싱
(
Parsing)
 
개념
 
파싱은
 
원하는
 
데이터를
 
추출하거나
 
큰
 
데이터를
 
작은
 
단위로
 
쪼개는
 
행위
 
HTTP
 
메시지에서
 
헤더
,
 
바디
 
등을
 
구분하여
 
추출하는
 
것도
 
파싱
 
 
 
Day
 
02
 
코랩
 
세션
 
주어진
 
업스테이지
 
교육용
 
aws
 
키를
 
받아
 
rigion
설정하고
 
인스턴스
 
생성함
 
upstage-project-yyk
 
ssh
 
-i
 
\"upstage-keypair.pem\"
 
ubuntu@18.216.226.68
 
ssh
로
 
서버
 
접속(
aws
 
우분투환경)
 
notepad
 
$HOME/.ssh/conﬁg
 
생성해서
 
ssh
 
설정
 
Host
 
upstage-project-yyk-atozwizard
 
HostName
 
18.216.226.68
 
User
 
ubuntu
 
IdentityFile
 
\"D:\\01.
 
study\\01.sesac_upstage_ai\\04.4
주차_네트워크와클라우드\\00.
project\\upstage-keypair.pe
m\"
 
ssh
 
-G
 
upstage-project-yyk-atozwizard
 
이걸로
 
연결가능해졌음
 
ec2
 
안에서
 
sudo
 
apt
 
update
 
sudo
 
apt
 
install
 
-y
 
nginx
 
sudo
 
systemctl
 
enable
 
nginx
 
sudo
 
systemctl
 
start
 
nginx
 
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
 

 
 
upstage-project-yyk.duckdns.org
 
도메인
 
만들고,
 
aws
 
서버에는
 
우분투
 
환경에서
 
엔진엑스
 
설치,
 
구동한
 
뒤
 
도메인에서
 
정상적으로
 
돌아가는
 
것
 
확인함.
 
nslookup
 
upstage-project-yyk.duckdns.org
 
서버
 
도메인
 
설정된것
 
확인
 
🏆
 
오늘
 
진행한
 
작업
 
요약
 
(Infrastructure
 
Milestone)
 
단계
 
작업
 
내용
 
핵심
 
결과물
 
1.
 
클라우드
 
확보
 
AWS
 
EC2
 
인스턴스
 
생성
 
및
 
리전
 
설정
 
18.216.226.68
 
서버
 
자원
 
획득
 
2.
 
접속
 
보안
 
설정
 
.pem
 
키
 
권한
 
수정
 
및
 
SSH
 
접속
 
성공
 
서버
 
내부
 
터미널
 
제어권
 
확보
 
3.
 
접속
 
편의화
 
~/.ssh/config
 
별칭
(
Alias)
 
설정
 
ssh
 
upstage-project-yyk-atozwizard
로
 
간편
 
접속
 
4.
 
웹
 
서버
 
설치
 
Nginx
 
설치
 
및
 
백그라운드
 
서비스
(
systemctl)
 
등록
 
80
번
 
포트를
 
통한
 
HTTP
 
응답
 
준비
 
완료
 
5.
 
도메인
 
연결
 
DuckDNS
 
설정
 
및
 
IP
 
매핑
 
upstage-project-yyk.duckdns.org
 
주소
 
확보
 
6.
 
검증
 
nslookup
 
및
 
브라우저
 
접속
 
확인
 
전
 
세계
 
어디서든
 
내
 
서버로
 
접속
 
가능한
 
상태
 
인스턴스
 
꺼졌다
 
다시
 
켜지면
 
ip
 
변경됨
 
확인해야함
 
sudo
 
adduser
 
<username>
 
꺽쇠
 
빼야함
 
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
 

 
 
sudo
 
usermod
 
-aG
 
sudo
 
<username>
 
키가
 
복사,
 
부여되지
 
않아서
 
작업해야했음
 
sudo
 
mkdir
 
-p
 
/home/atozwizard/.ssh
 
sudo
 
cp
 
~/.ssh/authorized_keys
 
/home/atozwizard/.ssh/
 
sudo
 
chown
 
-R
 
atozwizard:atozwizard
 
/home/atozwizard/.ssh
 
sudo
 
chmod
 
700
 
/home/atozwizard/.ssh
 
sudo
 
chmod
 
600
 
/home/atozwizard/.ssh/authorized_keys
 
권한
 
부여
 
600
 
700
 
ssh
 
-i
 
\"upstage-keypair.pem\"
 
atozwizard@3.142.222.56
 
 
Day
 
03
 
코랩
 
세션
 
 
강사님의
 
리포지를
 
클론을
 
만들고,
 
내
 
깃헙에
 
새
 
리포지를
 
만들어서
 
리모트를
 
했음.
 
그랬더니
 
리모트된
 
url
이
 
강사님것과
 
내것
 
두가지가
 
동시에
 
나왔고,
 
브랜치를
 
옮길
 
때에도
 
둘이
 
같이
 
옮겨가는게
 
재미있었음.
 
내
 
리포지에
 
리모트를
 
할
 
때에,
 
별칭을
 
짓기도
 
했었다.
 
network
라고.
 
git
 
remote
 
add
 
별칭
 
url
 
 
git
 
fetch
 
--all
 
git
 
switch
 
feature/fastapi/orm
 
git
 
pull
 
uv
 
sync
 
cd
 
infra/mysql
 
docker-compose
 
up
 
-d
 
도커로
 
mysql
 
실행
 
 
뭘
 
하긴
 
했는데
 
뭘했는지
 
잘
 
모르겠다.
 
눈팅.
 
뭔가
 
강사님이
 
해놓은
 
것을
 
봤다.
 
그게
 
뭐지..남은게
 
없다.
 
하루
 
공친기분.
 
리트코드나
 
볼걸..
 
 
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
 

 
 
Day
 
04
 
코랩
 
세션
 
ssh
 
접속!!
 
ssh
 
-i
 
\"D:\\01.
 
study\\01.sesac_upstage_ai\\04.4
주차_네트워크와클라우드\\00.
project\\upstage-keypair.pe
m\"
 
atozwizard@18.219.123.49
 
ssh
접속후
 
서버에
 
리포지
 
클론
 
git
 
clone
 
https://github.com/atozwizard/upstage-network-lecture.git
 
github
 
repo
 
secret
 
에는
 
USERNAME,
 
HOST,
 
PASSWORD
 
등
 
각기
 
항목별로
 
등록해놔야
 
했다.
 
한번에
 
넣었더니
 
안됨.
 
가능하게
 
하려면
 
뭘
 
읽어와야하는지
 
잘
 
적어놔야함.
 
디플로이
 
했고.
 
서버에
 
GET
 
응답이
 
오는데,
 
POST
가
 
응답이
 
안왔음.
 
도커
 
컨테이너로
 
띄워놓은
 
MYSQL
 
DB
를
 
인스턴스
 
서버에
 
연동했어야
 
함.
 
서버에
 
dockercompose
 
yaml
파일
 
만들어
 
올려보냈음.
 
그러나
 
강사님
 
레포지가
 
origin
 
내것은
 
별칭으로
 
설정해
 
두어서,
 
서버에
 
origin
 
pull
 
하라고
 
했는데,
 
이것은
 
내것인
 
network
로
 
바꾸어야
 
하지
 
않을까??
 
그래서
 
일단
 
내쪽에서
 
test
브랜치에
 
origin
을
 
pull
하면
 
강사님께
 
오는
 
것을
 
확인함,
 
conﬁlct
 
대강
 
처리하고
 
서버에
 
network
 
pull
하도록
 
deploy.yml
 
수정
 
후
 
commit,push
 
도커
 
띄워서
 
서버에
 
post
를
 
보내
 
db
연결
 
확인해야함.
 
api
 
단위테스트
 
까지
 
하면
 
완료
 
 
 
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
 

 
 
 
1.
 
배포
 
아키텍처의
 
완성
 
단순히
 
코드를
 
올리는
 
것을
 
넘어,
 
GitHub
 
→
 
GitHub
 
Actions
 
→
 
AWS
 
EC2
로
 
이어지는
 
자동화
 
흐름을
 
구축했습니다.
 
●
 
GitHub
 
Actions
:
 
코드의
 
관문을
 
지키는
 
로봇
 
역할을
 
합니다.
 
●
 
.github/workflows/deploy.yml
:
 
이
 
로봇에게
 
내리는
 
\"설명서\"입니다.
 
(반드시
 
이
 
경로에
 
있어야만
 
작동한다는
 
것을
 
배웠죠!)
 
●
 
SSH
 
접속
:
 
로봇이
 
내
 
서버(
EC2)
에
 
열쇠(
Secrets)
를
 
가지고
 
들어가서
 
명령어를
 
대신
 
실행하게
 
만들었습니다.
 
2.
 
주요
 
문제
 
해결
 
기록
 
(Troubleshooting)
 
오늘
 
해결한
 
문제들은
 
나중에
 
현업에서도
 
똑같이
 
마주칠
 
소중한
 
경험치입니다.
 
●
 
404
 
Not
 
Found
 
에러
:
 
서버에
 
코드는
 
배포됐지만,
 
실제
 
API
 
경로가
 
없는
 
구버전이
 
돌아가고
 
있을
 
때
 
발생한다는
 
것을
 
확인했습니다.
 
●
 
YAML
 
파일
 
위치
 
문제
:
 
.github/workflows
라는
 
약속된
 
폴더가
 
아니면
 
자동화가
 
시작되지
 
않는다는
 
것을
 
Move-Item
으로
 
해결했습니다.
 
●
 
Git
의
 
파일
 
이동(
delete
 
mode
)
:
 
파일을
 
옮길
 
때
 
Git
이
 
기존
 
파일을
 
삭제하고
 
새
 
파일을
 
만드는
 
과정을
 
이해했습니다.
 
●
 
서버
 
환경
 
구성
:
 
코드만
 
넘어가면
 
끝이
 
아니라,
 
서버의
 
가상환경에도
 
pytest
 
같은
 
도구가
 
설치되어
 
있어야
 
테스트가
 
돌아간다는
 
점을
 
배웠습니다.
 
3.
 
최종
 
작동
 
확인
 
(The
 
Result)
 
마지막에
 
확인한
 
프로세스는
 
다음과
 
같습니다.
 
1.
 
로컬
에서
 
코드를
 
수정하고
 
push
.
 
2.
 
GitHub
 
Actions
 
탭에서
 
초록불(
Success
)
 
확인.
 
3.
 
EC2
 
서버
에서
 
pytest
를
 
돌려
 
3
 
passed
 
확인.
 
ai
 
agent
 
할
 
예정
 
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
    s.raw_texts['00 Course Introduction.pptx.txt'] = """25 Upstage 
LLM 서비스 기반 지식을 위한 
네트워크 및 클라우드 강의 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 강사 소개 
서영학 
엔씨소프트 (18.01~24.12) 
• AI연구 → 백엔드 서버 개발자 
• 24.01~24.12 : 플랫폼센터 계정 플랫폼 개발팀 
• 23.01~23.12 : 금융플랫폼 개발팀 
• 금융플랫폼 개발 
• 18.01~22.12 : AI 서비스개발실 서버팀 
• KBO AI 플랫폼 개발 
부트캠프 강사 
• upstage 새싹프로젝트 CS  part (26.01~) 
• 멋쟁이사자처럼 백엔드 단기심화 4기 (25.03~06) 
기타 
•23, 24 년 실전코딩  Testing 강의, 
22 년 실전코딩  백엔드  강의 ( 충남대 )
• 대학교  알고리즘  동아리  회장 
•elice 카이스트  머신러닝  부트캠프 (AI) 
최우수상 
•16 년 ACM-ICPC 대전 본선
개인블로그  활동
•inspire12.tistory.com 
•github.com/inspire12 수업소개 
4 네트워크 및 클라우드 
: 수업 소개 00 - 00 
수업의 목표 
수업 진행방식 
 

5 수업 목표 : 네트워크 기본 지식과 실제 서버 운영 
기본적으로 알아야 할 네트워크 궁금증 
컴퓨터는 어떻게 외부 신호를 인식해서 우리 한테 알려줄까? 
어떻게 그 수 많은 컴퓨터들과 통신할 수 있을까? 
웹 서버를 만들고 클라우드에서 운영해보기 + AI 서비스를 한다면? 
클라이언트-서버(HTTP통신) 
fastapi 로 웹서버 구동하기 
AWS 클라우드 서버 설정과 운영 하기 
리눅스 서버 운영하기 
웹서버 서비스 배포 해보기 
수업소개 
6 수업 전체 목차 
네트워크 이해 → AWS 서버인프라 → 웹서버 개발 → 운영하기 
1. 웹 데이터 통신 
- HTTP , REST , 클라이언트-서버 모델 
2.네트워크 기반지식 
- 네트워크 요청 인식 과정 
- 데이터가 인터넷 길 찾는 방법 
3. 클라우드 컴퓨팅 시작하기 
- ec2, 포트포워딩, ssh  
4. 클라우드 컴퓨팅 접속과 운영 
- 서버 띄우기(배포), 네트워크 진단 도구 5,6. 클라우드 활용: 유저 → 제품 (웹 서버 개발/유지보수) 
- fastapi 
7,8 . 클라우드 활용: 코드 → 제품 (배포) 
- github action 
- CI/CD 
- aws cli, IaC(infra as a code) 
9. 클라우드  심화: 서버 다양한  구성 요소 탐험하기  
10. 서비스에 AI가 들어간다면? 
수업소개 
7 상황, 실습 위주로 생각 수업소개 
각 실습 코드를 기록 
git 기반 실습 코드 기록 
직접 작업 해 볼수도 
만약 수업 흐름을 놓쳐도 
따라올 수 있도록  
개념/진행 
중요 페이지 실습 해보기 

8 수업에서 사용할 프로젝트 
프로젝트 주소 
https://github.com/inspire12/upstage-network-lecture.git 
프로젝트 위치(추천) 
mkdir -p {내문서}/workspace/upstage-project/(위치에서 클론) 
cd 내문서 / workspace/upstage-project/upstage-network-lecture 
git clone https://github.com/inspire12/upstage-network-lecture.git  
수업소개 
9 수업 전 최소한의 선수 지식 
이전 수업에서 배운 것들 
파이썬 코딩 경험  + ide (pycharm) 
shell 에서 명령어를 입력한 경험 
pip, uv 등의 패키지매니저 이해 
git 사용법 
shell 명령 도구 (터미널, wsl) 
(docker) mysql  
수업소개 
10 수업 피드백 
1. 더 알고 싶은 부분 
2. 수업의 난이도 
3. 수업 질문 
4. 진행 방향에 대한 피드백 
온라인 강의:  이미 강의가 만들어진 상태 
- 실시간은 현장 조교님 
- 궁금한 점 / 과제 진행 어려움  / 수업 난이도 / 기타 상담 등  오픈 카톡방 활용 
https://open.kakao.com/o/gbpQzC5h 수업소개 

11 수업 전 준비할 것들 
설치해야할 것 
1. 네트워크 요청 도구: Postman 
2. 터미널 앱: iterm(mac) / warp  
- windows의 경우 wsl 설정 을 통한 shell 설정 
- 패키지 설치 도구 (apt: linux, brew : mac , scoop : windows) 
3. pycharm (community / ultimate: 학생 이메일 🡪 무료) 
4. python 설치 (3.12 버전 이상) 
- pyenv 를  통해 버전별로 설정하는 걸 추천 
구글 설문 링크 공유와 퀴즈 공유 
잘 풀리지 않는 것들, 궁금증, 과제 난이도 
5. git 설치 
6. docker 설치 
수업소개 
www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['01 Understanding Web Communication and HTTP.txt'] = """25 Upstage 
LLM 서비스 기반 지식을 위한 
네트워크 및 클라우드 강의 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: 웹을 통해 데이터를 주고받기 
Network 
목차 
1. 네트워크를 알아야하는 이유 
2. 네트워크 요청 응답 과정 
- HTTP 프로토콜 
3. REST 요청 방법과 실제 보내기 
- URL과 PORT 
- 브라우저/Postman(curl 명령어)/코드 
4. REST 응답 서버 구현 
- fastapi 
4 네트워크 공부의 필요성 
01 - 01 
네트워크 
- 연결, 그룹, 계층 
네트워크 장단점 
5 네트워크를 알아야 하는 이유 Network 
네트워크란 (Network) ? 
두 대 이상의 장치가 연결해서 서로 정보를 주고 받는 통신망 
계층적으로 연결되어있다. 

6 네트워크를 알아야 하는 이유 Network 
네트워크를 사용하면 좋은 점 
외부의 컴퓨터 파워를 사용하기 위해 
ex) GPT 
외부의 데이터/알고리즘을 사용하기 위해 
ex) 실시간 영상(미디어), 수 많은 데이터, 수 많은 알고리즘 

7 네트워크를 알아야 하는 이유 Network 
네트워크를 사용하면 좋은 점 
•외부의 컴퓨터 파워를 사용하기 위해 
•ex) GPT 
•외부의 데이터/알고리즘을 사용하기 위해 
•ex) 실시간 영상(미디어), 수 많은 데이터, 수 많은 알고리즘 
대부분, 수많은 앱들은 네트워크를 사용한다 

8 네트워크를 안 쓴다면? Network 
GPU가 없는 컴퓨터 
: (CPU 모델 없는) LLM 실행 불가 
온디바이스 AI 
: 스마트폰에 내장된 칩에서 AI 연산 
장점 
- 네트워크 지연등이 없다 
- 개인정보 보호 
단점 
- 속도/품질이 떨어진다 
- 업데이트(하드웨어)에 한계 / 기기별 성능 편차가 있다 

9 네트워크를 사용하는 단점 Network 
보안 위험성 
- 다른 사람들이 중간 탈취할 가능성 
- DDoS 등 서비스 공격 
불안정성 
- 데이터 지연, 패킷 손실 
- 연결 끊김 (특히 무선 환경) 
- 네트워크 장애 → 서비스 장애 
복잡성 
- 문제 추적 어려움 
비용 
- 트래픽 비용, 추가 인프라 

10 네트워크 요청-응답 과정 01 - 02 
네트워크에서 데이터를 어떻게 요청할까 
클라이언트-서버 
HTTP 프로토콜 
URL 
- port 
RESTFul API 

11 네트워크 첫 번째 질문 Network 
네트워크로 다른 컴퓨터의 데이터를 어떻게 요청할까? 
오늘 공부할 용어 
- 클라이언트-서버 모델 
- 프로토콜 / HTTP 
- REST Ful API/JSON 포맷 

12 클라이언트 ‒ 서버 모델 Network 
데이터를 요청하고 데이터를 응답 받는다 
클라이언트: 
\"GET /users 주세요!\" (요청) 
서버: 
\"200 OK, 여기 데이터!\"  (응답) 
클라이언트  = 고객 
• 요청을  하는 사람
서버  = 서빙에서  유래
• 요청을  들어주는  
사람

13 클라이언트 ‒ 서버 모델 Network 
브라우저 (ex 크롬) 는 훌륭한  클라이언트  도구

14 HTTP 프로토콜 Network 
주고받을 때 규칙 필요(약속) 
택배 송장 같은 규칙 
도착할 곳, 내용물 종류, 보내는 사람 등에 대한 내용을 포함 

15 (참고) 규격의 중요성 (인터페이스) Network 
주고받을 때 규격 
콘센트 규격 → 어떤 기기도 꽂으면 전기가 흐름 
USB 규격 → 어떤 장치도 꽂으면 컴퓨터가 인식 
HTTP 규격  → 어떤 서버든 URL 요청을 이해하고 응답 
API 규격  → 어떤 클라이언트든 동일한 방식으로 사용 가능할 곳, 내용물 종류, 보내는 사람 등에 대한 내용을 포함 
인터페이스:  서로 다른 시스템이 약속된 방식으로 소통하기 위해 만들어 놓은 사용 설명서 
실제 구현과 사용방법이 분리될 수 있다. 
프로토콜: 컴퓨터는 예측 가능하고 안정적으로 통신 

16 HTTP 구조 Network 
HTTP   : HyperText Transfer Protocol 
✔  텍스트 기반 
요청과 응답이  사람이 읽을 수 있는 형태 라 이해하기 쉽다 
✔ 요청/응답 구조 
클라이언트 → Request (요청 메소드: GET , POST 등) 
서버 → Response (상태코드: 200, 404 등) 
✔ Stateless(상태를 기억하지 않음) 
서버는 이전 요청의 상태를 유지하지 않는다 
그래서 쿠키/세션/JWT 등이 등장하게 됨 
✔ 확장성 
HTML, JSON, 이미지 등 다양한 형식을 전송할 수 있다 

17 HTTP 기반 RESTFul API Network 
RESTFul API 란? 
REST는 웹에서 자원을 다루는 방법을 규칙처럼 정리한 아키텍처 스타일 
“웹의 자원(Resource) 을 어떻게 식별하고” 
“어떤 규칙 으로  자원을 조작 할지” 
HTTP 를 더 예쁘고 일관성  있게 쓰기 위한  자원 중심의 설계 철학 

18 HTTP 기반 RESTFul API 핵심원칙 Network 
1. (요청) 자원(Resource)은 URL로 표현한다 
ex) 브라우저 주소창에 입력하는 주소 

19 port 란? Network 
같은 IP(서버)에 여러 개의 서비스가 동시에 뜰 수 있기 때문! 
도메인 / 호스트가 '주소' , 포트는 \"문 번호\" 
웹서버를 띄울 때 우리 서버는 기본 포트가 아닌 포트에서 실행할 예정 
ex) 8001, 8000, 8800 등 

20 그런데.. 지금까지 Port 입력 따로 안 했는데? Network 
프로토콜마다 기본 port가 존재한다 
보통 요청할 때 Port 를 입력하지 않는다 
그러나 실제 URL은 Port가 포함되어있다 
포트를 생략해도 되는 이유는 프로토콜 마다 
기본 포트(Default Port) 가 있기 때문! 
운영에서는 대부분 Nginx같은 Load Balancer가 
(요청을 먼저 받아서 분배해주는 서비스) 
80 / 443 포트를 대신 받고 내부로 포워딩 

21 HTTP 기반 RESTFul API 핵심원칙 
Network 
2) (요청) 행동은 HTTP 메서드로 구분한다 
HTTP 메서드 의미 예시
GET ⭐
 조회 GET /users 
POST ⭐
 생성 POST /users 
PUT 전체 수정 PUT /users/10 
PATCH 부분 수정 PATCH /users/10 
DELETE 삭제 DELETE /users/10 
22 HTTP 기반 RESTFul API 핵심원칙 
Network 
3) (응답) 상태 코드로 결과 종류 전달 

23 네트워크 요청 과정 01 - 03 
네트워크에서 데이터를 어떻게 응답할까 
요청 분석 
- 브라우저 
- Postman 
- python requests 
24 클라이언트 입장에서 요청하기 Network 
클라이언트 = 고객 
사용자와 상호작용하는 프로그램 
클라이언트는 서버에 요청(Request)  을 보내고 받은 데이터를 다룬다 
서버로부터 서비스를 요청하고 제공받는 컴퓨터나 소프트웨어 
가장 대표적인 클라이언트 
- 브라우저 

25 브라우저 주소창에 URL 을 치면 어떻게 화면이 뜰까? Network 
브라우저 뒷단에서 일어나는 일들 
upstage.ai 를 입력했을 때 일어나는 일들 
1. URL 입력 
2. DNS 조회 (IP 주소 확인) 
3. 서버로 요청 (HTTP) 
 - 브라우저는 데이터를 “패킷(Packet)”으로 쪼개서 보낸다 
 - 패킷은 여러 라우터(Router)를 거쳐 목적지까지 이동 
    - 네트워크 통신(ISP → 지역 라우터 → 백본망 → 해외 거점 → 서버) 
    - 손실되면 자동 재전송하도록 TCP(handshake) 과정 
https://aws.amazon.com/ko/blogs/korea/what-happens-when-you-type-a-url-into-your-browser/ 
4. 브라우저는 요청 받은 응답을 파싱 
- 상태코드, Header, Body 
5. html, javascript 파일을 렌더링 

26 브라우저를 통해 요청 해보기 + 개발자 도구로 확인 Network 
실습 순서 
1. 테스트 API사이트 브라우저로 접속하기 
- https://jsonplaceholder.typicode.com 
2. 개발자 도구 실행 → 네트워크 탭 
Ctrl + Alt + I 혹은 우클릭 후 개발자도구 (Inspect) 
3. Run script 실행 이후 데이터 확인 

27 브라우저를 통해 요청 해보기 + 개발자 도구로 확인 Network 
실습 순서 
1. 테스트 API사이트 브라우저로 접속하기 
- https://jsonplaceholder.typicode.com 
2. 개발자 도구 실행 → 네트워크 탭 
Ctrl + Alt + I 혹은 우클릭 후 개발자도구 (Inspect) 
3. Run script 실행 이후 데이터 확인 

28 Postman 을 활용해 REST 통신 해보기 Network 
실습 순서 
사전) Postman 을 설치  
https://jsonplaceholder.typicode.com /todos/1 
GET 
POST 
PUT
DELETE 
요청 해보기 

29 python requests 를 통해 API 호출하기 Network 
실습 순서 
0. uv 설치 (설치가 안 되었다면) 
pip install uv 
1. request 모듈 설치 
uv init 
uv add requests 
2. requests 코드 작성 
코드 참고 
3. GET , POST , DELETE, PUT  실행하고 Debugging 해보기 
requests 사용법 
import requests 

30 (실습) python requests로 API 호출하기 Network 
GET 요청 
import requests 
BASE_URL = \"https://jsonplaceholder.typicode.com/posts\" 
def get_post (post_id ):
    resp = requests.get( f\"{BASE_URL }/{post_id }\")
    print (\"===== HTTP Response 분석 =====\" )
    print (\"1) Status Code:\" , resp .status_code) 
    print (\"2) Headers:\" , resp .headers) 
    print (\"3) Body(text):\" , resp .text) 
    print (\"4) Body(json):\" , resp .json()) 
    print (\"==============================\" )
    return resp .json() 
if __name__ == '__main__' :
    data  = get_post( 1)
    print (data ['title' ])
git switch lecture/requests 
git pull 
uv sync 
31 네트워크 응답 
서버를 통해 요청을 받아 처리 하는 과정 01 - 04 
서버 
웹서버 제작: fastapi 
RESTFul API 
uvicorn 

32 서버란? Network 
클라이언트의 요청을 받아 \"실제 기능\"을 수행하는 프로그램 
요청 처리 프로그램 
데이터 저장 및 조회 
비즈니스 로직 수행 
응답(Response) 반환 
API 제공 
- 요청 방식 제공 
33 서버 특징 Network 
서버를 개발하면서 고려할 게 많다 
•항상 실행된 상태로 요청을 기다리는 프로그램  (24/7) 
•여러 사람들의 요청을 처리해야한다. ‒ 동시 처리 
•멀티스레딩  (하나의 요청에 하나의 스레드) 
•외부 사용자, 브라우저, 앱, 다른 서버가 모두 입력을 보낼 수 있다 

34 서버 기능을 직접 개발하려면? Network 
직접 서버를 만들기엔 너무 복잡하고 할 일이 너무 많다 
•요청은 어떻게 읽지? 
•요청 포맷은(JSON) 은 어떻게 파싱하지? 
•에러 처리 어떻게 하지? 
•수백 개 API는 어떻게 유지하지? 
•...
이런 처리를 만들어놓은 서버 프레임워크 가 필요하다 
* 프레임워크: 소프트웨어 개발을 위한 '뼈대' 또는 '틀'로서, 반복적인 공통 기능을 미리 만들어 제공해 개발자가 
애플리케이션의 핵심 로직에 집중하도록 돕습니다 
35 python 서버 프레임워크: FastAPI Network 
FastAPI 의 특징 
빠른 개발 
적은 코드로 구현 가능한 생산성 
자동 문서화 
- Swagger 자동 생성 
타입 기반 검증 
- 코드 읽기 쉬워진다 
- Pydantic 비동기  지원 ( 좋은  성능 ) 동시성  처리  간편 
Python 생태계와  좋은  궁합 
• 최신 파이썬  개념 적극 사용 
36 (실습) FastAPI 시작하기 Network 
실습 과정 
1. 가상환경 설정 
uv init 
# source .venv/bin/activate 
2. fastapi 설치 
uv add fastapi \"uvicorn[standard]\" 
from fastapi import FastAPI 
app = FastAPI() 
@app.get( \"/hello\" )
def hello(): 
  return {\"message\" : \"Hello\" }3. app/main.py 
37 uvicorn: 요청을 받는 역할 Network 
HTTP 요청을 받아 FastAPI 애플리케이션을 실제로 실행하는 ASGI 서버 
개발/운영 모두 사용 가능 
uvloop, httptools 기반 → 매우 빠른 성능 
개발 모드에서 자동 재시작(--reload) 지원 → 개발 편의성 향상 
ASGI (Asynchronous Server Gateway Interface) 표준 기반 
- Python 비동기 서버 표준 
- Uvicorn은 대표적인 ASGI 서버 구현체 
FastAPI 앱을 실제 웹 서버 형태로 실행해, 
인터넷에서 서비스될 수 있도록 해주는 엔진 역할 
38 uvicorn - FastAPI Network 
https://devocean.sk.com/blog/techBoardDetail.do?ID=165922&boardType=techBlog uvicorn - FastAPI 흐름 

39 (실습) pycharm FastAPI 실행 Network 
https://fastapi.tiangolo.com/ko/tutorial/ﬁrst-steps/#_9 pycharm 에서 python 실행 설정 
무료 버전일 경우 
Edit Conﬁguration > + > python 선택 > module  > uvicorn > main:app --reload 실행 
app.main:app --reload git switch feature/fastapi/start 
git pull 
uv sync 
40 troubleshooting) FastAPI 설치 후에도 빨간 줄 일때  Network 
Pycharm 에서 Python 경로를 잘못 가리키고 있을 때 
터미널에서 
which python 
설정 > interpreter > Add interpreter > Add new interpreter > Select existing > 위 경로 복붙 

41 (실습) terminal 에서 FastAPI 실행 Network 
https://fastapi.tiangolo.com/ko/tutorial/ﬁrst-steps/#_9 FastAPI cli 
uv add \"fastapi[standard]\" 
fastapi dev 
fastapi run uvicorn 
uvicorn main:app --reload 
uvicorn main:app --host 0.0.0.0 --port 8000 

42 (실습) pycharm 에서 FastAPI 실행 Network 
https://fastapi.tiangolo.com/ko/tutorial/ﬁrst-steps/#_9 FastAPI 실행 후 로그 확인 
FastAPI 실행 로그  
Postman 으로 요청 전달 후 응답 확인 
localhost:8080/hello 

43 데이터를 받아보기 Network 
https://fastapi.tiangolo.com/ko/tutorial/ﬁrst-steps/ Path 변수형식 
api 함수에 매개 변수로 받는다 
이 때 url path 와 변수 명이 같으면 path 로 인식 
Query 매개 변수형식 
api 함수에 매개 변수로 받는다 
이 때 url path 와 변수 명이 없으면 query param로 인식 매개변수들은 타입이 같으면 자동으로 매핑해준다 fastapi 튜토리얼  참고
https://fastapi.tiangolo.com/ko/tutorial/path-params 
44 데이터를 받아보기 Network 
https://fastapi.tiangolo.com/ko/tutorial/ﬁrst-steps 요청 본문 (Request body) 
헤더 (Header) 
from fastapi import Header from fastapi import Request 
45 (실습) 데이터를 받아보기 Network 
https://fastapi.tiangolo.com/ko/tutorial/ﬁrst-steps git switch feature/fastapi/routes 
git pull 
uv sync 
46 총 정리 Network 
네트워크로 다른 컴퓨터의 데이터를 어떻게 요청할까? 
- HTTP 프로토콜을 통해 
- GET/POST/PUT/DELETE 와 URL, 상태코드, Header, Body 
네트워크를 사용하면 장단점은? 
- 장점:  외부의 컴퓨터 파워를 사용 / 외부의 데이터/알고리즘/기능을 사용하기 위해 
- 단점: 네트워크 보안 이슈, 네트워크 불안정성, 문제추적 어려움 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['02 Network Fundamental Knowledge.txt'] = """25 Upstage 
네트워크를 이해하기 위한 기반 지식 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: 네트워크 요청 방법 뒷단 Network 
목차 
컴퓨터가 네트워크를 인식하는 과정 
- OSI 7계층 
IP 주소와 네트워크 그룹 
- IP 고갈문제와 Public IP 와 Private IP 
네트워크 상에서 데이터 전달 
- 패킷과 데이터분해 
- 패킷 헤더 
4 컴퓨터가 네트워크를 인식하는 과정 02 - 01 
OSI 7계층 
- 개발할 수 있는 포맷 / 길찾기 / 신호 인식 

5 네트워크 두 번째 질문 Network 
컴퓨터는 네트워크 요청을 
어떻게 인식하고 있는 걸까? 
네트워크 인식: OSI 7계층 
OSI 7계층은 네트워크 통신 과정을 
단계별로 나눈 개념적 모델 
네트워크는 계층(레이어) 형태 
각 계층 처리 해야 할 목적이 다르다 

6 네트워크 인식하기: OSI 7계층 Network 
Application Layer (앱 사용) 
프로그램이 네트워크를 사용하는 방법과 규칙 
- HTTP 등 사용자와 가장 가까운 계층 
- 메일, 소켓(실시간데이터) 등 다양한 프로토콜 
→ 실제 서비스 개발을 다루는 포맷 제공 

7 네트워크 인식하기: OSI 7계층 Network 
Network Layer (길찾기) 
- 생각보다 멀 수 있는 물리적 거리 
- 길을 찾게 보내주는 네트워크 장비들 
- 라우팅을 통해 최종 목적지로 도착 

8 네트워크 인식하기: OSI 7계층 Network 
Physical Layer (신호인식) 
랜선으로 들어오는 전기신호를 
컴퓨터가 인지할 수 있는 데이터(비트)로 변경 
인프라/네트워크 엔지니어 
너무 깊게 알필요는 없지만 
존재는 인식 해야 한다 

9 전기 신호를 데이터로 전환 Network 
컴퓨터 네트워크 카드(랜카드) 
https://80000coding.oopy.io/86e608e7-089b-4df2-96cc-553274ef4ae9 
https://learn.microsoft.com/ko-kr/windows-hardware/drivers/gettingstarted/what-is-a-driver- 

10 전기 신호를 데이터로 전환 Network 
컴퓨터가 2진수로 작동하는 이유 
진기 신호(아날로그 파동) → (샘플링) → 디지털 숫자 
https://80000coding.oopy.io/86e608e7-089b-4df2-96cc-553274ef4ae9 
샘플링 

11 전기 신호 전달, 해저 케이블 Network 
중간중간 전기신호를 증폭 
https://80000coding.oopy.io/86e608e7-089b-4df2-96cc-553274ef4ae9 

12 (심화) 인터넷을 버티게 하는 정체 Network 
https://programmerhumor.io/programming-memes/the-whole-internet-relies-on-that-one-shark-5w52 

13 컴퓨터가 네트워크에서 쓰는 주소 02 - 02 
인터넷 주소 = IP(인터넷 프로토콜) 
- IP와 DNS 
- IP 고갈 문제 
네트워크는 그룹과 연결이다 
- Public IP vs Private IP 
- LAN vs WAN 
14 인터넷에서 컴퓨터들은 서로 어떻게 찾아갈까? Network 
인터넷에 연결된 수백억개의 컴퓨터 
인터넷은 거대한 연결망, 전 세계에는 수백억 개가 넘는 컴퓨터, 서버, 스마트폰이 연결 
이렇게 수많은 장치를 서로 찾아가기 위해서는 각 장치를 구분할 수 있는 고유한 방법이 필요하다 
집을 찾아가려면 \"주소\" 가 필요하듯 
인터넷 세상에서도 \"주소\" 가 필요하다 

15 네트워크에서의 주소 체계? Network 
IP 주소 = 인터넷 세계에서 \"내가 어디 있는지\" 를 알려주는 집 주소 
인터넷에서 컴퓨터를 구별하는 고유 주소 (식별자/숫자) 
IP 는 네트워크 그룹에서 할당(빌려준) 주소 
- 같은 기기도 연결할 때마다 IP가 달라질 수 있음 
전송 시 데이터에 포함 
•출발지 IP (누가 보냈는지) 
•목적지 IP (누구에게 보낼지) 

16 DNS (Domain N ame System) Network 
우리가 입력하는 건  문자(Domain) 인데?   ex) naver.com 
우리가 입력하는 문자를 인터넷이 이해하는 숫자로 바꿔주는 시스템 
만약 DNS 에서  장애가 난다면? 
내 서버가 멀쩡해도 주소를 못 찾아 
인터넷이 '없어진 것처럼' 보인다 
17 IP로 표현할 수 있는 수 한계 Network 
https://hongong.hanbit.co.kr/network-범위에-따른-네트워크-분류lan-wan/ IP 고갈 문제를 어떻게 접근했을까? 
•IP로 표현할 수 있는 수 (43억 개 주소) 
•컴퓨터 수 백억개 + 알파 
• 컴퓨터는 PC 뿐만 아니라 스마트폰, 로봇청소기들도 컴퓨터도 포함 (네트워크가 되는 기기들) 
IP 주소 배정할 수 있는 개수는 한계가 존재 
주소 개수  <  기기 개수  → IP 고갈 문제 발생 
 

18 Private IP 의 필요성 Network 
https://hongong.hanbit.co.kr/network-범위에-따른-네트워크-분류lan-wan/ 집/회사 내부에서 여러 기기가 인터넷을 같이 쓴다 
집: 노트북, 휴대폰, TV, 로봇청소기, 스피커… 
회사: 수백~수천 대 기기 
→ 이 모든 기기가 한 개의 인터넷 회선으로 외부에 나가야 함 
→ 내부 기기끼리는 사설 IP로 서로 구분 
\"내부 전용 주소 체계\" 역할이 필요하다 = Private IP 
요청을 받는 쪽은 private IP를 몰라도 public IP로 돌려줄 수 있다 
근데 public IP로 받은 라우터는 어떻게 내 컴퓨터로 보내지? 
 
19 NAT / Port forwarding Network 
https://2jinishappy.tistory.com/334 Private IP - Public IP 연결 
하나의 Public IP로 여러 기기가 인터넷 사용 가능 
공유기에서 private IP가 public IP로 바뀔 때 Port 번호를 내부적으로 할당 해서 보낸다 
(임시) 라우팅 Private IP = Public IP + Port 조합 
20 LAN 과 WAN Network 
LAN: 근거리 통신망 
라우터 및 스위치와 같은 커넥터를 사용하여 
물리적으로 서로 가까운 디바이스를 연결합니다. 
https://aws.amazon.com/ko/compare/the-diﬀerence-between-lan-and-wan/  WAN: LAN 끼리 연결하는 광역 통신망 
하나의 건물이나 대규모 캠퍼스를 넘어 
특정 지역, 심지어 전 세계에 분산된 여러 위치까지도 포함 
AWS 에서  VPC 
21 Public IP - Private IP 정리 Network 
https://hongong.hanbit.co.kr/network-범위에-따른-네트워크-분류lan-wan/ 네트워크는 그룹과 그룹의 연결 
네트워크는 그룹과 그룹의 연결로 이루어져 있다 
WAN : 전 세계가 공유하는 네트워크 
Public IP : 외부용, 공인 IP 
LAN : 회사, 학교, 집, AWS VPC 같은 \"내부 네트워크 영역\" 
Private IP : 내부용 IP , 사설 IP 

22 (심화) 회사에서 처음 일할 때 가장 당황했던 점 Network 
사내 네트워크 시스템 (LAN) 의 \"보안 시스템\" 혹은 내부 규칙의 존재 
•회사 내부 LAN 은 다양한 규칙을 추가로 가지고 있을 수 있다. 
•사내망 (회사의 데이터 보안을 위해 존재) 
•보안을 위한 접근 허가 시스템에 신청이 필요 (방화벽, ACL:접근제어목록) 
실무를 하면서 네트워크 지식이 없을 때 (물어볼 수가 없어서) 답답함 

23 (실습) Public IP와 Private IP 비교하기 Network 
내 컴퓨터의 IP 주소 확인하기 
https://ip.pe.kr  
내 공인IP 확인
1. 공인 IP 가 옆 친구와  IP 가 같은지  확인
다르다면  같은 WIFI 를 연결 중인지 ?
같다면  왜 같을까 ? 
ipconfig // mac 이라면  ifconfig  확인 
여러 어댑터  마다 IPv4 존재 
하지만  위 사이트의  공인 IP 와 같은 게 있을까 ? 
24 먼 거리의 컴퓨터로 어떻게 요청이 전달이 될까? 
: 네트워크의 길찾기 02 - 03 
OSI 7계층:  network, transport 레이어 
패킷 
데이터 신뢰성 
네트워크 계층 구조 
IP 주소 
Public IP 와 Private IP 
25 패킷이란? Network 
패킷 = 소포  
네트워크에서 전송하기 위해 데이터를 작은 단위로 분할 한 것 
각 패킷은 \"주소 + 제어 정보 + 실제 데이터\"를 포함한 독립적인 운반 단위 
페이로드: 내용물 
헤더: 주소(송장) 
https://hongong.hanbit.co.kr/network-회선-교환-방식과-패킷-교환-방식/ 
https://ngwoon.github.io/network/2020/11/12/OSI-7%EA%B3%84%EC%B8%B5/ 

26 네트워크 길찾기 Network 
OSI 7계층: 3,4 층 
3층: 길찾기 (라우팅) 
4층: 데이터 정확도 
https://hanamon.kr/네트워크-기본-프로토콜이란-osi-7-계층-별-프로토콜/ 

27 데이터는 어떻게 전달될 수 있을까? Network 
라우터: 네트워크를 연결하고 \"패킷\"의 \"길안내\" 
https://www.youtube.com/watch?v=1z0ULvg_pW8 

28 패킷 헤더 Network 
패킷 헤더 = 송장  
OSI 7계층 마다 패킷 헤더를 본다 
(3 단계 레이어) 다음으로 이동할 주소를 확인하고 다음 길로 보낸다 
(4단계 레이어) 패킷 단위로 순서를 부여해 데이터를 
나누고 보내면 받는 쪽에서 조립한다 
https://hongong.hanbit.co.kr/network-회선-교환-방식과-패킷-교환-방식/ 
https://ngwoon.github.io/network/2020/11/12/OSI-7%EA%B3%84%EC%B8%B5/ 

29 각 패킷은 네트워크 상에서 독립적으로 이동 Network 
회선 통신 
네트워크는 그룹으로 나뉘어져 그룹마다 길을 찾을 수 있게 도와주는 도구(라우터) 들이 있다 
https://hongong.hanbit.co.kr/네트워크/ 

30 패킷 형태로 잘라서 보내는 이유 Network 
패킷은 왜 필요한 걸까? 
1. 효율적인 데이터 전송 
실제 하나의 묶음으로 데이터를 보내면 너무 사이즈가 크다, 네트워크가 혼잡해질 수 있다. 
2. 오류 처리 용이 
전송 중 일부 데이터가 손상되거나 사라지면, 전체 데이터를 다시 보내는 대신 손상된 패킷만 재전송 
3. 경로 다양성 
인터넷망은 하나의 경로만 있는게 아니라 다양하게 경유할 수 있다 
각 패킷은 상황에 따라 서로 다른 경로를 통해 목적지에 도달할 수 있다. 
31 (실습) Fastapi 에서 응답 데이터를 큰 데이터 (이미지)로 보내보기 Network 
실제 데이터와 받은 쪽에서 해석한 데이터 차이 
https://aws.amazon.com/ko/compare/the-diﬀerence-between-lan-and-wan/ 

32 총 정리 Network 
컴퓨터는 네트워크 요청을 어떻게 인식하고 있는 걸까? 
- 전기신호를 샘플링해서 2진수 데이터로 바꾼다 
- 데이터를 패킷 단위로 나눠서 계층적으로 전달하고 받을 때 조립해서 읽는다 
너무 먼 거리의 컴퓨터로 어떻게 요청이 전달이 될까? 
- 네트워크는 그룹과 계층형태 로 이루어져 있다 
- IP 주소를 통해 보낼 주소가 결정된다 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['03 Getting Started with Cloud Computing.txt'] = """25 Upstage 
클라우드 컴퓨팅 시작하기 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 복습:1강 Network 
네트워크로 다른 컴퓨터의 데이터를 어떻게 요청할까? 
네트워크를 사용하면 장단점은? 

4 복습:1강 Network 
네트워크로 다른 컴퓨터의 데이터를 어떻게 요청할까? 
- HTTP 프로토콜을 통해 
- GET/POST/PUT/DELETE 와 URL, 상태코드, Header, Body 
네트워크를 사용하면 장단점은? 
- 장점:  외부의 컴퓨터 파워를 사용 / 외부의 데이터/알고리즘/기능을 사용하기 위해 
- 단점: 네트워크 보안 이슈, 네트워크 불안정성 

5 복습:2강 Network 
다른 컴퓨터의 데이터를 어떻게 요청할까? 
 
컴퓨터는 네트워크 요청을 어떻게 인식하고 있는 걸까? 
너무 먼 거리의 컴퓨터로 어떻게 요청이 전달이 될까? 

6 복습:2강 Network 
다른 컴퓨터의 데이터를 어떻게 요청할까? 
- 네트워크는 데이터 요청 과정은 약속(프로토콜) 기반으로 이루어진다 
- HTTP 기반 RESTFul API 로 요청한다 
 
컴퓨터는 네트워크 요청을 어떻게 인식하고 있는 걸까? 
- 전기신호를 샘플링해서 2진수 데이터로 바꾼다 
너무 먼 거리의 컴퓨터로 어떻게 요청이 전달이 될까? 
- 데이터를 패킷 단위로 나눠서 계층적으로 전달하고 받을 때 조립해서 읽는다 
- 네트워크는 그룹과 계층형태 로 이루어져 있다 

7 오늘의 목표: 클라우드 컴퓨터 시작하기 - EC2 띄우기 Network: Cloud 
목차 
클라우드 컴퓨팅 개념 잡기 
AWS 계정 시스템과 권한 (옵션) 
- root, iam 
클라우드 컴퓨터(인스턴스) 빌려보기 (EC2) 
인스턴스 접속하기 with IP 
- 키페어(pem), ssh 

8 클라우드 컴퓨팅 개념 잡기 03 - 01 
클라우드 컴퓨터 이해하기 
AWS와 EC2 
9 내 노트북에서만 돌던 서비스, 진짜 서비스가 되려면? Network: Cloud 
인터넷에 서버를 올려야 한다 
로컬에서만 개발 → 나만 접속 가능 
친구 한 명 정도 테스트 → 간단히 가능 
사용자들은 내 컴퓨터가 아니라 인터넷을 통해 접속한다 
즉, 서비스를 24시간 공개된 컴퓨터(서버) 에 올려야 함 
서버는  항상 켜져 있고, 
어디에서나 접근 가능한 고정된 주소(IP)  를 가짐 

10 내 서비스가 갑자기 유명해지면 어쩌지? Network: Cloud 
인플루언서 한 번 타서 순식간에 수만 명이 접속한다면? 
오늘 아침까지는 잘 되던 서비스가 
점심 지나자마자 계속 느려지고, 아예 안 열리기 시작한다면? 
장애가 나면 고민 
- 서버 한 대 더 사야 하나? 
- 지금 당장 어디부터 늘려야 하지? 
하지만 이런 사람들의 관심이 한 순간만이라면? 

11 점점 고도화되고 메모리와 연산이 필요해지는 작업들 Network: Cloud 
막대한 연산량(Compute Power)의 필요 
- AI, LLM 
- 게임 
- 영상처리 / 영상편집 
- 대규모 데이터 처리 
등등 
대부분의 서비스는 순간적으로 높은 컴퓨팅 성능을 필요 
하지만  컴퓨터를  직접 구매하는  방식은  
빠르게  바뀌는  환경을  따라가기  어렵다 
12 클라우드 컴퓨팅이란? Network: Cloud 
클라우드 컴퓨팅이란? 
인터넷을 통해 서버, 스토리지, 네트워크 자원을 빌려 쓰는  기술 
인프라 전체를 서비스 형태(IaaS, PaaS, SaaS)로 제공하는 구조입니다 
개발자는 서버를 구매·설치·관리하는 과정을 생략하고 
몇 분 만에 인프라를 준비 가능 
서버·스토리지·네트워크·AI 기능까지 제공 
사용한 만큼만 비용 지불 
13 클라우드 컴퓨팅 장/단점 Network: Cloud 
장점 
•빠른 확장/축소 
•전 세계 인프라 기반 
•관리 부담 감소 
•초기 비용 최소화 단점 
•사용량 기반 과금 → 비용 예측 어려움 
•설정 실수 시 보안 사고 위험 
•특정 서비스 종속 가능성 

14 클라우드 컴퓨팅 서비스: AWS Network: Cloud 
클라우드 제공 서비스: 회사 
•AWS: 아마존 
•Azure: 마이크로소프트 
•Oracle Cloud Infra: 오라클 
•Naver Cloud 
AWS 소개 
•세계 1위 클라우드 
•서버, DB, 네트워크, AI 모델까지 제공 
•리전 / AZ 구조로 높은 안정성 
* 리전: 특정 지리적  위치에  있는 데이터센터들의  그룹 

15 AWS 계정 세팅 03 - 02 
AWS 계정과 IAM 

Region 이 같은 지 확인 
- 실습은 ap-southeast-2 에서 진행한 자료입니다 
IAM 계정과 권한 
- Root 계정으로 작업X 
- 권한을 받아야 작업 가능 
EC2 연결 실패시 
보안그룹 + 키페어 확인 
16 시작 전) AWS 를 사용하며 주의사항 Network: Cloud 
AWS 비용 
- AWS는 미사용 요금도 나온다 (보관료, 기본요금) 
- 각 컴포넌트마다 요금 주의 사항 첨부 
모든 리소스를 다 껐는지 마지막에 체크 
- 사이트에서 일일이 확인하기 어려워.. 
- aws에서 cli를 제공 
  - 따로 스크립트를 만들어 체크 

17 AWS의 계정 시스템 Network: Cloud 
Root 와 IAM 
•Root: 계정 전체 권한 
•IAM: 실무에서 사용하는 표준 사용자 
•보안을 위해 Root는 최소 사용 
실제 계정은 IAM으로 사용 
실제 수업에선 발급 받은 IAM 계정 
* IAM ( Identity and Access Management): 인증 접근 관리 

18 EC2 란? Network: Cloud 
Elastic Compute Cloud 
•AWS의 가상 서버 서비스 
•CPU, 메모리, 디스크, 네트워크를 원하는 만큼 
선택
•웹 서비스·API 서버·AI 추론까지 가장 넓게 
사용되는 핵심 서비스 

19 (실습) AWS 를 통해 계정을 만들고 (서버용) 컴퓨팅 자원 빌리기 
Network: Cloud 
실습과정 
1. 계정 생성 (AWS 가입) 
2. IAM 계정 생성 
3. EC2 발급 
새싹 프로젝트는 따로 AWS 계정을 지급해주셔서 
이 부분은 실습 하지 않습니다. 
다만 나중에 개인 AWS 서비스를 운영하실 수도 있으니 
페이지를 남겨놓습니다. 
AWS는 계정(email)마다 하나의 유저에 무료 크레딧을 줍니다 
한도 + 시간이 있기 때문에 나중에 필요할 때 만드시는 걸 
추천합니다. 
20 (실습) 클라우드 계정 생성 Network: Cloud 
AWS 가입 
AWS 계정 발급 시 생략 가능 
과정 종료 이 후 
서비스를 위해 알아야 한다 
 

21 (실습) IAM 계정 생성 및 로그인 Network: Cloud 
가입 직 후 IAM 계정 생성 전 상황 
우선 Root 계정으로 로그인 
22 (실습) IAM 계정 생성 Network: Cloud 
실습 순서 
1. 루트 계정으로 로그인 
2. https://console.aws.amazon.com/iam/home 
a. dashboard 오른쪽 → Account Alias 설정 
3. IAM 계정 생성 
a. 생성 후 IAM 계정도 Alias 설정 
4. IAM 계정으로 로그인 

23 (실습) IAM 계정 생성 Network: Cloud 
IAM 계정 생성 
1. user 생성 → 이름 입력 및 
Provide user access to the AWS Management Console ‒ optional 선택 
2. access management → users → create user 
1. 이름 정하기 
2. 권한 설정  > create group 
3. AmazonEC2FullAccess , EC2InstanceConnect  권한 검색 후 등록 
그룹명 EC2 으로 그룹 생성 
4. 완료 
3. create user (완료) 
* Provide user access to the AWS Management Console ‒ optional 선택 안 했으면 
   생성 후 Security credentials 에서 부여 가능 
* 권한 그룹은 추후에 권한 추가 제거 (수정) 가능 

24 AWS 계정 권한 그룹 Network: Cloud 
AWS 계정 권한 그룹 
•기본값: 모든 접근은 Deny 
•부여한 정책에 Allow된 권한이 있으면 허용 
•단, 명시적 Deny가 있으면 무조건 거절 
왜 사용자에게 직접 권한을 주지 않고 그룹을 쓸까? 
•사용자 직접 관리 = 위험 + 비효율 
•그룹 기반 관리 = 확장성 + 보안 + 감사 용이 

25 (실습) IAM 계정으로 콘솔 로그인 해보기 Network: Cloud 
IAM 콘솔 로그인 필요한 점 
user 생성 → 이름 입력 & 
Provide user access to the AWS Management Console ‒ optional 선택 
1. Account Alias 설정 
2. (iam) user 이름 
3. password 설정 
IAM 으로 로그인 

26 AWS를 통해 클라우드 컴퓨팅으로 
컴퓨터 자원 빌리기 03 - 03 
EC2 생성하기 

27 EC2 생성하기 Network: Cloud 
알아야할 필수 정보 
•Region 정하기 (강사 region: ap-southeast-2 ) 
•Key pair 생성 및 저장 
•클라우드 컴퓨팅 성능 정하기 (일단 free tier) 
•OS: ubuntu 24.04 L TS 
•인스턴스 타입: t3.micro 
•방화벽: security group 설정 (네트워크 설정) 

28 (실습) EC2 생성하기 Network: Cloud 
EC2 생성하기 
https://ap-southeast-2.console.aws.amazon.com/EC2 

29 Region(리전) 정하기 Network: Cloud 
Region(리전): 데이터센터가 있는 지역 그룹 
https://console.aws.amazon.com/EC2 
https://ap-southeast-2.console.aws.amazon.com/EC2 
한국(가장 가까움) : ap-northeast-2 
호주(가깝고 좀 더 저렴한 경우가 많음): ap-southeast-2 
인스턴스 타입이나 구매 모델에 따라 
가격은 달라질 수 있어서 비교해봐야함 

30 (실습) EC2 생성하기 Network: Cloud 
Launch an instance 
ubuntu 24.04 
t3.micro (free tier) 
key pair 생성 

31 (실습) 보안,인증을 위한 키페어 생성하기 Network: Cloud 
create key pair 
•RSA
•pem 
•생성 후 
•PEM 다운로드 (자동) 
•(~Documents/workspace 로 옮기자) 
pem 파일 권한 변경 
  chmod 400  Documents/workspace/upstage-keypair.pem 

32(실습) EC2 생성하기 Network: Cloud 
완료 
추후 할 일 
•인스턴스 들어가보기 (Connect to your instance) 
•서버 띄우기 
•포트 포워딩 

33 내 컴퓨터에서 AWS 클라우드로 접근하기 03 - 03 
ssh 접속 
key pair 

34 (실습) 웹 콘솔로 접속해보기 Network: Cloud 
웹 콘솔 내에서 EC2 서버 접근하기 
1. 인스턴스 페이지 접근, 서버 클릭 후 연결 
2. EC2 인스턴스 연결 
3. 웹 콘솔에서 리눅스 접근 확인 

35 ssh 란? Network: Cloud 
https://benfatto.tistory.com/54 ssh: S ecure  Shell
서버에 원격으로 접속하기 위한 가장 기본적인 기술 
네트워크를 통해 보안이 적용된 채널 을 만들어주는 기술 
•Telnet은 평문(plaintext) → 계정/비밀번호 유출 위험 
TCP 22번 포트 사용 
키 기반 인증 방식 
- 키 파일(.pem 파일)을 사용 - 파일 권한 chmod 600 필요(남들이 볼 수 없는 상태) 
- SSH는 비공개 키를 절대 유출되면 안 되는 비밀번호 로 취급하기 때문에 
   다른 사람이 읽기만 할 수 있어도 접속을 아예 거부한다. 

36 ssh 설치 / 사용 Network: Cloud 
https://toycoding.tistory.com/entry/%EC%9C%88%EB%8F%84%EC%9A%B0-OpenSSH-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0 ssh: OpenSSH 설치 
맥/리눅스는 기본 설치되어있음 
Windows는 설치해야함 
윈도우 검색 → 선택적 기능 관리 → 기능 추가 → OpenSSH 검색 후 추가 
터미널 실행 후 
ssh 확인 

37 (실습) 로컬 터미널에서 ssh 로 접속해보기 Network: Cloud 
https://benfatto.tistory.com/54 ssh 와 key pair 를 통한 접근 
1. pem 파일 ~\\Documents\\workspace 으로 이동 (내 문서 > 생성한 workspace 폴더) 
2. pem 파일 권한 설정 
chmod 600 {keyﬁle} 
 혹은 
2. pem 파일 권한 설정 (windows cmd) 
icacls .\\{키페어이름} /inheritance:r 
icacls .\\{키페어이름} /grant:r \"$($env:USERNAME):R\" 
혹은 
2. pem 파일 탐색기에서 권한 설정 
우클릭 → 속성 → 보안탭 → 고급 → 상속사용안함 

38 로컬 터미널에서 ssh 로 접속해보기 (실습) Network: Cloud 
https://benfatto.tistory.com/54 ssh 와 key pair 를 통한 접근 
3. ssh 를 통해 접속 
ssh -i \"{키페어주소}\" ubuntu@{접속주소} 

39 troubleshooting) 접속 실패시 Network: Cloud 
터미널 (shell) 이란? 
1. 보안 그룹에서 22번 포트(ssh) 오픈 확인: 방화벽 이슈 
ssh 요청 후 응답이 오래도록 오지 않는 경우 
2. key pair 권한 이슈 
Permission denied (publickey) ... too Open 
3. public ip 가 없는 경우 (elastic ip 연결 여부) 
- 기본 생성이되면 default vpc 로 배정되어 문제 없다 (추후 vpc 시 체크사항) 

40 총 정리 Network: Cloud 
클라우드 컴퓨팅이란? 
EC2 생성 및 접속 
ec2 생성과 key pair 로 접속 AWS 계정 시스템 
Root 와 IAM 
권한과 권한 그룹 
www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['04 Managing Cloud Servers.txt'] = """25 Upstage 
클라우드 컴퓨팅 서버 다루기 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3목표: aws 인스턴스에 웹서버 띄워보고 운영해보자  
Network: Cloud 
목차 
리눅스 환경 적응하기 
EC2에 웹서버 띄워보기 
- Port Forwarding 
- 웹 서버(fastapi) 
네트워크 도구 사용해보기 

4클라우드 서버 다루기 04 - 01 
클라우드와 서버 리눅스 OS(ubuntu) 
네트워크 도구 
5초기 EC2 세팅 필요성 Network: Cloud 
서버는 만들었는데 이제 뭘 해야하지? 
처음 EC2는 빈 깡통 
컴퓨터를 새로 샀으면 크롬도 깔고, 파이썬도 깔고, 자바도 깔고, 게임도 깔고.. 등등 
초기 세팅이 중요하다 
클라우드 컴퓨터를 빌린 목적 상기 
- 웹 서버 운영해보기 
- 웹 서버 띄우고 통신해보기 
 

6서버 인프라 시작하기 Network: Cloud 
linux 웹서버용 인프라와 Ubuntu 서버  
linux 웹서버용 인프라 
- 서버는 365일 꺼지지 않고 돌아간다 → 안정성 
- 실행할 애플리케이션과 개발환경에 집중 → 가볍다 
    - GUI 대신 CUI (검은 명령창) , 기타 기본 앱이 더 없음 
- 패키지 설치가 편해야한다 
서버 운영체제  Ubuntu 
Ubuntu 는 Linux 계열의 운영체제 중 하나 
: 무료고 가볍고 안정적이고 패키지 설치도 쉽고 많이 사용 

7Ubuntu 서버 명령어 Network: Cloud 
https://inpa.tistory.com/entry/LINUX-%EC%98%A8%EB%9D%BC%EC%9D%B8-%EB%A6%AC%EB%88%85%EC%8A%A4-%ED%84%B0%EB%AF%B8%EB%84%90-BASH%EC%89%98-%EC%8A%A4%ED%81%AC%EB%A6%BD%E
D%8A%B8-%EC%97%B0%EC%8A%B5-%EC%82%AC%EC%9D%B4%ED%8A%B8 명령어 치트시트 
리눅스 명령어 연습 사이트 
https://bellard.org/jslinux/ 
https://copy.sh/v86 

8리눅스(우분투) 명령어 다뤄보기 
: EC2 안에서 명령어 실행해보기 04 - 02 
클라우드와 서버 리눅스(ubuntu) 
리눅스 기본 명령어 

9Ubuntu 서버 명령어 Network: Cloud 
일반적인 명령어 구조 
 [명령]  [옵션/플래그]  [인수/대상] 
ex)
ls ‒l  (ls라는 명령어를 l이라는 옵션을 사용해서 사용) 
mv /test /home/test 
(test라는 파일을 /home/test 경로로 이동) 
--help로 확인 가능 

10Ubuntu 서버 명령어 - ls Network: Cloud 
 
ls : 목록을 간결하게 표시 
-l 옵션 : 권한,소유자,크기 등 자세한 내용 표시 
-a 옵션 : 숨김파일까지 모두 표시 
-al : a옵션과 l옵션 둘다 사용 
ls : 파일 및 폴더 내용 확인 
11Ubuntu 서버 명령어 - pwd Network: Cloud 
pwd : 현재 자신의 위치 
현재 자신이 어디에 위치하고 있는지 출력 
리눅스는 CLI 기반 환경이기때문에, 
윈도우 폴더창처럼 현재위치를 항상 눈으로 확인 불가 

12Ubuntu 서버 명령어 - cd Network: Cloud 
cd: 해당 경로로 이동 //  경로 개념: 절대경로와 상대경로 
cd [이동할 경로] 
경로를 나타내는 방법은? 
구분 절대경로 상대경로 
설명컴퓨터  최상위  위치부터  목적지까지  
경로를  모두 적는 방식현재기준위치를  기준으로  목적지까지  
변화를  적는 방식
시작점 루트 (/) 현재위치  (pwd 로 확인)
예시/home/upstage/hello/1.txt ( 현재위치가  /home/upstage 일경우 ) 
./hello/1.txt 
13Ubuntu 서버 명령어 - mkdir Network: Cloud 
mkdir: 폴더 만들기 
 
-mkdir [만들 폴더 명] 
14Ubuntu 서버 명령어 - rm, rmdir Network: Cloud 
rm: 파일 삭제 / rmdir : 폴더 삭제 
 
rm [삭제할 파일 이름] 
rmdir [삭제할 폴더 이름] 
rmdir을 하기위해선 해당 폴더가 모두 비어져있어야함 
-rf 옵션: 강제 삭제 

15Ubuntu 서버 명령어 - cp Network: Cloud 
cp: 파일 복사 
[명령]  [옵션/플래그]  [인수/대상] 
cp {대상 파일 위치} {타겟 파일 위치} 
왼쪽 파일을 오른쪽 위치에 복사 

16계정 설정과 sudo Network: Cloud 
계정 기본 지식 
기본 계정 
root : 서버 전체를 통제하는 최상위 관리자 
ubuntu /ec2-user: AWS EC2 기본 계정 
sudo: 필요한 순간만 root 권한 빌려쓰기 
권한 구조 : rwx (읽기, 쓰기, 실행) 
권한 부여 
chmod: 사용권한 
chown: 소유 권한 
ls -al (권한까지 출력) 
 
17Ubuntu 서버 명령어 - chmod Network: Cloud 
파일 사용 권한 확인 

18Ubuntu 서버 명령어 - chmod Network: Cloud 
파일 사용 권한 확인 
파일 권한 구조 (r, w, x) 
r = 4,  w = 2, x = 1 
rwx = 7 (4+2+1) 
rw- = 6 (4+2) 
r-x = 5 (4+1) 
r-- = 4 

19패키지 설치 매니저 apt Network: Cloud 
ubuntu 패키지 설치 매니저 apt 
Ubuntu/Debian 계열 리눅스에서 사용하는 패키지 설치·업데이트·삭제·의존성 관리 도구 
공식 저장소(repository) 를 통해 안전하고 검증된 패키지를 제공 
apt update 
apt install {package} 

20클라우드 인프라에 웹서버 띄우고 접속하기 04 - 03 
클라우드와 서버 리눅스 

21aws 에 웹 서버를 띄우고 접근하려면? 
서버 실행과 포트포워딩 
인스턴스 내부에서 애플리케이션이 해당 포트를 LISTEN 중이어야 함 
❗
콘텐츠 서버(애플리케이션)에서 포트를 Listen 
EC2 네트워크 계층에서 포트가 열려 있어야 함 
❗
Security Group \"포트 오픈\" 
포트 개방은 2개가 모두 만족해야 한다. Network: Cloud 
22(실습) aws 인프라에 웹 서버 띄우기 Network: Cloud 
작업 공간 설정 
EC2 접속 후 workspace/deploy 폴더 생성 및 접속 
git clone https://github.com/inspire12/upsta ge-network-lecture 
git fetch --all 
git switch release/start 

23(실습) aws 인프라에 웹 서버 띄우기 Network: Cloud 
linux 내에서 uv 설치 
curl -LsSf https://astral.sh/uv/install.sh | sh 
source ~/.bashrc 
uv --version 
python3 --version 
24(실습) aws 인프라에 웹 서버 띄우기 Network: Cloud 
웹서버 실행 
uv sync 
uv run uvicorn main:app --host 0.0.0.0 --port 8000 
쉘 하나 더 띄고 접속 후 확인 
uvicorn 실행 확인 
•ps aux | grep uvicorn 
서버 listen 확인 

25(실습) 내 컴퓨터에서 요청 보내기 Network: Cloud 
postman 을 통해 요청해보기 
curl {내 ec2 ip 주소}:8000/hello 
•왜 ec2 서버 내에서 localhost:8000 로 했을 때는 됐는데 
•내 컴퓨터에서는 접속이 안될까? 
26방화벽, Security Group과 포트포워딩 Network: Cloud 
EC2로 드나드는 트래픽을 IP·포트 기준으로 통제 
방화벽 
   허용된 트래픽만 통과시키고 나머지는 막아주는 네트워크의 출입문 관리자 
Security Group 
  AWS에서 인스턴스 수준 방화벽 
(참고) NACL 
: 서브넷 VPC (AWS LAN) 수준에선 더 복잡한 제어 가능한 방화벽 
포트 규칙을 정하는 것 : Security Group 
27(실습) Security Group으로 포트포워딩 Network: Cloud 
실습 순서 
1. security group 설정 
2. 8000 포트 등록 
- inbound 
3. security group 을 ec2 인스턴스에 적용 
28(실습) aws 인프라에 웹 서버 띄우기 Network: Cloud 
서버 접속을 위한 Security Group 설정 
왼쪽 아래 Network: Cloud & Security > Security Groups > 오른쪽 위 Create security group  

29(실습) aws 인프라에 웹 서버 띄우기 Network: Cloud 
Security Group 생성 

30(실습) aws 인프라에 웹 서버 띄우기 Network: Cloud 
EC2 인스턴스에 적용 

31(실습) 다시 aws 인프라에 웹 서버 접속해보기 Network: Cloud 
서버 접속 

No Hang Up: 터미널이 끊겨도 프로세스가 종료되지 않도록 실행해주는 명령어 
SSH 를 끊으면 백그라운드로 돌던 서버 종료: 터미널을 끄면 웹 서버도 꺼진다. 그걸 막아주는 명령어 
nohup  uv run uvicorn main:app --host 0.0.0.0 --port 8000 & 
로그를 기록 
nohup  uv run uvicorn main:app --host 0.0.0.0 --port 8000 > app.log 2>&1 &
# 로그확인    tail -f app.log 
# 포트로 서버 확인 
netstat -tulnp | grep 8000 혹은 ss -ltnp | grep 8000 
kill {{pid}} 
32웹서버를 백그라운드로 실행하기 Network: Cloud 
nohup & 
1. nohup 붙이지 않은 상태로 서버 실행 후 Shell 종료, api 확인 
2. 재접속 후 nohup , &을 붙이고 확인 
3. 켜있는 서버 process id 확인 후 종료 
4. 로그 확인 붙이고 실행 및 로그 확인 
33(실습) nohup Network: Cloud 
ssh 끊었을 때 웹서버가 살아있는지 확인 

34네트워크 도구 사용해보기 04 - 04 
클라우드와 서버 리눅스 

35Ubuntu 네트워크 도구 시작하기 전에 Network: Cloud 
네트워크 도구 설치 
-ec2 접속, linux 환경에서 실행 
-설치 
명령어  링크
sudo apt update 
sudo apt install -y net-tools iproute2 dnsutils traceroute curl htop 
36Ubuntu 네트워크 명령어 - curl Network: Cloud 
curl : URL 으로 서버와 통신하는 명령어 도구 
- 웹 브라우저  없이 서버와  직접 대화할  수 있음
-HTTP/HTTPS 요청을  직접 만들어  보내고  응답을  자세히  확인 
가능
-API 테스트 , 서버 상태 점검, 네트워크  문제 추적에  필수 
curl  -v 옵션으로 자세하게 확인 가능 
37Ubuntu 네트워크 명령어 - ip address / curl ip.me Network: Cloud 
ip adress / ip a: ip주소 확인 
•기존 ip확인 명령어인 ifconﬁg 의 최신 버전 
내 public IP 를 확인하는 명령어 

38(심화) Ubuntu 네트워크 명령어 - ip route Network: Cloud 
ip route/ ip r: 라우팅 테이블 확인 
•AWS, GCP에서 서브넷 문제 있을 때 자주 씀 
•기본 게이트웨이 설정이 잘못되었는지 확인할 때 사용 

39Ubuntu 네트워크 명령어 - ping Network: Cloud 
ping : 다른 서버나 인터넷 연결 테스트. 
•DNS 문제인지  네트워크  문제인지  빠르게  판단 가능
• 내부 서버 간 통신 확인할  때도 사용 

40Ubuntu 네트워크 명령어 - ss Network: Cloud 
ss: 포트 상태 확인 
• 서버가  실행중인데  접속이  안 된다면  포트가  열려있는지  
확인
ss -tuln | grep 8000 

41Ubuntu 네트워크 명령어 - traceroute Network: Cloud 
traceroute : 패킷이 어떤 경로로 가는지 확인. 
sudo apt install traceroute 로 설치 필요
-* * * 응답없음  표시 
주로 보안상  노출을  거부한  곳
42Ubuntu 네트워크 명령어 - nslookup Network: Cloud 
nslookup: 특정 도메인에 대해 연결된 IP주소를 질의 
sudo apt install bind9-dnsutils 로 설치 필요
- 도메인이  올바른  IP 로 매핑돼  있는지  확인
-Cloudflare, Route53 문제 디버깅  시 필수
43총 정리 Network: Cloud 
EC2 접속 
SSH
Security 그룹: port forwarding 
 
네트워크 도구 사용하기 
ip, ifconﬁg, curl ifconﬁg.me 
traceroute, nslookup linux 서버 환경 적응하기 
리눅스 명령어 사용법 
www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['05 Web Server User Service 1.txt'] = """25 Upstage 
웹 서버 개발하기 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: 웹서버를 고도화 해보자 (route - service) 
fastapi 
목차 
fastapi 개발 (route - service) 
API 라우터 
Pydantic : 요청/응답 모델링과 모델 안정성 
Global Exception Handler 
- 에러/예외 
로그 시스템 
4 FastAPI 개발하기 05 - 01 
웹 서버 기능 고도화 
라우트 
Pydantic 과 모델 안정성 
서비스 

5 웹서버에 기능을 넣어보자 fastapi 
지금 서버는 너무 기능이 없다 
웹 서버 구조(책임별 계층화) 
•router ‒ service - repository 
fastapi 를 통해 api 라우팅 

6 요구사항  fastapi 
User 를 생성하는 API를 만들어주세요 
1. HTTP 요청을 받기 
- 생성이기 때문에 POST 
- 요청 포맷 정의 (request) 
- 응답 포맷 정의 (response) 
2. 유저 입력이 검증 및 기타 로직 
3. 유저 저장 
- 유저 저장 성공/실패 여부 알려주기 

7 (실습) API 생성 fastapi 
실습 순서 
0. uvicorn 으로 fastapi 실행 설정 
1. 라우터 분리 후 API 생성 
2. 요청/응답 정의 
3. api에 적용 git switch feature/fastapi/userapi-practice 
git pull 
uv sync 
8 (실습) APIRouter로 API 분리하기 fastapi 
실습 과정  app/api/route/user_routers 
1. 라우터 분리 후 API 생성 
main.py  FastAPI() 에 user_router 추가 
9 Pydantic 이란? fastapi 
Python 타입 힌트를 기반으로 데이터 검증과 변환을 자동으로 해주는 라이브러리 
Python은 동적 타입 언어라 잘못된 타입의 데이터가 들어오면 에러 
Python은 동적 타입 → 검증을 직접 해야 함 
API에서 들어오는 JSON은 타입이 제각각 → 안정적인 검증 필요 
데이터 모델링 = BaseModel 

10 (실습) API 요청/응답 모델  fastapi 
실습 과정 
2. 요청/응답 정의 
 
git switch feature/fastapi/userapi 
git pull 
uv sync 
11 (실습) API 생성 fastapi 
실습 순서 
3. api에 적용 

12 (실습) API 생성 fastapi 
실습 순서 
3. api에 적용 

async가 무조건 빠른 것이 아니다 
I/O작업이 많고 동시 요청 async def 
- 웹소켓, 스트림 등 실시간 처리 
- I/O작업, OpenAI API 호출 
- 비동기 
CPU 연산이 많으면 def 
- 이미지 처리, 복잡한 연산 
- 간단한 CRUD 위주의 API 
- 블로킹 라이브러리(pymysql)등 사용시 
13 (심화) async def / def 차이 fastapi 
https://velog.io/@dbstjrwnekd/%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D 동기 처리와 비동기 처리 
FastAPI는 내부적으로 Starlette의 이벤트 루프를 사용 
async def → event loop에서 실행 
def → 내부적으로 자동으로 threadpool에서 실행 
async def 
\"async 는 ‘ 많이 기다리는  상황\" 을 최적화하는  도구
14 서비스 로직을 위한 Service 05 - 02 
Service 
Repository 
15 요구사항  fastapi 
User 를 생성하는 API를 만들어주세요 
1. HTTP 요청을 받기 
- 생성이기 때문에 POST 
- 요청 포맷 정의 (request) 
- 응답 포맷 정의 (response) 
2. 유저 입력이 검증 및 기타 로직 
3. 유저 저장 
- 유저 저장 성공/실패 여부 알려주기 

16 요구사항이 많아질수록 읽기 어려워지는 Router 코드 fastapi 
라우터에 로직이 많아지면 어떻게 될까? 
•로직 중복 증가 
•한 눈에 역할이 보이지 않는다 
•수정 난이도 증가 
•팀 협업 충돌 (git conﬂict) 
•유지보수 비용 폭증 
API layer는 요청을 받고 응답 포맷을 다루는 역할만 수행하자 

17 서비스 로직 처리를 위한 Service fastapi 
Service의 역할 
서버의 역할: 요청을 받고, 요청을 처리하고 응답을 보낸다 
이 \"요청을 처리\"하는 부분 
핵심 로직(비즈니스 로직)을 담당 

18 서비스 로직 처리를 위한 Service fastapi 
요구사항:  User 를 생성하는 API를 만들어주세요 
들어온 데이터가 정확한지 검증 로직 필요 
1. service 객체를 만들고 api 로직을 service로 옮기자 
2. 옮긴 로직에 요청을 검증하는 로직을 추가하자 
19 (실습) Service에 간단한 저장 로직 추가 fastapi 
요구사항:  User 를 생성하는 API를 만들어주세요 
git switch feature/fastapi/userservice 
git pull 
uv sync 
들어온 데이터가 정확한지 검증 로직 필요 
1. service 객체를 만들고 api 로직을 service로 옮기자 
2. 옮긴 로직에 요청을 검증하는 로직을 추가하자 
20 서비스 에러 상황에 대처 
Global ExceptionHandler 05 - 03 
에러 / 예외 
응답 안정성 
21 예측하지 않은 다양한 문제 상황들 fastapi 
요청은 언제나 정직하지 않다 
•잘못된 요청 형식 
•예상 못한 None 접근 
•비즈니스 로직 예외 
등등 
클라이언트 크러쉬 발생 
에러 핸들링과 예외 처리 필요성 
문제는  반드시  발생한다 . 문제를  막는 것이 아니라 , 
문제를  예측하고  처리하는  구조 를 만드는  것이 
중요
22 에러 / 예외 fastapi 
오류는 어떤 상황이 있을까? 
예측 못하는 버그 = 에러 
예측하고 관리할 수 있으면  = 예외(Exception) 
에러 핸들링과 예외 처리 
코드를 try/except로 도배하는 것이 아니라, 
문제를 처리하는 레이어를 아예 따로 만드는 것이 좋은 설계 

23 예외와 Global Exception Handler fastapi 
전체 서비스의 오류를 한곳에서 통제하는 ExceptionHandler 
클라이언트에게 일관된 형태의 응답(JSON) 제공 
로그 추적을 체계화 
보안적 이유로 내부 에러 메시지를 그대로 노출하지 않도록 보호 
트랜잭션 롤백 같은 공통 처리 가능 
24 (실습) Global Exception Handler fastapi 
실습 순서 
1. 디버깅을 이용해 GlobalException에 붙는지 확인 
2. 허용 불가능한 이메일로 요청 보내기 
코드 위치 
예외 정의 
exceptions.py 
핸들러 
main.py 
git switch feature/fastapi/exceptionhandler 
git pull 
uv sync 
25 로그 시스템 05 - 04 
개발자 블랙박스 
26 로그 시스템 fastapi 
장애는 꼭 내가 안 볼 때 터진다 
문제를 발견하고 서버에 접속해도 이미 지난 상태 
에러가 발생한 시점에 기록이 있어야 에러를 잡을 수 있다 
로그는 개발자의 블랙박스 
27 fastapi 로그 시스템 fastapi 
로그는 개발자의 블랙박스 
logging 
  파이썬의 “로그 시스템 전체” 
  파이썬 표준 라이브러리 
  import logging 
logger 
   실제로 로그를 찍는 객체 
  logger = logging.getLogger(\"app\") 
  logging 으로 로그를  찍으면  어디서  찍힌 로그인지  파악이  안된다  
각 파일마다  logger 객체를  만들어  쓰자 
28 logging 설정 fastapi 
logging level 과 format 

29 logging 설정과 로그 레벨 fastapi 
logging 은 노출할 로깅 레벨 설정, logger는 레벨에 맞게 기록 

30 (실습) 실제 로그 찍히는 지 확인 fastapi 
실습 순서 
1. logger.info / logging.error 로 로그 코드 추가 
2. 로그 찍히는 지 확인 
3. logging 옵션에 error 로 설정 
4. 로그 찍히는 지 확인 
git switch feature/fastapi/logging 
git pull 
uv sync 
31 logging 설정과 로그 포맷 fastapi 
로그 기록은 어떤 내용을 담을 수 있을까? 

32 logger + exception handler fastapi 
Exception handler는 실제 에러난 곳이 아니다 
logger.exception  은 에러가 일어난 위치를 확인할 수 있다. 
error + exc=true 

33 로그 파일 저장 fastapi 
ﬁlename 지정하면 ﬁle로 log 저장 

34 logger 에서 콘솔과 파일 둘 다 출력 할 수 있나? fastapi 
logging 과 핸들러 
. basicConﬁg 는 로그에 대한 “단일 핸들러”만 만들 수 있다 
콘솔 핸들러와 파일 핸들러를 각각 만든 후 핸들러 등록하는 식으로 작동 

35 (실습) 실제 로그 찍히는 지 확인 fastapi 
실습 순서 git switch feature/fastapi/logging-ﬁlehandler 
git pull 
uv sync 
1. logger.info / logging.error 로 앱 시작 전 로그 찍기 
2. logs 폴더 안에 로그가 찍히는지 확인 

36 (심화) log 파일 크기 관리 fastapi 
로그 파일을 시간 별로 잘라서 저장한다: Rolling 
하나의 파일에 계속 로그가 붙게 되면, 읽는 시간이 오래 걸린다 
- 메모리 부족 
- 가독성 하락 
파일을 시간 별로 나눠 저장해주는 handler 
git switch feature/fastapi/logging-ﬁlehandler-rolling 
git pull 
uv sync 
37 총정리 fastapi 
웹서버의 요청 처리 흐름과 계층화 
- router 
데이터 모델과 타입 Pydantic 
- 데이터 검증과 타입 힌트 
- 요청 응답 모델 기반 
비즈니스 로직을 처리하는 Service 
- 요구사항을 실제로 수행하는 층 
Exception Handler / Logging 
예외를 처리하는 방법 
서버에서 일어난 일을 기록하는 방법 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['06 Web Server User Service 2.txt'] = """25 Upstage 
웹서버 유저서비스-2 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: 웹서버를 고도화해보자 (Service - Repository / Dependency, DI ) 
fastapi 
목차 
데이터 처리를 위한 Repository 
FastAPI와 DI 
- (객체지향) 책임, 위임, 사용 그리고 의존성 
- Dependency Injection 
Repository + MySQL + ORM 

4 데이터 처리를 위한 Repository 06 - 01 
Service  - Repository 
(docker-compose) mysql 
orm model - table 

5 요구사항  fastapi 
User 를 생성하는 API를 만들어주세요 
1. HTTP 요청을 받기 
- 생성이기 때문에 POST 
- 요청 포맷 정의 (request) 
- 응답 포맷 정의 (response) 
2. 유저 입력이 검증 및 기타 로직 
3. 유저 저장 
- 유저 저장 / 불러오기 
유저 id 발급 및 유저 생성할 때마다 증가 

6 (실습) 간단하게 데이터를 가지고 있을 때  fastapi 
service에서 memory_db(dict)로 저장 
service 코드 내 git switch feature/fastapi/usermemorydb 
git pull 
uv sync 

7 Service 데이터를 직접 처리하면 생기는 문제점 fastapi 
비즈니스 로직 처리를 위해선 데이터가 필요하다 
서비스 로직을 만들다 보면 반드시 데이터 처리가 필요해진다 
● 데이터 조회 
● 데이터 저장 / 수정 
● 조건에 따른 검색 
● 트랜잭션 처리 
이 모든 것을 Service가 직접 처리하면 문제가 생긴다 
● Service 코드에 DB 접근 코드가 섞인다 
● 비즈니스 로직과 저장 기술이 뒤엉킨다 
● Service의 책임이 과도하게 커진다 
Service 가 \" 무엇을  할지\" 보다
\" 어떻게  저장할지 \" 에 집중하게  된다
8 Repository 레이어의 필요성 fastapi 
Repository에 데이터 저장 방식을 위임한다 
Repository는 데이터 접근 책임을 분리한다 
Service는 \"저장해야 한다, 가져와야 한다\" 만 안다 
실제 저장 방식과 DB 기술은 Repository가 담당한다 
비즈니스 로직은 데이터 저장 방식을 몰라도 되어야 한다 
Service는 비즈니스에 집중하고 
Repository는 데이터 접근에 집중한다 
9 Repository fastapi 
https://aws.amazon.com/ko/what-is/repo/ 데이터를 어디서, 어떻게 가져오는지 감춰주는 중간 계층 
데이터 접근 추상화 
데이터 저장·조회 등 담당자 
데이터 매핑 
10 (실습) 메모리 기반 Repository 로 구성해보기 fastapi 
https://aws.amazon.com/ko/what-is/repo/ 실습순서 
1. repository/user_repo 생성, 저장할 데이터 포맷을 정의한다 
2. 서비스에 dict 생성 (key 로 요청이 오면 데이터를 준다, 메모리 DB) 
 
3. dict 에 넣고 성공하면 하나씩 증가하는 키를 발급해준다  
4. save, select, update, delete 로직을 추가 
5. depends 로 서비스와 연결 

11 (실습) 메모리 기반 Repository 로 구성해보기 fastapi 
https://aws.amazon.com/ko/what-is/repo/ 실습과정 
1. repository/user_repo 생성, 저장할 데이터 포맷을 정의한다 
2. 서비스에 repo 생성 (key 로 요청이 오면 데이터를 준다, 메모리 DB) 
 
3. dict 에 데이터가 들어가면 성공하면 하나씩 증가하는 키를 발급해준다  
4. 
git switch feature/fastapi/userdatarefactor 
git pull 
uv sync 
12 (실습) 메모리 기반 Repository 로 구성해보기 fastapi 
https://aws.amazon.com/ko/what-is/repo/ 실습과정 
3. dict 에 데이터가 들어가면 성공하면 
하나씩 증가하는 키를 발급해준다  
4. save, select, update, delete 로직을 추가 
git switch feature/fastapi/userdatarefactor 
git pull 
uv sync 
13 (실습) 메모리 기반 Repository 로 구성해보기 fastapi 
https://aws.amazon.com/ko/what-is/repo/ 실습과정 
5. depends 로 서비스와 연결 
user_service 는 user_repository를 
가지고 있어서 user_service(user_repo) 
로 사용법이 복잡해진다 
deps.py 
routes/api/user_routers.py 
실제 사용하는  곳 코드는  바뀌지  않는다 :  DI 의 장점 
git switch feature/fastapi/userdatarefactor 
git pull 
uv sync 
14 deps.py fastapi 
https://aws.amazon.com/ko/what-is/repo/ 의존성을 넣을 때 두가지 방식 
get_user_repository 
이미 만들어진 객체를 넣어주는 방식 
get_user_service 
매번 새로운 객체를 생성해서 넣어주는 방식 
git switch feature/fastapi/userdatarefactor 
git pull 
uv sync 
15 데이터 모델 정리 fastapi 
https://aws.amazon.com/ko/what-is/repo/ 데이터 모델(모양)을 한 곳에 모으는 리팩토링 
데이터 포맷을 알면 서비스 구조를 파악하기 쉽다 
schemas : 유저랑 요청을 주고받는 데이터 
entities: DB와 연결되는 데이터 
git switch feature/fastapi/userdatarefactor 
git pull 
uv sync 

16 데이터 모델 정리 fastapi 
데이터 포맷을 알면 서비스 구조를 파악하기 쉽다 
schemas : 유저랑 요청을 주고받는 데이터 
entities: DB와 연결되는 데이터 
데이터 모델(모양)을 한 곳에 모으는 리팩토링 
git switch feature/fastapi/userdatarefactor 
git pull 
uv sync 
17 계층형(레이어드) 아키텍처 구조 fastapi 
route / service / repository 구조로 책임을 분리 
route 
● 요청 받기 
● 입력 검증 
● service 호출 
service 
● 비즈니스 로직 
● 트랜잭션 제어 
● repository 호출 repository 
● DB 접근 
● SQL 실행 
● 데이터 반환 
core 
● DB 연결 
● 설정 

18 fastapi 와 DI 06 - 02 
객체지향설계와 Dependency(의존성) 
Dependency 와 Dependency Injection 
Service  - Repository 
19 사람의 언어 - 프로그래밍 언어 사이 간극 fastapi 
프로그래밍은 역할과 책임을 나누는 생각 과정 이다 
코드를 어디에다가 작성해야할까? 
역할, 책임, 레이어 
작업을 사용한다, 넘긴다, 위임한다 등 
이런 추상적인 단어(객체지향)가 한글로 들으면 어렵게 느껴진다 
하지만 코드로 보면 굉장히 간단하다 

20 의존성 Dependency fastapi 
A가 B를 가지고 사용하면(가지고 있으면) A는 B에 의존 
class A: 
    b_service : B = new B() 
    fun do_a (): 
        b_service.do_b() 
A 가 하는 일 = A 안의 코드 로직 = A의 책임 
B가 하는 일 = B 안의 코드 로직 = B의 책임 
A가 하는일 을 B한테 넘긴다(일을 맡긴다)  = A 코드를 B로 옮긴다 = 위임한다 
A가 B를 가지고 와서 B의 기능을 실행한다 의존성 (Dependency) 
어떤 기능이  다른 기능을  필요로  하는 관계
21 의존성 Dependency fastapi 
A가 B를 사용하면(가지고 있으면:has-a) A는 B에 의존 
user_router 가 user_service를 사용한다 = user_router는 user_service 에 의존한다 

22 의존성을 직접 생성하면 생기는 문제들 fastapi 
코드가 적으면 객체 생성이 쉽지만 복잡해지면 문제가 생긴다 
하나의  의존성이  변경된다 
1 곳에 쓴다→1 번의 변경
100 곳에 쓴다 → 100 번의 변경
객체를  생성할  때 조건( 파라미터 ) 이 생긴다면 ? 
사용하는  코드가  알 필요 없는 것까지  알아야한다  
테스트하려고 했는데, 
외부 시스템이 같이 따라온다 

23 의존성을 직접 생성하면 생기는 문제들 fastapi 
구현을 직접 생성하면, 나중에 코드 변경이 전파되고 테스트/디버깅이 어려워진다 
변경 전파 
B의 생성 방식/생성자 인자 변경이 A까지 따라온다 
연쇄 의존 
의존성이 깊어질수록(서비스→레포→DB…) 수정 범위가 커진다 
테스트 어려움 
외부 의존(DB/Email)을 쉽게 Mock으로 바꾸기 힘들다 
디버깅 비용 
실패가 “사용 코드”가 아니라 “초기화/주입 내부”에서 터져 원인 추적이 어려워진다 

24 DI: Dependency Injection 이란? fastapi 
https://fastapi.tiangolo.com/ko/reference/dependencies/?h=dep 필요한 객체를 (사용하는 객체가) 직접 만들지 않고 외부에서 넣어주는 방식 
필요한 객체를 
사용하는 쪽에서 직접 만들지 않고 
외부에서 만들어서 전달받는 설계 방식 
의존성을 내가 직접 만들고 있다 
→ 객체 생성 책임까지 함께 가지고 있다 
DI를 사용하면 
→ 객체 생성 책임을 밖으로 분리한다 

25 DI: Dependency Injection 장점 fastapi 
https://fastapi.tiangolo.com/ko/reference/dependencies/?h=dep 객체 생성과 사용이 분리된다 
객체 생성 위치를 한 곳으로 모을 수 있다 
- 생성 규칙(설정, 옵션, 순서)을 중앙에서 관리 
생성 방식이 바뀌어도 수정 범위가 줄어든다 
- \"사용하는 코드\"는 그대로 두고 \"만드는 코드\"만 바꾸면 됨 
객체의 생명주기를 FastAPI가 관리해준다 
- 요청마다 새로 만들지 / 재사용할지 선택 가능 
- 요청이 끝나면 자동 정리(cleanup)도 가능 
- 요청 단위로 의존성 라이프사이클을 제어할 수 있다 
dependency_overrides나 mock을 통해 테스트/환경별로 의존성을 교체할 수 있다 
26 FastAPI 에서 DI: Depends() fastapi 
FastAPI DI는 \"요청 시점\"에 의존성을 실행, 주입하는 방식(함수형태) 
FastAPI Depends는 요청 단위 
의존성의 생명주기를 요청 1번 으로 잡는다 
- 요청이 들어오면 의존성을 만들고 
- 같은 요청 안에서는 재사용하고 
- 요청이 끝나면 자동으로 정리한다 

27 FastAPI 에서 DI: Depends() fastapi 
FastAPI DI는 \"요청 시점\"에 의존성을 실행, 주입하는 방식(함수형태) 
1. 의존성을 어떻게 만들지 Provider 함수 등록 (정의) 
2. 선언 단계에서 객체 생성 책임을 fastapi 을 넘긴다 (위임) 
- 의존성 주입 
3. 요청 시점에 의존성으로 생성한 객체를 사용한다 

28 (실습) fastapi 에서 DI fastapi 
필요한 객체를 (사용하는 객체가) 직접 만들지 않고 외부에서 받아오는 방식 
1. 의존성을 어떻게 만들지 Provider 함수 등록 (정의) 
2. 선언 단계에서 객체 생성 책임을 fastapi 을 넘긴다 (위임) 
- 의존성 주입 
3. 요청 시점에 의존성으로 생성한 객체를 사용한다 
git switch feature/fastapi/userservicerefactor 
git pull 
uv sync 

29 fastapi 와 ORM 06 - 03 
Service  - Repository 
(docker-compose) mysql 
orm model - table 

30 SQLAlchemy fastapi 
파이썬 ORM DB 연동 라이브러리 
개발 환경 10강 강의 참고 
Repository 는 SQLAlchemy API를 캡슐화 
서비스 단에서는 UserRepository만 보이기 때문에 DB 교체도 가능 
테스트 시 Fake Repository로 교체 가능 → 단위 테스트 강력해짐 
FastAPI 공식 문서, 예제 코드에서도 SQLAlchemy를 기본 조합 

31 (실습) fastapi Repository 와 ORM fastapi 
실습 순서 
1. mysql 실행 (docker) 및 sql 세팅 
infra/mysql/docker-compose.yml 
db 실행 및 user 테이블 sql 적용  (작업이 안되신 경우) 
2. 접속 정보 기반 sqlalchemy 설치 및 fastapi 세팅 
3. model - table mapping 
4. repository 생성 및 query 확인 
5. service 와 연결 git switch feature/fastapi/orm 
git pull 
uv sync 
32 (실습) fastapi DB연결, Repository와 DB fastapi 
실습 진행 
1. mysql 실행 (docker-compose) 
0) docker 실행 
1) 기존 mysql 종료 및 infra/mysql/docker-compose.yml 실행 
cd infra/mysql 
docker-compose up -d 
2) datagrip 읕 통해 접속 및 ddl 실행 
cd ../sql 
ddl
git switch feature/fastapi/orm 
git pull 
uv sync 
33 (실습) fastapi 에 DB연결하고 Repository 로 DB 조작 fastapi 
실습 진행 
2. 접속 정보 기반 sqlalchemy 설치 및 fastapi 세팅 
git switch feature/fastapi/orm 
git pull 
uv sync 
34 (실습) fastapi 에 DB연결하고 Repository 로 DB 조작 fastapi 
실습 순서 
3. model - table mapping 
app/model/entities/base.py 
app/model/entities/user s.py
git switch feature/fastapi/orm 
git pull 
uv sync 
35 (실습) fastapi 에 DB연결하고 Repository 로 DB 조작 fastapi 
실습 순서 
4. repository 생성 및 query 확인 
app/repository/user_repo.py 
5. service 와 연결 
app/service/user_service.py 
app/deps.py 
git switch feature/fastapi/orm 
git pull 
uv sync 
36 (실습) SQLAlchemy 연동된 코드 확인 fastapi 
실습 순서 
6. 결과 확인 
git switch feature/fastapi/orm 
git pull 
uv sync 
37 총정리 fastapi 
FastAPI 와 Layered 아키텍처 
routers - service -  repository - db 
(객체지향) 책임, 위임, 사용 그리고 의존성 
의존성 주입의 장점 
dependency injection 
fastapi + ORM 
www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['07 Cloud Deployment Automation 1.txt'] = """25 Upstage 
클라우드 배포자동화-1 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: 배포 과정을 자동화하자 배포:자동화 
목차 
클라우드 서버 배포 
- 배포 
Github 을 통한 배포 자동화 
- github action 
- workﬂow 파일 작성 
- on: 트리거 
- jobs: 시킬 일 정의 
배포 branch 
- 배포 전략 (실습) 

4 클라우드 서버 배포 07 - 01 
배포란? 
배포 자동화: Github action 

5 배포란? 배포:자동화 
개발된 소프트웨어, 웹 페이지 등을 사용자들이 사용할 수 있도록 서비스하는 과정 
배포: 코드 → 제품 
- 코드 변경 내용을 서버에 반영하는 과정 
우리가 지금까지 git - github 을 통해 (clone, push, pull) 
EC2 에 웹서버를 올리고 실행하는 과정 
= 배포 과정 

6 현실 세상의 배포 배포:자동화 
달리는 차에 바퀴를 갈아 끼우는 과정 
밤낮 없이(24/7) 살아있는 서버  
언제 몰릴지 모르는 유저의 요청 
내가 짠 (이따위)코드가 나가도 돼? 
배포는 단순히 \"코드 올리기\"가 아니라, 안전하게, 반복 가능하게 
동일한 환경에서 서비스가 갱신되는 작업임. 
안전한 배포방법이 있을까? 

7 일관성 있는 배포의 필요성 배포:자동화 
팀원마다 배포 방법 제각각 이라면? 
● 시간 소모 
● 사람의 실수 배포 실패 가능성 (명령어 실수, 누락, 다른 브랜치 등) 
● 누가 언제 무엇을 배포했는지 모름 
● 롤백 기준 애매 
● 배포 기록 부재 
배포 과정을 자동화하자 
github 에서 제공하는 배포 자동화 도구: GitHub Actions 지금까지  배포  과정 
 코드 수정 → 로컬 개발/ 테스트 → ssh 로 EC2 접속  → 프로젝트위치  → git pull → 설치 → 서비스  재시작 
8 Github 을 통한 배포 자동화 07 - 02 
언제 실행해야할까? 
배포 단계는? 
9 GitHub Action 이란? 배포:자동화 
GitHub가 제공하는 자동화 플랫폼 
GitHub 제공 자동화 플랫폼 
push 이벤트 기반 실행 
YAML 기반 Workﬂow 
CI/CD 구현 가능 

10 GitHub Action 준비단계 배포:자동화 
개인 Repository (fork) 
(개인) 작업 repository // Fork 
(필수) 
git remote add my-origin {fork 된 주소} 
이번 시간 push 는 remote 입력 
git push my-origin {브랜치} 실습은 ORM 이전 코드로 진행 
(혹시나) DB 의존성 때문에 실습 실패할 경우가 
많을 수도 있어서 실습에선 제외하고 진행 
ec2에 docker 설치 후 
docker-compose 후 작업 진행해도 무방 github token 
workﬂow 권한 필요 
11 GitHub Secret 배포:자동화 
https://www.dailysecu.com/news/articleView.html?idxno=165043 배포 단계에서 비밀 정보 노출 위험 
github 은 오픈소스 기반이라 노출이 쉽다 
외부 서비스 접근을 위한 비밀번호, 데이터베이스 계정, 클라우드 접근 토큰 
외부 API를 사용하기 위한 API KEY  등이 들어가 있을 수 있다. 
github은 이런 비밀정보를 repository에서 안전하게(암호화) 저장할 수 있는 
비밀 저장소(Key-Value 형태)  github secret 을 가지고 있다. 

12 (실습) Repository에 github secret 등록 배포:자동화 
실습 과정 
0. fork 로 내 repo 등록 
1. secret 등록 
- repository 설정 
(주의 - 계정설정이 아님) 

13 (실습) ec2 에서 하던 작업을 스크립트로 만들기 배포:자동화 
start.sh git switch release/0.0.1 
git pull 
uv sync 
쉘 설정 
사용 중인 앱 중지 시작 (백그라운드, shell 종료해도 남도록) 
켜진 process id 기록 이 명령어를  ec2 에서 쳐보기  
수동으로  진짜 배포 되는지  체크
14 Github 을 통한 배포 자동화 
작성하기 07 - 03 
언제 실행해야할까? 
배포 단계는? 
15 Github action 배포 전체 흐름 배포:자동화 
https://tech.ktcloud.com/entry/What-is-DevOps-Github-Action 전체 배포 ‒ 협업 과정 

16 (예시) Github action 문법 둘러보기 배포:자동화 
Action → New workﬂow → Python Application (참고 예시) 
on: 배포 트리거(시작 시점) 
 jobs: 할 일들 

17 (실습) github ec2 서버 접속 배포:자동화 
파일 위치 
.github/workﬂows  폴더에 github action 파일들 
* 푸시 이벤트 발생 시 github 이 .github/workﬂows 
파일을 읽고 실행한다 
git switch release/0.0.1 
git pull 
uv sync 
18 on 스크립트: 트리거 배포:자동화 
on > push > branches 
github 은 이벤트를  인지한다  (push / pull request 등등  ) 
push 된 브랜치가  branches 의 브랜치와  맞는지  확인
push 한 branch 와 on: push: branches 가 맞아야   실행 
만약 release/0.0.1 에서 push 를 했는데  파일이  왼쪽과  같다면  
push 이벤트의  브랜치  ref = refs/heads/release/0.0.1 
branches 조건 = [\"main\"] 
→ 불일치  → 실행하지  않음
push 브랜치  ( 현재 브랜치 )
github 내부에서  변수로  처리 가능 
BRANCH=\"${{ github.ref_name }}\" workflow_dispatch: 
github ui 에서 조종 가능 옵션
19 jobs 스크립트: 할 일 배포:자동화 
jobs  > deploy > steps > with 
secret 값실제 agent 가 할일 
20 (실습) github 현재 브랜치를 on push 조건에 넣고 github 배포:자동화 
실습 순서 
.github/workﬂows  폴더에 github action 파일 
deploy-ec2.yml  변경 후 푸시 (fork 된 내 branch 여야 한다) 
변경 후 커밋 푸시  (branch와 맞는 지 확인) 
* 푸시 이벤트 발생 시 github 이 .github/workﬂows 파일을 읽고 실행한다 
git switch deploy/githubaction 
git pull 
uv sync 
21 (실습) github 현재 브랜치를 on push 조건에 넣고 github 배포:자동화 
실습 순서 
git switch deploy/githubaction 
git pull 
uv sync 
22 배포 branch 07 - 04 
언제 실행해야할까? 
배포 단계는? 
23 어떤 브랜치를 배포해야할까? 배포:자동화 
잘못된 브랜치 배포 = 장애 + 롤백 지옥 
CI/CD 파이프라인은 \"어떤 브랜치를 기준으로 배포할지\" 명확해야 안정적 운영 가능 
팀 규모가 커질수록 브랜치 전략은 점점 중요해짐 
배포 브랜치 기준 
•항상 안정 상태를 기준으로 한다 
•미리 merge 된 코드만 배포한다 (핫픽스 제외) 
•배포 브랜치는 팀 컨벤션으로 고정해 둔다 
•\"개발 중인 기능\"이 섞인 브랜치는 절대 배포 금지 
24 main 브랜치 / develop 브랜치 배포:자동화 
실제 배포 대상이 되는 제품 브랜치 
main branch 는 라이브 버전 
develop branch 는 개발 버전 
develop 에서 개발이 끝나고 테스트 된 버전이 main으로 

25 release 브랜치 배포:자동화 
develop 에서 main 으로 가기 전 테스트 하는 브랜치 
개발 환경에선 잘 동작해도 
라이브 환경에서 안 될 수가 있다 
라이브 환경과 흡사한 환경에서 확인할 필요가 있는데 
그 때 사용하는 브랜치 
곧 배포 기능을 테스트는 브랜치 

26 (실습) release branch 생성 후 배포 ‒ 실제 trigger 확인 배포:자동화 
실습순서 
1. release/0.0.1 이름으로 branch 분리 
2. github action workﬂow 에 release/* 일 경우 배포 하도록 설정 
3. 간단한 커밋 후  release/0.0.1 배포 후 github action 실행확인 
4. 웹 페이지에서 수동 실행 
27 (실습) release branch 생성 후 배포 ‒ 실제 trigger 확인 배포:자동화 
실습진행 
1. release/0.0.1 이름으로 branch 분리 
2. github action workﬂow 에 release/* 일 경우 배포 하도록 설정 
 
3. 간단한 커밋 후  release/0.0.1 배포 후 github action 실행확인 
4. 웹 페이지에서 수동 실행 
git switch release/0.0.1 
git pull 
uv sync 
28 (실습) release branch 생성 후 배포 ‒ 실제 trigger 확인 배포:자동화 
실습단계 https://github.com/inspire12/upstage-network-lecture/actions/runs/19958893728/job/57234247028 
git switch release/0.0.1 
git pull 
uv sync 
29 총 정리 배포: 자동화 
배포란? 
- 개발된 소프트웨어 등이 사용자가 사용할 수 있도록 서비스하는 과정 
- 내 코드가 제품(서비스)가 되는 과정 
 
배포 자동화와 github action 
- 배포 스크립트 
- 트리거  on 
- 에이전트 할일 Jobs    with / script 
배포 Branch 
- 안정적인 배포를 위한 브랜치 전략 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['09 Getting Started with Cloud Exploring AWS Components.txt'] = """25 Upstage 
클라우드시작하
기
AWS컴포넌트 알아보기 SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: AWS 컴포넌트를 통해 시스템 디자인 맛보기 AWS 컴포넌트 
목차 
AWS 컴포넌트 알아보기 
AWS 컴퓨팅 서비스 & 계정 & 데이터베이스 
AWS 스토리지 & 모니터링 & 네트워킹 
AWS 데이터 분석 & AI 
AWS 컴포넌트 조합 

4 AWS 컴포넌트 알아보기 09 - 01 
AWS를 컴포넌트를 통해 알아보는 서비스와 네트워크 이해 
5 EC2 올인 구조의 한계 AWS 컴포넌트 
초기 서비스는 EC2에 여러 인프라를 올려서 사용해도 문제 없다 
그러나 서비스가 커지면 (한 곳에 몰려 있는) 구조적 문제가 생긴다 
•성능 문제: 모든 트래픽과 작업이 EC2 한 곳에 몰림 
•확장 문제: 필요한 부분만 늘릴 수 없음 
•장애 전파 문제 
•운영/배포 복잡성 증가 
• EC2에 모든 기능이 모여 있으니 배포 위험도 매우 큼 운영을 하다보면 ec2에서 AWS 컴포넌트 역할별 분리가 필요해진다 

6 AWS 아키텍처 다이어그램 AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories Compute / Storage / Networking / DB ... ETC 

7 AWS 서비스 종류 용어 정리 AWS 컴포넌트 
컴퓨팅 계열 
•EC2, Lambda, ECS, EKS, Fargate 
스토리지 계열 
•S3, EBS, EFS 
데이터베이스 계열 
•RDS, Aurora, DynamoDB, ElastiCache 
https://docs.aws.amazon.com/ko_kr/whitepapers/latest/aws-overview/amazon-web-services-cloud-platform.html 
https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/architecture-overview.html?utm_source=chatgpt.com 
어떤 역할의 서비스들이 있는지 지도를 그려보자 
네트워크·전달 계열 
•VPC, ALB, NLB, API Gateway, CloudFront, Route 53 
메시징·이벤트 계열 
•SQS, SNS, EventBridge 
관측·보안·관리 계열 
•CloudWatch, CloudTrail, 
IAM, Conﬁg, Cost Explorer 
8 AWS 컴퓨팅 서비스 & 계정 & 데이터베이스 09 - 02 
EC2 
Lightsail 
RDS 
DynamoDB 
9 컴퓨팅 서비스 AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 애플리케이션을 실행할 수 있는 컴퓨팅 리소스를 제공하는 서비스 집합 
Amazon EC2 
 가상 서버 인스턴스를  생성하여  직접 운영하는  방식. 가장 유연하지만  관리 부담도  있음.
AWS Lambda 
 서버를  관리하지  않고 코드를  실행하는  서버리스  서비스 . 요청 기반 과금.
AWS Fargate 
 컨테이너를  위한 서버리스  실행 환경. ECS/EKS 에서 인프라  없이 컨테이너  실행 가능.
AWS Elastic Beanstalk 
 인프라  자동 구성을  지원하는  PaaS. 코드만  올리면  자동으로  배포/ 확장 관리.
Amazon Lightsail 
 EC2 보다 단순한  서버 운영 환경. 정액 과금 + 쉬운 UI 로 소규모  앱에 적합.
10컴퓨팅: AWS - EC2 AWS 컴포넌트 
필요한 만큼 컴퓨팅 파워를 즉시 생성하고 확장할 수 있는 AWS의 가상 서버 서비스 
EC2 = 컴퓨터 한대  
EC2는 AWS가 제공하는 '빌려 쓰는 컴퓨터' 서비스이다.  
'PC방 컴퓨터를 시간제로 빌리는 것'과 같음  
EC2를 사용하는 이유  
초기 비용 없음 (서버 컴퓨터 안사도 됨)  
빠르게 만드는 서버 (1~2분이면 준비)  
어디서나 접속 가능 (SSH 접근) 

11 계정: AWS - IAM AWS 컴포넌트 
AWS 리소스에 대한 접근 권한을 안전하게 관리하는 인증·인가 서비스 
IAM이란?  
•AWS 계정의 '신분증 및 출입 통제소'  
•AWS 리소스(EC2, S3 등)에 대한 접근을 안전하게 
관리하는 서비스.  
IAM을 사용하는 이유  
•업무별 최소 권한만 가진 계정을 만들어 보안 강화 
•체계적인 관리  
•실수로 중요 리소스를 지우는 행위를 
사전에 차단  

12 Database AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 구조적/비구조적 데이터를 저장하는 다양한 데이터베이스를 제공하는 영역 
Amazon RDS 
 MySQL, PostgreSQL, MariaDB 등 관리형  관계형  데이터베이스 . 백업/ 패치 자동화 .
Amazon Aurora 
 고성능  클라우드  네이티브  관계형  DB. MySQL·PostgreSQL 호환.
Amazon DynamoDB 
 완전관리형  NoSQL 데이터베이스 . 초고속 , 대규모  스케일링  가능.
Amazon Redshift 
 데이터  웨어하우스 . 대규모  분석 쿼리에  최적화 .

13 데이터베이스: AWS - RDS AWS 컴포넌트 
안정적으로 DB를 운영할 수 있는 AWS 관리형 관계형 데이터베이스 서비스 
 RDS란?  
AWS가 제공하는 \"빌려 쓰는 데이터베이스\" 서비스  
직접 데이터베이스를 구축하는 대신 클라우드에서 안전한 데이터 창고를 
시간제로 빌림  
RDS를 사용하는 이유  
•서버 관리 불필요 / 설치,백업,유지보수를 AWS가 대신 해줌  
•빠르게 시작 가능 / 클릭 몇번으로 구축 완료  
•안전하게 보관  
•여러 컴퓨터에서 쉽게 접근 가능  

14 AWS 스토리지 & 모니터링 & 네트워킹 09 - 02 
S3
cloudwatch 
VPC 
ELB 
Route53 
15 Storage 서비스 AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 파일, 객체, 블록 등 다양한 형태의 데이터를 저장·보관·백업하는 영역 
Amazon S3 
 고내구성 객체 스토리지. 파일 업로드, 정적 웹 호스팅 등 거의 모든 저장에 사용. 
Amazon EBS 
 EC2에 붙여 사용하는 블록 스토리지. 디스크처럼 사용하며 고성능 가능. 
Amazon S3 Glacier 
 장기 보관용 아카이브 스토리지. 매우 저렴하지만 복구 시간이 길다. 
Amazon EFS 
 여러 EC2 인스턴스에서 동시에 사용할 수 있는 공유 파일 스토리지. 

16 스토리지 서비스: AWS - S3 AWS 컴포넌트 
S3란?  
S3 = 인터넷 저장소  
S3는 aws가 '제공하는 파일을 저장하고 꺼내쓰는 공간' 
클라우드에 있는 안전한 폴더를 빌리는 것 
저렴하고 기간 무제한 
RDS vs S3 ?  
RDS는 구조화된 데이터를 저장하고, 
S3는 파일/이미지/영상 등 비정형 데이터를 저장  
RDS는 SQL쿼리로 접근, 
S3는 URL or API로 접근  
RDS는 앱 정보 저장,검색,연산 
S3는 대용량 파일 저장,배포,백업 목적 
언제 어디서나 원하는 만큼 데이터를 저장하고 가져올 수 있는 고내구성 객체 스토리지 서비스 
17 Management & Governance AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 리소스 모니터링, 로그 수집, 인프라 구성 자동화, 거버넌스 구축을 위한 도구 
Amazon CloudWatch 
 로그/ 메트릭  모니터링  및 알람 서비스 .
AWS CloudFormation 
 코드로  인프라를  정의(IaC) 하고 자동 구축.
AWS CloudTrail 
 모든 API 호출 기록을  저장하여  감사· 보안 분석에  활용.
AWS Systems Manager 
 EC2/ 서버 운영 자동화 , 패치 관리, 명령 실행 등 통합 관리 도구.

18 모니터링 AWS 컴포넌트 
https://www.atatus.com/blog/logging-traces-metrics-observability/ 애플리케이션의 로그·메트릭·트레이싱·알람 

19 모니터링 툴: AWS ‒ CLOUD WATCH AWS 컴포넌트 
AWS 자원의 모니터링 및 로깅 서비스  
EC2, RDS 등 모든 AWS 서비스의 건강상태를 체크하고, 
문제 발생 전 경고를 보냄  
cloud watch 는 저장된 로그량에 따라 과금이 되어 주기적 지워줘야한다 
오래된 로그를 S3에 저장하는 식으로 저렴하게 보관 
모니터링은 왜 필요한가?  (중앙화) 
서버가 갑자기 CPU 사용률이 90%로 치솟는다면  
이를 감지하고 경고   100%로 치솟을시, 
서버다운 장애 발생   서버에서 일어난 
모든일을 기록하여  나중에 문제의 
원인을 추적하는데 도움 
AWS 리소스와 애플리케이션의 로그·메트릭·알람을 제공하는 통합 모니터링 서비스 

20 네트워킹 & 콘텐츠 전달 서비스 AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 네트워크 구성, 도메인 관리, 트래픽 라우팅, 글로벌 콘텐츠 전달 등을 담당 
Amazon VPC 
 독립적인 가상 네트워크 환경 구성. 서브넷, 라우팅, 보안 등 설정 가능. 
Amazon Route 53 
 DNS 서비스. 도메인 등록/관리 및 트래픽 라우팅 기능 제공. 
Amazon CloudFront 
 CDN(Content Delivery Network) 서비스. 전 세계에 빠르게 콘텐츠 배포. 
Elastic Load Balancing (ALB/NLB) 
 여러 서버로 트래픽을 자동 분산하는 로드 밸런서. 

21 네트워킹: AWS - ELB AWS 컴포넌트 
여러 서버로 트래픽을 자동 분산해 서비스의 안정성과 확장성을 높여주는 AWS 로드 밸런싱 서비스 
 ELB란?  
AWS에서 제공하는 로드밸런서 서비스(Elastic Load Balancer)  
서버앞에서 트래픽을 나눠주는 장치  
하나의 서버로는 여러 트래픽을 감당하기 어려울때, 
여러 서버를 띄운 후, ELB로 트래픽 분산  
ELB를 사용하는 이유?  
- 직접 LoadBalancer를 설치 하는것보다 설정이 간편 

22 네트워킹: AWS - ROUTE53 AWS 컴포넌트 
도메인 등록부터 DNS 라우팅, 헬스 체크까지 제공하는 고가용성 DNS 서비스 
ROUTE53이란?  
•도메인 관리 서비스  
•사용자가 입력한 주소를 AWS 주소로 변환  
왜 도메인 관리가 필요할까?  
•도메인주소 (https://www.upstage.ai/) : 사람이 식별하기 쉬운 주소  
•실제 IP주소 (100.XXX.XXX.XXX) : 컴퓨터가 식별하기 쉬운 주소  
•사이트에 접근하기위해서는 
도메인주소 → 실제IP 주소로 변환 필요  
•이것을 수행하는 서버를 DNS서버라고 함 

23 AWS 데이터 분석 & AI 09 - 03 
Athena 
Glue 

24 데이터 분석을 위한 데이터 아키텍처 AWS 컴포넌트 
https://aws.amazon.com/ko/what-is/data-architecture/ 데이터가 있어야 분석을 할 수 있다, 분석을 위한 데이터는 어떻게 다룰까? 

25 Analytics (Data Engineering) AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 데이터 수집, 분석, 처리, 시각화를 위한 서비스 모음 
Amazon Athena 
 S3 데이터를 SQL로 바로 조회하는 서버리스 쿼리 서비스. 
Amazon Redshift 
 페타바이트급 분석을 위한 데이터 웨어하우스. 
Amazon Kinesis 
 실시간 스트리밍 데이터 수집 및 처리 플랫폼. 
AWS Glue 
 ETL(Extract/Transform/Load) 자동화 처리, 데이터 카탈로그 관리. 

26 데이터 분석을 위한 데이터 아키텍처 AWS 컴포넌트 
https://aws.amazon.com/ko/what-is/data-architecture/ 데이터가 있어야 분석을 할 수 있다 

27 AI & 머신러닝 AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 
1) AI Services → Amazon Rekognition 
이미지/영상 분석(객체 탐지, 얼굴 인식 등)을 API로 제공하는 완전관리형 AI 서비스 
2) ML Platform → Amazon SageMaker 
데이터 준비 → 학습 → 튜닝 → 배포까지 ML 전 과정을 지원하는 통합 ML 플랫폼 
3) Generative AI → Amazon Bedrock 
다수의 LLM(Claude, Titan 등)을 API로 제공하는 생성형 AI 허브 
4) ML Hardware → AWS Trainium 
GPU 대비 높은 학습 비용 효율을 제공하는 학습 전용 칩 
5) Data Preparation → AWS Glue 
ETL, 데이터 카탈로그, 데이터 정제를 지원하는 데이터 준비 자동화 서비스 
28 AI & 머신러닝 AWS 컴포넌트 
https://trailhead.salesforce.com/content/learn/modules/aws-cloud/discover-the-aws-service-categories 6) ML Workﬂow → SageMaker Pipelines 
학습 → 평가 → 배포까지 ML 파이프라인을 자동화하는 워크플로우 엔진 
7) Personalization → Amazon Personalize 
개인화 추천을 손쉽게 구축할 수 있는 완전관리형 추천 시스템 
8) Conversational AI → Amazon Lex 
NLU·ASR 기반 챗봇·음성봇 제작 서비스 (Amazon Alexa 기술 기반) 
9) AI Security → Amazon GuardDuty 
ML 기반 이상 탐지·위협 분석 보안 서비스 

29 AWS ‒ 그 외 수많은 컴포넌트 AWS 컴포넌트 

30 AWS 컴포넌트 조합 09 - 02 
시스템 디자인 관점 
31 웹서비스 기본 아키텍처 AWS 컴포넌트 
EC2 + ALB + RDS + S3 + CloudFront + IAM + CloudWatch 
구성 요소 
EC2: 웹/백엔드 서버 
ALB: 트래픽 분산 + 헬스체크 
RDS: MySQL/Postgres 등 관리형 DB 
S3: 정적 파일 업로드 
CloudFront: 이미지/정적 자원 글로벌 캐싱 
CloudWatch: 로그/지표/알람 
전통적인 웹서비스 구성에서 가장 많이 사용하는 정석 조합. 
애플리케이션 서버 계층, 데이터베이스 계층, 정적 자원 계층이 
분리되어 확장성, 안정성, 유지보수성이 좋아진다. 
32 이미지/파일 업로드가 많은 서비스 AWS 컴포넌트 
S3 + CloudFront + API Gateway(또는 EC2) + Lambda@Edge 
구성 요소 
S3: 이미지 원본 저장 
CloudFront: 빠른 CDN 제공 
API Gateway / EC2: 업로드 URL 발급 
Lambda@Edge: 이미지 변환/헤더 처리 등 엣지 로직 
EC2 에 파일을  저장하면  디스크  폭주, 장애 
전파 등이 발생하기  때문에  이미지 · 파일 
저장을  전부  S3 로 빼는  것이  베스트  
프랙티스 
33 비동기 작업 / 백그라운드 처리 아키텍처 AWS 컴포넌트 
API → SQS → Lambda(or EC2 Worker) → S3/RDS 
구성 요소 
API Gateway / EC2: 요청 수신 
SQS: 메시지 큐, 비동기 처리 
Lambda/Worker Server: 메시지 소비 후 실제 처리 
S3/RDS: 처리 결과 저장 \" 느려도  되는 작업\" 을 요청- 응답 
사이에서  제거하여  서비스  속도를  
빠르게  유지하기  위해.
• 이메일  발송
• 영상 인코딩 
• 썸네일  생성
• 대량 백오피스  작업
34 AI / 생성형 AI + RAG + 검색 기반 서비스 AWS 컴포넌트 
Amazon Bedrock + S3 + OpenSearch(KNN) + Lambda(or EC2) + API Gateway 
구성 요소 
Bedrock: LLM API (Claude, Titan 등) 
S3: 문서 저장소 
OpenSearch: 벡터검색 기반 RAG 
Lambda/EC2: Retrieval + 프롬프트 구성 
API Gateway: 외부 API 제공 생성형  AI 서비스에  가장 널리 쓰이는  아키텍처 
문서 기반 QA, 추천, 사내 지식 검색 등 대부분의  AI 
서비스가  이 구조를  따른다 .
35 총 정리 AWS 컴포넌트 
AWS 컴포넌트 종류 
- 컴퓨팅 
- 저장소 
- 네트워킹 
- 데이터베이스 
- 모니터링 
- AI 등 
 
상황에 맞는 AWS 조합 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['1-08 Cloud Deployment Automation 2.txt'] = """25 Upstage 
클라우드 배포자동화-2 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: CI / CD 과정 이해하기 배포:자동화 
목차 
CI/CD 
- github action 구조와 현업 배포 구조 
유닛 테스트 
배포를 위한 AWS 작업 

4 CI/CD 08 - 01 
CI에서 빌드 검증이 필요한 이유 

5 Github action 전체 흐름 배포:자동화 
https://medium.com/@armond10holman/a-guide-to-setting-up-ci-cd-pipelines-with-github-actions-d7fc98e78a87 전체 배포 ‒ 협업 과정 

6 빌드 검증이 필요한 이유 
만약 코드가 잘못 되었다면? 
지금까지는 작업이 완료되면 배포 서버에서 바로 작동 
배포 서버에서 에러가 발생, 기존 서버가 꺼진 후 
재시작 시 에러가 난다면 서버 장애 
PR 하나가 전체 시스템을 깨뜨릴 수도 있다 
 
배포:자동화 
7 CI: 지속적 통합 (Continuous Integration) 배포:자동화 
CI는 코드의 건강검진이다 
배포 자동화 툴 내에서 아래 사항들을 진행 
•Lint 검사 
•타입 검사 (mypy) 
•유닛 테스트 
•패키지 빌드 검증 
•빌드 후 빌드 결과물 저장소에 업로드 → 버전 관리/롤백 

8 Github action 구성 요소 배포:자동화 
https://tech.ktcloud.com/entry/What-is-DevOps-Github-Action GitHub가 제공하는 자동화 플랫폼 
Action 
Github Actions Workﬂow의 개별 작업 단위 
Runner 
 Action을 실행하는 컴퓨팅 리소스 
- Github Hosted Runner 
- Self Hosted Runner 
Package 
프로젝트 Build 결과물을 저장하고 배포 
빌드 버전 

9 CD: 지속적 배포 (Continuous Delivery / Deployment) 배포:자동화 
빌드를 배포에 전달/릴리즈 
검증된 코드를 자동으로 배포하는 과정 
•스테이징/프로덕션 배포 
•수동 승인 
•롤백 전략 
•”

10 유닛 테스트 08 - 02 
유닛 테스트와 자동화 
pytest 

11 유닛 테스트 필요성 배포:자동화 
가장 작은 단위의 기능을 검증하는 테스트 
코드 변경이 많아질수록 \"안전망\"이 필요하다 
기능을 추가하거나 수정할 때 다른 부분이 깨지는 것을 잡아줌 
\"어제까지 잘 됐는데 오늘은 왜 안 돼?\" → 테스트가 방지함 
리팩토링과 구조 개선의 자신감을 준다 
테스트가 커버하는 로직은 마음 놓고 바꿀 수 있음 
성능 개선, 코드 정리 등 장기 유지보수에 필수 
•”

12 유닛 테스트 필요성 배포:자동화 
가장 작은 단위의 기능을 검증하는 테스트 
반복적인 수동 테스트를 줄여서 개발 속도를 높여준다 
서버 켜고, 요청 보내고, 콘솔 확인하는 반복 작업을 자동화 
pytest 한 줄로 즉시 확인 가능 
팀 개발에서 품질 기준을 통일한다 
테스트가 \"프로젝트의 규칙 문서\" 역할 
새 팀원이 와도 기존 기능이 깨지는지 자동 확인 
•”

13 유닛 테스트란? 배포:자동화 
가장 작은 단위의 기능을 검증하는 테스트 
•”
비즈니스 규칙/계산/검증 로직 등 핵심 로직을 독립적으로 테스트 
데이터베이스 / 네트워크 / UI와 같은 외부 요소는 제거하고 테스트함 
실패 시 바로 피드백 → 오류 위치와 기대 값이 자동 표시 
테스트 실패 메시지가 \"디버깅 가이드\" 역할 
테스트 코드를 만드는 이유 
● 코드를 마음 놓고 고치기 
● 의존성을 분리하게 만드는 설계 압박 
○ 테스트하기 좋은 코드 = 좋은 설계 
● 이 코드가 뭘 책임지는지 명확해짐 

14 pytest 배포:자동화 
파이썬 테스트 실행기이자 테스트 작성 프레임워크 
문법이 간결, 설정할 게 거의 없음 
assert 하나로 유닛 테스트 작성 가능 
파일 이름 규칙: test_*.py 또는 *_test.py 파일을 테스트 파일로 인식 
함수 이름 규칙: test_로 시작하는 함수가 테스트로 인식 
•”

15 (실습) pytest 로 유닛테스트 만들기 배포:자동화 
간단한 pytest 작성하기 + 디버깅하기 
assert를 통한 검증  
•”
git switch deploy/unittest-mock 
git pull 
uv sync 
테스트  실행
  pytest tests/test_easy.py 

16 (실습) pytest 로 유닛테스트 만들기 배포:자동화 
의존성이 있는 객체 pytest 작성하기 + 디버깅하기 
assert를 통한 검증  
•”
git switch deploy/unittest-mock 
git pull 
uv sync 
테스트  실행
  pytest tests/test_user_repository.py 

17 의존성과 mock 을 통한 외부 의존성 끊기 배포:자동화 
Mock은 진짜 객체 대신 \"가짜 객체\"를 넣어서 테스트하는 기술 
정말 테스트할 대상 객체만 다룰 수 있다. 
테스트에서 우리가 알고 싶은 것 = \"이 함수가 어떤 행동을 했는가?\" 
테스트 때 실제로 저장되었나? X 
→ repository.save 가 호출되면 된다 
Mock 객체 전용 행동 검증 메서드 
해당 함수가 테스트 과정에서 호출이 되었나 
외부 시스템 호출을 가짜로 대체해, 단위 테스트를 빠르고 안정적으로 만드는 기법 
•”

18 (실습) mock pytest 로 유닛테스트 만들기 배포:자동화 
실습 순서 
1. tests/test_user_service.py 
TestUserService 생성 
2. setup_method 에서 UserRepository 를 mock 으로 선언 
     service 생성 시 mock_repo를 넘겨서 service 를 생성 
•”
git switch deploy/unittest-mock 
git pull 
uv sync 
테스트  실행
  pytest tests/test_user_service.py 
19 (실습) mock pytest 로 유닛테스트 만들기 배포:자동화 
실습 순서 
3. 테스트 시 mock_repo 함수를 호출할 때 실행하는 대신 반환할 값을 설정 
4. 테스트 진행(디버깅)으로 실제 실행하는 대신 값만 반환되는지 확인 
5.테스트 결과 확인 
•”
git switch deploy/unittest-mock 
git pull 
uv sync 

20 배포 과정에서 유닛 테스트 필요성 배포:자동화 
유닛 테스트는 배포 전 자동 검증 단계 
배포 = 기존 코드 위에 계속해서 변경을 얹는 작업 
작은 수정이 기존 기능을 망가뜨릴 수 있음 
유닛 테스트는 \"이전 기능이 아직 살아있다\"는 확인 
배포 후 발견되는 버그의 비용은 훨씬 큼 
● 긴급 롤백 
● 장애 공지 
● 사용자 신뢰 하락 
유닛 테스트는가장 싸게 실패할 수 있는 단계 
•”

21 github action 에서 유닛 테스트 실행 배포:자동화 
jobs: test: 
•”
테스트 돌기 위한 최소한의 설치 
테스트 실행 git switch deploy/ci 
git pull 
uv sync 
.github/workﬂows/ci.yml 
22 github action 에서 유닛 테스트 실패시 중지 배포:자동화 
jobs: test: 
•”
테스트 돌기 위한 최소한의 설치 
테스트 실행 git switch deploy/cicd 
git pull 
uv sync 
.github/workﬂows/cicd.yml 
23 (심화) 테스트 커버리지란? 배포:자동화 
코드 경로가 실제로 검증되었는지를 측정 
커버리지는 목표가 아니라 신호(signal) 
낮은 커버리지 → 테스트되지 않은 코드 영역이 명확함 
•”
\"어디까지 검증했는가\"를 수치로 표현한 지표 

(실습) github action (CI) 단계에서 유닛테스트 진행 
24 배포:자동화 
•”
예시 링크
25 (참고) Elastic IP : 접근 주소 고정 08 - 03 
고정 공인 IP 
안정적인 배포 장소 
26 클라우드 컴퓨터는 빌리고 반납을 자주하게 된다 배포:자동화 
배포하는 위치가 계속 바뀐다면? 
다만 인스턴스를 껐다 키면 IP 가 바뀐다 
 
ip가 자주 바뀌게 되면 서비스가 불안정해진다 
인스턴스를 종료하고 다시 시작해도 바뀌지 않을 
고정된 IP(elastic ip) 가 필요하다 

27 (참고) Elastic IP 할당과 인스턴스 연결 배포:자동화 
실습 순서 
1. elastic ip 할당 
2. 생성된 elastic ip 우클릭 Associate Elastic IP address 
3. ec2 와 연결 

28 (실습) Elastic IP 발급 이후 배포:자동화 
(주의) 기존 IP 아닌 새로 받은 Elastic IP 로 접근해야한다 

29 주의) Elastic IP 비용 이슈 배포:자동화 
ec2 종료 후 다시 쓰지 않을 목적이면  Elastic ip 도 삭제 
실행 중인 인스턴스에 연결된 IP 주소 (Elastic IP) 한 개는 무료로 사용 가능 
하지만 두 개 이상의 Elastic IP 혹은 할당되지 않은 Elastic IP는 비용 청구된다 
주의) 
서비스 완전 종료 시 Elastic IP 도 같이 삭제 해줘야한다 

30 코드로 인프라 관리 하기 
AWS CLI 08 - 04 
Aws cli 
IaC (Infra as a Code) 

31 사람이 매번 손으로 하는 설정의 위험 
배포:자동화 
실수, 불일치, 누락 등등 
콘솔에서 하는 클릭 기반 설정의 가장 큰 단점은 일관성의 부족 
태그 누락, EC2 타입 실수, 보안 그룹 규칙 순서 변경 같은 사소한 차이가 나중에 큰 문제의 씨앗 
- 운영 환경에서만 생기는 버그 
- 개발/운영 환경이 서로 다른 모습 
- 비용 정리가 안 되고 태그가 뒤죽박죽 
- 누가 무슨 설정을 바꿨는지 추적 불가능 
\"클릭은 빠르게 만들 수는 있지만, 정확하게 만들 수는 없다. \" 

32 IaC: Infrastructure as Code 배포:자동화 
인프라도 코드로 관리할 수 있을까? 
인프라를 '설정'이 아니라 '코드'로 정의 
재현 가능: 같은 코드를 적용하면 어디서든 똑같은 인프라 생성 
버전 관리: Git으로 이력 추적, 이전 버전으로 되돌리기 가능 
리뷰 가능: PR로 인프라 변경도 코드 리뷰 
자동화: CI/CD 파이프라인에 인프라 변경까지 포함 가능 

33 aws cli 란? 배포:자동화 
웹 콘솔 대신 명령어(텍스트)로 aws를 조작하는 도구 
https://aws.amazon.com/ko/cli/ - 명령줄 쉘에서 명령을 사용하여 AWS 서비스와 상호 작용할 수 있는 오픈 소스 도구 
- EC2, ECR, S3, IAM 같은 AWS 리소스를  명령줄에서 직접 생성/수정/삭제 가능 
- 사람이 버튼을 누르지 않아도  스크립트나 자동화에서 동일한 작업을 반복 가능 
- 리소스 확인 및 제거 

34 (실습) aws cli 사용 방법 배포:자동화 
(실습과정) aws cli 
1. ec2 인스턴스에 aws cli role 추가 
권한이 된  ec2 내에서 cli 로 명령 가능 
실습은 이 방식으로 진행 
2. 키 발급 방식 
aws conﬁgure 으로 로컬 등에서 사용할 수 있다  
단점: aws key 노출 위험  

35 (실습) 계정에 role 이 있는지 확인 배포:자동화 
IAM → Roles → SafeRole-upstage-sesac-1 검색 

36 (실습) ec2에 role 를 추가하기 - 끝 배포:자동화 
ec2 instance 우클릭 → Security → Modify IAM Role → SafeRole-upstage-sesac-{X} 등록 

37 (실습) aws 스크립트 설치 배포:자동화 
ec2 접속 후 aws 스크립트 설치 
https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-install.html 
sudo apt install unzip 
curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\" 
unzip awscliv2.zip 
sudo ./aws/install 

38 (참고) ec2 에 role 을 등록 방법 배포:자동화 
IAM → Roles → Create Role (계정엔 해당 권한이 없습니다) 
AWS Service, ec2 선택 → policy 선택  → AmazonEC2FullAccess, AWSBillingReadOnlyAccess 선택 

39 (참고) aws access key 로 aws cli 설정 배포:자동화 
key 발급 & aws cli 설정 
aws conﬁgure 
key 발급 
1. iam users 접속
https://console.aws.amazon.com/iam/home?region=ap-southeast-2#/users 
2. 유저 선택 
3. Security credentials 
4. create access key 

40 (참고) aws access key 로 aws cli 설정 배포:자동화 
aws 설정 
4. create access key 
next → create access key 

41 (참고) aws access key 로 aws cli 설정 배포:자동화 
aws conﬁgure 
https://us-east-1.console.aws.amazon.com/iam/home?region=ap-southeast-2#/users/create 
aws conﬁgure 저장 위치 

42 (참고) aws 키 발급 과정과 aws cli 계정 세팅 배포:자동화 
aws conﬁgure 
IAM → User → Create User 
계정 키 받아오기 
https://us-east-1.console.aws.amazon.com/iam/home?region=ap-southeast-2#/users/create 

43 (참고) aws 세팅 키 발급 과정 배포:자동화 
aws conﬁgure 
IAM → User → Create User 
생성된 유저 클릭 → 계정 키 생성 → CLI 선택 생성 
https://us-east-1.console.aws.amazon.com/iam/home?region=ap-southeast-2#/users/create 

44 (참고) aws 세팅 키 발급 과정 배포:자동화 
aws conﬁgure 
IAM → User → Create User 
생성된 유저 클릭 → 계정 키 생성 → CLI 선택 생성 
키 복사 (혹은 csv 저장) 
region 은 url 의 ?region= 부분 
https://us-east-1.console.aws.amazon.com/iam/home?region=ap-southeast-2#/users/create 

45 AWS CLI 명령어 조합 08 - 05 
사용 중인 리소스 확인 
리소스 시작/종료 
비용 확인 
46 aws cli 사용법 배포:자동화 
aws <서비스> <명령어> <옵션> --파라미터 값 
aws: CLI 실행 명령 
서비스(service): ec2, s3, iam, lambda 등 
명령어(command): describe, list, get, put, create, delete 
옵션(option): --region, --proﬁle, --output 
파라미터(parameter): 인자 값들 (리소스 ID, 파일 경로 등) 

47 aws cli 자주 쓰는 명령 패턴 배포:자동화 
인스턴스 조회 
aws ec2 describe-instances 
인스턴스 시작/중지 
aws ec2 start-instances --instance-ids i-1234567890 
aws ec2 stop-instances --instance-ids i-1234567890 
새 인스턴스 생성 
aws ec2 run-instances --image-id ami-1234 --instance-type t2.micro 
사용자 생성 
aws iam create-user --user-name developer1 
정책 붙이기 
aws iam attach-user-policy \\ 
  --user-name upstage \\ 
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess 

48 비용 최적화를 위한 aws cli 명령어 배포:자동화 
사용중인 인스턴스 조회 
 aws ec2 describe-instances \\ 
  --ﬁlters \"Name=instance-state-name,Values=running\" \\ 
  --query \"Reservations[].Instances[].{ID:InstanceId,Name:Tags[?Key=='Name']|[0].Value}\" \\ 
  --output table --no-cli-pager 
 
(월간) AWS 비용 확인하기  
aws ce get-cost-and-usage --time-period Start=$(date +%Y-%m-01),End=$(date 
+%Y-%m-%d) --granularity MONTHLY --metrics BlendedCost --query 
\"ResultsByTime[0]. Total.BlendedCost.{Amount:Amount,Unit:Unit}\" --output table 
--no-cli-pager 링크 
49 (실습) 비용 최적화를 위한 aws cli 명령어 배포:자동화 
사용중인 인스턴스 조회 
--output table --no-cli-pager 
 
(월간) AWS 비용 확인하기 ( 권한이 없음) 
링크 
50 총 정리 배포: 자동화 
github action 배포 과정에서 빌드 검증 
- CI/CD 
- 유닛 테스트와 유닛 테스트 자동화 
 
aws cli 로 코드로 인프라 관리 
- aws cli 및 등록 
- aws cli 명령어 
- aws cli 자주 쓰는 명령 모음 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['1-Why Cloud Computing Is Essential for AI Agent.txt'] = """"""
    s.raw_texts['2-10 Network and AI.txt'] = """25 Upstage 
네트워크와 AI 
SPEAKER 
서영학 © 2025 Upstage Co., Ltd. 
2 저작권 안내 
 
(주)업스테이지가 제공하는 모든 교육 콘텐츠의 지식재산권은 
운영 주체인 (주)업스테이지 또는 해당 저작물의 적법한 관리자에게 귀속되어 있습니다. 
콘텐츠 일부 또는 전부를 복사, 복제, 판매, 재판매 공개, 공유 등을 할 수 없습니다. 
유출될 경우 지식재산권 침해에 대한 책임을 부담할 수 있습니다. 
유출에 해당하여 금지되는 행위의 예시는 다음과 같습니다. 
● 콘텐츠를 재가공하여 온/오프라인으로 공개하는 행위 
● 콘텐츠의 일부 또는 전부를 이용하여 인쇄물을 만드는 행위 
● 콘텐츠의 전부 또는 일부를 녹취 또는 녹화하거나 녹취록을 작성하는 행위 
● 콘텐츠의 전부 또는 일부를 스크린 캡쳐하거나 카메라로 촬영하는 행위 
● 지인을 포함한 제3자에게 콘텐츠의 일부 또는 전부를 공유하는 행위 
● 다른 정보와 결합하여 Upstage Education의 콘텐츠임을 알아볼 수 있는 저작물을 작성, 공개하는 행위 
● 제공된 데이터의 일부 혹은 전부를 Upstage Education 프로젝트/실습 수행 이외의 목적으로 사용하는 행위위 
3 목표: AI 가 있는 시스템 Network와 AI 
목차 
GPU 운영에 대한 기초적 이해 
AI가 있는 서비스 아키텍처 
RAG 란? 
- AI 클라우드와 Vector DB를 통해 AI서비스 연동하기 
4 GPU 운영을 한다면 10 - 01 
5 AI 서버를 다룰 때 알아야할 것들 Network와 AI 
GPU 는 귀하고 비싼 컴퓨터 자원이다 
일반 서버는 금방 생기지만 GPU 서버는 수량이 적고 예약도 어렵다 

6 AI 를 쓰기 위해선 GPU 메모리에 모델이 올라가야(로드)된다 Network와 AI 
GPU 는 켜는데 시간이 더 오래 걸린다 
•GPU NVIDIA 드라이버 로딩, CUDA , cuDNN 등 라이브러리 초기화 시간 
•모델 파일 (수십 GB)을 GPU 메모리에 올리는 과정도 오래 걸린다 
•GPU 서버 한 번 줄이면 (scale-in) 다시 늘리는데 오래 걸려 장애로 이어지기도 한다 
그래서 첫 요청을 처리할 때 생기는 지연 시간(cold start)이 생긴다 
LLM 모델은 특히 더 크다 
LLM 모델 크기, LLAMA 70B = 140GB 
메모리에 올려야 연산이 되는데 모델이 너무 커서 올리는 시간이 오래걸림 
7 GPU 장애는 왜 잘 날까? Network와 AI 
GPU 는 열·메모리·연산 구조가 훨씬 민감한 특수 장치 
- 동시 연산 처리가 CPU보다 훨씬 많아 열이 크게 발생 
- 열이 많으면 속도 감소 및 커널 에러 발생 위험 
- 전력, 발열 때문에 하드웨어 스트레스가 크다 (수명) 
- GPU 모니터링에서 온도는 중요한 지표 
- 냉각(쿨링) 시스템의 중요성 
GPU는 메모리가 비싸고 LLM은 메모리를 엄청 쓴다 
- 계산량이 늘어나면 (긴 프롬프트) 쉽게 OOM (Out Of Memory) 

8 GPU 장애는 왜 잘 날까? Network와 AI 
Multi-GPU 환경 등 \"GPU끼리 대화 통신\" 과정에서 지연 문제 
- 큰 모델은 GPU 여러 개가 나눠서 계산하는데 이때 GPU끼리 데이터를 계속 주고받아야 함 
- GPU 간 통신이 조금만 느려도 전체 모델 느려짐 
- 하나의 GPU에서 오류 나면 전체 오류로 전파될수도 있다 
GPU 드라이버, CUDA, PyTorch 등 버전 충돌 
- GPU 생태계는 보전 호환성이 아주 민감 
하드웨어 에러 
- GPU 생태계는 보전 호환성이 아주 민감 
9 GPU 를 잘 쓰는 방법 Network와 AI 
요청은 하나가 아니라 묶어서 처리 
GPU는 한 번에 많이 계산할 때 효율적이다 
GPU 하나에 여러 모델을 위험 
GPU 하나에 여러 모델이 올라가면 두 개가 GPU 서로 뺏는다 
메모리 단편화 발생 
OOM 발생 위험이 커짐 (토큰 캐시, batch buﬀer 등 추가 메모리) 
다만 최근에 GPU 가상화 기술들이 많이 발전하고 있는 중 (ex- AWS Bedrock) 
하나의 모델에 여러 GPU는 굿 
모델의 한 층을 여러 GPU가 나눠 계산하는 기술 (NV LINK) 
다만 이 때 네트워크 문제 (Latency 급증, throughput 감소) 가능 
10 현실적으로 AI를 사용하는 방법 Network와 AI 
GPU 없이도 클라우드를 통해 AI 서비스 운영 

11 (실습) Upstage API를 활용해 AI chat 해보기 Network와 AI 
실습 순서 
1. Upstage API 키발급(가입) 
1-1. API key 환경변수로 처리 
2. 프로젝트  세팅 후 upstage 샘플 코드 확인 
 
3. FastAPI API와 연동 
openai 설치 (버전) + 호환성 
4. 답변확인 
git switch feature/ai/upstage-chat 
git pull 
uv sync 
LLM 쓰기 전 주의할 점 
● API Key는 코드에 직접 넣지 않는다 
● 환경 변수로 관리한다 
● 외부 API 호출이므로 실패 가능성을 고려한다 
● 응답 속도와 비용을 인지한다 
12 (실습) Upstage API를 활용해 AI chat 해보기 Network와 AI 
실습 진행 https://console.upstage.ai/docs/capabilities/generate/chat 
1. Upstage API 키발급 ( 가입) https://console.upstage.ai/docs/getting-started 
1-1. 발급한 API key 환경변수로 처리 
 .env 파일 
git switch feature/ai/upstage-chat 
git pull 
uv sync 
13 (실습) Upstage API를 활용해 AI chat 해보기 Network와 AI 
실습 진행 https://console.upstage.ai/docs/capabilities/generate/chat 
2. 프로젝트  세팅 후 
     upstage 샘플 코드 확인 
git switch feature/ai/upstage-chat 
git pull 
uv sync 
14 (실습) Upstage API를 활용해 AI chat 해보기 Network와 AI 
실습 진행 
3. FastAPI API와 연동 
openai 패키지 설치 (버전) + 호환성 
API 생성 
git switch feature/ai/upstage-chat 
git pull 
uv sync 
15 (실습) Upstage API를 활용해 AI chat 해보기 Network와 AI 
실습 결과 
git switch feature/ai/upstage-chat 
git pull 
uv sync 
16 router에 AI 연동 코드가 있는게 맞을까? Network와 AI 
Router의 책임은 요청/응답 처리 
유저의 채팅 메시지(요청)를 받아 chat_service로 넘기자 
Service는 요청을 받고 AI 호출 전, 추가적인 전처리를 통해 질문을 다듬고 Client에 보낸다 
● 비용 최적화, 답변 최적화, 답변 정제 등 
Repository는 DB 뿐 아니라 외부 의존성(LLM API 호출)을 관리한다 
● Repository / AI Client 에서 Upstage AI 연동 
추후 다른 LLM으로 서비스를 바꾼다고 했을 때 Repository만 수정하면 된다. 
17 (실습) client로 Upstage API 연동 리팩토링 Network와 AI 
실습 진행 
1. service/ chat_service.py 생성
● chat request를 받아서 repository에 이관 (추가적인 로직을 넣을 준비) 
2. repository / upstage_client.py 에 UpstageClient 생성 
● router의 코드 중, 연동 관련 코드를 UpstageClient로 이관 
● OpenAI 라이브러리 의존성, key 관리 등 
git switch feature/ai/upstage-layered 
git pull 
uv sync 
18 서비스 아키텍처 with AI 모델 10 - 02 
19 복잡해지는 서비스 구조와 서버 Network와 AI 
수 많은 기능들을 추가되는 서비스 
•Web Server 
•Auth Server 
•API Gateway 
•AI Inference Server 
•Vector DB Server 
•Background Worker 

20 여러 서버로 나눈 이유? (역할을 나눠 각각 띄우는 이유) Network와 AI 
각 서버가 하는 역할이 다르다, 그리고 각 서버가 받는 부하(메모리크기, 연산량)가 다르다 
단순 요청을  넘겨주는  서버 
인증 데이터를  가져오는  서버 
영상 같은 미디어를  압축 저장하는  서버 
AI 추론을  진행하는  서버 
수 많은 데이터를  저장하는  서버
유저의 응답과 연관 
속도가 중요
리소스를 많이 먹는다
21 AI 모델: 학습과정 / 추론 과정 Network와 AI 
AI 서비스화를 위해 학습이 된 모델을 \"추론 과정에 집중한다 \" 
결국 모델을 학습을 시키는 이유는 추론을 시키기 위해 
추론과정 특징 
- 응답 속도  = 서비스 품질 
- 모델 크기 커질 수록 추론 가격 증대 (GPU 비용) 
어떻게 추론을 안정적이고 빠르게 제공하는가? 

22 AI 모델을 가진 시스템에서 주의할 점 Network와 AI 
AI에서 중요한 건 데이터! 
•모델 성능 상한선은 데이터 품질이 결정 
•같은 AI모델이라도 데이터 따라 성능 차이 큼 
•데이터 수집 · 정제 · 업데이트 중요 
•추론은 학습의 결과물 재사용 과정 
데이터를 어떻게 효율적으로 구조화하고 저장할까? 
23 데이터 처리가 중요한 이유 Network와 AI 
AI는 '망가진 데이터'를 그대로 이해하지 못한다 
데이터 품질 = 모델 품질 
•noise 제거 
•schema 통일 
•텍스트 정규화 
•문서 chunk 분할 
•토큰 길이 최소화 
•이상한 답변 필터링, 정제 
24 데이터 전처리 / 후처리 예시 Network와 AI 
전처리 예시 
•HTML 태그 제거 
•표/리스트 구조 정리 
•제목/본문 분리 
•문서 단위 chunking 
•embed-friendly 형식으로 변환 후처리 예시 
•모델 출력 정제 
•포맷팅 · JSON 변환 
•hallucination 필터링 
•요약/정답 구조화 
25 AI 데이터는 지속적으로 재학습한다 Network와 AI 
데이터가 바뀌면 학습도 다시 필요함 
실무 데이터는 계속 업데이트 
데이터 수집의 필요성과 AI 학습 파이프라인으로 연결 재수집  → 재전처리  → 재임베딩  → 재학습의  루프
26 RAG 시스템 10 - 03 
vector db 
embedding 
Indexing 
RAG 
27 AI 서비스를 만들고 싶은데.. Network와 AI 
좀 더 현실적인 문제점 
AI 서비스를 만들고 싶다. 
챗봇도 만들고, 추천도 하고, 질문도 잘 답했으면 좋겠다. 
모델은 우리 서비스의 최신 정보를 모른다 
사내 문서, 정책, DB 내용은 반영되지 않음 
데이터가 바뀔 때마다 다시 학습할 수도 없다 

모델이 모르는 정보를 \"외부 지식으로 보완\" 
AI 모델 
일반 지식은 많지만 
우리 회사 문서나 특화된 자료는 모르는 사람 
Vector DB 
잘 정리된 참고서 모음집 
Vector DB(벡터 데이터베이스) 에 저장해둔 자료들 중에서 
가장 비슷한 내용(top-k)을 검색해서 
그 자료를 AI 모델에게 함께 전달하면 
모델이 훨씬 정확하고 풍부한 답변을 만들 수 있음 
28 RAG: Retrieval + Generation Network와 AI 
https://medium.com/@drjulija/what-is-retrieval-augmented-generation-rag-938e4f6e03d1 

29 Vector DB (Store) 란? Network와 AI 
Vector 검색 
Vector 는 행렬 (공간) 
데이터를 행렬로 표현할 수 있으면 
거리를 찾을 수 있다(코사인 유사도) 
거리 = 유사도 
대화가 아니라 단순 유사도 찾을 거면 vector store 에서 처리 가능 
ex) 추천 시스템, 닮은 사진 찾기 등 

30 Embedding Network와 AI 
데이터를 숫자(행렬) 로 바꾸는 과정 
문서 수집 
전처리 
chunk 분할 
임베딩 생성 
vector 저장 
검색 
디테일한 과정은 수업 외 내용 
https://www.syncly.kr/blog/what-is-embedding-and-how-to-use 
https://www.syncly.kr/blog/what-is-embedding-and-how-to-use 
https://console.upstage.ai/docs/capabilities/embed 
https://console.upstage.ai/docs/capabilities/embed 

31 RAG: Data indexing Network와 AI 
https://medium.com/@drjulija/what-is-retrieval-augmented-generation-rag-938e4f6e03d1 vector db 에 데이터(지식)를 저장하는 방식 

32 RAG: Retrieval & Generation Network와 AI 
https://medium.com/@drjulija/what-is-retrieval-augmented-generation-rag-938e4f6e03d1 실제 답변을 하는 단계 

33 (실습) Upstage API 를 활용해 embedding 해보기 Network와 AI 
실습 순서 https://console.upstage.ai/docs/capabilities/embed 
1. Upstage API 키발급 
2. Upstage 샘플 코드 사용 
model = \"embedding-query\" 
3. fastapi api 와 연동 
openai 설치 (버전) + 호환성 
4. 답변확인 git switch feature/ai/upstage-embedding 
git pull 
uv sync 
34 (실습) Upstage API 를 활용해 embedding 해보기 Network와 AI 
실습 순서 
1. Upstage API 키발급 ( 가입)
https://console.upstage.ai/docs/getting-started 
2. 프로젝트  세팅 후 upstage 샘플 코드 복사 
https://console.upstage.ai/docs/capabilities/embed git switch feature/ai/upstage-embedding 
git pull 
uv sync 
35 (실습) Upstage API 를 활용해 embedding 해보기 Network와 AI 
실습 순서 
3. fastapi api 와 연동 
openai 설치 (버전) + 호환성 
api 생성 
git switch feature/ai/upstage-embedding 
git pull 
uv sync 
36 (실습) Upstage API 를 활용해 embedding 해보기 Network와 AI 
실습 순서 
4. 답변확인: 행렬 값 추출 

37 (심화) VectorDB에 지식 넣기 ( indexing) Network와 AI 
지식 Embedding 하고 ChromaDB에 넣기 
1. 문서 수집 & 정제 (Document Collection) 
2. 문서 → 청크 → 임베딩(Embedding) 
3. Vector DB에 저장 (Indexing) 
4. API 생성 
git switch complete/vectordb 
git pull 
uv sync 
38 (실습) docker-compose 로 chromadb 실행해보기 Network와 AI 
실습 진행 
1. infra/chromadb/docker-compose.yml 확인 
cd infra/chromadb 
2. docker-compose 실행 
docker-compose up -d 
3. docker-compose 안에 정의된 서비스 컨테이너 확인 
docker-compose ps 
5. 실행된 서비스 로그 확인 
docker-compose logs 
git switch complete/vectordb 
git pull 
uv sync 
39 VectorDB에 지식 넣기 ( indexing) Network와 AI 
지식 Embedding 하고 ChromaDB에 넣기 
1. 문서 수집 & 정제 (Document Collection) 
// 요청할 때 정제되었다고 가정 
2. 문서 → 청크 → 임베딩(Embedding) 
2-1
// 데이터 샘플 
infra/chromadb/sample_knowledge.json 
2-2
// 임베딩 : upstage 에서 embedding 작업 
app/service/embedding_service.py 
3. VectorDB에 저장 (Indexing) 
UpstageClient 
4. API 생성 
POST /agent/knowledge 
https://console.upstage.ai/docs/capabilities/embed 
git switch complete/vectordb 
git pull 
uv sync 
40 VectorDB에 지식 넣기 ( indexing )Network와 AI 
결과 
git switch complete/vectordb 
git pull 
uv sync 
41 (실습) 지식 기반으로 AI에 질문해보기 (Generation) Network와 AI 
질문을 임베딩하고 ChromaDB 에서 값을 받고 AI 에 적용 
1. 질문을 받는 API 생성 
POST /agent/query 
{
    \"query\": \"ChromaDB 사용법을 알려줘\" 
}
2. 질문에 embedding 적용 
vector_service.search() 
3. embedding 값으로 query 
4. query된 값을 프롬프팅해서 Upstage AI에 질문 
git switch complete/vectordb 
git pull 
uv sync 

42 (실습) 지식 기반으로 AI에 질문해보기 (Generation) Network와 AI 
(결과)질문을 임베딩하고 ChromaDB 에 질문해보기 
git switch complete/vectordb 
git pull 
uv sync 
43 총정리 Network와 AI 
GPU 운영에  대한 기초적  이해
- 비싸고 민감한 GPU 자원 
AI 가 있는 서비스  아키텍처 
- 코드로 AI와 대답해보기 
- AI 서버 분리 (MSA 환경) 
- 데이터 품질, 데이터 전처리 후처리 
RAG 
- Embedding 
- Vector DB를 통한 AI에게 정보 
44 네트워크 수업 총 리뷰 Complete 
클라우드 시작을 위한 네트워크 CS 지식 
- 유저 요청이 서버로 오는 과정 
- LAN과 WAN 
- IP , Port 개념과 NAT 
Fast API 사용법과 서버 아키텍처 
- 유저 API 요청과 요청을 처리하는 방법 
- 계층형 아키텍처 
- 의존성과 의존성 주입 
45 네트워크 수업 돌아보기 Network 
AWS 사용법과 운영 
- EC2 세팅과 운영, 접근 방법(ssh, 방화벽) 
배포와 배포 자동화 
- 내 코드가 제품(서비스화) 되는 과정 
- github action과 배포 자동화 
서비스 아키텍처와 with AI 
- 다양한 AWS 컴포넌트와 조합 
- AI API 사용해보기 
- RAG 

www.upstage.ai © 2025 Upstage Co., Ltd. 

"""
    s.raw_texts['[SeSAC] [네트워크와 클라우드] advanced mission_day01_answer의 사본.txt'] = """step
 
1.
 
Todo
 
List
 
API
 
요청
·
응답
 
구조
 
로깅하기
 
 
 
 
Day
 
01
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
Todo
 
List
 
API
 
요청·응답
 
구조
 
로깅하기
 
로깅한
 
화면을
 
스크린샷으로
 
첨부
 
한
 
후,
 
작성한
 
코드를
 
레포지에올려
 
push
하여
 
업데이트
 
후,
 
git
 
repository
를
 
첨부해주세요.
 
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
 

 
step
 
2JSON
 
응답
 
vs
 
HTML
 
응답
 
비교하기
 
 
 
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
JSON
 
응답
 
vs
 
HTML
 
응답
 
비교하기
 
응답이
 
어떻게
 
다른지
 
표로
 
작성하여
 
기재해주세요.
 
jason
 
응답
 
Header
  
 
Value
 
date
 
 
Wed,
 
14
 
Jan
 
2026
 
07:57:39
 
GMT
 
server
 
 
uvicorn
 
content-length
 
 
59
 
content-type
 
 
application/json
 
connection
 
 
close
 
html
 
응답
 
Header
 
 
Value
 
date
 
 
 
Wed,
 
14
 
Jan
 
2026
 
08:06:05
 
GMT
 
content-type
 
 
text/html;charset=UTF-8
 
transfer-encoding
 
chunked
 
connection
 
 
close
 
 
 
 
content-type
 
에서의
 
차이
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] advanced mission_day02_answer의 사본.txt'] = """ 
 
 
Day
 
02
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
무료
 
도메인
 
발급
 
및
 
DNS
 
설정
 
도메인
 
발급
 
화면
 
및
 
dns
 
설정
 
화면을
 
캡처하여
 
스크린샷으로
 
첨부해주세요.
 
http://upstage-project-yyk.duckdns.org/
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] advanced mission_day03_answer의 사본.txt'] = """step
 
1.
 
기존
 
구조
 
분석
 
및
 
문제점
 
정리하기
 
 
 
 
Day
 
03
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
기존
 
구조
 
분석
 
및
 
문제점
 
정리하기
 
LLM
 
없이
 
스스로
 
코드의
 
문제점을
 
파악해
 
보세요.
 
미션지에서
 
표를
 
복사하여
 
작성,
 
제출하는
 
것을
 
권장합니다.
 
 
제가한게
 
없네요..브랜치를
 
바꾸니까
 
뭔가..다
 
되어있어서
 
답안지보고
 
아-이렇게하는구나
 
하고
 
넘어가게
 
되는거
 
같아요…쉐도잉도
 
아니고,
 
정말
 
티비보는거
 
같은..
 
분석
 
대상
 
(Endpoint)
 
분석
 
항목
 
분석
 
결과
 
(
제출
 
필요
 
부분
)
 
힌트
 
POST
 
/todos
 
입력
 
및
 
검증
 
user_routers.p
y
에서
 
UserCreateRequ
est
 
스키마가
 
입력을
 
받고
,
 
user_service.p
y
의
 
create_user
 
메서드
 
내
 
_valid_email
과
 
email
 
==
 
\"admin@example
.com\"
 
체크
 
로직에서
 
검증이
 
이루어집니다
.
 
request.json()
 
호출과
 
if
 
not
 
content
 
검증
 
로직이
 
어디에
 
위치하나요
?
 
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
 

 
 
 
데이터
 
저장
 
과정
 
user_repo.py
의
 
create_user
 
메서드에서
 
conn.add(user)
를
 
통해
 
객체를
 
추가하고
,
 
conn.commit()
으로
 
DB
에
 
영구
 
저장한
 
뒤
 
conn.refresh(u
ser)
로
 
생성된
 
ID
를
 
가져옵니다
.
 
INSERT
 
쿼리
 
실행부터
 
commit()
까지의
 
흐름을
 
기술해
 
보세요
.
 
 
응답
 
데이터
 
생성
 
user_service.p
y
에서
 
DB
 
객체
(
Entity)
를
 
딕셔너리
 
형태로
 
변환하고
,
 
최종적으로
 
user_routers.p
y
에서
 
UserResponse
 
Pydantic
 
모델에
 
담아
 
JSON
으로
 
반환합니다
.
 
생성된
 
데이터를
 
사용자에게
 
돌려주기
 
위해
 
어떤
 
가공
 
과정을
 
거치나요
?
 
GET
 
/todos
 
데이터
 
조회
 
및
 
변환
 
user_repo.py
의
 
get_user_by_id
에서
 
SQLAlchemy
의
 
conn.query(Use
r).filter(...)
를
 
사용하여
 
데이터를
 
조회합니다
.
 
튜플이
 
아닌
 
객체
 
형태를
 
서비스
 
계층에서
 
딕셔너리로
 
fetchall()
로
 
가져온
 
튜플
(
Tuple)
 
데이터를
 
어떻게
 
JSON
 
리스트로
 
변환하고
 
있나요
?
 
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
 

 
 
변환하여
 
처리합니다
.
 
DELETE
 
/todos/{id}
 
상태
 
확인
 
및
 
예외
 
user_repo.py
의
 
delete_user_by
_email
 
메서드에서
 
해당
 
유저를
 
조회한
 
후
 
conn.delete(us
er)
와
 
commit()
을
 
호출합니다
.
 
유저가
 
없을
 
경우의
 
예외
 
처리는
 
서비스
 
계층에서
 
판단하도록
 
설계되었습니다
.
 
삭제
 
성공
 
여부를
 
판단하는
 
기준
(
예
:
 
affected
)
과
 
예외
 
처리
 
방식을
 
분석해
 
보세요
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
 
리팩토링
 
구현
 
및
 
기능
 
검증하기
 
 
 
 
 
Day
 
03
 
답안지
 
작성자:
 
(이영기기)
 
Step
 
2.
 
리팩토링
 
구현
 
및
 
기능
 
검증하기
 
LLM
 
없이
 
스스로
 
코드를
 
리팩토링해
 
보세요.해당
 
코드가
 
업데이트된
 
Github
 
Repository
를
 
첨부해야
 
합니다
 
 
.https://github.com/atozwizard/upstage-network-lecture
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] advanced mission_day04_answer의 사본.txt'] = """ 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
Todo
 
List
 
API
 
단위
 
테스트
 
작성하기
 
단위테스트
 
작성
 
결과
 
스크린샷과,
 
github
 
repository
 
주소를
 
첨부해주세요.
 
https://github.com/atozwizard/upstage-network-lecture
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] advanced mission_day05_answer의 사본.txt'] = """ 
 
 
Day
 
05
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
FastAPI
에서
 
AI
 
요약
 
API
 
만들기
 
포스트맨에서
 
API
를
 
실행한
 
결과를
 
스크린샷으로
 
첨부해주세요
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] basic mission_day01_answer의 사본.txt'] = """step
 
1.
 
Client
 
-
 
Server
간
 
Http
 
통신의
 
과정을
 
그림으로
 
그려보기
 
 
 
 
Day
 
01
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
Client
 
-
 
Server
간
 
Http
 
통신의
 
과정을
 
그림으로
 
그려보기
 
Client
 
-
 
Server
간
 
HTTP
통신
 
과정을
 
excalidraw
를
 
이용하여
 
그려
 
스크린샷을
 
첨부해주세요
 
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
 
Http
의
 
구성요소를
 
그려보기
 
 
 
 
 
Day
 
01
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
Http
의
 
구성요소를
 
그려보기
 
Http
의
 
구성요소를
 
excalidraw
를
 
이용하여
 
그려
 
스크린샷을
 
첨부해주세요
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] basic mission_day02_answer의 사본.txt'] = """step
 
1.
 
SSH
 
접속
 
및
 
서버
 
초기
 
설정하기
 
 
 
 
Day
 
02
 
답안지
 
작성자:
 
(이영기기)
 
Step
 
1.
 
SSH
 
접속
 
및
 
서버
 
초기
 
설정하기
 
EC2
 
생성된
 
AWS
 
화면과,
 
SSH
 
설정파일을
 
캡쳐합니다.
 
 
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
 
SSH
 
접속
 
테스트
 
및
 
정리
 
문서
 
작성하기
 
 
 
 
 
Day
 
02
 
답안지
 
작성자:
 
(이영기)
 
step
 
2.
 
SSH
 
접속
 
테스트
 
및
 
정리
 
문서
 
작성하기
 
ssh
 
접속
 
완료한
 
모습을
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] basic mission_day03_answer의 사본.txt'] = """ 
 
 
Day
 
03
 
daily
 
mission
 
답안지
 
작성자:
 
(이영기)
 
각
 
스텝의
 
항목을
 
모두
 
수행한
 
결과를
 
github
 
repository
로
 
제출합니다.
 
 
로그
 
파일
 
생성
 
및
 
내용
 
확인하기
 
로그파일이
 
생긴
 
결과를
 
스크린샷으로
 
첨부하고,
 
 
작성한
 
코드가
 
push
되어있는
 
github
 
repository
를
 
첨부해주세요.
 
 
https://github.com/atozwizard/upstage-network-lecture
 
 
다음
 
항목이
 
모두
 
만족되어야
 
합니다.
 
1.
 
로그
 
파일이
 
자동
 
생성된다
 
2.
 
API
 
요청
 
시
 
로그가
 
파일에
 
기록된다
 
3.
 
콘솔과
 
파일에
 
동시에
 
로그가
 
출력된다
 
4.
 
RotatingFileHandler
 
또는
 
TimedRotatingFileHandler
가
 
적용되어
 
있다
 
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
    s.raw_texts['[SeSAC] [네트워크와 클라우드] basic mission_day04_answer의 사본.txt'] = """Step
 
1.
 
EC2
 
생성
 
및
 
보안그룹
 
설정
 
 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
1.
 
EC2
 
생성
 
및
 
보안그룹
 
설정(60분)
 
1)보안그룹
 
설정화면을
 
캡처해서
 
업로드해주세요.
 
 
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
 
2.
 
스크립트
 
작성
 
및
 
실행
 
 
 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
2.
 
스크립트
 
작성
 
및
 
실행
 
1)작성한
 
스크립트를
 
작성해주세요.
 
name
:
 
Deploy
 
to
 
EC2
 
 
on
:
 
  
push
:
 
    
branches
:
 
      
-
 
main
 
      
-
 
\"release/*\"
  
#
 
release/0.0.1,
 
release/v1
 
등
 
모든
 
release
 
브랜치
 
허용
 
 
jobs
:
 
  
deploy
:
 
    
runs-on
:
 
ubuntu-latest
 
    
steps
:
 
      
-
 
name
:
 
SSH
 
Remote
 
Commands
 
        
uses
:
 
appleboy/ssh-action@v1.0.3
 
        
with
:
 
          
host
:
 
${{
 
secrets.HOST
 
}}
 
          
username
:
 
${{
 
secrets.USERNAME
 
}}
 
          
key
:
 
${{
 
secrets.KEY
 
}}
 
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
 

 
 
          
script
:
 
|
 
            
cd
 
~/workspace/upstage-network-lecture
 
          
  
git
 
pull
 
origin
 
main
 
          
  
#
 
기존
 
프로세스
 
종료
 
(8000
포트
 
사용
 
중인
 
프로세스
)
 
          
  
fuser
 
-k
 
8000/tcp
 
||
 
true
 
          
  
#
 
uv
 
환경에서
 
서버
 
백그라운드
 
실행
 
          
  
nohup
 
uv
 
run
 
uvicorn
 
main:app
 
--host
 
0.0.0.0
 
--port
 
8000
 
>
 
app.log
 
2>&1
 
&
 
 
 
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
 
3.
 
GitHub
 
Actions
로
 
FastAPI
 
자동
 
배포
 
구성하기
 
 
 
 
 
Day
 
04
 
답안지
 
작성자:
 
(이영기)
 
Step
 
3.
 
GitHub
 
Actions
로
 
FastAPI
 
자동
 
배포
 
구성하기
 
1)
 
workﬂow
 
파일을
 
작성해주세요
 
2)
 
postman
 
테스트
 
결과
 
화면을
 
캡처해주세요.
 
 
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
    s.raw_texts['Why CI_CD Is Essential  for AI Agent.txt'] = """"""
    s.raw_texts['Why Operational and AI Infrastructure Integration Is Essential for AI Agent (1).txt'] = """"""
    s.raw_texts['Why Operational and AI Infrastructure Integration Is Essential for AI Agent.txt'] = """"""
    s.raw_texts['Why Web Server Development Is Essential for AI Agent.txt'] = """"""
    return s

def print_summary():
    s = get_summary()
    print("Week:", s.week)
    print("Files count:", len(s.files))
    print("Tech stack:", s.tech_stack)