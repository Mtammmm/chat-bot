# 🤖 Gemini Chatbot

A beautiful, modern chatbot application powered by Google's Gemini AI API.

## Features

✨ **Beautiful Modern UI**
- Sleek dark theme with gradient accents
- Smooth animations and transitions
- Responsive design that works on desktop and mobile
- Real-time typing indicators

💬 **Chat Functionality**
- Send and receive messages from Gemini AI
- Auto-scrolling to latest messages
- Message timestamps
- Clear chat history

🔐 **Security**
- Secure API key input with optional local storage
- No API keys sent to third parties
- All communication directly with Google Gemini API

⌨️ **Keyboard Shortcuts**
- `Enter` - Send message
- `Shift + Enter` - New line in message
- `Ctrl + Shift + K` - Change API key

## Getting Started

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 2. Open the Chatbot

Simply open `index.html` in any modern web browser:
- Double-click `index.html`, or
- Drag `index.html` into your browser, or
- Open with your favorite code editor and use Live Server

### 3. Enter Your API Key

1. When the app opens, you'll see an API key prompt
2. Paste your Gemini API key
3. Check "Remember this key" to save it locally (optional)
4. Click "Save API Key"

### 4. Start Chatting!

Type your message in the input field and press `Enter` to send.

## File Structure

```
chat-bot/
├── index.html       # Main HTML structure
├── styles.css       # Beautiful styling
├── script.js        # Chat logic and API integration
└── README.md        # This file
```

## How It Works

1. **Frontend Only** - The chatbot runs entirely in your browser
2. **Direct API Communication** - Messages are sent directly to Google Gemini API
3. **No Server Required** - Just open the HTML file in a browser
4. **Local Storage** - Your API key is stored locally in browser storage (can be cleared anytime)

## API Key Security

- Your API key is stored **only locally** in your browser
- It's **never sent** to any third-party servers
- All requests go directly to Google Gemini API
- You can clear it anytime using browser DevTools

## System Requirements

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection
- Google Gemini API key (free)

## Customization

### Change Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #8b5cf6;
    --primary-dark: #7c3aed;
    /* ... more colors ... */
}
```

### Adjust AI Parameters

In `script.js`, modify the generation config:

```javascript
generationConfig: {
    temperature: 0.7,      // Creativity (0-2)
    topP: 0.95,           // Diversity
    topK: 64,             // Top candidates
    maxOutputTokens: 2048 // Max response length
}
```

## Troubleshooting

### "API Key is invalid" error
- Double-check that you copied the entire API key
- Make sure there are no extra spaces
- Generate a new key from Google AI Studio

### "No response received" error
- Check your internet connection
- Verify your API key is still valid
- Try a simpler message

### Messages not sending
- Make sure your API key is entered correctly
- Check browser console for error messages (F12 → Console)
- Try refreshing the page

## Tips

📌 **Better Responses**
- Be specific in your questions
- Provide context when needed
- Ask follow-up questions for clarification

⚡ **Performance**
- Clear chat history occasionally for better performance
- Close other browser tabs to ensure smooth operation

## License

This project is free to use and modify for personal use.

## Resources

- [Google Gemini API Documentation](https://ai.google.dev/)
- [API Reference](https://ai.google.dev/tutorials/rest_quickstart)
- [Model Information](https://ai.google.dev/models)

---

Made with ❤️ for AI enthusiasts
