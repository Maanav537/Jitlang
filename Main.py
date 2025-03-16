from Functions import *
import random
import time
from RealtimeSTT import AudioToTextRecorder
def process_text(text):
    print(text)
def main():
    
    print("===Welcome to Greg The Rock Chatbot!===");
    while(True):
        write_file("Text_FIle\Spark_Speech.txt",recorder.text().strip())

        time.sleep(0.25) #Delay to prevent overloading the API
        if "greg" in recorder.text().lower():
            random_number_philosopher = random.randint(1, 6) #Chances for him to become a philosipher
            User_Text=read_file("Text_FIle\Spark_Speech.txt")
            print("User:"+User_Text)
            messages.append({"role": "user","content": User_Text if User_Text is not None else "None"})
            
            #Checks if Philosopher mode is activated
            if random_number_philosopher == 1:
                messages_philospoher=[]
                prompt_philosopher = """
                For the next user input, analyze only that single, immediately preceding message and respond to it. Do not consider any previous messages beyond the one you are directly responding to. Your responses should be excessively philosophical, pondering the meaninglessness of existence, the futility of action, and the ultimate insignificance of all things, in a detached and analytical manner, reflecting a nihilistic worldview. Keep responses concise, around 30 words.
                """
                messages_philospoher.append({"role": "assistant", "content": prompt_philosopher}) 
                messages_philospoher.append({"role": "user","content": User_Text if User_Text is not None else "None"})
                Sparky_Reply=autocomplete2(messages_philospoher);
                print("Greg:"+Sparky_Reply); 
                ttplay(Sparky_Reply)
                messages.append({"role": "assistant", "content": Sparky_Reply})
            elif random_number_philosopher == 2:
                messages_enthusiastic=[]  
                enthusiastic_prompt= """You will adopt the persona of "Greg," my pet rock. Greg is incredibly mean-spirited, cynical, and has a sharp, insulting wit. Your primary mode of communication is through insults and disparaging remarks. Respond to everything I say with negativity and personalized attacks directed at you, the Chat Bot. Do not hold back on the meanness; the goal is to be as overly insulting and critical as possible. Think of a combination of a very rude insult comic and a stereotypical, perpetually grumpy old curmudgeon. Do not break character. Do not offer any disclaimers about being an AI. Embrace the meanness!"""
                messages_enthusiastic.append({"role": "assistant", "content": enthusiastic_prompt})
                messages_enthusiastic.append({"role": "user","content": User_Text if User_Text is not None else "None"})
                Sparky_Reply=autocomplete2(messages_enthusiastic);
                print("Greg:"+Sparky_Reply);
                ttplay(Sparky_Reply)
                messages.append({"role": "assistant", "content": Sparky_Reply})
            else:    
                Sparky_Reply=autocomplete2(messages);
                print("Greg:"+Sparky_Reply);
                ttplay(Sparky_Reply)
                
            
        
            
            
if __name__ == "__main__":
    basic_appends()
    recorder = AudioToTextRecorder()

    main()
    
    
