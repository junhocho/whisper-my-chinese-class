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

import json
import sys
# json_file = './sentences_230222.json'
# first argument is the json file
json_file = sys.argv[1]
with open(json_file, "r") as f:
    sentences = json.load(f)
    # for each sentence, convert to olosia format
    for key, value in sentences.items():
        print(value["sentence"] + ", " + value["pinyin"] + value["korean"])

