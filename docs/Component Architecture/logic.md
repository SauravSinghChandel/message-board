# Logic
This module contains all the code regarding app logic

### fetching.py
It creates an empty dictionary named res.
It assigns values from the message_table to corresponding keys in the res dictionary.
It retrieves additional information from a database using the dataBaseHandler class from the dataHandler module. This information includes ratings for a specific message identified by a username and message ID.
It adds the retrieved rating information to the res dictionary with keys: 'structure', 'quality', 'likeStat', and 'dislikeStat'.
Finally, it returns the populated dictionary.

### post.py
make_post function:
Triggered on form submission.
Extracts current date, username, post content, and topic.
Generates a unique message ID.
Stores post data in the database.
Redirects the user to the root URL.

display_posts function:
Retrieves messages from the database.
Formats each message using post_formatter.
Returns a list of formatted post HTML strings.

post_formatter function:
Takes a dictionary with post data.
Formats data into an HTML string with inline CSS.
Includes sections for topic, username, message content, like/dislike buttons, counts, and rating bars.

CSS:
Basic styling for better visualization.
Defines classes for post, user-topic-line, topic-heading, user-name, content-box, button-box, like/dislike buttons, counts, and rating box.

HTML structure:
Uses divs and inline styles to structure the post display.
Includes sections for topic, username, message content, like/dislike buttons, counts, and rating bars.

### ratings.py
defines a function called like

### search.py
search_results function:
Triggered on form submission with the name search_box.
Retrieves the search query from the submitted form.
Prints the search query to the console.
Initializes an empty list (res) for search results.
Calls lookUpSpecificSubstring to retrieve messages containing the search query.
Formats each message using post.post_formatter and fetching.post_data_formatter.
Appends the formatted posts to the res list.
Returns the list of formatted posts.

return_search_page function:
Calls search_results to obtain search results.
Calls search_page.return_template with the search results.
The exact functionality of return_template is not provided.
Returns the result of search_page.return_template.
