import requests

COMPANY_NAME = input("What is the official name of the company: ")
STOCK_NAME = input("What is the stock name of this company: ")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stocks = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey=DNG5NQBM88R42L6C")
if len(stocks.json()) < 2:
    print("Company name not found, please try a different name.")
else:
    timeSeriesPrices = stocks.json()["Time Series (Daily)"]
    dates = []
    for key in timeSeriesPrices.keys():
        dates.append(key)
    prevDayClosingDate = timeSeriesPrices[dates[0]]
    prevDayClosing = prevDayClosingDate["4. close"]
    prevDayClosing = float(prevDayClosing)
    print(f"The {COMPANY_NAME} stock price for {dates[0]} was {prevDayClosing}")

    dayBeforeClosingDate = timeSeriesPrices[dates[1]]
    dayBeforeClosing = dayBeforeClosingDate["4. close"]
    dayBeforeClosing = float(dayBeforeClosing)
    print(f"The {COMPANY_NAME} stock price for {dates[1]} was {dayBeforeClosing}")

    diff = prevDayClosing - dayBeforeClosing

    percentage = (diff/prevDayClosing) * 100
    percentage = round(percentage, 2)
    if percentage > 0:
        print(f"There was a raise in the stock prices of {percentage}%🔺")
    else:
        print(f"There was a reduction(loss) in the stock prices of {percentage}%🔻")

    print(f"\nNews regarding {COMPANY_NAME}: ")
    news = requests.get(url=f"https://newsapi.org/v2/everything?q={STOCK_NAME}&from={dates[0]}&sortBy=publishedAt&apiKey=5545956174ec4177b43b8d07076ae1ce")
    news = news.json()
    newsArr = []
    if news["totalResults"] == 0:
        print("No news found for this company.")
    else:
        i = 0
        while i < 4:
            newsArr.append(news["articles"][i])
            i += 1
    for obj in newsArr:
        title = obj["title"]
        content = obj["content"]
        url = obj["url"]
        author = obj["author"]
        print(f"Title: {title}")
        print(f"Content: {content}")
        print(f"Url: {url}")
        print(f"Author: {author}\n")




