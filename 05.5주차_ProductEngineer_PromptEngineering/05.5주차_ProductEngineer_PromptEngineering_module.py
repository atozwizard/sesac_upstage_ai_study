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
    """05.5주차_ProductEngineer_PromptEngineering: 학습 기록 모듈 (한국어)
    
    AI 제품 엔지니어링, 프롬프트 엔지니어링, LLM 기반 응용 개발.
    """

    w = WeekDetail(week="05.5주차_ProductEngineer_PromptEngineering")

    w.files = [
        "00.강의자료 (프롬프트 엔지니어링, LLM, RAG, Agentic Workflow)",
        "01.daily_mission (매일 LLM 실습 미션)",
        "02.advanced_mission (심화 AI 에이전트 미션)",
        "03.project (LLM 기반 제품 개발 프로젝트)",
    ]

    w.tech_stack = [
        "LLM: GPT, Claude, 오픈소스 모델 API",
        "프롬프트 엔지니어링: 지시어, Few-shot, Chain-of-Thought",
        "RAG (Retrieval-Augmented Generation): 문서 검색 + LLM",
        "Agentic Workflow: 에이전트, 도구(Tools), 메모리 관리",
        "임베딩 & 벡터 DB: Vector Search, Semantic Similarity",
        "평가 지표: Precision, Recall, F1, BLEU 등",
        "비용/성능 최적화: 토큰 개수, API 호출 최소화",
    ]

    w.learning_paragraphs = [
        (
            "What I practiced: LLM API(OpenAI, Claude 등)를 직접 호출하고 응답을 받는 기본 흐름을 습득했습니다. "
            "프롬프트 엔지니어링의 다양한 기법(Zero-shot, Few-shot, Chain-of-Thought)을 실험해보고, "
            "각 기법이 LLM의 성능에 미치는 영향을 관찰했습니다. "
            "RAG를 이용해 외부 문서를 검색한 뒤 그 결과를 LLM에 전달하는 파이프라인을 구현했습니다. "
            "간단한 에이전트(Agent) 구조를 만들어 LLM이 도구(Tools)를 사용하도록 유도하는 경험을 했습니다."
        ),

        (
            "What I learned: LLM은 완벽한 솔루션이 아니며, 프롬프트와 환경설정에 따라 성능이 크게 달라진다는 것을 배웠습니다. "
            "프롬프트에서 '역할(Role)', '맥락(Context)', '지시사항(Instruction)', '예제(Example)'를 명확히 제시하면 결과가 향상됨을 체감했습니다. "
            "RAG의 핵심은 '검색 품질'이며, 잘못된 문서 검색은 오히려 LLM의 답변을 방해한다는 점을 이해했습니다. "
            "에이전트 기반 아키텍처에서는 LLM 출력의 예측 불가성을 관리하고, 오류 처리(fallback)를 설계해야 함을 배웠습니다."
        ),

        (
            "Project/Assignment: LLM 기반 질문-답변 시스템(Q&A Bot), 문서 요약 도구, 또는 멀티턴 대화 에이전트를 구현했습니다. "
            "RAG를 적용해 회사 내부 문서나 외부 소스에서 정보를 검색하고, 그를 바탕으로 정확한 답변을 생성하도록 했습니다. "
            "프롬프트 템플릿을 설계하고, 다양한 프롬프트 버전을 A/B 테스트해서 최적의 성능을 찾는 과정을 거쳤습니다. "
            "LLM 응답의 정확성, 관련성, 안전성을 평가하기 위한 평가 지표를 정의하고 측정했습니다."
        ),
    ]

    w.code_examples = {}

    w.code_examples['basic_llm_api.py'] = '''import openai

# OpenAI API 호출 (기본)
def query_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

result = query_llm("파이썬에서 리스트의 중복을 제거하는 방법은?")
print(result)
'''

    w.code_examples['prompt_engineering.py'] = '''# 프롬프트 엔지니어링: 역할, 맥락, 지시사항, 예제

def create_optimized_prompt(task: str) -> str:
    prompt = f"""
# 역할 (Role)
당신은 전문적인 기술 문서 작성자입니다.

# 맥락 (Context)
본사는 Python 기반 데이터 처리 도구를 개발하고 있으며, 사용자를 위한 명확한 설명서를 작성해야 합니다.

# 지시사항 (Instruction)
다음 기술 개념을 초보자도 이해할 수 있도록 설명하세요:
- 개념을 3문장 이내로 요약
- 실제 사용 예제 1가지 포함
- 주의사항 1가지 포함

# 예제 (Example)
개념: 리스트 컴프리헨션
설명: 리스트 컴프리헨션은 간단한 반복문을 한 줄로 표현하는 방법입니다.
예: [x*2 for x in range(5)]는 [0, 2, 4, 6, 8]을 생성합니다.
주의: 복잡한 로직은 오히려 가독성을 해칠 수 있으니 일반 반복문을 사용하세요.

이제 다음 개념을 같은 형식으로 설명하세요:
{task}
"""
    return prompt

# Few-shot learning: 여러 예제를 제공
messages = [
    {"role": "system", "content": "당신은 한국어-영어 번역기입니다."},
    {"role": "user", "content": "안녕하세요"},
    {"role": "assistant", "content": "Hello"},
    {"role": "user", "content": "오늘 날씨가 좋네요"},
    {"role": "assistant", "content": "Nice weather today"},
    {"role": "user", "content": "감사합니다"},
]
'''

    w.code_examples['rag_pipeline.py'] = '''from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

# 1. 문서 로드 및 임베딩
loader = TextLoader("documents.txt")
documents = loader.load()

embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(documents, embeddings)

# 2. 검색 (Retrieval)
def retrieve_relevant_docs(query: str, k: int = 3):
    docs = vector_store.similarity_search(query, k=k)
    return docs

# 3. LLM에 맥락 추가 (Augmentation)
def rag_query(query: str) -> str:
    relevant_docs = retrieve_relevant_docs(query)
    context = "\\n".join([doc.page_content for doc in relevant_docs])
    
    prompt = f"""다음 문서를 참고하여 질문에 답하세요:

문서:
{context}

질문: {query}

답변:"""
    
    # LLM 호출
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

answer = rag_query("우리 회사의 핵심 가치는 무엇입니까?")
'''

    w.code_examples['agentic_workflow.py'] = '''# 간단한 에이전트 구조 (Agent + Tools + Memory)

class SimpleAgent:
    def __init__(self):
        self.tools = {
            "calculator": self.calculate,
            "web_search": self.search_web,
            "database_query": self.query_db
        }
        self.memory = []
    
    def calculate(self, expression: str) -> str:
        return str(eval(expression))
    
    def search_web(self, query: str) -> str:
        return f"[Web Search Result for: {query}]"
    
    def query_db(self, sql: str) -> str:
        return "[Database Result]"
    
    def run(self, user_input: str) -> str:
        # 사용자 입력을 LLM에 전달하여 어떤 도구를 사용할지 결정
        prompt = f"""
당신은 AI 어시스턴트입니다.
사용 가능한 도구: {list(self.tools.keys())}

사용자: {user_input}

사용할 도구와 입력을 결정하세요. 포맷: [도구명] [입력값]
"""
        # LLM 호출 (생략)
        # 도구 실행
        # 결과를 메모리에 저장
        # 최종 답변 생성
        
        return "Agent의 최종 답변"

agent = SimpleAgent()
result = agent.run("2+3의 결과는 무엇이고, 날씨는 어떻게 되나요?")
'''

    return w


def print_detail():
    d = get_detail()
    print("Week:", d.week)
    print("Tech Stack:", len(d.tech_stack), "technologies")
    print("Learning Sections:", len(d.learning_paragraphs))
    print("Code Examples:", list(d.code_examples.keys()))
