my_list = []

for i in (10,20,30,40):
  my_list.append(i)
print (my_list)

my_list[1] = 15
print (my_list)

my_list2 = [50,60,70]
my_list.extend(my_list2)
print (my_list)

my_list.pop(-1)
print (my_list)

my_list.sort(reverse=False)
print (my_list)

print("The index of the value 30 is: ", my_list.index(30))
  
