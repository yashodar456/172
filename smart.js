const quiz = [
{
question: "Which language is used for web pages?",
options: ["Python", "Java", "HTML", "C++"],
answer: 2
},
{
question: "Which language styles web pages?",
options: ["CSS", "Python", "Java", "SQL"],
answer: 0
},
{
question: "Which language adds interactivity?",
options: ["C", "JavaScript", "PHP", "Python"],
answer: 1
}
];

let currentQuestion = 0;
let score = 0;

function loadQuestion(){

if(currentQuestion >= quiz.length){
document.querySelector(".quiz-container").innerHTML =
`<h1>🎉 Quiz Completed!</h1>
<h2>Your Score: ${score}/${quiz.length}</h2>`;
return;
}

document.getElementById("question").textContent =
quiz[currentQuestion].question;

const buttons =
document.querySelectorAll(".option");

buttons.forEach((btn,index)=>{
btn.textContent =
quiz[currentQuestion].options[index];
});
}

function checkAnswer(selected){

if(selected === quiz[currentQuestion].answer){
score++;
}

document.getElementById("score").textContent =
"Score: " + score;

currentQuestion++;

loadQuestion();
}

loadQuestion();