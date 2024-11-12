# You need to set a voice that supports Chinese before using pyttsx3:

import pyttsx3


def get_chinese_voice(engine):
    """Get a Chinese voice"""
    voices = engine.getProperty("voices")
    for voice in voices:
        if "zh-CN" in voice.languages:
            return voice
        if "Chinese" in voice.name or "Mandarin" in voice.name.title():
            return voice

    raise KeyError(f"No Chinese voice found among {voices}")


engine = pyttsx3.init()

chinese_voice = get_chinese_voice(engine)
engine.setProperty("voice", chinese_voice.id)
engine.say("劉律師現在很忙，請再約時間，謝謝")
engine.runAndWait()