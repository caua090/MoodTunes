from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def recomendar(request):
    if request.method == 'POST':
        humor = request.POST.get('humor')
        
        context = {
            'humor': humor,
            'sugestoes': gerar_mock_de_musicas(humor)
        }
        return render(request, 'recomendar.html', context)
    return render(request, 'home.html')

def gerar_mock_de_musicas(humor):
    mocks = {
        'feliz': ['Happy - Pharrell Williams', 'Can’t Stop the Feeling - JT'],
        'triste': ['Someone Like You - Adele', 'Fix You - Coldplay'],
        'estressado': ['Weightless - Marconi Union', 'Breathe - Telepopmusik'],
        'cansado': ['Lo-Fi Beats', 'Coffee Table Jazz'],
        'focado': ['Focus - Hanz Zimmer', 'Deep Work Playlist'],
        'apaixonado': ['Perfect - Ed Sheeran', 'All of Me - John Legend'],
    }
    return mocks.get(humor, ['Playlist genérica'])