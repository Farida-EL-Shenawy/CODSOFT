import json
import re
import random_responses

#load JSON data
def load_KnowledgeBase(file) : 
  with open(file) as bot_responses:
    print(f"loaded'{file}' successfully!")
    return json.load (bot_responses)        


#store JSON data
responses_data = load_KnowledgeBase("KnowledgeBase.json")

def get_response(input_string):
 split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
 score_list = []
 

  #check all the responses 
 for response in responses_data:
         response_score = 0
         required_score = 0
         required_words = response["required_words"]
         
         #check if there are any required words
         if required_words:
             for word in split_message:
              if word in required_words:
               required_score += 1
         
         
         #Amount of required words should match the required score
         if required_score == len(required_words):
             for word in split_message:
               #if the word is in the response, add to the score
                 if word in response["user_input"]:
                   response_score += 1
         
         #add to the score list             
         score_list.append(response_score)
         #Debugging: Find the best phrase
         #print(response_score, response["user_input"])
         
         
 #find the best response and return it if they're not all 0
 best_response = max(score_list)
 response_index = score_list.index(best_response)
         
 #check if input is empty        
 if input_string == "":
    return "Please type something so we can chat :)"
 
 #if there is no best response, return a random one 
 if best_response != 0:
    return responses_data[response_index]["bot_response"]
         
 return random_responses.random_string()

while True:
  user_input = input("\nYou: ")
  print("\nBot: ", get_response(user_input))