import random
import string
import re

class Chatbot:
    def __init__(self):
        # Load responses from the responses.txt file
        self.responses = self.load_responses()

    def load_responses(self):
        """
        Load responses from the responses.txt file.
        Each line in the file should contain keyword(s) followed by a colon and response(s) separated by commas.
        """
        responses = {}
        with open('responses.txt', 'r') as file:
            for line in file:
                # Split each line into keyword(s) and response(s)
                keyword_str, response_str = line.strip().split(': ')
                keywords = tuple(keyword_str.split(', '))
                responses[keywords] = response_str.split(', ')
        return responses

    def respond(self, input_text):
      """
      Respond to user input by finding the first keyword(s) in the input text.
      If no keywords are found, respond with a default message.
      """
      formatted_text = self.format_input_text(input_text)
      keyword_positions = self.find_keyword_positions(formatted_text)
      if not keyword_positions:
          print(random.choice(self.responses[("no match",)]))
          return
      first_keyword = self.get_first_keyword(keyword_positions)
      responses = self.get_responses_for_first_keyword(first_keyword)
      response = self.choose_response(responses, formatted_text, first_keyword)
      print('\n' + response)

    def format_input_text(self, input_text):
      """
      Format the input text for response by converting it to lowercase and removing punctuation.
      """
      formatted_text = input_text.lower()
      formatted_text = formatted_text.translate(str.maketrans('', '', string.punctuation))
      return formatted_text

    def find_keyword_positions(self, input_text):
      """
      Track the position of each keyword in the input text.
      """
      keyword_positions = {}
      for keywords in self.responses.keys():
          for keyword in keywords:
              match = re.search(r'\b{}\b'.format(re.escape(keyword)), input_text)
              if match:
                  keyword_positions[keyword] = match.start()
      return keyword_positions

    def get_first_keyword(self, keyword_positions):
      """
      Find the first occurring keyword in the input text.
      """
      return min(keyword_positions, key=keyword_positions.get)

    def get_responses_for_first_keyword(self, first_keyword):
      """
      Look up responses for all keywords that appear first.
      """
      responses = []
      for keywords, response_list in self.responses.items():
          if first_keyword in keywords:
              responses.extend(response_list)
      return responses

    def choose_response(self, responses, formatted_text, first_keyword):
      """
      Choose a random response from the responses associated with the first occurring keyword.
      """
      response = random.choice(responses)
      if '*' in response:
          response = response.replace('*', formatted_text.split(first_keyword, 1)[1].strip())
      return response

    def get_known_keywords(self):
      """
      Retrieve the keywords the chatbot knows.
      """
      known_keywords = set()
      for keywords in self.responses.keys():
        known_keywords.update(keywords)
      return known_keywords

def main():
    # Initialize the Chatbot
    bot = Chatbot()
    # Continuously prompt the user for input until they type 'bye'
    print("The doctor is in. Say 'help' if you need something to talk about!\n")
    while True:
        user_input = input(" - ")
        if 'help' in user_input.lower():
            print("Here is a list of things we can talk about:\n")
            for word in bot.get_known_keywords():
              print(word)
            print("\n What would you like to talk about?")
        elif 'bye' in user_input.lower():
            print("\nGoodbye!")
            break
        else: 
            bot.respond(user_input)

if __name__ == "__main__":
    main()

