document.getElementById('urlForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = document.getElementById('urlInput').value.trim();
    const resultDiv = document.getElementById('result');
    const shortUrlLink = document.getElementById('shortUrl');
    
    if (!url) return;
    
    try {
        const response = await fetch('/api/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url })
        });
        
        if (!response.ok) {
            throw new Error(await response.text());
        }
        
        const data = await response.json();
        shortUrlLink.textContent = data.short_url;
        shortUrlLink.href = data.short_url;
        resultDiv.classList.add('visible');
    } catch (error) {
        alert('Error: ' + error.message);
    }
});