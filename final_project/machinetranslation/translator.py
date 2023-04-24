import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)
# # test the service
# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))
# translation = language_translator.translate(
#     text='Hello, how are you today?',
#     model_id='en-es').get_result()
# print(json.dumps(translation, indent=2, ensure_ascii=False))

def englishToFrench(englishText):
    '''
    This function transaltes English text to French
    '''
    result = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    frenchText=result["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    '''
    This function transaltes French text to English
    '''
    result = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    englishText=result["translations"][0]["translation"]
    return englishText