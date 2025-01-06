import feedparser

# Defining the function for writing the url
def get_url(option):
    # Create a loop for the user to enter the link and validate it
    while option == False:
        direction = input("Enter the link of the RSS feed: ")
        # Analysing the feed
        feed = feedparser.parse(direction)
        if feed.bozo:
            print("Please enter a different link")
            option = False
        else:
            option = True
            return feed

def print_info(feed):
    # Printing the information
    print(f"Feed Title: {feed.feed.title}")
    print(f"Description: {feed.feed.description}")
    print(f"Link: {feed.feed.link}")

# Function for continuing the program
def continue_program():
    url = False
    # Checking if the user wants to continue or not
    while True:
        iteration = input("Write Y to continue OR N to exit: ")
        # If is yes, the loop will continue
        if iteration.lower() == "y":
            url = False
            return url
        # If is no, the loop will break
        elif iteration.lower() == "n":
            url = True
            return url
        # checking if the input is valid
        else:
            print("Please enter a valid input")
            True

# Function for the main program
def main():
    option = False
    while option == False:
        init_url = get_url(option)
        print_info(init_url)
        option = continue_program()

# Running the main program
if __name__ == "__main__":
    main()