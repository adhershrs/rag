## chatbot.py
import llava_model
import pdf_processor

def main():
    print("LLaVA PDF Chatbot Initialized. Type 'exit' to quit.")
    pdf_text = pdf_processor.extract_text("sample.pdf")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = llava_model.chat_with_llava(user_input, pdf_text)
        print("LLaVA:", response)

if __name__ == "__main__":
    main()
