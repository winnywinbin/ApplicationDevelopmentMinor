from django.shortcuts import render, redirect
from .models import Highscore
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.db import connection
import itertools
from .forms import InstellingenForm, CustomForm
import re
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'home.html')

def instellingenDatabase(request):
    error_naam, error_spelmodus, error_tijd, error_woorden, error_taal, error_moeilijkheid, spelmodus = "", "", "", "", "", "", ""
    if request.method == "POST":
        form = InstellingenForm(request.POST)
        naam, spelmodus, tijd, woorden, taal, moeilijkheid = \
            request.POST.get('naam'),\
            request.POST.get('spelmodus'),\
            request.POST.get('tijd'),\
            request.POST.get('woorden'),\
            request.POST.get('taal'),\
            request.POST.get('moeilijkheid')
        if naam == "" or naam.isalpha() == False:
            error_naam = "Dit veld is verplicht en mag alleen letters bevatten."
        if spelmodus == "":
            error_spelmodus = "Dit veld is verplicht"
        if taal == "":
            error_taal = "Dit veld is verplicht"
        if moeilijkheid == "":
            error_moeilijkheid = "Dit veld is verplicht"
        if spelmodus == 'tijd':
            if tijd  == "":
                error_tijd = "Dit veld is verplicht"
            elif error_naam == "" and error_spelmodus == "" and error_tijd == "" and error_taal == "" and error_moeilijkheid == "":
                request.session['data'] = request.POST
                return redirect('speelscherm-tijd')
        if spelmodus == 'woorden':
            if woorden == "":
                error_woorden = "Dit veld is verplicht"
            elif error_naam == "" and error_spelmodus == "" and error_woorden == "" and error_taal == "" and error_moeilijkheid == "":
                request.session['data'] = request.POST
                return redirect('speelscherm-woorden')
    else:
        form = InstellingenForm()
    return render(request, 'instellingenDatabase.html', {'formulier': form, "error_naam":error_naam,
                                                         "error_spelmodus":error_spelmodus, "error_tijd":error_tijd,
                                                         "error_woorden":error_woorden, "error_taal": error_taal,
                                                         "error_moeilijkheid": error_moeilijkheid, 'spelmodus':spelmodus})


def instellingenCustom(request):
    error_naam, error_spelmodus, error_tijd, error_woorden, error_file, spelmodus = "", "", "", "", "", ""
    data_file = ""
    if request.method == "POST":
        customform = CustomForm(request.POST)
        naam, spelmodus, tijd, woorden = \
            request.POST.get('naam'),\
            request.POST.get('spelmodus'),\
            request.POST.get('tijd'),\
            request.POST.get('woorden')
        if "," in woorden:
            type_woorden = list(filter(None, re.sub('[^A-Za-z,]+', '', woorden).lower().split(',')))
        if naam == "" or naam.isalpha() == False:
            error_naam = "Dit veld is verplicht en mag alleen letters bevatten."
        if spelmodus == "":
            error_spelmodus = "Dit veld is verplicht"
        if "," not in woorden or len(type_woorden) < 50:
            error_woorden = "Voldoet niet aan format en/of minimumaantal van 50 woorden."
        try:
            file = request.FILES['file']
            if file.name.endswith('.csv') == False and file.name.endswith('.txt') == False:
                error_file = "Voldoet niet aan format en/of minimumaantal van 50 woorden."
            else:
                data_file = file.read()
                data_file = data_file.decode('ascii')
                if "," in data_file:
                    type_woorden = list(filter(None, re.sub('[^A-Za-z,]+', '', data_file).lower().split(',')))
                    if len(type_woorden) < 50:
                        error_file = "Voldoet niet aan format en/of minimumaantal van 50 woorden."
                elif ";" in data_file:
                    type_woorden = data_file.lower().strip().split(';')
                    if len(type_woorden) < 50:
                        error_file = "Voldoet niet aan format en/of minimumaantal van 50 woorden."
                else:
                    error_file = "Voldoet niet aan format en/of minimumaantal van 50 woorden."
        except KeyError:
            error_file = "Voldoet niet aan format en/of minimumaantal van 50 woorden."
        if spelmodus == 'tijd':
            if tijd  == "":
                error_tijd = "Dit veld is verplicht"
            elif error_naam == "" and error_spelmodus == "" and error_tijd == "" and error_woorden == "" or error_file == "":
                request.session['data'] = request.POST
                request.session['file'] = {'file': data_file}
                return redirect('speelscherm-tijd')
        if spelmodus == 'woorden':
            if error_naam == "" and error_spelmodus == "" and error_woorden == "" or error_file == "":
                request.session['data'] = request.POST
                request.session['file'] = {'file': data_file}
                return redirect('speelscherm-woorden')
    else:
        customform = CustomForm()
    return render(request, 'instellingenCustom.html', {'customform': customform, "error_naam":error_naam,
                                                       "error_spelmodus":error_spelmodus, "error_tijd":error_tijd,
                                                       "error_woorden":error_woorden, "error_file":error_file, "spelmodus":spelmodus})


