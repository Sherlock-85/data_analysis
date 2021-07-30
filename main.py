import justpy as jp

def app():
    webpage = jp.QuasarPage()
    h1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-right q-pa-md")
    p1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis", classes="text-h2")

    return webpage


jp.justpy(app)

