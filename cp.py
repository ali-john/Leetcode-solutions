Problem 1

Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.
Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.
This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.
Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".
You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.
Input
The first line contains an integer n (1≤n≤100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.
Output

Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

Examples
inputCopy
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
outputCopy
word
l10n
i18n
p43s

solution:
times=int(input())
for i in range(0,times):
    str=input()
    length=len(str)
    if length>10:
        NewStr=f'{str[0]}{length-2}{str[length-1]} '
        print(NewStr)
    else:
        print(str)
		
Problem 2
Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:
deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.
Help Petya cope with this easy task.

Input
The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

Output
Print the resulting string. It is guaranteed that this string is not empty.


Solution:
vowels=['a','e','i','o','u','y']
str=input().lower()
NewStr=''
for i in str:
    if i not in vowels:
        NewStr=NewStr+i
    else:
        continue
length=len(NewStr)
Fstr=''
for j in range(0,length):
    Fstr=Fstr+f'.{NewStr[j]}'

print(Fstr)

Problem 3
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

Examples
input
aaaa
aaaA
output
0
input
abs
Abz
output
-1
input
abcdefg
AbCdEfF
output
1

Solution:

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str1=input().lower()
str2=input().lower()
length=len(str1)#it is guarenteed both strings are of same length
flag=True
for i in range(0,length):
    if str1[i]==str2[i]:
        continue
    else:
        flag=False
        if alphabets.index(str1[i])>alphabets.index(str2[i]):
            print('1')
            break
        elif alphabets.index(str1[i])<alphabets.index(str2[i]):
            print('-1')
            break
if flag==True:
    print('0')
	
Problem 4
Petya loves football very much. One day, as he was watching a football match, he was writing the players' current positions on a piece of paper. To simplify the situation he depicted it as a string consisting of zeroes and ones. A zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players of some team standing one after another, then the situation is considered dangerous. For example, the situation 00100110111111101 is dangerous and 11110111011101 is not. You are given the current situation. Determine whether it is dangerous or not.

Input
The first input line contains a non-empty string consisting of characters "0" and "1", which represents players. The length of the string does not exceed 100 characters. There's at least one player from each team present on the field.

Output
Print "YES" if the situation is dangerous. Otherwise, print "NO".

Examples
input
001001
output
NO
input
1000000001
output
YES

Solution:
positions=input()
length=len(positions)
total=0
flag=True
for i in range(0,length):
    if i+7<=length:
        for j in range(i,i+7):
            total=total+int(positions[j])
        if int(positions[i])*7== total:
            flag=False
            print('YES')
            break
        total=0
if flag==True:
    print('NO')
	
Problem 5
Vasya is very upset that many people on the Net mix uppercase and lowercase letters in one word. That's why he decided to invent an extension for his favorite browser that would change the letters' register in every word so that it either only consisted of lowercase letters or, vice versa, only of uppercase ones. At that as little as possible letters should be changed in the word. For example, the word HoUse must be replaced with house, and the word ViP — with VIP. If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.

Input
The first line contains a word s — it consists of uppercase and lowercase Latin letters and possesses the length from 1 to 100.

Output
Print the corrected word s. If the given word s has strictly more uppercase letters, make the word written in the uppercase register, otherwise - in the lowercase one.

Examples
input
HoUse
output
house
input
ViP
output
VIP
input
maTRIx
output
matrix

SOLUTION:
string=input()
lower=0
upper=0
for i in range(0,len(string)):
    if string[i].islower():
        lower+=1
    elif string[i].isupper():
        upper+=1
    else:
        continue
if lower>upper:
    NewStr=string.lower()
elif upper>lower:
    NewStr=string.upper()
elif upper==lower:
    NewStr = string.lower()
print(NewStr)

Problem 6
The translation from the Berland language into the Birland language is not an easy task. Those languages are very similar: a berlandish word differs from a birlandish word with the same meaning a little: it is spelled (and pronounced) reversely. For example, a Berlandish word code corresponds to a Birlandish word edoc. However, it's easy to make a mistake during the «translation». Vasya translated word s from Berlandish into Birlandish as t. Help him: find out if he translated the word correctly.

Input
The first line contains word s, the second line contains word t. The words consist of lowercase Latin letters. The input data do not consist unnecessary spaces. The words are not empty and their lengths do not exceed 100 symbols.

Output
If the word t is a word s, written reversely, print YES, otherwise print NO.

Examples
input
code
edoc
output
YES
input
abb
aba
output
NO
input
code
code
output
NO

SOLUTION:
word=input()
translated=input()
lenght=len(translated)
reverse=str()

for i in range(lenght-1,-1,-1):
    reverse=reverse+translated[i]

if reverse==word:
    print('YES')
else:
    print('NO')
	
Problem 7
Little girl Tanya is learning how to decrease a number by one, but she does it wrong with a number consisting of two or more digits. Tanya subtracts one from a number by the following algorithm:

if the last digit of the number is non-zero, she decreases the number by one;
if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).
You are given an integer number n. Tanya will subtract one from it k times. Your task is to print the result after all k subtractions.

