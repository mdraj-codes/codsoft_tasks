/* =================================
   PHISHING AWARENESS QUIZ
================================= */

function checkQuiz() {

    const answers = {
        q1: "correct",
        q2: "correct",
        q3: "correct"
    };

    let score = 0;
    let total = 3;

    for (let question in answers) {

        const selected = document.querySelector(
            `input[name="${question}"]:checked`
        );

        if (selected && selected.value === answers[question]) {
            score++;
        }
    }

    const result = document.getElementById("quiz-result");

    if (score === total) {

        result.innerHTML =
            `🎉 Excellent! You scored ${score}/${total}. You know how to spot phishing!`;

    } else if (score >= 2) {

        result.innerHTML =
            `👍 Good job! You scored ${score}/${total}. Keep improving your phishing awareness.`;

    } else {

        result.innerHTML =
            `⚠️ You scored ${score}/${total}. Review the safety tips and try again.`;
    }
}


/* =================================
   SIMPLE SCROLL EFFECT
================================= */

document.querySelectorAll('nav a').forEach(link => {

    link.addEventListener('click', function () {

        const target = document.querySelector(
            this.getAttribute('href')
        );

        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }

    });

});


/* =================================
   PAGE LOADED MESSAGE
================================= */

console.log(
    "CyberSafe Phishing Awareness Program loaded successfully."
);