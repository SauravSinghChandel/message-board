# Hypothetical changes - Rishi

## Coding changes for App Logic

### Code Structure and Readability
All the code can be improved to be more modular and easier to read, along with refactoring some of the format
of code for better functionality.

### Variable naming
The variables couldve been named better to adhere to PEP 8 standards better, such as:

dh = dH.dataBaseHandler() (Original Name)
db_handler = dh.dataBaseHandler() (Suggested Name)

### Function naming and type hinting
The functions could've also been named and used better as 
per PEP 8 standards.

def post_data_formatter(message_table) -> dict: (Original Name)
def format_post_data(message_table: list) -> dict: (Suggested Name)

### Documentation

The original code lacks documentation, doc strings 
could've been added for making the code easier to 
understand

Suggested docstring for the function in fetching.py:

def format_post_data(message_table: list) -> dict:
    """
    Formats a message table into a dictionary with specific keys.

    Args:
        message_table (list): List containing message details.

    Returns:
        dict: Formatted dictionary containing date, username, topic, message, message_id,
              structure, quality, likeStat, and dislikeStat.
    """

### Error Handling

Original code assumes the existence of elements in 
message_table and rating without error handling.

Suggested error handling to ensure proper functioning in 
fetching.py:

def format_post_data(message_table: list) -> dict:
    """
    Formats a message table into a dictionary with specific keys.

    Args:
        message_table (list): List containing message details.

    Returns:
        dict: Formatted dictionary containing date, username, topic, message, message_id,
              structure, quality, likeStat, and dislikeStat.
    """
    res = dict()

    # Add error handling for index out of range to avoid potential issues
    if len(message_table) >= 5:
        res['date'] = message_table[0]
        res['username'] = message_table[1]
        res['topic'] = message_table[2]
        res['message'] = message_table[3]
        res['message_id'] = message_table[4]

        # Add error handling for potential NoneType from getSpecificMessageRatings
        rating = dh.getSpecificMessageRatings(res['message_id']) or [0, 0, 0, 0]
        res['structure'] = rating[0]
        res['quality'] = rating[1]
        res['likeStat'] = rating[2]
        res['dislikeStat'] = rating[3]

    return res

## Team Member Tasks

### Code & Performance Review Criteria
If the team came up with a better, more detailed and comprehensive criteria for code & performance reviews when evaluating other team 
members,there could be better code reviews done for the overall code, leading to more improvements.

### Thorough Documentation Standards 
Proposing a set of documentation standards that included not only issue descriptions but also guidelines for labeling could have ensured 
that each issue was well-defined, categorized, and easily accessible for team members.

### Feedback Consolidation
Recommending the creation of a structured system for consolidating and documenting feedback from code reviews could have provided a
valuable resource for future reference and continuous improvement.

### Kanban Board
The team tried their best to write down tasks on the Kanban board. But, it could be better if task descriptions and labels were clearer.
Making tasks easier to understand would help everyone in the team know what's going on more easily.

### UML Diagrams
The team made proper UML Diagrams but they were really overlapping and confusing at first, if the team would've communicated with each
other before making them, it would've been much easier. The job got done, but it could have been done faster.