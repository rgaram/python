import yfinance as yf

# 조회할 ETF 티커 리스트
tickers = ["SPY", "EFA", "EEM", "DBC", "GLD", "EDV", "LTPZ", "LQD", "EMLC"]
# tickers = "SPY"

# 세션 생성 후 다운로드 시도
session = yf.download(tickers, period="1y")

# 데이터 가져오기 (최근 1년치 종가)
data = yf.download(tickers, period="1y")["Close"]

# 데이터 확인
print(data.tail())  # 최근 5개 데이터 출력
