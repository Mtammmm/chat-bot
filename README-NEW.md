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
- API key stored securely in `config.js` (never commit to git)
- No API keys sent to third parties
- All communication directly with Google Gemini API
- `config.js` is automatically protected by `.gitignore`

⌨️ **Keyboard Shortcuts**
- `Enter` - Send message
- `Shift + Enter` - New line in message

## Getting Started

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 2. Configure Your API Key

1. Open `config.js` in your chat-bot folder
2. Replace `YOUR_GEMINI_API_KEY_HERE` with your actual API key
3. Save the file

**Example:**
```javascript
const API_KEY = 'AIzaSyAb8RN6LwcYZO3D12K0z-Gc23xF3rSbONqD3iY6l8j';
```

### 3. Open the Chatbot

Simply open `index.html` in any modern web browser:
- Double-click `index.html`, or
- Drag `index.html` into your browser, or
- Open with your favorite code editor and use Live Server

### 4. Start Chatting!

Type your message in the input field and press `Enter` to send.

## File Structure

```
chat-bot/
├── index.html       # Main HTML structure
├── styles.css       # Beautiful styling
├── script.js        # Chat logic and API integration
├── config.js        # API key configuration (⚠️ Keep private!)
├── .gitignore       # Prevents config.js from being committed
└── README.md        # This file
```

## How It Works

1. **Frontend Only** - The chatbot runs entirely in your browser
2. **Direct API Communication** - Messages are sent directly to Google Gemini API
3. **No Server Required** - Just open the HTML file in a browser
4. **Configuration File** - Your API key is stored in `config.js`

## API Key Security

⚠️ **IMPORTANT:**
- Your API key is stored in `config.js`
- **NEVER commit `config.js` to Git or GitHub** - it's in `.gitignore`
- **NEVER share your API key** publicly
- All requests go directly to Google Gemini API
- Keep your API key confidential

**If you accidentally share your API key:**
1. Delete it immediately from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Generate a new API key
3. Update `config.js` with the new key

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

### "API key not configured" error
- Open `config.js` and replace the placeholder with your actual API key
- Make sure there are no extra spaces around your key

### "API Key is invalid" error
- Double-check that you copied the entire API key from Google AI Studio
- Make sure there are no extra spaces or characters
- Generate a new key if needed

### "No response received" error
- Check your internet connection
- Verify your API key is still valid
- Try a simpler message

### Messages not sending
- Make sure `config.js` has your API key configured
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
