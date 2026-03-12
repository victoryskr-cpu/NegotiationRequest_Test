
# NegotiationRequest_Test

지자체 교섭요구공고 자동검색 테스트용 저장소

## 실행 방법

1. 패키지 설치

pip install -r requirements.txt

2. 실행

streamlit run app.py

## 구조

app.py  
→ Streamlit 테스트 실행 UI

crawler_site_handlers.py  
→ 사이트별 크롤러 로직

crawler_utils.py  
→ HTML 요청 / 파싱 공통 함수

data_targets.py  
→ 테스트 대상 사이트 목록

## 대상 사이트 관리

검색 대상은 `data_targets.py`에 직접 입력하지 않고 `targets.csv`에서 관리합니다.

주요 컬럼:
- 지자체명
- 광역
- 유형
- 홈페이지
- 고시공고게시판
- 검색URL
- 사용여부
- 비고

`사용여부`가 Y인 행만 앱에서 불러옵니다.
