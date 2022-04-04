def cloning(lst1):
	nw_list=[]
	nw_list=list(lst1)
	return nw_list
lst1=[12,2,3,4,5,67,8,90,2]
lst2=cloning(lst1)
print"cloning list: "+str(lst2)
for ele in lst2:
	if ele % 2!=0:
		print ele
	cnt=0
	elif ele==2:
		cnt=+1
		print cnt
