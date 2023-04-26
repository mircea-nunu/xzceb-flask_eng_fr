'''
Translator
'''
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

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

def english_to_french(english_text):
    '''
    This function transaltes English text to French
    '''
    if len(english_text.strip())==0:
        return "No text provided"
    result = language_translator.translate(
    text=english_text.strip(),
    model_id='en-fr').get_result()
    french_text=result["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    '''
    This function transaltes French text to English
    '''
    if len(french_text.strip())==0:
        return "No text provided"
    result = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=result["translations"][0]["translation"]
    return english_text
