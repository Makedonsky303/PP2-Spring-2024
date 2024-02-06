def is_good_imdb(dictionary):
    if dictionary["imdb"]>5.5:
        return True
    return False

def good_sublist(lst):
    newLst = []
    for i in lst:
        if is_good_imdb(i):
            newLst.append(i)
    return newLst 

def relevant_category(lst,category):
    newLst = []
    for i in lst:
        if i["category"]==category:
            newLst.append(i)
    return newLst 

def average_imdb(lst):
    total_imdb = 0
    for i in lst:
        total_imdb += i["imdb"]
    average_imdb = total_imdb/len(lst)

    return average_imdb    


# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# №1 
# print(is_good_imdb(movies[0]))

# №2
# for i in good_sublist(movies):
#     print(i,"\n")

# №3
# for i in relevant_category(movies,"Adventure"):
#     print(i,"\n")

# №4
# print('%.3f' % average_imdb(movies))

# №5
print(average_imdb(relevant_category(movies,"Romance")))