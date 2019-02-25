dc1={0:'zero',1:'one',2:'two'}
dc1.update({3:'threeNew'})
print(dc1)

'''for i in dc1:
	print(dc1[i])'''

'''
d1= {1:40,2:70,3:60}
d2= {1:30,2:74,3:65}
d3= {1:20,2:50,3:89}
dic ={"ryna":d1,'sunita':d2,'zeba':d3} 
for i in dic:
	print('name\n',i)
	print('Subject(keys)',' ','Marks')
	for j in dic[i]:

		print(j,'\t',dic[i][j])
'''

my = {'a':(4,3),'b':(1,2),'c':(5,1)}
max_x=0
max_y=0
for i in my:
	#print(my[i])
	if max_x<=my[i][0]:
		max_x=my[i][0]
	if max_y<=my[i][1]:
		max_y=my[i][1]
print(max_x,max_y)


dic1={"1":[1,2],(3,4):[3,4]}
#dic2={([1],[2]):[1,2],([3],[4]):[3,4]}
print(dic1.keys())
#print(list(dic1.values())[0])
#print(dic2)