def execute_sql(SQL, variabele):
    cursor = connection.cursor()
    cursor.execute(SQL, variabele)
    results = dictfetchall(cursor)
    return results


def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def speelscherm_tijd(request):
    woorden, seconden = "", ""
    data = request.session.get('data')
    if 'database' in data:
        naam = str(data['naam'])
        seconden = int(data['tijd'])
        taal = str(data['taal'])
        moeilijkheid = str(data['moeilijkheid'])
        woorden = execute_sql("SELECT woord FROM Woord WHERE taal = %s AND moeilijkheidsgraad = %s", (taal, moeilijkheid))
        woorden = [list(woord.values()) for woord in woorden]
        woorden = ' '.join(list(itertools.chain(*woorden)))
    elif 'custom' in data:
        naam = str(data['naam'])
        seconden = int(data['tijd'])
        woord = data['woorden']
        file = request.session.get('file')['file']
        if woord != '':
            woorden = ' '.join(list(filter(None, re.sub('[^A-Za-z,]+', '', woord).lower().split(','))))
        elif file != '':
            if "," in file:
                woorden = ' '.join(list(filter(None, re.sub('[^A-Za-z,]+', '', file).lower().split(','))))
            elif ";" in file:
                woorden = ' '.join(file.lower().strip().split(';'))
    if request.method == "POST":
        correct = int(request.POST.get('correct'))
        incorrect = int(request.POST.get('incorrect'))
        totaal = correct + incorrect
        time = int(request.POST.get('time'))
        wpm = round(correct / (time/60))
        score = ((correct/(correct+incorrect))*100) * wpm
        if 'database' in data:
            Highscore.objects.create(naam=naam, wpm=wpm, fouten=incorrect, score=score, moeilijkheidsgraad=moeilijkheid, taal=taal)
            request.session['resultaat_speler'] = {'speelmodus': 'database', 'aantal': totaal, 'wpm': wpm, 'fouten': incorrect, 'score': score, 'taal': taal, 'moeilijkheid':moeilijkheid}
        else:
            request.session['resultaat_speler'] = {'speelmodus': 'custom', 'aantal': totaal, 'wpm': wpm,'fouten': incorrect, 'score': score}
        return HttpResponseRedirect(reverse('Resultaat'))
    return render(request, 'speelscherm_tijd.html', {'woorden': woorden, 'seconden': seconden})


def speelscherm_woorden(request):
    woorden = ""
    data = request.session.get('data')
    if 'database' in data:
        naam = str(data['naam'])
        aantal_woorden = int(data['woorden'])/10 # we hebben 15 woorden en de opties zijn 50/100/150 dus voor nu gedeeld door 10
        taal = str(data['taal'])
        moeilijkheid = str(data['moeilijkheid'])
        woorden = execute_sql("SELECT woord FROM Woord WHERE taal = %s AND moeilijkheidsgraad = %s LIMIT %s", (taal, moeilijkheid, aantal_woorden))
        woorden = [list(woord.values()) for woord in woorden]
        woorden = ' '.join(list(itertools.chain(*woorden)))
    elif 'custom' in data:
        naam = str(data['naam'])
        woord = data['woorden']
        file = request.session.get('file')['file']
        if woord != '':
            woorden = ' '.join(list(filter(None, re.sub('[^A-Za-z,]+', '', woord).lower().split(','))))
        elif file != '':
            if "," in file:
                woorden = ' '.join(list(filter(None, re.sub('[^A-Za-z,]+', '', file).lower().split(','))))
            elif ";" in file:
                woorden = ' '.join(file.lower().strip().split(';'))
    if request.method == "POST":
        correct = int(request.POST.get('correct'))
        incorrect = int(request.POST.get('incorrect'))
        totaal = correct + incorrect
        time = int(request.POST.get('time'))
        wpm = round(correct / (time/60))
        score = ((correct/(correct+incorrect))*100) * wpm
        if 'database' in data:
            Highscore.objects.create(naam=naam, wpm=wpm, fouten=incorrect, score=score, moeilijkheidsgraad=moeilijkheid, taal=taal)
            request.session['resultaat_speler'] = {'speelmodus': 'database', 'aantal': totaal, 'wpm': wpm, 'fouten': incorrect, 'score': score, 'taal': taal, 'moeilijkheid': moeilijkheid}
        else:
            request.session['resultaat_speler'] = {'speelmodus': 'custom', 'aantal': totaal, 'wpm': wpm,'fouten': incorrect, 'score': score}
        return HttpResponseRedirect(reverse('Resultaat'))
    return render(request, 'speelscherm_woorden.html', {'woorden': woorden})


