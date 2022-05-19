function hideShow(value){
    if (value == 'tijd') {
        document.getElementById('tijdClass').style.display = "block";
        document.getElementById('tijderror').style.display = "inline-block"
        document.getElementById('tijdlabel').style.display = "block";
        document.getElementById('woordenClass').style.display = "none";
        document.getElementById('woordenerror').style.display = "none"
        document.getElementById('woordenlabel').style.display = "none";
        }
    if (value == "woorden") {
        document.getElementById('woordenClass').style.display = "block";
        document.getElementById('woordenerror').style.display = "inline-block"
        document.getElementById('woordenlabel').style.display = "block";
        document.getElementById('tijdClass').style.display = "none";
        document.getElementById('tijderror').style.display = "none"
        document.getElementById('tijdlabel').style.display = "none";
    }
    if (value == "") {
        document.getElementById('woordenClass').style.display = "none";
        document.getElementById('woordenerror').style.display = "none"
        document.getElementById('woordenlabel').style.display = "none";
        document.getElementById('tijdClass').style.display = "none";
        document.getElementById('tijdlabel').style.display = "none";
        document.getElementById('tijderror').style.display = "none"
    }
}

function customHideShow(value){
    if (value == 'tijd') {
        document.getElementById('tijdClass').style.display = "block";
        document.getElementById('tijderror').style.display = "inline-block"
        document.getElementById('tijdlabel').style.display = "block";
        }
    if (value == "woorden") {
        document.getElementById('tijdClass').style.display = "none";
        document.getElementById('tijdlabel').style.display = "none";
        document.getElementById('tijderror').style.display = "none"
    }
    if (value == "") {
        document.getElementById('tijdClass').style.display = "none";
        document.getElementById('tijdlabel').style.display = "none";
        document.getElementById('tijderror').style.display = "none"
    }
}

