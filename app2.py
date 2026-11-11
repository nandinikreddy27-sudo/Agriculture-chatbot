from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# =====================================
# AGRICULTURE CHATBOT RESPONSE SYSTEM
# =====================================

def chatbot_reply(message):

    msg = message.lower()

    if any(word in msg for word in ["hello", "hi", "hey"]):
        return "Hello Farmer! 🌱 Welcome to AgriSmart. How can I help you today?"

    elif "rice" in msg or "paddy" in msg:
        return "🌾 Rice grows well in clayey or loamy soil. It requires sufficient water, sunlight and proper field management."

    elif "wheat" in msg:
        return "🌾 Wheat grows well in well-drained loamy soil. Proper irrigation and timely sowing are important."

    elif "tomato" in msg:
        return "🍅 Tomato grows well in fertile, well-drained soil. Provide sunlight and balanced nutrients."

    elif "soil" in msg:
        return "🌱 Major soil types include red soil, black soil, sandy soil, clay soil and loamy soil. Soil testing helps select suitable crops."

    elif "red soil" in msg:
        return "Red soil can support groundnut, millets and pulses depending on rainfall and soil fertility."

    elif "black soil" in msg:
        return "Black soil retains moisture and is suitable for cotton, soybean and some pulses."

    elif "disease" in msg or "leaf" in msg:
        return "🍃 Crop diseases may be caused by fungi, bacteria or viruses. Check affected leaves and consult an agricultural expert for proper diagnosis."

    elif "pest" in msg or "insect" in msg:
        return "🐛 Use Integrated Pest Management (IPM). Inspect crops regularly and seek local agricultural advice."

    elif "water" in msg or "irrigation" in msg:
        return "💧 Drip irrigation and sprinkler irrigation can help save water. Choose according to crop and soil conditions."

    elif "fertilizer" in msg or "manure" in msg:
        return "🌿 Use fertilizers according to soil test results. Organic compost can improve soil health."

    elif "weather" in msg or "rain" in msg:
        return "🌦️ Check your local weather forecast before irrigation, pesticide spraying or harvesting."

    elif "organic" in msg:
        return "🌱 Organic farming uses compost, green manure, crop rotation and biological pest control."

    elif "crop" in msg:
        return "🌾 Crop selection depends on soil type, rainfall, climate and water availability. Tell me your soil type."

    elif "thank" in msg:
        return "😊 You are welcome, Farmer! Happy Farming!"

    else:
        return "🌱 I can help you with crops, soil, irrigation, fertilizers, pests and crop diseases. Please ask a farming question."


# =====================================
# WEBSITE HTML + CSS + JAVASCRIPT
# =====================================