It is guaranteed that the result will be positive integer number.

Input
The first line of the input contains two integer numbers n and k (2≤n≤109, 1≤k≤50) — the number from which Tanya will subtract and the number of subtractions correspondingly.

Output
Print one integer number — the result of the decreasing n by one k times.

It is guaranteed that the result will be positive integer number.

Examples
input
512 4
output
50
input
1000000000 9
output
1

SOLUTION:
def subtractor(n,k):
    for i in range(0,k):
        if n%10==0:
            n=n/10
        else:
            n=n-1
    return n

num,times=input().split()#TAke both inputs on single line
num,times=[int(num),int(times)]
#Driver code:
print(int(subtractor(num,times)))

Problem 8
Anton likes to play chess, and so does his friend Danik.

Once they have played n games in a row. For each game it's known who was the winner — Anton or Danik. None of the games ended with a tie.

Now Anton wonders, who won more games, he or Danik? Help him determine this.

Input
The first line of the input contains a single integer n (1≤n≤100000) — the number of games played.

The second line contains a string s, consisting of n uppercase English letters 'A' and 'D' — the outcome of each of the games. The i-th character of the string is equal to 'A' if the Anton won the i-th game and 'D' if Danik won the i-th game.

Output
If Anton won more games than Danik, print "Anton" (without quotes) in the only line of the output.

If Danik won more games than Anton, print "Danik" (without quotes) in the only line of the output.

If Anton and Danik won the same number of games, print "Friendship" (without quotes).

Examples
input
6
ADAAAA
output
Anton
input
7
DDDAADA
output
Danik
input
6
DADADA
output
Friendship



SOLUTION:
times=int(input())
games=input()
anton=0
danik=0

for i in games:
    if i=='A':
        anton+=1
    elif i=='D':
        danik+=1
    else:
        continue
if anton>danik:
    print('Anton')
elif danik>anton:
    print('Danik')
elif danik==anton:
    print('Friendship')
	
Problem 9
George has recently entered the BSUCP (Berland State University for Cool Programmers). George has a friend Alex who has also entered the university. Now they are moving into a dormitory.

George and Alex want to live in the same room. The dormitory has n rooms in total. At the moment the i-th room has pi people living in it and the room can accommodate qi people in total (pi ≤ qi). Your task is to count how many rooms has free place for both George and Alex.

Input
The first line contains a single integer n (1≤n≤100) — the number of rooms.

The i-th of the next n lines contains two integers pi and qi (0 ≤ pi ≤ qi ≤ 100) — the number of people who already live in the i-th room and the room's capacity.

Output
Print a single integer — the number of rooms where George and Alex can move in.

Examples
input
3
1 1
2 2
3 3
output
0
input
3
1 10
0 10
10 10
output
2

Solution:
NoOfRooms=int(input())
FreeRooms=0

for i in range(0,NoOfRooms):
    LivingPeople,RoomCapacity=input().split()
    LivingPeople,RoomCapacity=[int(LivingPeople),int(RoomCapacity)]
    if LivingPeople<RoomCapacity and (RoomCapacity-LivingPeople)>=2:#Since both people have to live in same room
        FreeRooms+=1
print(FreeRooms)

Problem 10
wHAT DO WE NEED cAPS LOCK FOR?

Caps lock is a computer keyboard key. Pressing it sets an input mode in which typed letters are capital by default. If it is pressed by accident, it leads to accidents like the one we had in the first passage.

Let's consider that a word has been typed with the Caps lock key accidentally switched on, if:

either it only contains uppercase letters;
or all letters except for the first one are uppercase.
In this case we should automatically change the case of all letters. For example, the case of the letters that form words "hELLO", "HTTP", "z" should be changed.

Write a program that applies the rule mentioned above. If the rule cannot be applied, the program should leave the word unchanged.

Input
The first line of the input data contains a word consisting of uppercase and lowercase Latin letters. The word's length is from 1 to 100 characters, inclusive.

Output
Print the result of the given word's processing.

Examples
input
cAPS
output
Caps
input
Lock
output
Lock

SOlution:

word=input()
flag=False
count=0

for i in range(1,len(word)):
    if word[i].isupper():
        count+=1
