from translate import Translator

Translator = Translator(from_lang="english", to_lang="spanish")

def traducir(txt):
    return Translator.translate(txt)
