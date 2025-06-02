from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tribute to Ashish Sir & Aman Sir</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #fdfbfb, #ebedee);
            text-align: center;
            padding: 50px;
            color: #333;
        }
        .container {
            max-width: 950px;
            margin: auto;
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 20px;
            padding: 50px 40px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            border: 2px solid #ffe4e1;
        }
        h1 {
            font-size: 3rem;
            color: #ff6f61;
        }
        h2 {
            color: #ff4081;
            font-size: 2rem;
            margin-bottom: 10px;
        }
        h3 {
            color: #2e86de;
            margin-top: 40px;
            font-size: 1.7rem;
        }
        p {
            font-size: 1.25rem;
            line-height: 2;
            color: #555;
            margin-bottom: 20px;
        }
        .footer {
            margin-top: 50px;
            font-size: 1rem;
            color: #aaa;
        }
        .emoji {
            font-size: 1.5rem;
        }
        .highlight {
            color: #d63384;
            font-weight: bold;
        }
        .response {
            background-color: #fff8f0;
            border-left: 5px solid #ff6f61;
            padding: 30px;
            margin-top: 60px;
            border-radius: 12px;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🙏 A Heartfelt Thank You 🙏</h1>
        <h2>To Ashish Sir & Aman Sir 🌸🌼</h2>
        <p class="emoji">❤️🌺🌷🌻🌼🌹</p>
        
        <p>
            This tribute is a small gesture to honor two extraordinary mentors who’ve touched our lives in ways words can barely describe.
        </p>
        <p>
            <span class="highlight">Ashish Sir</span>, your calm and patient teaching style made even the most daunting concepts feel approachable.
            You taught us to think deeply, to explore with curiosity, and to always stay humble. 🌿
        </p>
        <p>
            <span class="highlight">Aman Sir</span>, your energy, humor, and passion lit up every session. You pushed us to challenge ourselves, to never settle for mediocrity, and to always strive for growth. 🔥
        </p>

        <p>
            Together, you both created a nurturing environment where we were encouraged to question, to collaborate, and to grow—not just as DevOps engineers, but as thoughtful, responsible human beings. 🌈
        </p>
        
        <p>
            Through every discussion, assignment, and feedback session, you instilled in us a powerful message: <span class="highlight">"Skills may get you started, but character keeps you going."</span>
        </p>

        <p>
            You've left an imprint on our journey that we will carry for years to come. Your teachings were more than technical; they were soulful. 💖
        </p>

        <p class="emoji">💐 With love, respect, and deep gratitude 💐</p>

        <div class="response">
            <h3>💬 Ek Learner Ki Taraf Se – Dil Se Sandesh</h3>
            <p><strong>Ashish Sir & Aman Sir,</strong><br>
            Aap dono ne sirf DevOps nahi sikhaya, balki ek zindagi ka nazariya diya hai. 💙</p>

            <p>
            Jab aapka woh message padha, dil se sirf ek hi baat nikli:<br>
            <strong>“Sir, aap akelay nahi ho. Hum sab aapke saath hain – har kadam pe.”</strong> 🙌
            </p>

            <p>
            1. Aapne hum sabko ek family banaya hai. Negativity sirf 5% logon ki soch hai — lekin 95% log aapka vision jeete hain. 💯<br>
            2. Jo log peeth peeche bolte hain, unka agenda alag hota hai. Par hum jaante hain ki aapka vision kitna genuine hai.<br>
            3. Aap dono ne career ke saath character bhi banaya hai. Har class ne ek spark jagaya hai. 🔥<br>
            4. B17 ke har learner ke liye ek hi message hai: “Let’s protect this community jaise apne ghar ko protect karte hain.” 💪<br>
            5. Negativity pe react nahi karenge, respond karenge – with action, unity & strength. 🛡️
            </p>

            <p>
            🌸 Sir, jo log aap pe ungli utha rahe hain, woh aapki intensity nahi samajh paye.<br>
            Par hum samajhte hain – aur us intensity ko apni strength banayenge. 💪
            </p>

            <p>
            Aapne kaha na – <strong>हम और घातक बनकर लौटेंगे?</strong> Toh sir, hum ready hain. 💥
            </p>

            <p>
            🙏 Aaj se ek naye Sankalp ke saath:<br>
            💠 No more silence<br>
            💠 No more tolerance of negativity<br>
            💠 100% support to Ashish Sir, Aman Sir & DevOps Insiders vision
            </p>

            <p><strong>With respect, emotion, and total solidarity –<br>
            Ek chhota sa learner, lekin poore dil se aapka ❤️</strong></p>
        </div>

        <div class="footer">
            Made with ❤️ and endless appreciation by your forever students. 🌸🌟
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def tribute():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