HTML_PAGE = """

<!DOCTYPE html>
<html>

<head>

<title>AgriSmart - Farmer Assistant</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

/* GENERAL DESIGN */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    background: #edf7e9;
    color: #23452d;
}

/* HEADER */

header {
    background: linear-gradient(135deg, #124d2c, #39934c);
    color: white;
    padding: 30px;
    text-align: center;
}

header h1 {
    font-size: 32px;
    margin-bottom: 10px;
}

header p {
    color: #d9f5dc;
}

/* MAIN CONTAINER */

.container {
    max-width: 1100px;
    margin: 30px auto;
    padding: 15px;
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 25px;
}

/* CARDS */

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.09);
}

h2 {
    color: #218342;
    margin-bottom: 20px;
}

/* FORM DESIGN */

input, select {
    width: 100%;
    padding: 13px;
    margin-bottom: 15px;
    border: 1px solid #b9d7bd;
    border-radius: 9px;
    outline: none;
    font-size: 14px;
}

input:focus, select:focus {
    border-color: #29964d;
}

/* BUTTON */

button {
    background: #258b43;
    color: white;
    border: none;
    padding: 13px;
    width: 100%;
    border-radius: 9px;
    cursor: pointer;
    font-size: 15px;
    font-weight: bold;
    transition: 0.3s;
}

button:hover {
    background: #145b2c;
    transform: translateY(-2px);
}

/* CHAT AREA */

.chat-box {
    height: 350px;
    overflow-y: auto;
    background: #f2f9f1;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 15px;
}

.message {
    padding: 12px;
    margin: 10px 0;
    border-radius: 12px;
    max-width: 85%;
    line-height: 1.5;
    font-size: 14px;
    white-space: pre-wrap;
}

.bot {
    background: #d9f0d8;
    color: #174c27;
    border-bottom-left-radius: 2px;
}

.user {
    background: #258b43;
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 2px;
}

.chat-input {
    display: flex;
    gap: 10px;
}

.chat-input input {
    margin: 0;
    flex: 1;
}

.chat-input button {
    width: 100px;
}

/* FEATURES */

.features {
    max-width: 1100px;
    margin: 10px auto 30px;
    padding: 15px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}

.feature {
    background: white;
    padding: 25px;
    text-align: center;
    border-radius: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.07);
    transition: 0.3s;
}

.feature:hover {
    transform: translateY(-5px);
}

.feature span {
    font-size: 35px;
}

.feature h3 {
    color: #218342;
    margin: 12px;
}

/* FOOTER */

footer {
    background: #124d2c;
    color: white;
    padding: 22px;
    text-align: center;
    line-height: 1.8;
}

/* MOBILE RESPONSIVE */

@media(max-width: 750px) {

    .container {
        grid-template-columns: 1fr;
    }

    .features {
        grid-template-columns: 1fr;
    }

    header h1 {
        font-size: 23px;
    }

}

</style>

</head>

<body>

<!-- HEADER -->

<header>

    <h1>🌾 AgriSmart Assistant</h1>

    <p>Your Smart Agriculture & Farmers Chatbot</p>

</header>


<!-- MAIN SECTION -->

<div class="container">


<!-- FARMER REGISTRATION -->

<div class="card">

    <h2>👨‍🌾 Farmer Registration</h2>

    <form id="farmerForm">

        <input
            type="text"
            id="farmerName"
            placeholder="Enter Farmer Name"
            required
        >

        <input
            type="text"
            id="location"
            placeholder="Enter Village / Location"
            required
        >

        <select id="crop" required>

            <option value="">Select Your Crop</option>
            <option>Rice</option>
            <option>Wheat</option>
            <option>Tomato</option>
            <option>Groundnut</option>
            <option>Sugarcane</option>
            <option>Maize</option>
            <option>Other</option>

        </select>

        <select id="soil" required>

            <option value="">Select Soil Type</option>
            <option>Red Soil</option>
            <option>Black Soil</option>
            <option>Sandy Soil</option>
            <option>Clay Soil</option>
            <option>Loamy Soil</option>

        </select>

        <button type="submit">
            Register Farmer
        </button>

    </form>

    <p id="registrationResult"
       style="margin-top:15px;color:green;">
    </p>

</div>


<!-- CHATBOT -->

<div class="card">

    <h2>🤖 Ask AgriSmart</h2>

    <div class="chat-box" id="chatBox">

        <div class="message bot">
            Hello Farmer! 🌱

            Welcome to AgriSmart.

            Ask me anything about farming!
        </div>

    </div>

    <div class="chat-input">

        <input
            type="text"
            id="userInput"
            placeholder="Ask your farming question..."
            onkeydown="if(event.key==='Enter') sendMessage()"
        >

        <button onclick="sendMessage()">
            Send
        </button>

    </div>

</div>

</div>


<!-- FEATURES SECTION -->

<div class="features">

    <div class="feature">

        <span>🌱</span>

        <h3>Crop Guidance</h3>

        <p>Get information about different crops.</p>

    </div>


    <div class="feature">

        <span>💧</span>

        <h3>Water Management</h3>

        <p>Learn about irrigation and water saving.</p>

    </div>


    <div class="feature">

        <span>🍃</span>

        <h3>Disease Guidance</h3>

        <p>Learn about crop diseases and prevention.</p>

    </div>

</div>


<!-- FOOTER -->

<footer>

    <p>🌾 AgriSmart - Smart Farming, Better Future</p>

    <p>Developed as a BCA Agriculture Chatbot Project</p>

</footer>


<script>

/* CHATBOT FUNCTION */

async function sendMessage() {

    let input = document.getElementById("userInput");

    let message = input.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");

    input.value = "";

    try {

        let response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        let data = await response.json();

        addMessage(data.reply, "bot");

    }

    catch(error) {

        addMessage(
            "Sorry! Something went wrong. Please try again.",
            "bot"
        );

    }

}


/* DISPLAY CHAT MESSAGES */

function addMessage(message, sender) {

    let chatBox = document.getElementById("chatBox");

    let div = document.createElement("div");

    div.className = "message " + sender;

    div.textContent = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

}


/* FARMER REGISTRATION */

document.getElementById("farmerForm")
.addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("farmerName").value.trim();

    let location = document.getElementById("location").value.trim();

    let crop = document.getElementById("crop").value;

    let soil = document.getElementById("soil").value;

    document.getElementById("registrationResult").textContent =
        "✅ Welcome " + name +
        "! Your registration details have been received.";

    console.log({
        name: name,
        location: location,
        crop: crop,
        soil: soil
    });

});

</script>

</body>

</html>

"""


# =====================================
# FLASK APPLICATION ROUTES
# =====================================

@app.route("/")
def home():

    return render_template_string(HTML_PAGE)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "")

    reply = chatbot_reply(message)

    return jsonify({
        "reply": reply
    })


# =====================================
# START THE APPLICATION
# =====================================

if __name__ == "__main__":

    app.run(debug=True)