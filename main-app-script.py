import sys
import os
import json
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox, ttk

class GeminiAssistant:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.conversation_history = []
        
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Gemini Desktop Assistant")
        self.root.geometry("600x700")
        
        # API Key Setup
        if not api_key:
            self.prompt_for_api_key()
        else:
            self.setup_gemini_client()
        
        self.create_ui()

    def prompt_for_api_key(self):
        """Prompt user for Google Gemini API key"""
        api_key = simpledialog.askstring(
            "API Key", 
            "Enter your Google Gemini API Key:", 
            show='*'
        )
        
        if api_key:
            # Save API key to config file
            with open('config.json', 'w') as f:
                json.dump({"api_key": api_key}, f)
            
            self.api_key = api_key
            self.setup_gemini_client()
        else:
            messagebox.showerror("Error", "API Key is required to use the assistant")
            sys.exit(1)

    def setup_gemini_client(self):
        """Configure Gemini API client"""
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        except Exception as e:
            messagebox.showerror("API Error", str(e))
            self.prompt_for_api_key()

    def create_ui(self):
        """Create the main user interface"""
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.root, 
            state='disabled', 
            height=30, 
            width=70, 
            wrap=tk.WORD
        )
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # User input area
        self.user_input = tk.Entry(self.root, width=50)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)
        self.user_input.bind('<Return>', self.send_message)

        # Send button
        send_button = tk.Button(
            self.root, 
            text="Send", 
            command=self.send_message
        )
        send_button.grid(row=1, column=1, padx=10, pady=10)

        # New Chat button
        new_chat_button = tk.Button(
            self.root, 
            text="New Chat", 
            command=self.start_new_chat
        )
        new_chat_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def send_message(self, event=None):
        """Send user message and get AI response"""
        user_message = self.user_input.get()
        
        if not user_message.strip():
            return

        # Display user message
        self.update_chat_display(f"You: {user_message}\n")
        
        try:
            # Generate AI response
            response = self.model.generate_content(user_message)
            ai_response = response.text

            # Display AI response
            self.update_chat_display(f"AI: {ai_response}\n\n")
            
            # Clear input
            self.user_input.delete(0, tk.END)
            
            # Update conversation history
            self.conversation_history.append({
                'user': user_message,
                'ai': ai_response
            })
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_chat_display(self, message):
        """Update the chat display area"""
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, message)
        self.chat_display.configure(state='disabled')
        self.chat_display.yview(tk.END)

    def start_new_chat(self):
        """Clear the current chat and start a new conversation"""
        self.chat_display.configure(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.configure(state='disabled')
        self.conversation_history = []

    def run(self):
        """Start the application main loop"""
        self.root.mainloop()

def load_api_key():
    """Load API key from config file"""
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config.get('api_key')
    except FileNotFoundError:
        return None

def main():
    # Try to load existing API key
    api_key = load_api_key()
    
    # Create and run the assistant
    assistant = GeminiAssistant(api_key)
    assistant.run()

if __name__ == '__main__':
    main()
