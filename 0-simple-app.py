import justpy as jp

def app():
    page = jp.QuasarPage()

    h1 = jp.QDiv(a=page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=page, text="These graphs represent course review analysis")

    return page

jp.justpy(app)