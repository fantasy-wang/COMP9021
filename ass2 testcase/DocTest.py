# Made by Jian Gao 
# Cheaked by Richard
# Created time 14/3/2019

'''
>>> print(os.popen('echo test_1.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Eleonore Sanjay
There is no solution.
>>> print(os.popen('echo test_2.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Frank Nina Paul
There are 8 solutions.
>>> print(os.popen('echo test_3.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Andrew Bill Hilary Nancy
There is a unique solution:
Sir Andrew is a Knave.
Sir Bill is a Knight.
Sir Hilary is a Knave.
Sir Nancy is a Knight.
>>> print(os.popen('echo test_4.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Andrew Bill Hilary Nancy
There are 9 solutions.
>>> print(os.popen('echo test_5.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Andrew Bill Gaojian Hilary Nancy
There is no solution.
>>> print(os.popen('echo test_6.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Harry Richard
There are 3 solutions.
>>> print(os.popen('echo test_7.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Harry Richard
There is a unique solution:
Sir Harry is a Knave.
Sir Richard is a Knight.
>>> print(os.popen('echo test_8.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Gaojian Richard
There is a unique solution:
Sir Gaojian is a Knave.
Sir Richard is a Knight.
>>> print(os.popen('echo test_9.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Gaojian Richard
There is a unique solution:
Sir Gaojian is a Knight.
Sir Richard is a Knave.
>>> print(os.popen('echo test_10.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Gaojian Richard
There is a unique solution:
Sir Gaojian is a Knight.
Sir Richard is a Knave.
>>> print(os.popen('echo test_11.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Jenny John Paul
There is a unique solution:
Sir Jenny is a Knight.
Sir John is a Knave.
Sir Paul is a Knave.
>>> print(os.popen('echo test_12.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Adrian Bernice Carolyn Dawn Elizabeth Emma Greg Jeffery Joanne Lonnie Natalie Raymond Rodriguez Toni Tony Valerie Vincent Walsh
There are 4096 solutions.
>>> print(os.popen('echo test_13.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Billy Bonnie Fred Marcia Rhonda Scott Todd
There are 11 solutions.
>>> print(os.popen('echo test_14.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Callum Catherine Clifford Crystal Dale Eduardo Florence Garcia Hugh Isaac Luis Norma Perry Tremblay
There are 1280 solutions.
>>> print(os.popen('echo test_15.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Alexander Beverly Brittany Dave Davies Fernando Harvey Herbert Leona Nora Teresa Tina
There is no solution.
>>> print(os.popen('echo test_16.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Arnold Jordan Lam Mae Peggy Rhonda
There is no solution.
>>> print(os.popen('echo test_17.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Alma Anne Brent Dave Ellen Ethan Gail Jake Liam Pamela Sophia Stephanie
There is no solution.
>>> print(os.popen('echo test_18.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Anthony Dean Jimmy Julia June Kenneth Priscilla Ray Vivian
There are 80 solutions.
>>> print(os.popen('echo test_19.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: April Christopher Damian Elmer Gordon Walter
There are 6 solutions.
>>> print(os.popen('echo test_20.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Annie Deanna Donna Holly Matthew Megan Ross Russell Shannon
There are 26 solutions.
>>> print(os.popen('echo test_21.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Brenda Jacqueline Mason Renee
There are 9 solutions.
>>> print(os.popen('echo test_22.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Darlene George Lee Megan Nellie Nelson
There are 17 solutions.
>>> print(os.popen('echo test_23.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Cindy Eugene Frederick Max Michele Milton Murphy
There are 12 solutions.
>>> print(os.popen('echo test_24.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Beatrice Brown Darrell Ernest Lonnie Micheal Patrick Ray Sarah Vicki
There are 32 solutions.
>>> print(os.popen('echo test_25.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Gagnon Rodriguez Salvador Tiffany Travis
There are 5 solutions.
>>> print(os.popen('echo test_26.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Alexander Bruce Christine Eleanor Frances Judith Kirk Miguel Morton Priscilla Robin
There are 505 solutions.
>>> print(os.popen('echo test_27.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Bessie Isaac Jackie Patricia
There is no solution.
>>> print(os.popen('echo test_28.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Guy Jim Lily Linda Madison Marion
There is no solution.
>>> print(os.popen('echo test_29.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Daniel Harvey Jake Jonathan Regina Wade
There is no solution.
>>> print(os.popen('echo test_30.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Carrie Duane Hazel
There is a unique solution:
Sir Carrie is a Knight.
Sir Duane is a Knight.
Sir Hazel is a Knave.
>>> print(os.popen('echo test_31.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Beverly Fernando Frances Linda Mitchell Natalie Olivia Peter Williams
There are 30 solutions.
>>> print(os.popen('echo test_32.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Casey Isla Lillian Marshall Ramon Roberts Sue Sullivan
There is no solution.
>>> print(os.popen('echo test_33.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Joe Kathryn Wesley
There is a unique solution:
Sir Joe is a Knave.
Sir Kathryn is a Knight.
Sir Wesley is a Knave.
>>> print(os.popen('echo test_34.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Anna Charles Chris Diana Erin Herbert Hugh Jamie Nicholas Samantha Terrance Wendy White
There is no solution.
>>> print(os.popen('echo test_35.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: April Brown Manuel Marie Maurice Patricia
There are 21 solutions.
>>> print(os.popen('echo test_36.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Carolyn Ernest Jones Lydia Sue Viola
There are 7 solutions.
>>> print(os.popen('echo test_37.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Alice Clarence Connor Danielle Esther Judy Katie Mattie Rita Tremblay Vernon
There is no solution.
>>> print(os.popen('echo test_38.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Billy Cecil Deanna Hilda Jon Mark Terry Willard
There is no solution.
>>> print(os.popen('echo test_39.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Claude Ernest Martha Theodore Warren
There are 17 solutions.
>>> print(os.popen('echo test_40.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Amber Edna Marvin Scott Sharon Smith
There are 14 solutions.
>>> print(os.popen('echo test_41.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Bruce Chris Laura Maurice Raul
There are 2 solutions.
>>> print(os.popen('echo test_42.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Darlene Elaine Erika Hugh Julia Liam Miller Naomi Nathaniel Ray Rodney Ruby
There are 517 solutions.
>>> print(os.popen('echo test_43.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Antonio Cecil Georgia Irma Johnson Vivian
There are 2 solutions.
>>> print(os.popen('echo test_44.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Bertha Bethany Edna Gelbero Lisa Ronald
There are 16 solutions.
>>> print(os.popen('echo test_45.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Brittany Eddie Gelbero Heather Jenny Robert Wendy
There is no solution.
>>> print(os.popen('echo test_46.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Emily Jamie Jennifer Jo Shawn Teresa Vernon Wesley
There are 16 solutions.
>>> print(os.popen('echo test_47.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Bonnie Donna Floyd Jeff Willard
There is no solution.
>>> print(os.popen('echo test_48.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Charlie Chester Christy Jamie Kathy Ken Lawrence Maria Murphy Nathaniel
There is no solution.
>>> print(os.popen('echo test_49.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Brad David Erin Marsha Michael Pamela Wade
There are 11 solutions.
>>> print(os.popen('echo test_50.txt | python knights_and_knaves.py').read(), end = '')
Which text file do you want to use for the puzzle?The Sirs are: Bethany Patsy
There are 3 solutions.
'''
if __name__ == '__main__':
    import doctest
    import os
    print('Test Start......')
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
