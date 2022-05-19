var number = 0;
var starttime = false
var correct = 0
var incorrect = 0

function wordsToType(words) {
    document.getElementById('inputtext').innerHTML = '';
    words.split(' ').forEach(word => {
        const wordSpan = document.createElement('span');
        wordSpan.innerText = word;
        inputtext.appendChild(wordSpan);
    })
    inputtext.querySelectorAll('span')[number].classList.add('highlight');
}

function onEnter(gamemode) {
    document.getElementById("inputfield").addEventListener("keyup", function(event) {
        event.preventDefault();
        if (event.keyCode === 13) {
            const arrayWords = inputtext.querySelectorAll('span');
            const inputword = inputfield.value;
            if (inputword === arrayWords[number].innerText) {
                arrayWords[number].classList.add('correct');
                correct += 1
            } else {
                arrayWords[number].classList.add('wrong');
                incorrect += 1
            }
            arrayWords[number].classList.remove('highlight');
            number += 1;
            if (gamemode == 'time') {
                arrayWords[number].classList.add('highlight');
            } else if (gamemode === 'words') {
                var totalwords = parseInt(document.getElementById("total-words").innerText);
                if (number != totalwords) {
                    arrayWords[number].classList.add('highlight');
                }
                var width = ((number / totalwords) * 100).toFixed(2).toString() + "%";
                const progressionbar = document.querySelector('.progressionbar-inner');
                progressionbar.style.width = width;
            }
            document.getElementById('inputfield').value = "";
            document.getElementById('typed-words').innerText = number;
            if (number%8 == 0) {
                for (let i = 0; i < number; i++) {
                    arrayWords[i].classList.add('displayNone');
                }
            }
        }
    });
}

function stopwatch(display) {
    var allseconds = 0;
    setInterval(function () {
        minutes = parseInt(allseconds / 60);
        seconds = parseInt(allseconds % 60);
        allseconds += 1;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = minutes + ":" + seconds;
        var typedwords = document.getElementById('typed-words').innerText
        var totalwords = document.getElementById("total-words").innerText
        if (typedwords == totalwords) {
            javascriptToDjango(allseconds, "/speelscherm-woorden")
            window.location.replace("/resultaat");
        }
    }, 1000);
}

function timer(duration, display) {
    var allseconds = duration;
    setInterval(function () {
        minutes = parseInt(allseconds / 60);
        seconds = parseInt(allseconds % 60);
        allseconds -= 1;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = minutes + ":" + seconds;
        if (allseconds < 0) {
            javascriptToDjango(duration, "/speelscherm-tijd")
            window.location.replace("/resultaat");
        }
    }, 1000);
}

function startTime(gamemode, duration) {
    document.getElementById("inputfield").addEventListener("input", function () {
        if (starttime === false) {
            if (gamemode === 'time') {
                timer(duration, document.querySelector('#timer'));
            } else if (gamemode === 'words') {
                stopwatch(document.querySelector('#timer'));
            }
            starttime = true;
        }
    })
}

function setTime(duration) {
    minutes = parseInt(duration / 60);
    seconds = parseInt(duration % 60);
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;
    document.getElementById('timer').innerText = minutes + ":" + seconds;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function javascriptToDjango(time, url) {
    const csrftoken = getCookie('csrftoken');
    $.ajax({
          type: "post",
          url: url,
          data: {"correct": correct, "incorrect": incorrect, "time":time, "csrfmiddlewaretoken" : csrftoken }
    });
}