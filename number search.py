cards = []
query = 7

def locate_card(cards, query):

    print('cards:', cards)
    print('query:', query)

    # create a variable position with the value 0
    position = 0

    # set up a loop for repetition
    while position < len(cards):

        print('position:', position)

        #check if element at the current position matches the query
        if cards[position] == query:

            #Answer found! Return and Exit..
            return position

        #increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):

            # Number not found, return -1
            return -1 
    return 'No Element in list'


print(locate_card(cards, query))














