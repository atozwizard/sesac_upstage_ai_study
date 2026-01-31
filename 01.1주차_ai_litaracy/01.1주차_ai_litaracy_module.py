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
    """01.1주차_AI Literacy: 상세 학습 기록 (한국어)
    
    AI/ML 기초, Python 프롬프트 엔지니어링, 대형언어모델(LLM) 활용
    """

    w = WeekDetail(week="01.1주차_AI_Literacy")

    w.files = [
        "00.강의자료/AI_기초_개념.pdf",
        "01.강의자료/LLM_프롬프트_엔지니어링.pdf",
        "01.daily_mission/Day1_기초개념.ipynb",
        "01.daily_mission/Day2_프롬프트디자인.ipynb",
        "01.daily_mission/Day3_응용사례.ipynb",
        "02.advanced_mission/Day4_심화프로젝트.ipynb",
        "02.advanced_mission/Day5_최적화.ipynb",
    ]

    w.tech_stack = [
        "Python 3.9+",
        "LLM API: OpenAI GPT, Anthropic Claude",
        "프롬프트 엔지니어링: Zero-shot, Few-shot, Chain-of-Thought",
        "라이브러리: LangChain, LlamaIndex",
        "데이터 처리: JSON, CSV, 텍스트 파싱",
    ]

    w.learning_paragraphs = [
        (
            "📅 Day 1: AI와 LLM 기초 이해\n"
            "- AI, Machine Learning, Deep Learning의 개념 및 차이 학습\n"
            "- 대형언어모델(LLM)의 동작 원리 이해\n"
            "- 토큰(Token)과 컨텍스트 윈도우 개념\n"
            "- OpenAI API 가입 및 API 키 설정\n"
            "- 첫 번째 API 호출 (ChatGPT와 대화하기)"
        ),

        (
            "📅 Day 2: 프롬프트 엔지니어링 기초\n"
            "- 프롬프트의 핵심 3가지: 역할(Role), 지시사항(Instruction), 예제(Example)\n"
            "- 효과적인 프롬프트 작성 원칙\n"
            "- 온도(Temperature), 최대토큰(Max Tokens) 파라미터 조정\n"
            "- 프롬프트 템플릿 설계\n"
            "- 반복적 프롬프트 최적화 실습"
        ),

        (
            "📅 Day 3: 고급 프롬프트 기법\n"
            "- Few-shot Learning: 예제를 통한 학습\n"
            "- Chain-of-Thought Prompting: 단계별 추론 유도\n"
            "- 다국어 프롬프트 작성 및 번역\n"
            "- 구조화된 출력 형식 지정 (JSON, CSV)\n"
            "- 오류 처리 및 검증 로직"
        ),

        (
            "📅 Day 4: 심화 프로젝트 - 멀티턴 대화 시스템\n"
            "- 대화 기록 관리 및 컨텍스트 유지\n"
            "- 사용자 프롬프트 동적 구성\n"
            "- 응답 검증 및 재시도 로직\n"
            "- 비용 최적화 (토큰 사용량 추적)\n"
            "- 실제 사용 사례 구현 (Q&A 봇, 문서 분석 등)"
        ),

        (
            "📅 Day 5: 최적화 및 배포\n"
            "- 프롬프트 성능 측정 지표 정의\n"
            "- A/B 테스트를 통한 프롬프트 비교\n"
            "- 응답 시간 및 비용 최적화\n"
            "- 에러 케이스 분석 및 개선\n"
            "- 완성된 프로젝트 최종 검증"
        ),
    ]

    w.code_examples = {}

    w.code_examples['01_basic_api_call.py'] = '''import openai

# Day 1: 첫 번째 OpenAI API 호출
openai.api_key = "sk-your-api-key-here"

def chat_with_gpt(prompt: str) -> str:
    """OpenAI API를 이용한 기본 챗 함수"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 도움이 되는 어시스턴트입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

# 사용 예제
result = chat_with_gpt("파이썬 리스트의 장점은?")
print(result)
'''

    w.code_examples['02_prompt_templates.py'] = '''# Day 2: 프롬프트 템플릿 설계
import openai
from typing import Dict

class PromptTemplate:
    """프롬프트 템플릿을 관리하는 클래스"""
    
    def __init__(self, role: str, instruction: str, example: str = ""):
        self.role = role
        self.instruction = instruction
        self.example = example
    
    def build(self, user_input: str) -> str:
        """최종 프롬프트 생성"""
        prompt = f"""# 역할 (Role)
{self.role}

# 지시사항 (Instruction)
{self.instruction}

# 예제 (Example)
{self.example}

# 사용자 입력 (User Input)
{user_input}
"""
        return prompt

# 템플릿 사용 예제
template = PromptTemplate(
    role="당신은 Python 전문가입니다.",
    instruction="주어진 코드를 리뷰하고 개선점을 제시하세요.",
    example="예: # 나쁜 코드\\nx = [1,2,3,4,5]\\n# 개선: Pythonic하게 range() 사용"
)

user_code = "for i in range(len(my_list)): print(my_list[i])"
final_prompt = template.build(user_code)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": final_prompt}],
    temperature=0.5
)
print(response['choices'][0]['message']['content'])
'''

    w.code_examples['03_fewshot_learning.py'] = '''# Day 3: Few-Shot Learning 예제
import openai

def few_shot_translator(text: str) -> str:
    """Few-shot learning을 통한 자동 번역"""
    
    prompt = """당신은 한영 번역가입니다.

# 예제:
사용자: "안녕하세요"
어시스턴트: "Hello"

사용자: "오늘 날씨가 좋습니다"
어시스턴트: "The weather is nice today"

사용자: "감사합니다"
어시스턴트: "Thank you"

# 이제 다음을 번역하세요:
사용자: "{}"
어시스턴트: """.format(text)
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']

# Chain-of-Thought 예제
def reasoning_math(problem: str) -> str:
    """단계별 수학 문제 풀이 (Chain-of-Thought)"""
    
    prompt = f"""다음 수학 문제를 단계별로 풀어주세요.

예시:
문제: 10 + 20 * 2는?
답변:
1단계: 연산자 우선순위 확인 (곱셈이 덧셈보다 먼저)
2단계: 20 * 2 = 40 계산
3단계: 10 + 40 = 50
최종 답: 50

이제 다음 문제를 풀어주세요:
{problem}"""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# 사용 예제
print(few_shot_translator("프로그래밍을 배우고 있습니다"))
print(reasoning_math("12 + 8 * 3 - 5는?"))
'''

    w.code_examples['04_multiturn_conversation.py'] = '''# Day 4: 멀티턴 대화 시스템
import openai
from typing import List, Dict

class ConversationManager:
    """대화 기록을 관리하고 컨텍스트를 유지하는 클래스"""
    
    def __init__(self, system_message: str):
        self.messages = [
            {"role": "system", "content": system_message}
        ]
        self.token_count = 0
    
    def add_user_message(self, content: str) -> None:
        """사용자 메시지 추가"""
        self.messages.append({"role": "user", "content": content})
    
    def get_response(self) -> str:
        """LLM 응답 생성"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=self.messages,
                temperature=0.7,
                max_tokens=500
            )
            assistant_message = response['choices'][0]['message']['content']
            
            # 대화 기록에 추가
            self.messages.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # 토큰 사용량 추적
            self.token_count += response['usage']['total_tokens']
            
            return assistant_message
        except Exception as e:
            return f"오류 발생: {str(e)}"
    
    def get_conversation_summary(self) -> Dict:
        """대화 요약 정보"""
        return {
            "total_messages": len(self.messages) - 1,
            "total_tokens_used": self.token_count,
            "estimated_cost_usd": self.token_count * 0.00002
        }

# 사용 예제: 파이썬 튜터
tutor = ConversationManager(
    system_message="당신은 친절한 파이썬 튜터입니다. 초보자 수준으로 설명해주세요."
)

tutor.add_user_message("파이썬 리스트와 튜플의 차이가 뭐예요?")
print("어시스턴트:", tutor.get_response())

tutor.add_user_message("그럼 리스트를 변경할 수 없게 만들 수 있나요?")
print("어시스턴트:", tutor.get_response())

print("\\n대화 요약:")
for key, value in tutor.get_conversation_summary().items():
    print(f"  {key}: {value}")
'''

    w.code_examples['05_optimization.py'] = '''# Day 5: 프롬프트 최적화 및 비용 관리
import openai
import json
from datetime import datetime

class PromptOptimizer:
    """프롬프트 성능을 측정하고 최적화하는 클래스"""
    
    def __init__(self):
        self.results = []
    
    def test_prompts(self, prompts: dict, test_input: str) -> None:
        """여러 프롬프트를 테스트하고 성능 비교"""
        for name, prompt_template in prompts.items():
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt_template.format(test_input)}],
                    temperature=0.5
                )
                
                result = {
                    "prompt_name": name,
                    "input": test_input,
                    "output": response['choices'][0]['message']['content'],
                    "tokens_used": response['usage']['total_tokens'],
                    "cost_usd": response['usage']['total_tokens'] * 0.00002,
                    "timestamp": datetime.now().isoformat()
                }
                self.results.append(result)
                
                print(f"✓ {name}: {result['tokens_used']} tokens")
            except Exception as e:
                print(f"✗ {name}: {str(e)}")
    
    def get_best_prompt(self, metric: str = "tokens_used") -> dict:
        """가장 효율적인 프롬프트 찾기"""
        if not self.results:
            return None
        return min(self.results, key=lambda x: x[metric])
    
    def export_results(self, filename: str) -> None:
        """결과를 JSON 파일로 내보내기"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)

# 프롬프트 최적화 실습
prompts = {
    "verbose": "다음 문장을 한국어로 상세히 설명해주세요: {}",
    "concise": "이를 한 문장으로 정리하세요: {}",
    "structured": "다음에 대해 3가지 핵심 포인트를 나열하세요: {}"
}

optimizer = PromptOptimizer()
test_text = "프롬프트 엔지니어링은 LLM의 성능을 최적화하는 기술입니다."

optimizer.test_prompts(prompts, test_text)

print("\\n최적의 프롬프트:")
best = optimizer.get_best_prompt()
if best:
    print(f"  이름: {best['prompt_name']}")
    print(f"  토큰: {best['tokens_used']}")
    print(f"  비용: ${best['cost_usd']:.4f}")

optimizer.export_results("prompt_optimization_results.json")
'''

    return w


def print_detail():
    d = get_detail()
    print(f"Week: {d.week}")
    print(f"Files: {len(d.files)} files")
    print(f"Tech Stack: {len(d.tech_stack)} technologies")
    print(f"Learning Content: {len(d.learning_paragraphs)} days")
    print(f"Code Examples: {len(d.code_examples)} examples")
