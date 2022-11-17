import gradio as gr
from gtts import gTTS

def inference(audio, model):
    en_hk_two_pass = gr.Interface.load("huggingface/facebook/xm_transformer_unity_en-hk")
    hk_en_two_pass = gr.Interface.load("huggingface/facebook/xm_transformer_unity_hk-en")
    if model == "xm_transformer_unity_en-hk":
        out_audio = en_hk_two_pass(audio)
    else:
        out_audio = hk_en_two_pass(audio)
    return out_audio 

def text_to_speech(text):
    print("Generating english speech...")
    language = 'en'
        
    myobj = gTTS(text=text, lang=language, slow=True)
    myobj.save("/tmp/english_audio.mp3")

def speech_to_hk():
    print("Converting to hokkien ...")
    tmpfile_location = inference("/tmp/english_audio.mp3", "xm_transformer_unity_en-hk")
    return tmpfile_location
