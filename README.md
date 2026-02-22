# 퀀트 스크리너

한국 주식시장 퀀트 스크리닝 도구. 3가지 전략으로 종목을 평가하고 순위를 매긴다.

## 전략

### Ultra (강환국 울트라 전략)
12개 지표(1/PER, 1/PBR, 1/PSR, 1/PFCR, GP/A, 자산성장률, 영업이익/차입금, 영업이익 QoQ/YoY, 순이익 QoQ/YoY, 변동성) 백분위 순위 합산 + 신F-스코어(≥3) 필터.

### DCF (Discounted Cash Flow)
버핏이 유일하게 사용한 것으로 알려진 정량적 기업 분석 방법. FCF 기반 적정가 산출. 가정: 성장률 5%, WACC 10%, 영구성장률 2%, 예측기간 5년.

**한계**: 미래 실적을 알 수 없으므로 추정치에 의존한다. 성장률·WACC 가정을 어떻게 잡느냐에 따라 적정가가 크게 달라진다. 버핏이 "확실히 이해할 수 있는 기업"만 고른 이유도 이것이다 — 안정적인 캐시플로우와 단순한 사업구조를 가진 기업이어야 미래 실적 예측이 의미가 있다. 이 스크리너는 모든 종목에 동일한 가정을 일괄 적용하므로, 개별 적정가보다는 상대적 저평가 종목 필터링 용도로 봐야 한다.

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
