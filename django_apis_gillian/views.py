from datetime import datetime

import requests
from django.shortcuts import render


def homepage(request):
    context = {
    }
    return render(request, 'homepage.html', context)


def search_results(request):

    search_type = request.GET['stype']
    search_query = request.GET['searchterm']

    context = {
        'result_count': 0,
        'search_message': None,
        'search_term': search_query,
        'search_type': search_type,

        # Advanced bonus challenge
        'current_page': 1,
        'page_count': 1,
    }

    if search_type == 'booksearch':
        context['search_message'] = 'Books'
        context['results_count'] = 0
        # TODO Do more stuff here...
        # API URL Example:
        # http://openlibrary.org/search.json?q=Mockingjay
        url = 'http://openlibrary.org/search.json?q='
        url += search_query

        #########################################
        # Advanced Bonus Challenge: Pagination
        page_number = int(request.GET.get('page_number', 1))
        page_size = 24
        offset = (page_number - 1) * page_size
        url += '&offset=' + str(offset)
        url += '&limit=' + str(page_size)
        #########################################

        response = requests.get(url)
        results_data = response.json()
        book_list = results_data['docs']
        total_found = results_data['num_found']
        context['book_results'] = book_list
        context['results_count'] = total_found

        ########################################
        context['current_page'] = page_number
        context['page_count'] = int(total_found / page_size)
        ########################################

    elif search_type == 'newssearch':
        context['search_message'] = 'Headlines'
        context['results_count'] = 0
        # API URL Example:
        # http://content.guardianapis.com/search?q=coding&api-key=a938fccc-00e9-41ca-905c-741615da8be1
        url = 'http://content.guardianapis.com/search?q='
        url += search_query
        url += '&api-key=a938fccc-00e9-41ca-905c-741615da8be1'

        ########################################
        # Advanced Bonus Challenge: Add pagination
        page_number = int(request.GET.get('page_number', 1))
        url += '&page=' + str(page_number)
        ########################################


        response = requests.get(url)
        results_data = response.json()
        results_list = results_data['response']['results']
        context['news_results'] = results_list
        context['results_count'] = len(results_list)

        #########################################
        # Advanced bonus challenge: Pagination
        # Set up page information, and total results count
        current_page = results_data['response']['currentPage']
        page_count = results_data['response']['pages']
        page_size = results_data['response']['pageSize']
        context['current_page'] = current_page
        context['page_count'] = page_count
        context['results_count'] = page_count * page_size
        #########################################

    elif search_type == 'musicsearch':
        context['search_message'] = 'Music'
        context['results_count'] = 0
        # HINTS:
        # To search:
        # http://musicbrainz.org/ws/2/release/?fmt=json&query=cardi+b
        # To include images:
        # http://coverartarchive.org/release/4d223947-38ec-400e-9f19-1b9af5b4937a/front

        url = 'http://musicbrainz.org/ws/2/release/?fmt=json&query='
        url += search_query

        #########################################
        # Advanced Bonus Challenge: Pagination
        page_number = int(request.GET.get('page_number', 1))
        page_size = 24
        offset = (page_number - 1) * page_size
        url += '&offset=' + str(offset)
        #########################################

        response = requests.get(url)
        results_data = response.json()
        total_number_of_results = results_data['count']
        context['music_results'] = results_data['releases']
        context['results_count'] = total_number_of_results

        #########################################
        # Advanced bonus challenge: Pagination
        # Set up page information
        context['current_page'] = page_number
        context['page_count'] = int(total_number_of_results / page_size)
        #########################################

    else:
        context['search_message'] = 'Unknown search, bug?'


    #########################################
    # Advanced Bonus Challenge: Pagination
    context['next_page_number'] = context['current_page'] + 1
    context['previous_page_number'] = context['current_page'] - 1
    #########################################

    return render(request, 'search_results.html', context)


def giggle_news(request):

    # Do a GET request using the API key to get the latest Guardian headlines
    # The parameters are detailed here:
    # https://open-platform.theguardian.com/documentation/search
    url ='http://content.guardianapis.com/search?api-key=a938fccc-00e9-41ca-905c-741615da8be1&page-size=50'
    response = requests.get(url)
    news_data = response.json() # Interpret response as JSON

    # The Guardian API responds with a JSON dictionary, that has a key called
    # 'response', which in turn is another dictionary with a key called
    # 'results'. This final key has the list that we want
    results_list = news_data['response']['results']

    ####################################################################
    # Bonus Challenge: Invoke function to parse the date format
    _fix_guardian_dates(results_list)
    ####################################################################

    context = {
        'results': results_list,
    }
    return render(request, 'news.html', context)



def _fix_guardian_dates(results_list):
    # Note: Function or variable names that start with "_" is a way to indicate
    # that this is smaller "utility" function that is just used by this file,
    # as opposed to something that might be needed elsewhere
    for item in results_list:
        original_date = item['webPublicationDate']
        date_format = "%Y-%m-%dT%H:%M:%SZ"
        converted = datetime.strptime(original_date, date_format)
        item['python_date'] = converted


