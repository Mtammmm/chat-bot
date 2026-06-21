// Configuration
const CONFIG = {
    apiEndpoint: 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
};

// DOM Elements
const messagesContainer = document.getElementById('messagesContainer');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');

// State
let isLoading = false;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
    setupEventListeners();
});

function initializeApp() {
    // Check if API key is configured
    if (!API_KEY || API_KEY === 'YOUR_GEMINI_API_KEY_HERE') {
        alert('❌ Error: API key not configured!\n\n1. Open config.js\n2. Replace "YOUR_GEMINI_API_KEY_HERE" with your actual API key\n3. Get your free key at: https://makersuite.google.com/app/apikey');
        return;
    }
    
    // API key is configured, ready to chat
    console.log('✅ Chatbot initialized successfully');
}

function setupEventListeners() {
    sendBtn.addEventListener('click', sendMessage);
    clearBtn.addEventListener('click', clearChat);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Auto-resize textarea
    userInput.addEventListener('input', () => {
        userInput.style.height = 'auto';
        userInput.style.height = Math.min(userInput.scrollHeight, 120) + 'px';
    });
}

function clearChat() {
    if (confirm('Are you sure you want to clear the chat history?')) {
        messagesContainer.innerHTML = `
            <div class="welcome-message">
                <div class="welcome-icon">🤖</div>
                <h2>Welcome to Gemini Chat!</h2>
                <p>Start a conversation with Google's Gemini AI. Ask anything and get intelligent responses.</p>
            </div>
        `;
    }
}

function sendMessage() {
    const message = userInput.value.trim();

    if (!message) {
        return;
    }

    // Add user message to chat
    addMessage(message, 'user');
    userInput.value = '';
    userInput.style.height = 'auto';
    sendBtn.disabled = true;
    isLoading = true;

    // Show typing indicator
    const typingId = showTypingIndicator();

    // Send message to Gemini API
    getGeminiResponse(message)
        .then((response) => {
            removeTypingIndicator(typingId);
            addMessage(response, 'bot');
        })
        .catch((error) => {
            removeTypingIndicator(typingId);
            console.error('Error:', error);
            addMessage(
                `❌ Error: ${error.message || 'Failed to get response from Gemini API'}`,
                'bot'
            );
        })
        .finally(() => {
            sendBtn.disabled = false;
            isLoading = false;
            userInput.focus();
        });
}

async function getGeminiResponse(message) {
    const requestBody = {
        contents: [
            {
                role: 'user',
                parts: [
                    {
                        text: message
                    }
                ]
            }
        ],
        generationConfig: {
            temperature: 0.7,
            topP: 0.95,
            topK: 64,
            maxOutputTokens: 2048
        }
    };

    const response = await fetch(
        `${CONFIG.apiEndpoint}?key=${API_KEY}`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        }
    );

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(
            errorData.error?.message || `API error: ${response.status}`
        );
    }

    const data = await response.json();

    if (!data.candidates || data.candidates.length === 0) {
        throw new Error('No response received from Gemini API');
    }

    const generatedText = data.candidates[0]?.content?.parts?.[0]?.text;

    if (!generatedText) {
        throw new Error('Invalid response format from Gemini API');
    }

    return generatedText;
}

function addMessage(content, sender) {
    // Remove welcome message if it's the first real message
    const welcomeMessage = messagesContainer.querySelector('.welcome-message');
    if (welcomeMessage && (sender === 'user' || welcomeMessage.parentElement === messagesContainer)) {
        welcomeMessage.remove();
    }

    const messageGroup = document.createElement('div');
    messageGroup.className = `message-group message-${sender}`;

    const message = document.createElement('div');
    message.className = 'message';

    const bubble = document.createElement('div');
    bubble.className = `message-bubble bubble-${sender}`;
    bubble.textContent = content;

    const time = document.createElement('div');
    time.className = 'message-time';
    time.textContent = new Date().toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
    });

    message.appendChild(bubble);
    message.appendChild(time);
    messageGroup.appendChild(message);

    messagesContainer.appendChild(messageGroup);
    scrollToBottom();
}

function showTypingIndicator() {
    const id = Date.now();

    const messageGroup = document.createElement('div');
    messageGroup.className = 'message-group message-bot';
    messageGroup.id = `typing-${id}`;

    const message = document.createElement('div');
    message.className = 'message';

    const typing = document.createElement('div');
    typing.className = 'typing-indicator';

    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('div');
        dot.className = 'typing-dot';
        typing.appendChild(dot);
    }

    message.appendChild(typing);
    messageGroup.appendChild(message);
    messagesContainer.appendChild(messageGroup);
    scrollToBottom();

    return id;
}

function removeTypingIndicator(id) {
    const element = document.getElementById(`typing-${id}`);
    if (element) {
        element.remove();
    }
}

function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
