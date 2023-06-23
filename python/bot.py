from bardapi import Bard
import os
import time

def bot(qu):
     '''
     Bayan Banat
     Ibrahim Qaisi
     '''
     os.environ['_BARD_API_KEY'] = "XQg_zA4L1UClQssWKH5vAXpRtEaKCBrs0A85lLGxkouyyEiapUgoieE9UzfWQCk-JSGynQ."

     def get_bard_answer(question):
         response = Bard().get_answer(question)
         retries = 0
         while 'content' not in response and retries < 5:
             time.sleep(1)  # Wait for 1 second before checking again
             response = Bard().get_answer(question)
             retries += 1
         return response.get('content', '')
     x = get_bard_answer(qu+"in small paragraph")
     return x
    #  x = get_bard_answer(f"give me a summary of {qu} not more than three line")
    #  y = get_bard_answer(f"give me just yes or no answer without any additional if {x} is related to mental health")
    #  z = y.split(" ")

    #  if z[0] == 'Yes.' or z[0] == 'Yes,':
    #      return x
    #  else:
    #      return "As an AI model, I must answer questions related to mental health!"