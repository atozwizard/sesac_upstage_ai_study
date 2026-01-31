"""
Day 1 예제: API 기초 사용법
==========================
"""

# ============ 예제 1.1: 기본 API 호출 ============
basic_api_example = """
import openai
import os

# API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 기본 API 호출
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "당신은 도움이 되는 어시스턴트입니다."},
        {"role": "user", "content": "안녕하세요!"}
    ],
    temperature=0.7,
    max_tokens=500
)

# 응답 처리
answer = response['choices'][0]['message']['content']
print(f"답변: {answer}")

# 사용 정보
print(f"입력 토큰: {response['usage']['prompt_tokens']}")
print(f"출력 토큰: {response['usage']['completion_tokens']}")
print(f"총 토큰: {response['usage']['total_tokens']}")
"""

# ============ 예제 1.2: 토큰 계산 ============
token_calculation = """
import tiktoken

def count_tokens(text: str, model: str = "gpt-4") -> int:
    '''텍스트의 토큰 수 계산'''
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def estimate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    '''API 비용 추정 (GPT-4 기준)'''
    prompt_price = 0.00003  # $0.03 / 1K tokens
    completion_price = 0.00006  # $0.06 / 1K tokens
    return (prompt_tokens * prompt_price) + (completion_tokens * completion_price)

# 사용 예제
text = "파이썬은 배우기 쉬운 프로그래밍 언어입니다."
tokens = count_tokens(text)
print(f"토큰 수: {tokens}")

cost = estimate_cost(20, 50)
print(f"예상 비용: ${cost:.4f}")
"""

# ============ 예제 1.3: 에러 처리 ============
error_handling = """
import openai
import time

def api_call_with_retry(prompt: str, max_retries: int = 3) -> str:
    '''재시도 로직이 있는 API 호출'''
    
    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                timeout=30
            )
            return response['choices'][0]['message']['content']
        
        except openai.error.RateLimitError:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt  # exponential backoff
            print(f"Rate limit. {wait_time}초 대기...")
            time.sleep(wait_time)
        
        except openai.error.APIError as e:
            if attempt == max_retries - 1:
                raise
            print(f"API 오류: {e}. 재시도...")
            time.sleep(1)
        
        except openai.error.AuthenticationError:
            print("API 키 오류. 설정을 확인하세요.")
            raise

# 사용
try:
    result = api_call_with_retry("안녕하세요!")
    print(result)
except Exception as e:
    print(f"최종 오류: {e}")
"""

# ============ 예제 1.4: 스트리밍 응답 ============
streaming_example = """
import openai

def stream_response(prompt: str):
    '''스트리밍으로 실시간 응답 받기'''
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        stream=True
    )
    
    # 청크 단위로 응답 받기
    for chunk in response:
        if 'choices' in chunk:
            delta = chunk['choices'][0]['delta']
            if 'content' in delta:
                print(delta['content'], end='', flush=True)
    
    print()  # 줄바꿈

# 사용
stream_response("파이썬 리스트와 튜플의 차이를 설명해주세요.")
"""

# ============ 예제 1.5: 환경 변수 관리 ============
env_management = """
import openai
import os
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

# API 키 설정 (안전하게)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY 환경변수를 설정하세요.")

openai.api_key = api_key

# 초기화 확인
try:
    # 최소한의 API 호출로 키 검증
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "hi"}],
        max_tokens=1
    )
    print("✓ API 키가 유효합니다.")
except openai.error.AuthenticationError:
    print("✗ API 키가 유효하지 않습니다.")
except Exception as e:
    print(f"✗ 오류: {e}")
"""

# 모든 예제를 딕셔너리로 반환
examples_dict = {
    "01_basic_api_call": basic_api_example,
    "02_token_calculation": token_calculation,
    "03_error_handling": error_handling,
    "04_streaming_response": streaming_example,
    "05_env_management": env_management,
}

if __name__ == "__main__":
    print("Day 1 예제 코드")
    for name, code in examples_dict.items():
        print(f"\n{'='*50}")
        print(f"{name}")
        print(f"{'='*50}")
        print(code)
