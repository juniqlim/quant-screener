# 퀀트 스크리너

한국 주식시장 퀀트 스크리닝 도구. 3가지 전략으로 종목을 평가하고 순위를 매긴다.

## 전략

### Ultra (강환국 울트라 전략)
12개 지표(1/PER, 1/PBR, 1/PSR, 1/PFCR, GP/A, 자산성장률, 영업이익/차입금, 영업이익 QoQ/YoY, 순이익 QoQ/YoY, 변동성) 백분위 순위 합산 + 신F-스코어(≥3) 필터.

### DCF (Discounted Cash Flow)
FCF 기반 적정가 산출. 가정: 성장률 5%, WACC 10%, 영구성장률 2%, 예측기간 5년.

### Magic Formula (조엘 그린블라트)
ROIC 순위 + Earnings Yield 순위 합산.

### 종합 순위
Ultra·DCF·Magic Formula 각 전략 순위 합산 (미포함 종목은 101위 처리).

## 구조

| 파일 | 역할 |
|---|---|
| `fetch_kr.py` | DART + pykrx 데이터 수집 → SQLite 저장 |
| `screener.py` | Magic Formula + DCF 스크리너 |
| `ultra_screener.py` | 울트라 전략 스크리너 |
| `index.html` | 결과 표시 웹페이지 (GitHub Pages 배포) |
| `magic_formula.db` | 수집된 재무 데이터 (SQLite) |

## 실행

```bash
pip install -r requirements.txt
```

데이터 수집에는 [DART API 키](https://opendart.fss.or.kr/)가 필요하다. `~/.dart_api_key`에 저장.

```bash
python fetch_kr.py
python screener.py
python ultra_screener.py
```

## 배포

`main` 브랜치에 push하면 GitHub Actions가 `index.html`을 GitHub Pages로 배포한다.
