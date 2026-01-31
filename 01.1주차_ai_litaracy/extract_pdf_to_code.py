"""
PDF 파일에서 텍스트를 추출하고 코드로 변환하는 스크립트
"""

import os
import json
from pathlib import Path
from PyPDF2 import PdfReader

# 폴더 경로
base_path = Path(r"d:\01. study\01.sesac_upstage_ai\01.1주차_ai_litaracy")

# 추출할 폴더들
folders = {
    "lectures": base_path / "01.강의자료",
    "advanced_missions": base_path / "02.advanced mission",
    "basic_missions": base_path / "03.basic mission"
}

# 결과 저장 구조
extracted_data = {}

def extract_pdf_text(pdf_path):
    """PDF 파일에서 텍스트 추출"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error: {str(e)}"

# 각 폴더의 PDF 처리
for folder_name, folder_path in folders.items():
    print(f"\n{'='*60}")
    print(f"처리 중: {folder_name}")
    print(f"{'='*60}")
    
    extracted_data[folder_name] = {}
    
    if folder_path.exists():
        pdf_files = sorted(folder_path.glob("*.pdf"))
        
        for pdf_file in pdf_files:
            print(f"  → {pdf_file.name}")
            text = extract_pdf_text(pdf_file)
            
            # 파일명을 키로 사용
            file_key = pdf_file.stem
            extracted_data[folder_name][file_key] = {
                "filename": pdf_file.name,
                "content": text[:500] + "..." if len(text) > 500 else text,  # 처음 500자만 표시
                "full_content": text,
                "char_count": len(text)
            }
            print(f"     ✓ 완료 ({len(text)} 문자)")

# 결과 저장
output_dir = base_path / "extracted_content"
output_dir.mkdir(exist_ok=True)

# 전체 JSON 저장
json_output = output_dir / "extracted_content.json"
with open(json_output, "w", encoding="utf-8") as f:
    # JSON 직렬화를 위해 full_content 제거 후 저장
    json_data = {}
    for folder, files in extracted_data.items():
        json_data[folder] = {}
        for file_key, file_data in files.items():
            json_data[folder][file_key] = {
                "filename": file_data["filename"],
                "char_count": file_data["char_count"],
                "preview": file_data["content"]
            }
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print("✓ 추출 완료!")
print(f"{'='*60}")
print(f"\n결과 저장 위치: {output_dir}")
print(f"JSON 요약: {json_output}")

# 텍스트 파일로도 저장
for folder_name, files in extracted_data.items():
    text_output = output_dir / f"{folder_name}_extracted.txt"
    with open(text_output, "w", encoding="utf-8") as f:
        f.write(f"{'='*60}\n")
        f.write(f"{folder_name.upper()}\n")
        f.write(f"{'='*60}\n\n")
        
        for file_key, file_data in files.items():
            f.write(f"\n{'─'*60}\n")
            f.write(f"파일: {file_data['filename']}\n")
            f.write(f"문자 수: {file_data['char_count']}\n")
            f.write(f"{'─'*60}\n\n")
            f.write(file_data['full_content'])
            f.write(f"\n\n")

print(f"텍스트 파일: {output_dir}/*.txt")
print("\n다음 단계: 추출된 내용을 기반으로 코드화 진행")
