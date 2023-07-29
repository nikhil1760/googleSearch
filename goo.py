import googlesearch 
query=input("what do you want to search ")
for i in googlesearch.search(query,num=5,stop=5):
	print(i)
