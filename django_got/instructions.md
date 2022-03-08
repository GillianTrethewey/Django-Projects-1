In this activity, we'll want to warm up our Django skills to make an
interactive voting web application.


Challenge 1: Getting started
-----------------------------

Get the code working!

1. Run the following commands:


    pipenv --python 3           # Create a new virtualenv
    pipenv shell                # Enter the virtualenv
    pipenv install django       # Download Django package into virtualenv
    python manage.py runserver  # Run the Django Python web-server itself

2. Go to http://localhost:8000 and/or http://127.0.0.1:8000 in your browser

3. What's the first thing you do with a new Python file? Add a print! Add a
print with a custom message to the index view-function, above the return.

4. Examine the code. Explain in your own words how the parts of the file relate.

- NOTE: Don't bother reading or modifying the "boilerplate" at the bottom!





Challenge 2: Fix path
-----------------------

- Did you notice that there is an "Top GoT Episodes" link that goes to a 404
  page?  There is something wrong with the code.
- Spot the mistakes and fix the code by modifying the manage.py file





Challenge 3: New page
-----------------------

For the rest of this activity, we'll build a "voting" app for which is the best
"Game of Thrones House" (feudal titles from a fiction series), similar to what
you might see in a social network or "click-bait" article.

- Time to add a brand new page!
    - For now, just have it have the text "Vote for your favorite GoT house"
    - It should be available at the path "vote/", so the full URL should then
      be: http://localhost:8000/vote/
- Add a link from the index to this new page

Hint: Examine closely the code that goes into the other pages. You will have to
add code in 3 spots: You will need to add a new "path" in the "urlpatterns", a
new view function, and an "a-tag" link on the homepage (index view-function).






Challenge 4: Voting view functions
-----------------------------------

Now, repeat the process for 3 more brand new pages, one for each of 3 houses:
House Stark, House Lannister, and House Targaryen.

1. To keep this challenge from taking too much time, here is the updated HTML
for the view-function we just made:

        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />
        <h1>Vote for your favorite GoT house</h1>
        <a href="/vote/house-stark">House Stark: Winter is coming!</a> <br/>
        <a href="/vote/house-lannister">House Lannister: Hear me roar!</a> <br/>
        <a href="/vote/house-targaryen">House Targaryen: Fire and blood!</a> <br/>
        <hr />
        <a href="/">Back to home page</a>


2. And here is an example view function for "House Stark".

        def vote_stark(request):
            print('house stark getting a vote')
            return HttpResponse('''
                <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />
                <h2>Your vote was recorded</h2>
                <hr />
                <a href="/vote/">Back to voting page</a>
            ''')


    - Note: This will not actually record a vote: That's the next challenge.

3. Finally, here is a snippet of code for the urlpattern's path:


    path('vote/house-stark', vote_stark),


4. Repeat this process for each of the 3 houses.






Challenge 5: Count votes
------------------------

Next is to actually count the votes:

1. Create a dictionary assigned to a variable named "votes"
    - Three keys, each with a value of 0: 'stark', 'lannister', and 'targaryen'
    - Put it at the "global" level (outside of any function) so that it can be
      used by the different view functions

2. Add code to each of the 3 view functions to increment the respective
dictionary value

3. For now, just print to the terminal the value of the vote


HINT: Code snippet hints for this challenge are at the bottom of this file






Challenge 6: Show votes
-------------------------

Now, let's display the votes. Modify the initial page (the one you made in
Challenge 3) to show the vote totals of each of the 3 houses, formatted however
you like (such as in separate p-tags).

HINT: Normally in Django, we'd use templating to show the values, but since we
haven't gotten to that yet, we'll need to improvise. Hints for some "home-made
templating" using string-concatenation are included at the bottom of this file.




Challenge 7: HTTP redirect
------------------------------

Okay, now that our voting functionality is working, the remaining challenges
are for smoothing over the experience, and refactoring repetitive code. Right
now, unlike the popular UK clothing brand, our code is NOT "super DRY"!

"Redirects" are a special type of HTTP response that instead of having content,
they just tell the client (browser) to go to a new URL. In Django, we can do:

        return HttpResponseRedirect('http://google.com/')


- Using this code as reference, simplify your 3 vote view functions to
  automatically redirect the user back to the main voting page.



Challenge 8: GET parameter refactor
-----------------------------------


To dry it out, let's start by refactoring the 3 vote view functions into a
single view-function, which instead uses GET parameters to select which house
is getting voted on in the current request.


1. Create a new view function called `register_vote`. Include the following:

        house_selected = request.GET['house']
        print('getting a vote for', house_selected)

2. Add it to urlpatterns with the path of: 'vote/register-vote/'

3. Try visiting the following URL and examine the terminal. Can you establish a
pattern of how the '?house=' GET parameter works?

        http://localhost:8000/vote/register-vote/?house=stark

4. Once you figure out a pattern, complete the `register_vote` view function
with more code so that it will increment the vote counter for the house
specified with the GET parameter.

5. Finally, update your links to point to these new URLs, and delete your old
view functions.

Note: We'll cover these 'GET parameters' in more depth later in the course.




Challenge 9: For loop refactor
------------------------------

To further "DRY" out your code, generate the HTML for the voting links and vote
counts using for loops.

Once completed, you should be able to add more houses simply by editing the
dictionary. Consider adding Greyjoy, Baratheon, and Tyrell, or your other
favorite houses.


HINT: Code snippet hints for this challenge are at the bottom of this file


#### Bonus Challenges: Finished? Have more time? Go to `bonus_instructions.md`


---------------------------------------------------------


Challenge 5: Code hints
-----------------------

        votes = {
            'stark': 0,
            'lannister': 0,
            'targaryen': 0,
        }

        # How to increment house stark's vote count.
        # The code should go after the "def" and before the "return".
        votes['stark'] = votes['stark'] + 1
        votes['stark'] += 1 # shortcut syntax
        print('votes for stark:', votes['stark'])
        # Repeat for the other houses




Challenge 6: Code hints
-----------------------


        # Method 1: Include the variable in a triple quoted string that is
        # getting returned in the HttpResponse at the end of the view function:
        return HttpResponse('''
            ... other stuff goes here ...
            <p>Stark votes:
            ''' + str(votes['stark']) + '''</p>
            ... and more stuff goes here ...
        ''')


        # Method 2: Assemble the vote HTML in a separate variable, that then
        # gets included in the HTML at the bottom of the view function:
        votes_html = '<ul>'
        votes_stark_number = votes['stark']
        votes_stark_string = str(votes_stark_number)
        votes_html += '<li><strong>Stark:</strong> ' + votes_stark_string + '</li>'

        # ...and later on...
        ''' + votes_html + '''



Challenge 9: Code hints
-----------------------

        # Snippet 1: For loop over dict
        for name, count in votes.items():
            print(name)
            print(count)


        # Snippet 2: Using f-strings
        house_name = 'stark'
        vote_count = 13
        s = f'<a href="/vote/register-vote/?house={house_name}">{vote_count} {house_name}</a><br />'

