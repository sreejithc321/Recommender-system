from math import sqrt

# Sample user ratings data
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,'The Night Listener': 4.5, 'Superman Returns': 4.0,'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


### Pearson Correlation Score
def similar_PC(data,person_1,person_2):
	''' Pearson Correlation : give better results in situations where the data isn't well normalized'''
	common={}
	for item in data[person_1]:
		if item in data[person_2]: 
			common[item]=1
			
	n=len(common)
	if n==0: return 0
	per1_sum=sum([data[person_1][item] for item in common])
	per2_sum=sum([data[person_2][item] for item in common])
	per1_sum_sqr=sum([pow(data[person_1][item],2) for item in common])
	per2_sum_sqr=sum([pow(data[person_2][item],2) for item in common])

	prod_sum=sum([data[person_1][item]*data[person_2][item] for item in common])

	num=prod_sum-(per1_sum*per2_sum/n)
	den=sqrt((per1_sum_sqr-pow(per1_sum,2)/n)*(per2_sum_sqr-pow(per2_sum,2)/n))
	if den==0: return 0
	r=num/den
	return r

# Return recommendations for user
def return_recommendations(data,person,similarity=similar_PC):
	totals={}
	sum_of_sim={}
	for users in data:
		if users==person: continue
		sim=similarity(data,person,users)
		if sim<=0: continue
		for item in data[users]:
			# find out items to recomend
			if item not in data[person] or data[person][item]==0:
				# similarity * Score
				totals.setdefault(item,0)
				totals[item]+=data[users][item]*sim
				# sum of similarities
				sum_of_sim.setdefault(item,0)
				sum_of_sim[item]+=sim
	# normalize list
	rankings=[(total/sum_of_sim[item],item) for item,total in totals.items( )]
	# reverse sort list
	rankings.sort()
	rankings.reverse()
	return rankings 

print return_recommendations(critics,'Toby')
