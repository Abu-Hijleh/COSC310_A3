from google.cloud import translate_v2 as trans
import requests
from bs4 import BeautifulSoup

#Wikipedia API:
def Wiki(sentence):
    Sesh = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMETERS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": sentence
    }
    Data = Sesh.get(url=URL, params=PARAMETERS).json()
    snip = BeautifulSoup(Data['query']['search'][0]['snippet'], 'html.parser')
    title = BeautifulSoup(Data['query']['search'][0]['title'], 'html.parser')
    snip = snip.getText()
    title =title.getText()
    urltitle = title.replace(" ", "_")
    URL = "https://en.wikipedia.org/wiki/"+urltitle
    Response=("I was not able to answer your question. However, I did search wikipedia and I found the following page: \n\nTitle: " +title + "\n\nSome information: "+ snip + "\n\nYou can read more about \"" + title +"\" at the following link: \n" + URL)
    return Response

#Google translate API
def translating(lang, input):
    import six
    print(input)
    translate_client = trans.Client.from_service_account_json(
        r"C:\Users\Haneen\Desktop\cosc-310-chatbot-4bb21491a743.json")

    if isinstance(input, six.binary_type):
        input = input.decode("utf-8")
    print(input)
    result = translate_client.translate(input, target_language=lang)
    print(result["translatedText"])
    return result["translatedText"]


def detect_language(inputs):
    translate_client = trans.Client.from_service_account_json(
        r"C:\Users\Haneen\Desktop\cosc-310-chatbot-4bb21491a743.json")

    result = translate_client.detect_language(inputs)

    return result["language"]
