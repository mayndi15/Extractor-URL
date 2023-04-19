from extractor import extractor

url = "https://money.com/exchange/?fromCurrency=BRL&toCurrency=USD"
extractor_url = extractor(url)
print(extractor_url)

# url = url.replace(" ", "")  # replace char for another
# url = url.strip()  # remove all white spaces

