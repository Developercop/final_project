URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
import requests 

def emotion_detector(text_to_analyse):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   myobj = {"raw_document": { "text": text_to_analyse } }
   response = requests.post(url, json = myobj, headers = headers)
   res = json.loads(response.text)
  formatted_output = res[‘emotionPredictions’][0][‘emotion’]
    fominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])
    formatted_response[‘dominant_dictionary’] = dominant_emotion
    return formatted_response 
  {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': '<name of the dominant emotion>'
}
   return response.text 
