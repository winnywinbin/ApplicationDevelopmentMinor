function change_data(){
    let taal = document.getElementById('taal').value; //haalt de taal op die is geselecteerd
    let moeilijkheid = document.getElementById('moeilijkheid').value; //haalt de moeilijkheidsgraad op die is geselecteerd
    let type = document.getElementById('type').value; //haalt het type op die is geselecteerd
    let ranks = document.getElementById('aantal_ranks').value; //haalt op hoeveel ranks er getoond moeten worden

    /*
    De drie switch casen zorgen er voor dat de variable naam de het juiste id bevat van de tabel
    die getoond moet worden.
     */
    let naam
    switch (taal){
        case 'nederlands':
            naam = 'NL_';
            break;
        case 'engels':
            naam = 'EN_';
            break;
    }
    switch (moeilijkheid) {
        case 'makkelijk':
            naam += 'makkelijk';
            break;
        case 'gemiddeld':
            naam += 'gemiddeld';
            break;
        default:
            naam += 'moeilijk'
            break;
    }
    switch (type){
        case 'accuracy':
            naam += '_acc';
            break;
        case 'wpm':
            naam += '_wpm';
            break;
    }
    //de volende line zorgt ervoor dat het juiste plaatje getoond wordt
    document.getElementById('histogram').src = './static/images/' + naam + '.png';
    /*
    de forloop zet alle tabellen op niet zichtbaar.
     */
    for (let id of ["NL_makkelijk_acc", "NL_moeilijk_acc", "NL_gemiddeld_acc", "EN_makkelijk_acc",
        "EN_gemiddeld_acc", "EN_moeilijk_acc", "NL_makkelijk_wpm", "NL_moeilijk_wpm", "NL_gemiddeld_wpm",
        "EN_makkelijk_wpm", "EN_gemiddeld_wpm", "EN_moeilijk_wpm"]){
        document.getElementById(id).style.display = 'none';
    }
    //zorgt ervoor dat de juiste tabel getoond wordt met het id dat bij de switch casen is aan gemaakt.
    document.getElementById(naam).style.display = 'block';

    /*
    De eerste for loop maakt alle rows in de geselecteerde niet zichtbaar. de tweede forloop zorgt ervoor dat het
    opgeven aantal ranks zichtbaar wordt.
     */
    let rows = document.getElementById(naam).rows;
    for (let i = 0; i<rows.length; i++) {
        rows[i].style.display = 'none';
    }
    for (let i = 0; i<(eval(ranks) + 1); i++) {
        rows[i].style.display = 'block'
    }

}