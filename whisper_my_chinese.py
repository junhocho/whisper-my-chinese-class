# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os 
import sys
import jieba
import re
import pypinyin
from googletrans import Translator
import json
import time


## accept first argument as mp3 file
audio_file = sys.argv[1]
# audio_file = "./40448640_07071727029_01047829227_20230222090158_20230222093216_tJ7e8Ccpai.mp3"
# audio_file = './data/40360613_07071727029_01047829227_20230215090255_20230215093328_cChUxwNW59.mp3'

audio_opened= open(audio_file, "rb")


# date = audio_file.split("_")[-3][-6:]
# date : find fisrt "2023" and grab 4 digits after it,
date = audio_file.split("2023")[1][:4]
# and prepend 23 on it.
date = "23" + date



transcript_file = "./data/transcript_{}.txt".format(date)
json_file = "./data/sentences_{}.json".format(date)

# if transcript_file exists, read it
if os.path.exists(transcript_file):
    print("Transcription found. Reading transcript from file")
    with open(transcript_file, "r") as f:
        transcript = f.read()
else:
    print("Transcript file does not exist, creating it with OpenAI")
    # if transcript_file does not exist, create i
    transcript = openai.Audio.transcribe("whisper-1", audio_opened, prompt="让我们开始今天的中文课吧。", language='zh')
    transcript = transcript.text
    with open(transcript_file, "w") as f:
        f.write(transcript)


# replace comman with space
transcript = re.sub(r'[,]', '，', transcript)
sentences = re.split('[。？！]', transcript)
sentences = [s.strip() + '。' for s in sentences if s.strip()]
sentences = list(dict.fromkeys(sentences))



translator = Translator()


dict_to_dump = {}
# Print the sentences. Also dump to json.
c = 0

with open(json_file, "w") as f:
    for i, sentence in enumerate(sentences):
        # if length of sentence is less than 5, skip it
        if len(sentence) < 8:
            continue
        # Convert the sentence to Pinyin using the default settings
        pinyin = pypinyin.lazy_pinyin(sentence,style=pypinyin.Style.TONE)
        pinyin = ' '.join(pinyin).replace('   ','. ')
        
        # translate to korean. If error occurs, try translation 2 seconds later until error stops.
        # korean_text = translator.translate(sentence, dest='ko').text
        while True:
            try:
                korean_text = translator.translate(sentence, dest='ko').text
                break
            except:
                time.sleep(2)
                continue

        print(f"{c+1}.\n {sentence}\n {pinyin}\n {korean_text}\n=====================\n")
        # dump to json as i: {sentence, pinyin, korean}
        dict_to_dump[c] = {"sentence": sentence, "pinyin": pinyin, "korean": korean_text}
        c += 1

    # dump to json
    json.dump(dict_to_dump, f, ensure_ascii=False, indent=4)


# Example:
# {
#     "0": {
#         "sentence": "第一个问题 你叫什么名字? 我叫赵金浩。",
#         "pinyin": "dì yí gè wèn tí. nǐ jiào shén me míng zì ?  wǒ jiào zhào jīn hào 。",
#         "korean": "첫 번째 질문의 이름은 무엇입니까? 제 이름은 Zhao Jinhao입니다."
#     },
#     "1": {
#         "sentence": "第二个 请说出你的出生年月日。",
#         "pinyin": "dì èr gè. qǐng shuō chū nǐ de chū shēng nián yuè rì 。",
#         "korean": "두 번째는 당신의 출생과 하루를 말하십시오."
#     },
#     "2": {
#         "sentence": "我的生日是7月30日。",
#         "pinyin": "wǒ de shēng rì shì 7 yuè 30 rì 。",
#         "korean": "내 생일은 7 월 30 일입니다."
#     },
#     "3": {
#         "sentence": "年月日。",
#         "pinyin": "nián yuè rì 。",
#         "korean": "한 달."
#     },
#     "4": {
#         "sentence": "年。",
#         "pinyin": "nián 。",
#         "korean": "년도."
#     },
#     "5": {
#         "sentence": "年啊。",
#         "pinyin": "nián a 。",
#         "korean": "연령."
#     },
#     "6": {
#         "sentence": "1992年。",
#         "pinyin": "1992 nián 。",
#         "korean": "1992."
#     }
# }
# Convert above to olosia format
#  第一个问题 你叫什么名字? 我叫赵金浩。, dì yí gè wèn tí. nǐ jiào shén me míng zì ?  wǒ jiào zhào jīn hào 。첫 번째 질문의 이름은 무엇입니까? 제 이름은 Zhao Jinhao입니다.
#  第二个 请说出你的出生年月日。, dì èr gè. qǐng shuō chū nǐ de chū shēng nián yuè rì 。두 번째는 당신의 출생과 하루를 말하십시오.
# ....

with open(json_file, "r") as f:
    sentences = json.load(f)
    # for each sentence, convert to olosia format
    for key, value in sentences.items():
        print(value["sentence"] + ", " + value["pinyin"] + value["korean"])


