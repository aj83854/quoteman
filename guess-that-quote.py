import quoteman as qm


base_url = "http://quotes.toscrape.com"
all_quotes = qm.list_all_quotes(base_url)

def start_game(all_quotes_obj):
    """
    Takes an all_quotes list object as an argument;
    starts a new game of 'Guess that Quote'!
    """
    quote = qm.randquote(all_quotes)
    guesses_remain = 4
    author_soup = qm.make_soup_from(f"{base_url}{quote['bio-url']}")
    birth_date = author_soup.find(class_="author-born-date").get_text()
    birth_place = author_soup.find(class_="author-born-location").get_text()
    print("Here's a quote for you: ")
    print(quote["text"])
    guess = ''
    while guess.lower() != quote["author"] and guesses_remain > 0:
        guess = input(f"Who said this quote? (guesses remaining: {guesses_remain}): ")
        if guess.lower() == quote["author"].lower():
            print("FANTASTIC!! YOU GOT IT!!!")
            break
        guesses_remain -= 1
        if guesses_remain == 3:
            print("Here's a hint: The author was born on "
                  f"{birth_date} {birth_place}...")
        elif guesses_remain == 2:
            print("Here's another hint: "
                  f"The author's first name starts with {quote['author'][0]}")
        elif guesses_remain == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print("Here's one last hint! "
                  f"The author's last name starts with {last_initial}")
        else:
            print("Aww... sorry! You ran out of guesses... "
                  f"The answer was {quote['author']}!")
    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again ([Y]es or [N]o)? ")
        if again.lower() in ('y', 'yes'):
            return start_game(all_quotes)
        else:
            print("Thank you for playing!  GOODBYE! ")

start_game(all_quotes)