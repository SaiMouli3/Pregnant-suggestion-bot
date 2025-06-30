document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('mamaForm');
    const responseDiv = document.getElementById('response');
    const submitButton = form.querySelector('button[type="submit"]');
    const btnText = submitButton.querySelector('.btn-text');
    const btnIcon = submitButton.querySelector('.btn-icon');
    let isSubmitting = false;

    // Add animation to form elements on page load
    animateElements();

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        if (isSubmitting) return;
        isSubmitting = true;
        
        // Update button state
        submitButton.disabled = true;
        btnText.textContent = 'Processing...';
        btnIcon.textContent = '⏳';
        
        // Show loading state with animation
        responseDiv.innerHTML = `
            <div class="loading fade-in">
                <p>🤰 Crafting your personalized response...</p>
                <div class="loading-dots">
                    <span>.</span><span>.</span><span>.</span>
                </div>
            </div>`;
        
        // Smooth scroll to response
        setTimeout(() => {
            responseDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
        
        const formData = {
            question: document.getElementById('question').value.trim(),
            trimester: document.getElementById('trimester').value,
            diet: document.getElementById('diet').value,
            mood: document.getElementById('mood').value
        };
        
        try {
            // Show fake loading for better UX (min 1.5s)
            const loadingPromise = new Promise(resolve => setTimeout(resolve, 1500));
            
            const response = await Promise.race([
                fetch('/ask', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                }),
                loadingPromise.then(() => ({})) // This ensures we wait at least 1.5s
            ]);
            
            // If we're still here and response is not from fetch, wait for the actual fetch
            const data = response.json ? await response.json() : 
                await (await fetch('/ask', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                })).json();
            
            if (data.status === 'success') {
                displayResponse(data.response);
                // Add to history in localStorage
                addToHistory(formData.question, data.response);
            } else {
                throw new Error(data.message || 'Something went wrong');
            }
        } catch (error) {
            console.error('Error:', error);
            showError(error.message || 'Failed to get response. Please try again.');
        } finally {
            // Reset button state
            submitButton.disabled = false;
            btnText.textContent = 'Get Personalized Advice';
            btnIcon.textContent = '→';
            isSubmitting = false;
        }
    });
    
    function displayResponse(response) {
        // Format reminders as list items if they exist
        const remindersHtml = response.reminders && response.reminders.length > 0 
            ? `<ul class="reminders-list">${response.reminders.map(r => 
                `<li class="fade-in" style="animation-delay: ${0.2 + Math.random() * 0.3}s">
                    <span class="reminder-icon">🔔</span>
                    <span>${r}</span>
                </li>`
            ).join('')}</ul>`
            : '<p class="no-reminders">No reminders for now. Enjoy your day! 😊</p>';
        
        // Get mood emoji
        const moodEmoji = {
            'happy': '😊',
            'sad': '😔',
            'anxious': '😰',
            'tired': '😴',
            'excited': '🤩'
        }[document.getElementById('mood').value] || '💖';
        
        // Create response HTML with animations
        responseDiv.innerHTML = `
            <div class="response-content">
                <div class="response-header fade-in">
                    <h2>${moodEmoji} Your Personalized Response</h2>
                    <div class="divider"></div>
                </div>
                
                <div class="response-section fade-in" style="animation-delay: 0.1s">
                    <h3>🍼 Answer to Your Question</h3>
                    <div class="response-text">${response.qa_answer || 'I\'m here to help with any pregnancy-related questions you have!'}</div>
                </div>
                
                <div class="divider"></div>
                
                <div class="response-section fade-in" style="animation-delay: 0.2s">
                    <h3>🩺 Daily Health Tip</h3>
                    <div class="response-text">${response.daily_tip || 'Remember to stay hydrated and take short walks if possible!'}</div>
                </div>
                
                ${response.mood_response ? `
                    <div class="divider"></div>
                    <div class="response-section fade-in" style="animation-delay: 0.3s">
                        <h3>${moodEmoji} Mood Support</h3>
                        <div class="response-text">${response.mood_response}</div>
                    </div>
                ` : ''}
                
                <div class="divider"></div>
                
                <div class="response-section reminders-section fade-in" style="animation-delay: 0.4s">
                    <h3>🔔 Your Reminders</h3>
                    ${remindersHtml}
                </div>
                
                <div class="response-footer fade-in" style="animation-delay: 0.5s">
                    <p>💡 Remember to always consult with your healthcare provider for medical advice.</p>
                </div>
            </div>`;
        
        // Add visible class to trigger animations
        responseDiv.classList.add('visible');
        
        // Smooth scroll to response
        setTimeout(() => {
            responseDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    }
    
    function showError(message) {
        responseDiv.innerHTML = `
            <div class="error fade-in">
                <h3>⚠️ Oops! Something went wrong</h3>
                <p>${message}</p>
                <button onclick="location.reload()" class="retry-btn">Try Again</button>
            </div>`;
        responseDiv.classList.add('visible');
    }
    
    function addToHistory(question, response) {
        try {
            const history = JSON.parse(localStorage.getItem('mamacareHistory') || '[]');
            history.unshift({
                question,
                response,
                timestamp: new Date().toISOString()
            });
            // Keep only last 10 items
            localStorage.setItem('mamacareHistory', JSON.stringify(history.slice(0, 10)));
        } catch (e) {
            console.error('Failed to save to history:', e);
        }
    }
    
    function animateElements() {
        // Add animation to form elements
        const formElements = form.querySelectorAll('input, select, button');
        formElements.forEach((el, index) => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
            
            // Trigger reflow
            void el.offsetWidth;
            
            // Add visible class
            setTimeout(() => {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, 50);
        });
    }
    
    // Add input validation
    const inputs = form.querySelectorAll('input[required], select[required]');
    inputs.forEach(input => {
        input.addEventListener('invalid', function(e) {
            this.style.borderColor = '#ff4444';
            
            // Add error message if not already present
            if (!this.nextElementSibling || !this.nextElementSibling.classList.contains('error-message')) {
                const error = document.createElement('div');
                error.className = 'error-message';
                error.textContent = this.validationMessage;
                error.style.color = '#ff4444';
                error.style.fontSize = '0.8rem';
                error.style.marginTop = '-0.5rem';
                error.style.marginBottom = '1rem';
                this.parentNode.insertBefore(error, this.nextSibling);
            }
        });
        
        input.addEventListener('input', function() {
            this.style.borderColor = '#e0e0e0';
            const errorMsg = this.nextElementSibling;
            if (errorMsg && errorMsg.classList.contains('error-message')) {
                errorMsg.remove();
            }
        });
    });
});
