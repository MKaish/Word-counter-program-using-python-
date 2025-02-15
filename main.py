
import string

def count_words(text):
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    text = input("Enter a sentence or paragraph: ").strip()
    
    if not text:
        print("Error: No input provided. Please enter some text.")
        return
    
    word_count = count_words(text)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
