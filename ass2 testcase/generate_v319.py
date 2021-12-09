# Made by Jian Gao 19/3/2019

from random import choice, randint

name_list = ['Aaron', 'Abigail', 'Adam', 'Adrian', 'Agnes', 'Alan', 'Albert', 'Alberto', 'Alex', 'Alexander', 'Alfred', 
             'Alfredo', 'Alice', 'Alicia', 'Allan', 'Allen', 'Allison', 'Alma', 'Alvin', 'Amanda', 'Amber', 'Amelia', 'Amy',
             'Ana', 'Anderson', 'Andre', 'Andrea', 'Andrew', 'Andy', 'Angel', 'Angela', 'Anita', 'Ann', 'Anna', 'Anne', 'Annette',
             'Annie', 'Anthony', 'Antonio', 'April', 'Arlene', 'Armando', 'Arnold', 'Arthur', 'Ashley', 'Audrey', 'Ava', 'Barbara',
             'Barry', 'Beatrice', 'Becky', 'Ben', 'Benjamin', 'Bernard', 'Bernice', 'Bertha', 'Bessie', 'Beth', 'Bethany', 'Betty',
             'Beverly', 'Bill', 'Billie', 'Billy', 'Bob', 'Bobbie', 'Bobby', 'Bonnie', 'Brad', 'Bradley', 'Brandon', 'Brandy', 'Brenda',
             'Brent', 'Brett', 'Brian', 'Brien', 'Brittany', 'Brown', 'Bruce', 'Bryan', 'Byrne', 'Byron', 'Callum', 'Calvin', 'Carl',
             'Carla', 'Carlos', 'Carmen', 'Carol', 'Carole', 'Caroline', 'Carolyn', 'Carrie', 'Casey', 'Cassandra', 'Catherine', 'Cathy',
             'Cecil', 'Chad', 'Charlene', 'Charles', 'Charlie', 'Charlotte', 'Cheryl', 'Chester', 'Chris', 'Christian', 'Christina',
             'Christine', 'Christopher', 'Christy', 'Cindy', 'Clara', 'Clarence', 'Claude', 'Claudia', 'Clayton', 'Clifford', 'Clifton',
             'Clinton', 'Clyde', 'Cody', 'Colleen', 'Connie', 'Connor', 'Constance', 'Corey', 'Cory', 'Courtney', 'Craig', 'Crystal',
             'Curtis', 'Cynthia', 'Daisy', 'Dale', 'Damian', 'Dan', 'Daniel', 'Danielle', 'Danny', 'Darlene', 'Darrell', 'Darren', 'Darryl',
             'Daryl', 'Dave', 'David', 'Davies', 'Davis', 'Dawn', 'Dean', 'Deanna', 'Debbie', 'Deborah', 'Debra', 'Delores', 'Denise',
             'Dennis', 'Derek', 'Derrick', 'Diana', 'Diane', 'Dianne', 'Dolores', 'Don', 'Donald', 'Donna', 'Dora', 'Doris', 'Dorothy',
             'Douglas', 'Duane', 'Dustin', 'Dwayne', 'Dwight', 'Earl', 'Eddie', 'Edgar', 'Edith', 'Edna', 'Eduardo', 'Edward', 'Edwin',
             'Eileen', 'Elaine', 'Eleanor', 'Elizabeth', 'Ella', 'Ellen', 'Elmer', 'Elsie', 'Emily', 'Emma', 'Enrique', 'Eric', 'Erica',
             'Erik', 'Erika', 'Erin', 'Ernest', 'Esther', 'Ethan', 'Ethel', 'Eugene', 'Eva', 'Evans', 'Evelyn', 'Everett', 'Felicia',
             'Felix', 'Fernando', 'Florence', 'Floyd', 'Frances', 'Francis', 'Francisco', 'Frank', 'Franklin', 'Fred', 'Freddie',
             'Frederick', 'Gabriel', 'Gagnon', 'Gail', 'Gao', 'Garcia', 'Gary', 'Gelbero', 'Gene', 'George', 'Georgia', 'Gerald',
             'Geraldine', 'Gertrude', 'Gilbert', 'Gina', 'Gladys', 'Glen', 'Glenda', 'Glenn', 'Gloria', 'Gordon', 'Grace', 'Greg',
             'Gregory', 'Guy', 'Gwendolyn', 'Harold', 'Harry', 'Harvey', 'Hazel', 'Heather', 'Hector', 'Heidi', 'Helen', 'Henry',
             'Herbert', 'Herman', 'Hilda', 'Holly', 'Howard', 'Hugh', 'Ian', 'Ida', 'Irene', 'Irma', 'Isaac', 'Isabella', 'Isla',
             'Ivan', 'Jack', 'Jackie', 'Jacob', 'Jacqueline', 'Jaime', 'Jake', 'James', 'Jamie', 'Jane', 'Janet', 'Janice', 'Jared',
             'Jason', 'Javier', 'Jay', 'Jean', 'Jeanette', 'Jeanne', 'Jeff', 'Jeffery', 'Jeffrey', 'Jennie', 'Jennifer', 'Jenny',
             'Jeremy', 'Jerome', 'Jerry', 'Jesse', 'Jessica', 'Jessie', 'Jesus', 'Jian', 'Jill', 'Jim', 'Jimmie', 'Jimmy', 'Jo',
             'Joan', 'Joann', 'Joanne', 'Joe', 'Joel', 'John', 'Johnnie', 'Johnny', 'Johnson', 'Jon', 'Jonathan', 'Jones', 'Jordan',
             'Jorge', 'Jose', 'Joseph', 'Josephine', 'Joshua', 'Joy', 'Joyce', 'Juan', 'Juanita', 'Judith', 'Judy', 'Julia', 'Julian',
             'Julie', 'Julio', 'June', 'Justin', 'Karen', 'Karl', 'Katherine', 'Kathleen', 'Kathryn', 'Kathy', 'Katie', 'Kay', 'Keith',
             'Kelly', 'Ken', 'Kenneth', 'Kent', 'Kevin', 'Kim', 'Kimberly', 'Kirk', 'Kristen', 'Kristin', 'Kristina', 'Kurt', 'Kyle',
             'Lam', 'Lance', 'Larry', 'Laura', 'Lauren', 'Laurie', 'Lawrence', 'Leah', 'Lee', 'Lena', 'Leo', 'Leon', 'Leona', 'Leonard',
             'Leroy', 'Leslie', 'Lester', 'Lewis', 'Li', 'Liam', 'Lillian', 'Lillie', 'Lily', 'Linda', 'Lisa', 'Lloyd', 'Lois', 'Lonnie',
             'Loretta', 'Lori', 'Lorraine', 'Louis', 'Louise', 'Lucille', 'Lucy', 'Luis', 'Lydia', 'Lynn', 'Mabel', 'Madison', 'Mae',
             'Manuel', 'Marc', 'Marcia', 'Marcus', 'Margaret', 'Margie', 'Maria', 'Marian', 'Marie', 'Marilyn', 'Mario', 'Marion',
             'Marjorie', 'Mark', 'Marsha', 'Marshall', 'Martha', 'Martin', 'Marvin', 'Mary', 'Mason', 'Mathew', 'Matthew', 'Mattie',
             'Maureen', 'Maurice', 'Max', 'Maxine', 'Megan', 'Melanie', 'Melinda', 'Melissa', 'Melvin', 'Mia', 'Michael', 'Micheal',
             'Michele', 'Michelle', 'Miguel', 'Mike', 'Miller', 'Milton', 'Miriam', 'Misty', 'Mitchell', 'Monica', 'Morris', 'Morton',
             'Murphy', 'Myrtle', 'Nancy', 'Naomi', 'Natalie', 'Nathan', 'Nathaniel', 'Neil', 'Neill', 'Nellie', 'Nelson', 'Nicholas',
             'Nicole', 'Nina', 'Noah', 'Nora', 'Norma', 'Norman', 'Olga', 'Oliver', 'Olivia', 'Oscar', 'Pamela', 'Patricia', 'Patrick',
             'Patsy', 'Paul', 'Paula', 'Pauline', 'Pearl', 'Pedro', 'Peggy', 'Penny', 'Perry', 'Peter', 'Philip', 'Phillip', 'Phyllis',
             'Poppy', 'Priscilla', 'Rachel', 'Rafael', 'Ralph', 'Ramon', 'Ramona', 'Randall', 'Randy', 'Raul', 'Ray', 'Raymond', 'Rebecca',
             'Reece', 'Regina', 'Reginald', 'Rene', 'Renee', 'Rhonda', 'Rhys', 'Ricardo', 'Richard', 'Rick', 'Ricky', 'Rita', 'Robert',
             'Roberta', 'Roberto', 'Roberts', 'Robin', 'Rodney', 'Rodriguez', 'Roger', 'Roland', 'Ron', 'Ronald', 'Ronnie', 'Rosa', 'Rose',
             'Rosemary', 'Ross', 'Roy', 'Ruben', 'Ruby', 'Russell', 'Ruth', 'Ryan', 'Sally', 'Salvador', 'Sam', 'Samantha', 'Samuel',
             'Sandra', 'Sara', 'Sarah', 'Scott', 'Sean', 'Sergio', 'Seth', 'Shane', 'Shannon', 'Sharon', 'Shawn', 'Sheila', 'Shelly',
             'Sherri', 'Shirley', 'Sidney', 'Singh', 'Smith', 'Sonia', 'Sophia', 'Sophie', 'Stacey', 'Stanley', 'Stella', 'Stephanie',
             'Stephen', 'Steve', 'Steven', 'Sue', 'Sullivan', 'Susan', 'Suzanne', 'Tamara', 'Tammy', 'Tanya', 'Tara', 'Taylor', 'Ted',
             'Teresa', 'Terrance', 'Terrence', 'Terri', 'Terry', 'Thelma', 'Theodore', 'Theresa', 'Thomas', 'Tiffany', 'Tim', 'Timothy',
             'Tina', 'Todd', 'Tom', 'Tommy', 'Toni', 'Tony', 'Tonya', 'Tracey', 'Tracy', 'Travis', 'Tremblay', 'Troy', 'Tyler', 'Tyrone',
             'Valerie', 'Vanessa', 'Velma', 'Vera', 'Vernon', 'Veronica', 'Vicki', 'Vickie', 'Victor', 'Victoria', 'Vincent', 'Viola', 'Violet',
             'Virgil', 'Virginia', 'Vivian', 'Wade', 'Wallace', 'Walsh', 'Walter', 'Wanda', 'Wang', 'Warren', 'Wayne', 'Wendy', 'Wesley', 'White',
             'Willard', 'William', 'Williams', 'Willie', 'Wilma', 'Wilson', 'Yolanda', 'Yvonne', 'Zachary']

