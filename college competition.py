"""
#College competition 
A group of students selected for a competition, their rollnos and names given and 
the student roll numbers are also given who completed the assignment successfully(Won competition). 
Now you need to Display the names of the students those who did not complete the assignment(not won).

Input=

Group of selected students for the competition (n=4 -- Number of students selected)
+--------+--------+
| RollNo | S_Name |
+--------+--------+
| 1      | Joe    |
| 2      | Henry  |
| 3      | Sam    |
| 4      | Max    |
+--------+--------+

Roll numbers of student those who WON the competition(m=2 -- number of students won)
+------------+
| RollNo     |
+------------+
| 3          |
| 1          |
+------------+


Output= 
+-----------+
| S_Name    |
+-----------+
| Henry     |
| Max       |
+-----------+




Input
4    ----  (Number of students selected)   
1 Joe
2 Henry
3 Sam
4 Max
2     ----  (Number of students won)
3
1
Output=
Henry
Max
-------------------------
Input=
5
1001 Declan
1002 Stefan
1003 John
1004 Mahesh
1005 Gopal
4
1003
1005
1001
1004
Output=
Stefan
""" 
n=int(input()) #Number of students in the group
students=[]
for i in range(n):
    students.append(input().split())
m=int(input()) #Number of students those who won
wonStdRolls=[]
for j in range(m):
    wonStdRolls.append(input())
for lst in students:
    if lst[0] not in wonStdRolls:
        print(lst[1])
        
