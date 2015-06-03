from math import sqrt

# Sample user ratings data
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,'The Night Listener': 4.5, 'Superman Returns': 4.0,'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

### Euclidean Distance Score
def similar_ED(data,person_1,person_2):
	''' Euclidean distance : Add up the squares of all the differences '''
	score = 0
	for item in data[person_1]:
		if item in data[person_2]:
			dist = (data[person_1][item]-data[person_2][item])
			score = score + pow (dist, 2)
	# normalize to returns a value between 0 and 1,
	return 1/(1+score)

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

def transform_data(data):
	result={}
	for person in data:
		for item in data[person]:
			result.setdefault(item,{})
			# Flip item and person
			result[item][person]=data[person][item]
	return result


### Return top matches
def similar_items_score(data,person,n=5,similarity=similar_PC):
	scores=[(similarity(data,person,other),other)for other in data if other!=person]
	scores.sort( )
	scores.reverse( )
	return scores[0:n]

movies = transform_data(critics)
print similar_items_score(movies,'Superman Returns')