if count==len(word)-1:
    flag=True

if (word[0].isupper() or word[0].islower()) and flag==True:
    Newcpy=word.swapcase()
    print(Newcpy)
else:
    print(word)
	
Problem 11
A guy named Vasya attends the final grade of a high school. One day Vasya decided to watch a match of his favorite hockey team. And, as the boy loves hockey very much, even more than physics, he forgot to do the homework. Specifically, he forgot to complete his physics tasks. Next day the teacher got very angry at Vasya and decided to teach him a lesson. He gave the lazy student a seemingly easy task: You are given an idle body in space and the forces that affect it. The body can be considered as a material point with coordinates (0; 0; 0). Vasya had only to answer whether it is in equilibrium. "Piece of cake" — thought Vasya, we need only to check if the sum of all vectors is equal to 0. So, Vasya began to solve the problem. But later it turned out that there can be lots and lots of these forces, and Vasya can not cope without your help. Help him. Write a program that determines whether a body is idle or is moving by the given vectors of forces.

Input
The first line contains a positive integer n (1≤n≤100), then follow n lines containing three integers each: the xi coordinate, the yi coordinate and the zi coordinate of the force vector, applied to the body ( - 100 ≤ xi, yi, zi ≤ 100).

Output
Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.

Examples
input
3
4 1 7
-2 4 -1
1 -5 -3
output
NO
input
3
3 -1 7
-5 2 -4
2 -1 -3
output
YES

Solution:
'''A BODY IS IN EQUILIBRIUM IS SUMMATION OF ALL X,Y,Z COORDINATES IS EQUAL TO 0'''
n=int(input())
x,y,z=0,0,0
Sumx,Sumy,Sumz=0,0,0
for i in range(0,n):
    x, y, z = input().split()
    x, y ,z=[int(x),int(y),int(z)]
    Sumx, Sumy ,Sumz=Sumx+x,Sumy+y,Sumz+z
if(Sumx==Sumy==Sumz==0):
    print('YES')
else:
    print('NO')

Problem 12
Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.

Input
The single line contains an integer n (1≤n≤1000) — the number that needs to be checked.

Output
In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).

Examples
input
47
output
YES
input
16
output
YES
input
78
output
NO

SOLUTION:
'''THE NUMBER TO BE ENTERED IS LESS THAN EQUAL TO 1000. THEREFORE, ALL POSSIBLE FACTORS OF NUMBER FROM LUCK 
NUMBERS 4 AND 7 ARE 4 , 7,47,477 AND 74. '''
num=input()
LuckyNum=['4','7']
flag=True
for i in num:
    if i not in LuckyNum:
        flag=False
if (flag==False) and (int(num)%7==0 or int(num)%4==0 or int(num)%47==0 or int(num)%74==0 or int(num)%477==0):
    print('YES')
elif flag==True:
    print('YES')
else:
    print('NO')

Problem 13
An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

Input
The first line of the input contains an integer x (1≤x≤1000000) — The coordinate of the friend's house.

Output
Print the minimum number of steps that elephant needs to make to get from point 0 to point x.

Examples
input
5
output
1
input
12
output
3

SOLUTION:
FriendsHouse=int(input())
steps=0
if FriendsHouse<=5:
    print('1')

elif FriendsHouse>5:
    if FriendsHouse%5==0:
        steps=int(FriendsHouse/5)
        print(steps)
    else:
        temp_1=int(FriendsHouse/5)
        smaller_steps=1 #since temp_1 contain the max number of steps that can be moved by 5. Now the next step is <5, and can be covered in 1 more step:
        steps=temp_1+smaller_steps
        print(steps)

Problem 14
You've got a 5×5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

1)Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1≤i<5).
2)Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1≤j<5).
You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers: the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.

Output
Print a single integer — the minimum number of moves needed to make the matrix beautiful.

Examples
input
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
output
3
input
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
output
1


SOLUTION:
#include <iostream>
#include <cmath>
#define Xopt 2
#define Yopt 2          //optimal position of the '1'
using namespace std;

int main()
{
    bool matrix[5][5];
    int Xvalue=0, Yvalue=0;     //The current position of '1'

    for(int i = 0; i < 5; i++){     //Fill In The Matrix
        for(int j = 0; j < 5; j++){
            cin>>matrix[i][j];
            if(matrix[i][j] == 1){
                Xvalue = i;
                Yvalue = j;
            }
        }
        cout<<endl;
    }

    int moves = abs(Xvalue - Xopt) + abs(Yvalue - Yopt);\\manhattans formula
    cout<<moves;

    return 0;
}

