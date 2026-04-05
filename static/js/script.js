// Nothing fancy. Just honest JavaScript.

const SARCASTIC_MESSAGES = [
    { title: "Wow. Bold move.", body: "Link copied. Now actually send it to someone." },
    { title: "Look at you go.", body: "Link copied. Your friends are going to love this. Probably." },
    { title: "Sharing is caring.", body: "Or so they say. Link copied. Ball's in your court now." },
    { title: "Revolutionary.", body: "You copied a link. History will remember this moment." },
    { title: "Oh, a sharer.", body: "Link copied. Don't let it sit in your clipboard for 3 days." },
    { title: "Nice.", body: "Link copied. Go ahead, paste it into that group chat you've been ignoring." },
];

let toastTimeout = null;

function showToast(msg) {
    let toast = document.getElementById('share-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'share-toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }

    toast.innerHTML = `<strong>${msg.title}</strong>${msg.body}`;

    toast.classList.remove('show');
    clearTimeout(toastTimeout);

    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            toast.classList.add('show');
        });
    });

    toastTimeout = setTimeout(() => {
        toast.classList.remove('show');
    }, 3200);
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.share-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const path = this.dataset.url;
            const fullUrl = window.location.origin + path;

            navigator.clipboard.writeText(fullUrl).then(() => {
                const msg = SARCASTIC_MESSAGES[Math.floor(Math.random() * SARCASTIC_MESSAGES.length)];
                showToast(msg);
            }).catch(() => {
                showToast({ title: "Clipboard said no.", body: "Couldn't copy. Try doing it the old-fashioned way." });
            });
        });
    });
});