def resultaat(request):
    resultaat_speler = request.session.get('resultaat_speler')
    speelmodus = resultaat_speler['speelmodus']
    aantal_woorden = resultaat_speler['aantal']
    wpm = resultaat_speler['wpm']
    fouten = resultaat_speler['fouten']
    score_speler = resultaat_speler['score']
    score = {'aantal': aantal_woorden, 'wpm': wpm, 'fouten': fouten, 'score': score_speler}
    if speelmodus == 'database':
        taal = resultaat_speler['taal']
        moeilijkheid = resultaat_speler['moeilijkheid']
        highscore = highscore_filter(moeilijkheid, taal, 'score')
        player_score, index = player_score_filter(highscore)
        make_histogram(highscore, 'resultaat', 'score')
        return render(request, 'resultaat.html', {'score': score, 'speelmodus':speelmodus, 'taal': taal, 'moeilijkheidsgraad': moeilijkheid, 'top_5': highscore[:5], 'player_score': player_score, 'index': index,'image': ['resultaat.png']})
    else:
        return render(request, 'resultaat.html', {'score': score, 'speelmodus':speelmodus})


def highscore_filter(moeilijkheid, taal, acc_wpm):
    dj_filter = Highscore.objects.filter(moeilijkheidsgraad=moeilijkheid.lower(), taal=taal.lower()).order_by('-%s' % acc_wpm)
    return dj_filter


def player_score_filter(highscore):
    laatste = highscore.order_by('-id')[:1].get()
    i = 0
    while True:
        if highscore[i] == laatste:
            if i >= 5:
                return highscore[i-1:i+2], i-1
            else:
                return [], 0
        i += 1


def make_histogram(highscore, naam, acc_wpm):
    data = list(highscore.order_by(acc_wpm).values_list(acc_wpm, flat=True).order_by('-%s' % acc_wpm))
    plt.hist(x=data, bins=10, alpha=0.5, rwidth=0.85)
    plt.xlabel(acc_wpm)
    plt.ylabel('Frequentie')
    plt.title('Verdeling %s' % acc_wpm)
    plt.savefig('./static/images/%s.png' % naam)
    plt.close()


def my_custom_sql(SQL):
    cursor = connection.cursor()
    cursor.execute(SQL)
    results = dictfetchall(cursor)
    return results


def statistiek(request):
    score_lijst = [['nederlands', 'makkelijk', 'NL_makkelijk_acc', 'NL_makkelijk_wpm'],
                   ['nederlands', 'gemiddeld', 'NL_gemiddeld_acc', 'NL_gemiddeld_wpm'],
                   ['nederlands', 'moeilijk', 'NL_moeilijk_acc', 'NL_moeilijk_wpm'],
                   ['engels', 'makkelijk', 'EN_makkelijk_acc', 'EN_makkelijk_wpm'],
                   ['engels', 'gemiddeld', 'EN_gemiddeld_acc', 'EN_gemiddeld_wpm'],
                   ['engels', 'moeilijk', 'EN_moeilijk_acc', 'EN_moeilijk_wpm']]
    highscore_dict = {}
    for i in score_lijst:
        highscore = highscore_filter(i[1], i[0], 'score')
        make_histogram(highscore, i[2], 'score')
        highscore = highscore_filter(i[1], i[0], 'wpm')
        make_histogram(highscore, i[3], 'wpm')
        highscore = my_custom_sql("SELECT * FROM Highscore "
                                  "WHERE taal = '%s' "
                                  "AND moeilijkheidsgraad = '%s' "
                                  "ORDER BY score DESC"
                                  % (i[0], i[1]))
        highscore_dict[i[2]] = highscore
        highscore = my_custom_sql("SELECT * FROM Highscore "
                                  "WHERE taal = '%s' "
                                  "AND moeilijkheidsgraad = '%s' "
                                  "ORDER BY wpm DESC"
                                  % (i[0], i[1]))
        highscore_dict[i[3]] = highscore
    return render(request, 'statistiek.html', {
        'NL_makkelijk_acc': highscore_dict["NL_makkelijk_acc"][:25],
        'NL_gemiddeld_acc': highscore_dict["NL_gemiddeld_acc"][:25],
        'NL_moeilijk_acc': highscore_dict["NL_moeilijk_acc"][:25],
        'EN_makkelijk_acc': highscore_dict["EN_makkelijk_acc"][:25],
        'EN_gemiddeld_acc': highscore_dict["EN_gemiddeld_acc"][:25],
        'EN_moeilijk_acc': highscore_dict["EN_moeilijk_acc"][:25],
        'NL_makkelijk_wpm': highscore_dict["NL_makkelijk_wpm"][:25],
        'NL_gemiddeld_wpm': highscore_dict["NL_gemiddeld_wpm"][:25],
        'NL_moeilijk_wpm': highscore_dict["NL_moeilijk_wpm"][:25],
        'EN_makkelijk_wpm': highscore_dict["EN_makkelijk_wpm"][:25],
        'EN_gemiddeld_wpm': highscore_dict["EN_gemiddeld_wpm"][:25],
        'EN_moeilijk_wpm': highscore_dict["EN_moeilijk_wpm"][:25],
    })


def help_view(request):
    return render(request, 'help.html')

