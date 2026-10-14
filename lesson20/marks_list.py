empty_list=[]
print(empty_list)

marks=[89,64,86,99,93,100]
print(marks)

sample_marks=[42,12,65]*2
print(sample_marks)

print("The number of marks are: ", len(marks))

print("The first digit of marks is: ", marks[0])
print("The last digit of marks is; ", marks[-1])

first_three_marks= marks[0:3]
inversed_marks=marks[::-1]
print(first_three_marks)
print(inversed_marks)


# function to check whether palindrome or not
def match_marks(match_list):
	a = len(match_list) -1
	b = 0
	while(b<a):
		if(match_list[b]!=[a]):
			return False
		b+=1
		a-=1
	return True
List=3,5,3,53
print("This is the list: ", List)
print(f"This is a palantrom True/False ? {match_marks(List)}! ")

Total=0
for i in marks:
	Total+=i
print("The total marks is: ", Total)

length=len(marks)
average=Total/length
print("The average of the list is", average)

marks.sort

print("Smallest mark is: ",marks[0])
print("Larger mark is ",marks[-1])

print("Sorted Marks:", marks)
print("Total Marks:", Total)
print("Average Marks:", average)
print("Lowest Mark:", marks[0])
print("Highest Mark:", marks[-1])

	






