Note: These bonus challenges are tricky. Only start with these if you've
completed the first challenges in instructions.md!

Bonus Challenge: Part 1
-----------------------

- Create a brand new "Fan Mail" page that includes the following HTML form code:

        <h1>Game of Thrones Fan Mail</h1>
        <form method="POST">
            <input name="myname" placeholder="Your name" />
            <input name="message" placeholder="Your message" />
            <button>Submit</button>
        </form>

- In the function defined for your fanmail page, try adding the following print
  code before the return statement:

        message = request.POST.get('message')
        print('Fan-mail received:', message)

- Can you figure out a cause-and-effect with request.POST and messages being
  received?

- Add additional code to also print out the name, if any.


Bonus Challenge: Part 2
-----------------------

- Add in code that will put the message and name into a dictionary that is
  appended to a list

- The list should be "global" in scope (e.g. outside of any function)

- Hint: You should only add it if they do indeed submit something!



Bonus Challenge: Part 3
-----------------------

- Now, add in code that generates an HTML list containing the messages that
  people leave.

- Hint:

        messages_html = '<ol>'
        for message in messages:
            messages_html += '<li>' + message['name'] + ': ' + message['message'] + '</li>'


Advanced Bonus Challenge
------------------------

- Create a "chat room" where you first enter a username, and then can enter
  a message.

- It should consist of at least 2 pages:
    - The first page users enter their username into a form, which submits via
      GET parameters
    - In the second page, users can enter chat messages into a POST form
    - When a chat message is received, it should be put into a list, and
      displayed (similar to the previous fan-mail form)