logical_sentence_after = ['"At least one of Conjunction_of_Sirs/us is a Knight/Knave,"', '"At most one of Conjunction_of_Sirs/us is a Knight/Knave,"',\
                    '"Exactly one of Conjunction_of_Sirs/us is a Knight/Knave,"', '"All of us are Knights/Knaves,"', '"I am a Knight/Knave,"', \
                    '"Sir Sir_Name is a Knight/Knave,"', '"Disjunction_of_Sirs is a Knight/Knave,"', '"Conjunction_of_Sirs are Knights/Knaves,"']

logical_sentence_before = ['"at least one of Conjunction_of_Sirs/us is a Knight/Knave!" ', '"at most one of Conjunction_of_Sirs/us is a Knight/Knave." ',\
                    '"exactly one of Conjunction_of_Sirs/us is a Knight/Knave." ', '"all of us are Knights/Knaves." ', '"I am a Knight/Knave." ', \
                    '"Sir Sir_Name is a Knight/Knave!" ', '"Disjunction_of_Sirs is a Knight/Knave." ', '"Conjunction_of_Sirs are Knights/Knaves." ']

after = [' whispered Sir NAME. ', ' replies Sir NAME. ']
before = ['I asked Sir NAME who he was, and he answered impatiently: ', 'Then I met Sir NAME who introduced me to his friend and told me: ', 'Sir NAME said: ', 'You hear Sir NAME who says:']
sentence = ['Yesterday, I visited ', 'I have just met ', 'I have just seen ']

