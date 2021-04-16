from google.cloud import translate_v2 as trans


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
