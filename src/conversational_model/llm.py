import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

class SimpleFinanceBot:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            print("Please set GOOGLE_API_KEY in .env file")
            exit(1)
        
        self.client = genai.Client(api_key=self.api_key)
        
        # Try different models
        self.model_name = "gemini-3-flash-preview"  # Most stable
    
    def chat(self):
        print("\n🔹 Simple Finance Chatbot 🔹")
        print("Ask about money, budget, savings, etc.")
        print("Type 'quit' to exit\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! 💰")
                break
            
            # Create prompt
            prompt = f"""You are a financial advisor named vault. Help with this question: {user_input}
            
            If it's not finance-related, say: "I only answer finance questions."
            If it's finance-related, give helpful advice.
            
            Response:"""
            
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt
                )
                print(f"\nBot: {response.text}\n")
                
            except Exception as e:
                print(f"\nError: {e}")
                print("Trying with gemini-1.0-pro...")
                
                try:
                    response = self.client.models.generate_content(
                        model="gemini-3-flash-preview",
                        contents=prompt
                    )
                    print(f"\nBot: {response.text}\n")
                except:
                    print("\nSorry, service unavailable. Check your API key.")

if __name__ == "__main__":
    bot = SimpleFinanceBot()
    bot.chat()