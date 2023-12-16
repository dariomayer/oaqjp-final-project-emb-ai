import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header)
   
    # Convert the response text into a dictionary using the json library functions
    formatted_response = json.loads(response.text)
    
   # Estrai la lista delle emozioni e i relativi punteggi dal primo elemento della lista
    if 'emotionPredictions' in formatted_response:
        predictions = formatted_response['emotionPredictions']
        if predictions:
            first_prediction = predictions[0]
            emotion_data = first_prediction.get('emotion', {})
            emotions = emotion_data if emotion_data else {}
        else:
            emotions = {}
    else:
        emotions = {}

    # Assegna i punteggi alle variabili specifiche
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Calcola la dominanza dell'emozione
    dominant_emotion = max(emotions, key=lambda x: emotions[x])

    # Restituisci la struttura richiesta
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result