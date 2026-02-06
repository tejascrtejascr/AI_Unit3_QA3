import re

def get_response(user_input: str) -> str:
    """Return library response based on pattern matching."""
    text = user_input.lower().strip()
    
    # Exit conditions
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for using the library chatbot. Goodbye!"
    
    # Greetings
    if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", text):
        return "Hello! How can I help you with library services today?"
    
    # Library timings
    if re.search(r"\b(timing|hours|library open|library timings)\b", text):
        return "The library is open from 9:00 AM to 6:00 PM, Monday to Saturday."
    
    # Issue book - MOVED BEFORE general book pattern
    if re.search(r"\b(issue book|borrow book|take book)\b", text):
        return "To issue a book, please bring your library ID card to the counter."
    
    # Return book - MOVED BEFORE general book pattern
    if re.search(r"\b(return book|book return)\b", text):
        return "Books must be returned within 14 days from the issue date."
    
    # Book availability - NOW AFTER specific book patterns
    if re.search(r"\b(book|available books|find book)\b", text):
        return "You can search for available books using the library catalogue or ask the librarian for help."
    
    # Fine information
    if re.search(r"\b(fine|late fee|penalty)\b", text):
        return "Late return fine is ₹2 per day per book."
    
    # Membership
    if re.search(r"\b(membership|library card|new member)\b", text):
        return "Library membership is available for all students and staff with a valid ID."
    
    # Default response
    return (
        "Sorry, I didn't understand that. You can ask about library timings, "
        "book availability, issuing books, returning books, fines, or membership."
    )

def library_chatbot():
    """Main chatbot function."""
    print("LibraryBot: Welcome! I am your rule-based library assistant.")
    print("LibraryBot: Type 'bye', 'exit', or 'quit' to end the chat.\n")
    
    while True:
        user = input("You: ")
        response = get_response(user)
        print("LibraryBot:", response)
        
        if user.lower().strip() in ["bye", "exit", "quit", "goodbye"]:
            break

# Run the chatbot
library_chatbot()