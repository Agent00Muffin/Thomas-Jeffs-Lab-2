def main():

    # Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Thomas Jeffs',
        'student_id': '10226099',
        'toppings': [
            'pineapple',
            'bacon',
            'sausage'
        ],
        'movies': [
            {
                'title': 'deadpool',
                'genre': 'action'
            },
            {
                'title': 'wall-e',
                'genre': 'family'
            }
        ]
    }

    # Step 3 - Add another movie to the data structure
    new_movie ={
        'title': 'your name',
         'genre': 'romance'
     }
    about_me['movies'].insert(2, new_movie)



    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me,('pepperoni','chicken'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)

    pass

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):

    print(f'My name is {about_me["full_name"].title()}, but you can call me Sir{about_me["full_name"][1].title()}')
 


# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, new_toppings):

    about_me['toppings'].extend(new_toppings)

    for i,p in enumerate(about_me['toppings']):
        about_me['toppings'][i]= p.lower()

    about_me['toppings'].sort()

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):

    print("\nthe topping list")
    for p in about_me['toppings']:
        print (f"- {p}")


# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    print("\nI like to watch",end='')
    for i,g in enumerate(about_me['movies']):
        if i < len(about_me['movies']) - 1:
            print (f' {g["genre"]},',end='')
        else:
            print (f' {g["genre"]}')
    
    pass

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()