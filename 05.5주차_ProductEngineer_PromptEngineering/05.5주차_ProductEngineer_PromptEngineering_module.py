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
    """05.5주차_ProductEngineer_PromptEngineering: 상세 학습 기록 (한국어)
    
    LLM 활용, 프롬프트 엔지니어링, RAG, 에이전트 아키텍처
    """

    w = WeekDetail(week="05.5주차_ProductEngineer_PromptEngineering")

    w.files = [
        "00.강의자료/LLM_기초_및_API.pdf",
        "00.강의자료/프롬프트_엔지니어링_고급.pdf",
        "01.daily_mission/Day1_LLM_API_기초.ipynb",
        "01.daily_mission/Day2_프롬프트_구조화.ipynb",
        "01.daily_mission/Day3_RAG_시스템.ipynb",
        "02.advanced_mission/Day4_에이전트_아키텍처.ipynb",
        "02.advanced_mission/Day5_통합_프로젝트.ipynb",
    ]

    w.tech_stack = [
        "LLM API: OpenAI GPT-4, Claude, Gemini",
        "라이브러리: LangChain, LlamaIndex, Anthropic SDK",
        "벡터 데이터베이스: Pinecone, Weaviate, Chroma",
        "임베딩 모델: OpenAI Embeddings, Hugging Face",
        "프롬프트 패턴: Role/Instruction/Example/Chain-of-Thought",
        "에이전트 패턴: ReAct, Tool Use, Memory Management",
        "모니터링: LangSmith, Weights & Biases",
    ]

    w.learning_paragraphs = [
        (
            "📅 Day 1: LLM API와 기본 구조\n"
            "- OpenAI API 구조 및 모델 선택 (gpt-4, gpt-3.5-turbo)\n"
            "- Chat Completion vs Text Completion\n"
            "- 토큰 계산 및 비용 추정\n"
            "- API 에러 처리 및 재시도 로직\n"
            "- 스트리밍 응답 처리"
        ),

        (
            "📅 Day 2: 고급 프롬프트 엔지니어링\n"
            "- 프롬프트 구조 최적화 (System/User/Assistant roles)\n"
            "- Few-shot learning 패턴\n"
            "- Chain-of-Thought 프롬프팅\n"
            "- Temperature와 Top-P 파라미터 튜닝\n"
            "- 프롬프트 버전 관리 및 A/B 테스트"
        ),

        (
            "📅 Day 3: RAG (Retrieval-Augmented Generation) 시스템\n"
            "- 벡터 임베딩의 개념\n"
            "- 문서 청킹 및 전처리\n"
            "- 유사도 검색 알고리즘\n"
            "- 검색 결과를 LLM과 결합\n"
            "- Pinecone/Weaviate 통합"
        ),

        (
            "📅 Day 4: 에이전트 아키텍처 설계\n"
            "- 에이전트의 개념 (목표, 도구, 메모리)\n"
            "- Tool/Function Calling 구현\n"
            "- ReAct 패턴: Reasoning + Acting\n"
            "- 대화 메모리 관리\n"
            "- 반복 제한 및 에러 복구"
        ),

        (
            "📅 Day 5: 통합 프로젝트 및 배포\n"
            "- 전체 AI 파이프라인 구축\n"
            "- 다양한 데이터 소스 통합\n"
            "- 모니터링 및 성능 추적\n"
            "- 비용 최적화 전략\n"
            "- 프로덕션 배포 및 스케일링"
        ),
    ]

    w.code_examples = {}

    w.code_examples['01_basic_llm_api.py'] = '''# Day 1: OpenAI API 기초

import openai
import os
from typing import Optional

# API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def basic_completion(prompt: str, model: str = "gpt-4") -> str:
    """기본 텍스트 생성"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "당신은 도움이 되는 AI 어시스턴트입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

def streaming_completion(prompt: str) -> None:
    """스트리밍 응답 (실시간 출력)"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        stream=True
    )
    
    for chunk in response:
        if 'choices' in chunk:
            delta = chunk['choices'][0]['delta']
            if 'content' in delta:
                print(delta['content'], end='', flush=True)
    print()

def count_tokens(text: str) -> int:
    """토큰 수 계산 (대략적)"""
    import tiktoken
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    return len(tokens)

def estimate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    """API 비용 추정"""
    # GPT-4 가격 (2024 기준)
    prompt_price = 0.00003  # $0.03 / 1K tokens
    completion_price = 0.00006  # $0.06 / 1K tokens
    
    cost = (prompt_tokens * prompt_price + completion_tokens * completion_price)
    return cost

def api_with_retry(prompt: str, max_retries: int = 3) -> Optional[str]:
    """재시도 로직이 있는 API 호출"""
    import time
    
    for attempt in range(max_retries):
        try:
            return basic_completion(prompt)
        except openai.error.RateLimitError:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt
            print(f"Rate limit. {wait_time}초 대기...")
            time.sleep(wait_time)
        except openai.error.APIError as e:
            if attempt == max_retries - 1:
                raise
            print(f"API 오류: {e}. 재시도...")

# 사용 예제
if __name__ == '__main__':
    prompt = "파이썬에서 리스트와 튜플의 차이를 설명해주세요"
    
    print("=== 기본 완성 ===")
    result = basic_completion(prompt)
    print(result)
    
    print("\\n=== 스트리밍 ===")
    streaming_completion(prompt)
    
    print("\\n=== 토큰 수 ===")
    tokens = count_tokens(prompt)
    print(f"프롬프트 토큰: {tokens}")
'''

    w.code_examples['02_prompt_engineering.py'] = '''# Day 2: 프롬프트 엔지니어링 고급

import openai
from typing import List, Dict

class PromptEngineer:
    """프롬프트 엔지니어링 클래스"""
    
    def __init__(self):
        self.model = "gpt-4"
        self.temperature = 0.7
    
    def system_prompt(self, role: str) -> Dict:
        """시스템 프롬프트 정의"""
        return {"role": "system", "content": role}
    
    def few_shot_example(self, examples: List[Dict]) -> str:
        """Few-shot 예제 생성"""
        prompt = "다음은 예제입니다:\\n"
        for i, example in enumerate(examples, 1):
            prompt += f"예제 {i}:\\n"
            prompt += f"입력: {example['input']}\\n"
            prompt += f"출력: {example['output']}\\n\\n"
        return prompt
    
    def chain_of_thought(self, problem: str) -> str:
        """Chain-of-Thought 프롬프팅"""
        return f"""다음 문제를 단계별로 풀어주세요.
각 단계를 명확히 설명하고, 최종 답변을 제시해주세요.

문제: {problem}

단계:
1. 문제 이해
2. 필요한 정보 파악
3. 단계별 풀이
4. 최종 답변"""
    
    def structured_output(self, task: str, format_type: str = "json") -> str:
        """구조화된 출력 요청"""
        if format_type == "json":
            return f"""{task}

응답은 다음과 같은 JSON 형식으로 제공해주세요:
{{
    "answer": "답변",
    "confidence": 0.0-1.0,
    "reasoning": "이유"
}}"""
        elif format_type == "markdown":
            return f"""{task}

응답은 마크다운 형식으로 제공해주세요:
# 제목
## 부제
- 항목 1
- 항목 2"""
    
    def multilingual_prompt(self, text: str, target_lang: str) -> str:
        """다국어 프롬프트"""
        return f"""다음 텍스트를 {target_lang}로 번역해주세요.
원문의 의미와 톤을 최대한 보존해주세요.

원문:
{text}

번역:"""
    
    def prompt_variations(self, base_prompt: str, temperatures: List[float]) -> List[str]:
        """다양한 온도 설정으로 응답 생성"""
        variations = []
        for temp in temperatures:
            self.temperature = temp
            # API 호출 로직
            variations.append(f"온도 {temp}: [응답]")
        return variations

# 사용 예제
engineer = PromptEngineer()

# Few-shot 학습
examples = [
    {"input": "Cat", "output": "동물"},
    {"input": "Apple", "output": "과일"}
]
few_shot_prompt = engineer.few_shot_example(examples)

# Chain-of-Thought
cot_prompt = engineer.chain_of_thought("12 × 5 + 8 ÷ 2 = ?")

# 구조화된 출력
structured = engineer.structured_output(
    "감정 분석: '이 제품은 정말 훌륭합니다!'",
    format_type="json"
)

# 번역
translation = engineer.multilingual_prompt(
    "The quick brown fox jumps over the lazy dog",
    "한국어"
)

print("Few-shot 프롬프트:")
print(few_shot_prompt)
print("\\nChain-of-Thought:")
print(cot_prompt)
'''

    w.code_examples['03_rag_pipeline.py'] = '''# Day 3: RAG (Retrieval-Augmented Generation) 시스템

from typing import List, Dict, Tuple
import numpy as np
from dataclasses import dataclass

@dataclass
class Document:
    """문서 객체"""
    id: str
    content: str
    embedding: List[float] = None
    metadata: Dict = None

class RAGPipeline:
    """RAG 파이프라인"""
    
    def __init__(self, embedding_model="text-embedding-3-small"):
        self.embedding_model = embedding_model
        self.documents: List[Document] = []
        self.embeddings: np.ndarray = None
    
    def chunk_document(self, text: str, chunk_size: int = 500) -> List[str]:
        """문서를 청크로 분할"""
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i + chunk_size])
        return chunks
    
    def embed_text(self, text: str) -> List[float]:
        """텍스트를 벡터로 변환"""
        import openai
        
        response = openai.Embedding.create(
            input=text,
            model=self.embedding_model
        )
        return response['data'][0]['embedding']
    
    def add_documents(self, documents: List[Dict]):
        """문서 추가"""
        for doc in documents:
            chunks = self.chunk_document(doc['content'])
            
            for i, chunk in enumerate(chunks):
                embedding = self.embed_text(chunk)
                
                doc_obj = Document(
                    id=f"{doc['id']}_chunk_{i}",
                    content=chunk,
                    embedding=embedding,
                    metadata={"source": doc.get('source', '')}
                )
                self.documents.append(doc_obj)
    
    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """코사인 유사도 계산"""
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        
        dot_product = np.dot(vec1, vec2)
        magnitude1 = np.linalg.norm(vec1)
        magnitude2 = np.linalg.norm(vec2)
        
        return dot_product / (magnitude1 * magnitude2)
    
    def retrieve(self, query: str, top_k: int = 3) -> List[Document]:
        """쿼리와 유사한 문서 검색"""
        query_embedding = self.embed_text(query)
        
        similarities = []
        for doc in self.documents:
            similarity = self.cosine_similarity(query_embedding, doc.embedding)
            similarities.append((doc, similarity))
        
        # 상위 K개 반환
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in similarities[:top_k]]
    
    def generate_with_context(self, query: str, llm_model: str = "gpt-4") -> str:
        """RAG 기반 답변 생성"""
        import openai
        
        # 관련 문서 검색
        relevant_docs = self.retrieve(query)
        
        # 문맥 생성
        context = "\\n".join([doc.content for doc in relevant_docs])
        
        # LLM에 컨텍스트와 함께 질문
        response = openai.ChatCompletion.create(
            model=llm_model,
            messages=[
                {
                    "role": "system",
                    "content": f"""당신은 도움이 되는 어시스턴트입니다.
다음 컨텍스트를 기반으로 질문에 답변해주세요.
컨텍스트에 정보가 없으면 '해당 정보를 찾을 수 없습니다'라고 답변하세요.

컨텍스트:
{context}"""
                },
                {"role": "user", "content": query}
            ]
        )
        
        return response['choices'][0]['message']['content']

# 사용 예제
rag = RAGPipeline()

# 문서 추가
documents = [
    {
        "id": "doc1",
        "content": "파이썬은 고급 프로그래밍 언어입니다. 배우기 쉽고 강력합니다.",
        "source": "python_guide"
    },
    {
        "id": "doc2",
        "content": "머신러닝은 데이터로부터 패턴을 학습합니다.",
        "source": "ml_guide"
    }
]

# rag.add_documents(documents)
# answer = rag.generate_with_context("파이썬의 특징은?")
# print(f"답변: {answer}")
'''

    w.code_examples['04_agent_architecture.py'] = '''# Day 4: 에이전트 아키텍처 (ReAct 패턴)

from typing import List, Dict, Any, Callable
from dataclasses import dataclass
import json

@dataclass
class Tool:
    """에이전트가 사용할 수 있는 도구"""
    name: str
    description: str
    func: Callable
    parameters: Dict[str, str]

class ReActAgent:
    """ReAct (Reasoning + Acting) 패턴의 에이전트"""
    
    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.tools: Dict[str, Tool] = {}
        self.memory: List[Dict] = []
        self.max_iterations = 10
    
    def register_tool(self, tool: Tool):
        """도구 등록"""
        self.tools[tool.name] = tool
    
    def get_tools_prompt(self) -> str:
        """도구 설명 프롬프트 생성"""
        tools_text = "사용 가능한 도구:\\n"
        for name, tool in self.tools.items():
            tools_text += f"- {name}: {tool.description}\\n"
        return tools_text
    
    def think(self, observation: str) -> str:
        """사고 단계: 다음 행동 결정"""
        import openai
        
        history = json.dumps(self.memory[-3:], ensure_ascii=False)
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": f"""당신은 ReAct 에이전트입니다.
매 턴마다 다음을 수행합니다:
1. Thought: 현재 상황을 분석하고 다음 액션 결정
2. Action: 도구를 사용하거나 최종 답변 제시
3. Observation: 액션 결과 관찰

{self.get_tools_prompt()}"""
                },
                {
                    "role": "user",
                    "content": f"""현재 관찰:
{observation}

과거 메모리:
{history}

다음은 Thought, Action, Observation 형식으로 응답해주세요."""
                }
            ],
            temperature=0
        )
        
        return response['choices'][0]['message']['content']
    
    def act(self, action: str) -> str:
        """액션 실행"""
        try:
            # 액션 파싱 (예: "calculator(12 + 5)")
            if "(" in action and ")" in action:
                tool_name = action.split("(")[0].strip()
                params_str = action.split("(")[1].split(")")[0]
                
                if tool_name in self.tools:
                    tool = self.tools[tool_name]
                    result = tool.func(params_str)
                    return f"Action Result: {result}"
            
            return f"도구를 찾을 수 없습니다: {action}"
        
        except Exception as e:
            return f"액션 실행 오류: {str(e)}"
    
    def run(self, query: str) -> str:
        """에이전트 실행"""
        self.memory = []
        observation = f"질문: {query}"
        
        for i in range(self.max_iterations):
            # 사고 + 액션
            response = self.think(observation)
            self.memory.append({"step": i, "response": response})
            
            # 최종 답변 확인
            if "Final Answer:" in response:
                answer = response.split("Final Answer:")[1].strip()
                return answer
            
            # 다음 액션 실행
            if "Action:" in response:
                action = response.split("Action:")[1].split("\\n")[0].strip()
                observation = self.act(action)
        
        return "최대 반복 횟수 도달"

# 도구 정의
def calculator(expression: str) -> str:
    """계산기 도구"""
    try:
        result = eval(expression)
        return str(result)
    except:
        return "계산 오류"

def search_knowledge(query: str) -> str:
    """지식 검색 도구"""
    knowledge = {
        "파이썬": "고급 프로그래밍 언어",
        "머신러닝": "데이터로부터 패턴 학습"
    }
    return knowledge.get(query, "정보 없음")

# 에이전트 설정
agent = ReActAgent()
agent.register_tool(Tool(
    name="calculator",
    description="수학 계산 수행",
    func=calculator,
    parameters={"expression": "수식"}
))
agent.register_tool(Tool(
    name="search_knowledge",
    description="지식 기반 검색",
    func=search_knowledge,
    parameters={"query": "검색어"}
))

# 실행 예제
# result = agent.run("10 + 20은 얼마입니까?")
# print(result)
'''

    w.code_examples['05_end_to_end_project.py'] = '''# Day 5: 통합 AI 프로젝트

from typing import List, Optional, Dict
import openai
import os

class AIAssistant:
    """통합 AI 어시스턴트"""
    
    def __init__(self, name: str = "AI Assistant"):
        self.name = name
        self.conversation_history: List[Dict] = []
        self.max_memory = 10
        self.model = "gpt-4"
    
    def add_message(self, role: str, content: str):
        """대화 기록에 메시지 추가"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
        
        # 메모리 제한
        if len(self.conversation_history) > self.max_memory:
            self.conversation_history.pop(0)
    
    def generate_response(self, user_input: str) -> str:
        """사용자 입력에 대한 응답 생성"""
        self.add_message("user", user_input)
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "당신은 친절하고 도움이 되는 AI 어시스턴트입니다."
                    }
                ] + self.conversation_history,
                temperature=0.7,
                max_tokens=1000
            )
            
            assistant_message = response['choices'][0]['message']['content']
            self.add_message("assistant", assistant_message)
            
            return assistant_message
        
        except Exception as e:
            return f"오류 발생: {str(e)}"
    
    def get_summary(self) -> str:
        """대화 요약"""
        if not self.conversation_history:
            return "대화 기록이 없습니다."
        
        summary_prompt = "다음 대화를 간단히 요약해주세요:\\n"
        summary_prompt += "\\n".join([
            f"{msg['role']}: {msg['content']}"
            for msg in self.conversation_history
        ])
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": summary_prompt}],
            max_tokens=500
        )
        
        return response['choices'][0]['message']['content']
    
    def clear_history(self):
        """대화 기록 초기화"""
        self.conversation_history = []
    
    def interactive_chat(self):
        """대화형 인터페이스"""
        print(f"\\n=== {self.name} ===")
        print("'exit'를 입력하면 종료합니다.\\n")
        
        while True:
            user_input = input("당신: ").strip()
            
            if user_input.lower() == 'exit':
                print(f"{self.name}: 안녕히 가세요!")
                break
            
            if not user_input:
                continue
            
            response = self.generate_response(user_input)
            print(f"\\n{self.name}: {response}\\n")

# 사용 예제
if __name__ == '__main__':
    assistant = AIAssistant(name="Python Tutor")
    
    # API 키 설정
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # 대화형 채팅
    # assistant.interactive_chat()
    
    # 또는 단일 질문
    # response = assistant.generate_response("파이썬 리스트와 튜플의 차이는?")
    # print(f"응답: {response}")
    
    # 대화 요약
    # summary = assistant.get_summary()
    # print(f"\\n요약:\\n{summary}")
'''

    return w


def print_detail():
    d = get_detail()
    print(f"Week: {d.week}")
    print(f"Files: {len(d.files)} files")
    print(f"Tech Stack: {len(d.tech_stack)} technologies")
    print(f"Learning Content: {len(d.learning_paragraphs)} days")
    print(f"Code Examples: {len(d.code_examples)} examples")
