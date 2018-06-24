from reqfrom request import get
n = int(input("How many quotes do you want to fetch:\n"))
for i in range(n):
    try:
        r = get("http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jason&json=?:\n")
        d = r.json()
        for key in d.keys():
            if key in d.keys():
                if k=="quoteAuthor":
                    print("Author :",d['quoteAuthor'])
                    print("Quote :",d['quoteText'])
                    print("_"*50)
