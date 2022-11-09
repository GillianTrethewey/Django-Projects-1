from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h1>Game of Thrones Fan Page</h1>
        <a href="/vote/">Vote on your favorite house</a> <br />
        <hr />
        <a href="/my-favorite-characters">My favorite GoT characters</a> <br />
        <a href="/top-episodes">Top GoT Episodes</a> <br />
    ''')


def characters(request):
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h1>My favorite Game of Thrones Characters</h1>
        <ul>
            <li>Daenerys Targaryen</li>
            <li>Jon Snow</li>
            <li>Tyrion Lannister</li>
            <li>Arya Stark</li>
        </ul>
        <hr />
        <a href="/">Back to home page</a>
    ''')


def favorite_episodes(request):
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h1>Top 3 episodes</h1>
        <ol>
            <li>Season 2 Episode 9: Blackwater</li>
            <li>Season 3 Episode 9: The Rains of Castamere</li>
            <li>Season 4 Episode 9: The Watchers on the Wall</li>
        </ol>
        <hr />
        <a href="/">Back to home page</a>
    ''')

votes = {
    'stark': 0,
    'lannister': 0,
    'targaryen': 0,
}

def houses_vote(request):
    votes_html = '<ul>'
    votes_html += '<li><strong>Stark:</strong> ' + str(votes['stark']) + '</li>'
    votes_html += '<li><strong>Lannister:</strong> ' + str(votes['lannister']) + '</li>'
    votes_html += '<li><strong>Targaryen:</strong> ' + str(votes['targaryen']) + '</li>'
    votes_html += '</ul>'

    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />
        <h1>Vote for your favorite GoT house</h1>
        <a href="/vote/house-stark">House Stark: Winter is coming!</a> <br/>
        <a href="/vote/house-lannister">House Lannister: Hear me roar!</a> <br/>
        <a href="/vote/house-targaryen">House Targaryen: Fire and blood!</a> <br/>
        <h2>Current vote totals:</h2>
        ''' + votes_html + '''
        <hr />
        <a href="/">Back to home page</a>
        ''')

def vote_stark(request):
    votes['stark'] += 1
    return HttpResponseRedirect('/vote/')

def vote_lannister(request):
    votes['lannister'] += 1
    return HttpResponseRedirect('/vote/')


def vote_targaryen(request):
    votes['targaryen'] += 1
    return HttpResponseRedirect('/vote/')


urlpatterns = [
    path('', index),
    path('my-favorite-characters', characters),
    path('top-episodes', favorite_episodes),
    path('vote/', houses_vote),
    path('vote/house-stark', vote_stark),
    path('vote/house-lannister', vote_lannister),
    path('vote/house-targaryen', vote_targaryen),
]



# Boilerplate -- Don't worry about understanding anything from here down
def main():
    import sys
    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure(
        DEBUG=True,
        ALLOWED_HOSTS=['*'],
        ROOT_URLCONF=sys.modules[__name__],
    )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