Problem 15
Those days, many boys use beautiful girls' photos as avatars in forums. So it is pretty hard to tell the gender of a user at the first glance. Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man! Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).

Examples
input
wjmzbmr
output
CHAT WITH HER!
input
xiaodao
output
IGNORE HIM!
input
sevenkplus
output
CHAT WITH HER!




Solution:
name=input()
length=len(name)
distinct_characters=list()
count=0

for i in range(0,length):
    count=0
    for j in range(length-1,i,-1):
        if name[i]==name[j]:
            count+=1
    if count==0:
        distinct_characters.append(name[i])
if (len(distinct_characters))%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
	
Problem 16
Little Vasya loves orange juice very much. That's why any food and drink in his kitchen necessarily contains orange juice. There are n drinks in his fridge, the volume fraction of orange juice in the i-th drink equals pi percent.

One day Vasya decided to make himself an orange cocktail. He took equal proportions of each of the n drinks and mixed them. Then he wondered, how much orange juice the cocktail has.

Find the volume fraction of orange juice in the final drink.

Input
The first input line contains a single integer n (1≤n≤100) — the number of orange-containing drinks in Vasya's fridge. The second line contains n integers pi (0 ≤ pi ≤ 100) — the volume fraction of orange juice in the i-th drink, in percent. The numbers are separated by a space.

Output
Print the volume fraction in percent of orange juice in Vasya's cocktail. The answer will be considered correct if the absolute or relative error does not exceed 10  - 4.

Examples
input
3
50 50 100
output
66.666666666667
input
4
0 25 50 75
output
37.500000000000





SOLUTION:
#include<iostream>
#include<cmath>

using namespace std;
int main()
{
	int n=0;
	long double vol_frac=0,ans=0,t_vol_frac=0;
	cin>>n;
	for (int i=0 ; i<n;i++)
	{
		cin>>vol_frac;
		t_vol_frac=t_vol_frac+vol_frac;
		
	}
	ans=t_vol_frac/n;
	cout<<ans;	
}

Problem 17
One way to create a task is to learn from math. You can generate some random math statement or modify some theorems to get something new and build a new task from that.

For example, there is a statement called the "Goldbach's conjecture". It says: "each even number no less than four can be expressed as the sum of two primes". Let's modify it. How about a statement like that: "each integer no less than 12 can be expressed as the sum of two composite numbers." Not like the Goldbach's conjecture, I can prove this theorem.

You are given an integer n no less than 12, express it as a sum of two composite numbers.

Input
The only line contains an integer n (12≤n≤10^6).

Output
Output two composite integers x and y (1<x,y<n) such that x+y=n. If there are multiple solutions, you can output any of them.

Examples
input
12
output
4 8
input
15
output
6 9
input
23
output
8 15
input
1000000
output
500000 500000

SOLUTION:
def findNums(n):

            # If n is even
    if (n % 2 == 0):
        print("4 ", (n - 4), end=" ")

        # If n is odd
    else:
        print("9 ", n - 9, end=" ")

    # Driver code
n=int(input())

findNums(n)

Problem 18
Alice guesses the strings that Bob made for her.

At first, Bob came up with the secret string a consisting of lowercase English letters. The string a has a length of 2 or more characters. Then, from string a he builds a new string b and offers Alice the string b so that she can guess the string a.

Bob builds b from a as follows: he writes all the substrings of length 2 of the string a in the order from left to right, and then joins them in the same order into the string b.

For example, if Bob came up with the string a="abac", then all the substrings of length 2 of the string a are: "ab", "ba", "ac". Therefore, the string b="abbaac".

You are given the string b. Help Alice to guess the string a that Bob came up with. It is guaranteed that b was built according to the algorithm given above. It can be proved that the answer to the problem is unique.

Input
The first line contains a single positive integer t (1≤t≤1000) — the number of test cases in the test. Then t test cases follow.

Each test case consists of one line in which the string b is written, consisting of lowercase English letters (2≤|b|≤100) — the string Bob came up with, where |b| is the length of the string b. It is guaranteed that b was built according to the algorithm given above.

Output
Output t answers to test cases. Each answer is the secret string a, consisting of lowercase English letters, that Bob came up with.

Example
input
4
abbaac
ac
bccddaaf
zzzzzzzzzz
output
abac
ac
bcdaf
zzzzzz

SOLUTION:
test_cases=int(input())

for i in range(0,test_cases):
    '''' Observe that first two substrings are always included
         in string a and all other substrings at odd positions
         are also included in string a       '''
    strb=input()
    stra=strb[0]+strb[1]

    for j in range(3,len(strb)):
        if (j%2==0):
            continue
        else:
            stra=stra+strb[j]
    print(stra)
