// DOM Elements
const debugForm = document.getElementById('debugForm');
const codeInput = document.getElementById('codeInput');
const debugBtn = document.getElementById('debugBtn');
const outputContainer = document.getElementById('outputContainer');
const loadingSpinner = document.getElementById('loadingSpinner');
const charCount = document.querySelector('.char-count');
const themeToggle = document.getElementById('themeToggle');
const sunIcon = document.querySelector('.sun-icon');
const moonIcon = document.querySelector('.moon-icon');
const languageSelect = document.getElementById('languageSelect');

// Event Listeners
debugForm.addEventListener('submit', handleDebug);
codeInput.addEventListener('input', updateCharCount);
themeToggle.addEventListener('click', toggleTheme);

// Theme initialization
initTheme();

function initTheme() {
    // Check local storage or system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        document.documentElement.setAttribute('data-theme', 'dark');
        updateThemeIcons('dark');
    }
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcons(newTheme);
}

function updateThemeIcons(theme) {
    if (theme === 'dark') {
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
    } else {
        sunIcon.classList.remove('hidden');
        moonIcon.classList.add('hidden');
    }
}

// Update character count
function updateCharCount() {
    const count = codeInput.value.length;
    charCount.textContent = `${count} / 5000`;
}

// Main debug handler
async function handleDebug(e) {
    e.preventDefault();

    const code = codeInput.value.trim();
    const language = languageSelect.value;

    if (!code) {
        showError('Please enter your code or error log');
        return;
    }

    try {
        // Show loading spinner
        loadingSpinner.classList.remove('hidden');
        debugBtn.disabled = true;

        // Send request to API
        const response = await fetch('/api/debug', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code, language }),
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to debug code');
        }

        const data = await response.json();

        // Display result
        displayResult(data.result);
    } catch (error) {
        showError(error.message);
    } finally {
        // Hide loading spinner
        loadingSpinner.classList.add('hidden');
        debugBtn.disabled = false;
    }
}

// Display debugging result
function displayResult(result) {
    outputContainer.classList.add('has-content');

    const formattedResult = formatMarkdown(result);

    outputContainer.innerHTML = `
        <div class="result-content">
            ${formattedResult}
        </div>
    `;

    // Scroll to output
    outputContainer.scrollTop = 0;
}

// Format markdown-like text to HTML
function formatMarkdown(text) {
    let html = text;

    // Headers
    html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.*?)$/gm, '<h3>$1</h3>');
    html = html.replace(/^# (.*?)$/gm, '<h3>$1</h3>');

    // Bold
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/__(.*?)__/g, '<strong>$1</strong>');

    // Italic
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    html = html.replace(/_(.*?)_/g, '<em>$1</em>');

    // Code blocks
    html = html.replace(/```(.*?)```/gs, '<pre><code>$1</code></pre>');

    // Inline code
    html = html.replace(/`(.*?)`/g, '<code>$1</code>');

    // Line breaks
    html = html.replace(/\n\n/g, '</p><p>');
    html = `<p>${html}</p>`;

    // Lists
    html = html.replace(/^\* (.*?)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

    return html;
}

// Show error message
function showError(message) {
    outputContainer.classList.add('has-content');
    outputContainer.innerHTML = `
        <div class="error-message">
            <strong>⚠️ Error:</strong><br>
            ${escapeHtml(message)}
        </div>
    `;
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;',
    };
    return text.replace(/[&<>"']/g, (m) => map[m]);
}

// Clear form
debugForm.addEventListener('reset', () => {
    outputContainer.innerHTML = `
        <div class="empty-state">
            <p>👉 Enter your code and click "Debug Code" to start</p>
        </div>
    `;
    outputContainer.classList.remove('has-content');
    updateCharCount();
});
