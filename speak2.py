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
# engine.say("昨日北捷新埔站晚間發生持刀傷人事件，一名42歲王姓女子晚間10點多，疑似因為幻聽，竟持美工刀隨機攻擊身旁的一名17歲男高中生，造成該男學生臉上被劃出3公分刀傷。所幸當時「口罩伯」台北市警局防治科警務正薛先得緊急上前壓制，警方獲報後也立即趕到月台，在捷運車廂外，直接將王女壓制上銬並帶回警局，面對記者提問也是全程不發一語。")

engine.runAndWait()