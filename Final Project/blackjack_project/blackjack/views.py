from django.shortcuts import render
from django.http import HttpResponse

pol_def = {
	'policy 1' : 'If our hand ≥ 17, stick. Else hit.',
	'policy 2' : 'If our hand ≥ 17 and is hard, stick. In all other cases hit (unless our hand = 21).',
	'policy 3' : 'If our hand ≥ 17 and is hard stick. If our hand ≥ 17 and is soft, stick 50 percent of the time. In all other cases hit (unless our hand = 21).',
	'policy 4' : 'Always stick.',
	'policy 5' : 'If dealer’s hand is 2-6, lower policy 2 requirement to ≥ 12. Else perform policy 2.',
	'policy 6' : 'If dealer’s hand is 2-6, lower policy 3 requirement to ≥ 12. Else perform policy 3.'
}

# Create your views here.
def home(request):
    return render(request, 'blackjack/home.html', pol_def)
