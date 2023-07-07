from voice import listen

from chatbot import chatbot1
from save import say


def voice_text_qu():
    qu=listen()
    print(qu)
    return qu

def text_ans(qu):
    ans=chatbot1(qu)
    print(ans)
    return ans
def say_ans(ans):
    say(ans)
