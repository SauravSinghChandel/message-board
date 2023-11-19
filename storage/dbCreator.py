from dataHandler import dataBaseHandler



newHandle = dataBaseHandler()
# newHandle.addUser((1, "JamesBond", "bondybond"))
# newHandle.addUser((2, "MarkTwain", "twainyMark"))
# newHandle.addUser((3, "LickLider", "liderLick"))
# newHandle.addUser((4, "Edwin Van Der Sar", "flyingdutchman"))



"""
USERS:

(1, 'JamesBond', 'bondybond')
(2, 'MarkTwain', 'twainyMark')
(3, 'LickLider', 'liderLick')
(4, 'Edwin Van Der Sar', 'flyingdutchman')

"""

newHandle.addMessage(("21-02-2023 17:42", "JamesBond","random" ,"Vodka Martini, Shaken, not Stirred.", "1"))

# newHandle.addMessage(("21-02-2023 17:44", "LickLider","random" ,"Might invent something else today.", "1"))

# newHandle.addMessage(("21-02-2023 17:49", "JamesBond","random" ,"WHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", "2"))

# newHandle.addMessage(("21-02-2023 17:53", "twainyMark", "random","If you tell the truth, you don't have to remember anything.", "1"))

# newHandle.addMessage(("21-02-2023 18:00", "JamesBond","random" ,"OW :(", "3"))

# newHandle.addMessage(("21-02-2023 18:08", "LickLider","random" ,"Nice", "2"))

"""
MESSAGES:

('21-02-2023 17:42', 'JamesBond', 'Vodka Martini, Shaken, not Stirred.', 1)
# ('21-02-2023 17:44', 'LickLider', 'Might invent something else today.', 1)
# ('21-02-2023 17:49', 'JamesBond', 'WHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 2)
# ('21-02-2023 17:53', 'twainyMark', "If you tell the truth, you don't have to remember anything.", 1)
# ('21-02-2023 18:00', 'JamesBond', 'OW :(', 3)
# ('21-02-2023 18:08', 'LickLider', 'Nice', 2)
"""

# print(newHandle.displayTableMessages())
# print(newHandle.lookUpuserMessages('JamesBond'))
# print(newHandle.lookUpSpecificMessage('JamesBond', '1'))

# print(newHandle.displayTableUsers())
# print(newHandle.displayTableUsers())
# newHandle.removeUser("10")
# print(newHandle.displayTableUsers())
# newHandle.removeUser("11")
print("Users Entries:")
print(newHandle.displayTableUsers())
print("Message Table Entries:")
print(newHandle.displayTableMessages())
print("Ratings Data:")
print(newHandle.displayTableMessageRatings())
newHandle.updateMessageRating('JamesBond', '1', 'MarkTwain', '7','7', '7', '7')
print("Ratings Data:")
print(newHandle.displayTableMessageRatings())
print("Search Data:")
print(newHandle.lookUpSpecificSubstring("StIrReD"))
print("Specific Rating Data:")
print(newHandle.getSpecificMessageRatings("JamesBond", "1"))



