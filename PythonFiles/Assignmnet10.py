# Given a list strings containing
#   team1, slash, team2, space, score1, dash, score2
# Print a series of tables in different formats
# There is always a space between team2 and the first score
# There may or may not be any spaces between the other six items
#
def get_first_team(score_line):
    # returns first team name with no extra spaces or other characters
    # Note this doesn't currently work
    # strip the leading and trailing extra spaces to get a correct first team name
    score_line = score_line.strip()
    # get position of the first space
    # pos = score_line.find(' ')
    slash_pos = score_line.find("/")
    # first team name is everything before the first space
    return score_line[:slash_pos].strip()



def get_second_score(score_line4):
    # finds the second score in the score line
    score_line4 = score_line4.strip()
    # find position of -, seperating the scores
    pos = score_line4.rfind("-")
    # collect what is behind the dash and strip it of extra spaces
    second_score = score_line4[pos + 1:].strip()
    return second_score

def get_first_score(score_line3):
    # get the first score before the dash
    score_line3 = score_line3.strip()
    # find the dash seperating the numbers
    pos = score_line3.find("-")
    # seperate the first portion of the string, from team name all the way to the dash, from the last number after the dash
    first_half = score_line3[0:pos].strip()
    # find the first occurance of a spacefrom that first half starting at the right hand side
    space_pos = first_half.rfind(" ")
    # the first score is between that first space and the - from earlier
    first_score = first_half[space_pos:pos].strip()
    return first_score

def get_second_team(score_line2):
    #returns the second team name with no added spaces or characters
    # Strip leading and tailing spaces
    score_line2 = score_line2.strip()
    # get position of slash and position split string in half
    pos = score_line2.find("/")
    dash_pos = score_line2.find("-")
    second_team_half = score_line2[pos + 1:dash_pos].strip()
    space_pos = second_team_half.rfind(" ")
    second_team_half = second_team_half[0:space_pos]
    return second_team_half

def main():
    score_lines = []
    # Make a variable for the file you are reading from
    scores = open("scores.txt","r")
    # use a for loop to go through each line on the file and append it to the score_lines list above
    for aline in scores:
        score_lines.append(aline.strip())
    #I printed out the actual list to check if i was removing the new line character with the .strip above!
    #print(score_lines)
    # Print the table without formatting
    # this is for the left just and right just of the teams
    for a_score_line in score_lines:
        print(get_first_team(a_score_line).ljust(0))
    for a_score_line in score_lines:
        print(get_first_team(a_score_line).rjust(17))
    for a_score_line in score_lines:
        # print(a_score_line) - the original score line from the list above, blanked out so the print out looks good
        # create a number variable to use as a baseline for the right adjustment of the score
        num = 20
        # print the team, and the score rjust based on the length of the team name and the variable above so they are both alligned
        print(get_first_team(a_score_line).ljust(1) + get_first_score(a_score_line).rjust(num - len(get_first_team(a_score_line))))
        print(get_second_team(a_score_line).ljust(1) + get_second_score(a_score_line).rjust(num - len(get_second_team(a_score_line))))
        # create a variable for both the first and second score, and make them integers to compare them
        first_score = int(get_first_score(a_score_line))
        second_score = int(get_second_score(a_score_line))
        # print(first_score > second_score) --- I used this while having issues before i realised i had to make them integers
        # use an if statment to find which score is higher, and print ut whichever team has the higher score
        if first_score > second_score:
            print(get_first_team(a_score_line))
            print(" ")
        elif first_score < second_score:
            print(get_second_team(a_score_line))
            print(" ")
        else:
            print("Tie")
        #print(get_first_score(a_score_line))
        #print(get_second_score(a_score_line))


main()