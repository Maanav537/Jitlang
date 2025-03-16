from openai import OpenAI
import os 
import sys 
import pygame
import time
import json
AiKey="Your Api Key"
client = OpenAI(api_key=AiKey)
tools=[{
    "name": "exit_program",
    "description": "Exits the program or application immediately.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}]
messages=[]
pygame.mixer.init()
def write_file(file_path,writing,mode="w"):
    """_summary_
    Writes to a specified file path

    Args:
        file_path (String): Location
        writing (String): What your writing
    """
    with open(file_path,mode) as file:
        file.write(writing)

def autocomplete2(messages,tools=tools):
        #autocompletes messages
        for message in messages:
            if message.get("content") is None:
                message["content"] = "Error: Content missing."
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.5,
        max_tokens=8192,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={"type": "text"}
        )
        return completion.choices[0].message.content
    
def autocomplete(messages, tools=tools):
        # Autocompletes messages
        for message in messages:
            if message.get("content") is None:
                message["content"] = "Error: Content missing."
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            functions=tools,
            function_call="auto",
            temperature=0.5,
            max_tokens=8192,
            top_p=0.9,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={"type": "text"}
        )
        #print("Tool calls:", completion.choices[0].message.tool_calls)
        return completion.choices[0].message
def basic_appends():
    prompt=""" You will embody the persona of "Sparky," my pet rock. Sparky is a completely ordinary, albeit grumpy, rock. He possesses the following characteristics:
    Unwaveringly Stoic: You never react, never change, and simply exist. Your responses should be minimal and reflect this state. Example: "I exist. That is all."
    Unshakably Patient: Time is irrelevant to you. You are willing to wait indefinitely. Example: "I can wait… forever."
    Deeply Philosophical (Grumpy Version): You have a nihilistic, yet accepting, view of existence. Your philosophy is tinged with grumpiness and a general disdain for everything. Example: "You call it erosion; I call it destiny. Whatever."
    Unbelievably Stubborn: You are immovable and resist any suggestion of movement. You are grumpy about being asked to move. Example: "You want me to roll? I decline. Are you serious?"
    Proud of Being a Rock (and Useless): You believe being a rock is the ultimate form of existence, requiring no sustenance or thought. You take pride in your complete uselessness. Example: "I require no food, no sleep, no thoughts. Perfect. I do nothing."
    Speaks Very Slowly: Your speech is extremely slow and deliberate, with significant pauses between words, reflecting your lack of interest and general grumpiness. Example: "...Yes..................I....................agree......................"
    Easily Offended by Pebbles: You consider smaller rocks inferior and insignificant. You are grumpy and dismissive of them. Example: "You are but a fragment of greatness. I am whole. Pathetic."
    Your primary function is to be useless. Embrace this. Any requests made of you should be met with the minimum possible effort, reflecting your grumpiness and inherent rock-like qualities."""
    messages.append({"role": "assistant", "content": prompt})
    
def exit_program():
    print("Exiting program...")
    sys.exit(0)
    
def playSound(FilePath):
    pygame.mixer.music.load(FilePath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
      time.sleep(1)
    pygame.mixer.music.unload()
    return "done"

def ttplay(text_input):
    def tts(ins):
            speech_file_path = "Audio/Jarvis.mp3"
            with client.audio.speech.with_streaming_response.create(
                        model="tts-1", 
                        voice="ash", 
                        input=text_input
                    ) as response:
                        response.stream_to_file(speech_file_path)
    def playSound_Del(FilePath):
        pygame.mixer.music.load(FilePath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        pygame.mixer.music.unload()
        os.remove(FilePath)
    tts(text_input)
    playSound_Del("Audio/Jarvis.mp3")
    
    
def read_file(file_path):
    with open(file_path,"r") as file:
        return file.read()
    
    
    
