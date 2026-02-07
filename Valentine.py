from flask import Flask, render_template_string

app = Flask(name)

HTML = """

<!DOCTYPE html><html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Nuha ❤️ Will You Be My Valentine?</title><!-- Google Font -->
<link href=\"https://fonts.googleapis.com/css2?family=Pacifico&display=swap\" rel=\"stylesheet\">

<style>
    body {
        background: linear-gradient(135deg, #ff758c, #ff7eb3);
        font-family: 'Pacifico', cursive;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        overflow: hidden;
    }
    .card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        width: 90%;
        max-width: 350px;
        z-index: 2;
    }
    h1 {
        color: #e63946;
        font-size: 32px;
    }
    p {
        font-size: 20px;
    }
    button {
        padding: 12px 22px;
        font-size: 18px;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        margin: 10px;
    }
    .yes {
        background: #e63946;
        color: white;
    }
    .no {
        background: #adb5bd;
        color: white;
        position: absolute;
    }
    #response {
        margin-top: 20px;
        color: #e63946;
        font-size: 22px;
    }
    .heart {
        position: absolute;
        color: rgba(255, 0, 80, 0.7);
        font-size: 20px;
        animation: floatUp 6s linear infinite;
    }
    @keyframes floatUp {
        from { transform: translateY(100vh); opacity: 1; }
        to { transform: translateY(-10vh); opacity: 0; }
    }
</style>

</head>
<body><!-- Background Music --><audio autoplay loop>
    <source src=\"https://cdn.pixabay.com/download/audio/2022/03/15/audio_2d90b1bb44.mp3?filename=romantic-piano-112191.mp3\" type=\"audio/mpeg\">
</audio><div class=\"card\">
    <h1>Nuha ❤️</h1>
    <p>Will you be my Valentine?</p>
    <button class=\"yes\" onclick=\"yesClicked()\">Yes 💕</button>
    <button class=\"no\" id=\"noBtn\">No 💔</button>
    <div id=\"response\"></div>
</div><script>
    const noBtn = document.getElementById('noBtn');

    noBtn.addEventListener('touchstart', moveNo);
    noBtn.addEventListener('mouseover', moveNo);

    function moveNo() {
        const x = Math.random() * (window.innerWidth - 100);
        const y = Math.random() * (window.innerHeight - 50);
        noBtn.style.left = x + 'px';
        noBtn.style.top = y + 'px';
    }

    function yesClicked() {
        document.getElementById('response').innerHTML = "You just made me the happiest 💖";
    }

    // Floating hearts
    setInterval(() => {
        const heart = document.createElement('div');
        heart.className = 'heart';
        heart.innerHTML = '❤️';
        heart.style.left = Math.random() * window.innerWidth + 'px';
        heart.style.fontSize = Math.random() * 20 + 15 + 'px';
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 6000);
    }, 400);
</script></body>
</html>
"""@app.route('/') def home(): return render_template_string(HTML)

if name == 'main': app.run(debug=True)
