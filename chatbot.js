function sendMessage(){

    let input = document.getElementById("userInput");
    let message = input.value.trim();

    if(message === "") return;

    let chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `<div class="user">${message}</div>`;

    let reply = getAIResponse(message);

    setTimeout(()=>{
        chatBox.innerHTML += `<div class="bot">${reply}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    },500);

    input.value="";
}

function getAIResponse(msg){

    msg = msg.toLowerCase();

    if(msg.includes("fever"))
        return "Take rest and drink fluids.";

    if(msg.includes("headache"))
        return "Relax and stay hydrated.";

    if(msg.includes("hello"))
        return "Hello! I am your AI Health Assistant.";

    return "Please consult a doctor for professional advice.";
}