def random_name(flag = 0):
     if flag:
         return choice(name_list)
     return list(set(choice(name_list) for _ in range(1, randint(2, 5))))

def random_logical_sentence(names, speakers):
    if not speakers:
         if randint(1, 10) > 7:
             speaker = random_name(1)
             if speaker not in names:
                  names.append(speaker)
         else:
             speaker = choice(names)         
    elif randint(1, 5) > 1:
         if randint(1, 10) > 7:
             speaker = random_name(1)
             if speaker not in names:
                  names.append(speaker)
         else:
             speaker = choice(names)
    else:
         speaker = choice(speakers)
    speakers += [speaker]
    flag = randint(0,2)
    if flag == 0: # after
        sentence = choice(logical_sentence_after)
    else:
        sentence = choice(logical_sentence_before)
        
    sentence = sentence.replace('Knight/Knave', choice(['Knight', 'Knave']))
    sentence = sentence.replace('Knights/Knaves', choice(['Knights', 'Knaves']))
    if 'Conjunction_of_Sirs/us' in sentence and choice(['Conjunction_of_Sirs', 'us']) == 'us':
        sentence = sentence.replace('Conjunction_of_Sirs/us', 'us')
    L = []
    for _ in range(randint(2, 6)):
        if randint(1, 10) > 2:
            L.append(choice(names))
        else:
            name = random_name(1)
            if name not in L:
                 L.append(name)
            if name not in names:
                 names.append(name)
    sentence = sentence.replace('Conjunction_of_Sirs/us', 'Conjunction_of_Sirs')
    sentence = sentence.replace('Conjunction_of_Sirs',"Sir " + ", Sir ".join(names[:-1]) + ' and Sir ' + names[-1])
    sentence = sentence.replace('Disjunction_of_Sirs',"Sir " + ", Sir ".join(names[:-1]) + ' or Sir '+ names[-1])
    if randint(1, 10) > 2:
         Sir_Name = random_name(1)
         if Sir_Name not in names:
              names.append(Sir_Name)
    else:
         Sir_Name = choice(names)
    sentence = sentence.replace('Sir_Name', Sir_Name)
    
    if flag == 0: # after
        output = sentence + choice(after).replace('NAME', speaker)
    else:
        output = choice(before).replace('NAME', speaker) + sentence
    return output

def random_sentence():
    names = random_name()
    if len(names) > 1:
         output = choice(sentence) + "Sirs " + ", ".join(names[:-1]) + ' and ' + names[-1] + choice(['. ','! '])
    else:
         output = choice(sentence) + "Sir "+ names[0] + choice(['. ','! '])
    speakers = []
    for _ in range(randint(2, 12)):
        output += random_logical_sentence(names, speakers)
    return output

# write into txt file. you need replace "start" and "end" with some number
# it will generate texts,the names from test_{start}.txt to test_{end}.txt
'''
for i in range(start, end):
    with open(f'test_{i}.txt', 'w') as file:
        print(random_sentence(), file = file)
'''

