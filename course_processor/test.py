# import re
#
# # Define your input string
# input_string = "This is a sample string with the keyword. Another keyword appears here."
#
# # Define the keyword you want to match
# keyword = "keyword"
#
# # Define the replacement string
# replacement = "replacement"
#
# # Use regular expression to find and replace the keyword
# output_string = re.sub(r'\b%s\b' % re.escape(keyword), replacement, input_string)
#
# print(output_string)

print("To enrol in this course you must\n   - be enrolled in the Master of Computing AND have successfully completed\nCOMP8260\nand\nCOMP6442\n, OR\n   - be enrolled in the Master of Machine Learning and Computer Vision AND have successfully completed:\nCOMP6710\nOR\nCOMP6730\n, AND\nCOMP6250\nOR\nCOMP8260\nOR\nENGN6250\nOR\nENGN8260\n.\nIncompatible with\nCOMP8715\nand\nCOMP8755\n.\n\nYou will need to undergo competitive entry to enrol in this course, please see CECS webpage for more information.".replace('\n', ' ').replace('  ', ' '))