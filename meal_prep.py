import random

print("""
    1 - Breakfast
    2 - Lunch
    3 - Dinner 
    4 - Snack
    """)

prep = input("What is your meal: ")

if prep == '1': 
    breakfast_options = [
        "Continental Breakfast", "American Breakfast", "English Breakfast",
        "Cereal", "Smoothies", "Oatmeal", "Breakfast Burritos/Wraps",
        "Yogurt Parfait", "Avocado Toast", "Pastries and Coffee"
    ]
    for index, option in enumerate(breakfast_options, start=1):
        print(f"{index} - {option}") 

    choice = input("What type of breakfast do you want: ")

    if choice.isdigit() and 1 <= int(choice) <= len(breakfast_options):
        choice = int(choice)
        if choice == 1:
            print("""
            Continental Breakfast
            Ingredients: 
            - Croissants, bread or toast, butter, jam, fresh fruit (like berries or sliced oranges), coffee or tea.

            Instructions:
            1. Toast the bread or heat the croissants until warm and slightly crispy.
            2. Serve with butter and a selection of jams or preserves.
            3. Prepare a pot of coffee or tea.
            4. Arrange fresh fruit on a plate and enjoy with your pastries.
            """)
        elif choice == 2:
            print("""
            American Breakfast
            Ingredients: 
            - Eggs, bacon or sausage, bread, butter, hash browns, pancakes or waffles, syrup.

            Instructions:
            1. Eggs: Cook the eggs as you prefer (scrambled, fried, or poached).
            2. Bacon/Sausage: Cook bacon or sausage in a skillet over medium heat until crispy and fully cooked.
            3. Hash Browns: Grate potatoes, then cook them in a skillet with oil until golden and crispy.
            4. Pancakes/Waffles: Prepare pancake or waffle batter and cook according to package or recipe instructions. Serve with butter and syrup.
            5. Serve everything together with toast or pancakes.
            """)
        elif choice == 3:
            print("""
            English Breakfast
            Ingredients: 
            - Eggs, bacon, sausages, baked beans, tomatoes, mushrooms, black pudding (optional), bread, butter, tea or coffee.

            Instructions:
            1. Eggs: Fry or poach the eggs.
            2. Bacon & Sausages: Fry or grill the bacon and sausages until cooked.
            3. Baked Beans: Heat the baked beans in a small saucepan.
            4. Tomatoes & Mushrooms: Slice tomatoes and mushrooms, then grill or sauté them until soft.
            5. Black Pudding: If using, fry slices of black pudding.
            6. Serve with buttered toast and a cup of tea or coffee.
            """)
        elif choice == 4:
            print("""
            Cereal
            Ingredients: 
            - Your favorite cereal, milk, optional fruits (like bananas, berries).

            Instructions:
            1. Pour cereal into a bowl.
            2. Add milk.
            3. Top with fresh fruit if desired.
            """)
        elif choice == 5:
            print("""
            Smoothies
            Ingredients: 
            - Fruits (like bananas, berries, mango), yogurt or milk, optional spinach or protein powder.

            Instructions:
            1. Add all the ingredients to a blender.
            2. Blend until smooth.
            3. Pour into a glass and enjoy immediately.
            """)
        elif choice == 6:
            print("""
            Oatmeal
            Ingredients: 
            - Oats, milk or water, optional toppings (fruits, nuts, honey).

            Instructions:
            1. Bring milk or water to a boil.
            2. Add oats and reduce heat to simmer.
            3. Cook until the oats are soft and the mixture has thickened.
            4. Top with fruits, nuts, and a drizzle of honey.
            """)
        elif choice == 7:
            print("""
            Breakfast Burritos/Wraps
            Ingredients: 
            - Eggs, cheese, cooked meat (bacon, sausage), tortillas, optional vegetables (peppers, onions).

            Instructions:
            1. Scramble the eggs in a skillet.
            2. Warm the tortillas in a pan.
            3. Layer eggs, cheese, and meat onto the tortillas.
            4. Add any vegetables you like.
            5. Roll up the tortilla into a burrito.
            6. Serve with salsa or hot sauce if desired.
            """)
        elif choice == 8:
            print("""
            Yogurt Parfait
            Ingredients: 
            - Yogurt, granola, fresh fruits (like berries or sliced bananas), honey.

            Instructions:
            1. Layer yogurt, granola, and fruit in a glass or bowl.
            2. Drizzle with honey.
            3. Repeat the layers until the glass is full.
            4. Serve immediately.
            """)
        elif choice == 9:
            print("""
            Avocado Toast
            Ingredients: 
            - Ripe avocado, bread, salt, pepper, optional toppings (poached egg, tomatoes, chili flakes).

            Instructions:
            1. Toast the bread.
            2. Mash the avocado with a fork and spread it on the toast.
            3. Season with salt and pepper.
            4. Add any additional toppings like a poached egg or sliced tomatoes.
            5. Serve immediately.
            """)
        elif choice == 10:
            print("""
            Pastries and Coffee
            Ingredients: 
            - Pastry (like a croissant or Danish), coffee.

            Instructions:
            1. Warm the pastry in the oven if desired.
            2. Brew a cup of coffee.
            3. Serve the pastry with your coffee.
            """)
    else:
        print("Invalid choice. Please choose a valid breakfast option.")

elif prep == '2':
    lunch_options = [
        "BLT Sandwich", "Grilled Cheese", "Caesar Salad", "Greek Salad", 
        "Margherita Pizza", "Spaghetti Bolognese", "Fettuccine Alfredo", 
        "Cheeseburger", "Veggie Burger", "Chicken Caesar Wrap", "Hummus and Veggie Wrap"
    ]
    for index, option in enumerate(lunch_options, start=1):
        print(f"{index} - {option}") 

    choice = input("What type of lunch do you want: ")

    if choice.isdigit() and 1 <= int(choice) <= len(lunch_options):
        choice = int(choice)
        if choice == 1:
            print("""
            BLT Sandwich
            Ingredients: 
            - Bread, bacon, lettuce, tomato, mayonnaise.

            Instructions:
            1. Toast two slices of bread.
            2. Spread mayonnaise on each slice.
            3. Layer cooked bacon, lettuce, and tomato slices.
            4. Close the sandwich and slice in half.
            """)
        elif choice == 2:
            print("""
            Grilled Cheese
            Ingredients: 
            - Bread, butter, cheese.

            Instructions:
            1. Butter two slices of bread on one side each.
            2. Place a slice of cheese between the bread, buttered side out.
            3. Grill in a skillet over medium heat until both sides are golden brown and the cheese is melted.
            """)
        elif choice == 3:
            print("""
            Caesar Salad
            Ingredients: 
            - Romaine lettuce, Caesar dressing, croutons, Parmesan cheese, optional grilled chicken.

            Instructions:
            1. Toss romaine lettuce with Caesar dressing.
            2. Add croutons and grated Parmesan cheese.
            3. Top with grilled chicken if desired.
            """)
        elif choice == 4:
            print("""
            Greek Salad
            Ingredients: 
            - Cucumbers, tomatoes, red onion, olives, feta cheese, olive oil, lemon juice.

            Instructions:
            1. Combine chopped cucumbers, tomatoes, red onion, and olives in a bowl.
            2. Add feta cheese and toss with olive oil and lemon juice.
            """)
        elif choice == 5:
            print("""
            Margherita Pizza
            Ingredients: 
            - Pizza dough, tomato sauce, mozzarella cheese, fresh basil leaves, olive oil.

            Instructions:
            1. Preheat the oven to 475°F (245°C).
            2. Roll out pizza dough on a floured surface.
            3. Spread tomato sauce evenly on the dough.
            4. Add slices of fresh mozzarella cheese and basil leaves.
            5. Drizzle with olive oil and bake for 10-15 minutes until the crust is golden and the cheese is bubbly.
            """)
        elif choice == 6:
            print("""
            Spaghetti Bolognese
            Ingredients: 
            - Spaghetti, ground beef, onions, garlic, marinara sauce, Parmesan cheese.

            Instructions:
            1. Cook spaghetti according to package instructions.
            2. In a separate pan, sauté onions and garlic, then add ground beef and cook until browned.
            3. Add marinara sauce and simmer for 15 minutes.
            4. Toss the cooked spaghetti with the sauce and serve with grated Parmesan.
            """)
        elif choice == 7:
            print("""
            Fettuccine Alfredo
            Ingredients: 
            - Fettuccine, butter, heavy cream, Parmesan cheese.

            Instructions:
            1. Cook fettuccine according to package instructions.
            2. In a pan, melt butter and add heavy cream.
            3. Stir in grated Parmesan cheese until the sauce thickens.
            4. Toss with the cooked fettuccine and serve.
            """)
        elif choice == 8:
            print("""
            Cheeseburger
            Ingredients: 
            - Ground beef, burger buns, cheese, lettuce, tomato, condiments.

            Instructions:
            1. Form ground beef into patties.
            2. Grill or pan-fry the patties until fully cooked.
            3. Place a slice of cheese on top of each patty to melt.
            4. Assemble the burger with the bun, lettuce, tomato, and condiments.
            """)
        elif choice == 9:
            print("""
            Veggie Burger
            Ingredients: 
            - Veggie patty, burger buns, toppings, condiments.

            Instructions:
            1. Cook veggie patties according to package instructions or your recipe.
            2. Assemble the burger with your choice of toppings and condiments.
            """)
        elif choice == 10:
            print("""
            Chicken Caesar Wrap
            Ingredients: 
            - Tortilla, grilled chicken, chopped romaine lettuce, Caesar dressing, Parmesan cheese, croutons.

            Instructions:
            1. Fill a tortilla with grilled chicken, chopped romaine lettuce, and Caesar dressing.
            2. Add grated Parmesan cheese and croutons.
            3. Roll up the tortilla and slice in half.
            """)
        elif choice == 11:
            print("""
            Hummus and Veggie Wrap
            Ingredients: 
            - Tortilla, hummus, sliced cucumbers, tomatoes, bell peppers, spinach.

            Instructions:
            1. Spread hummus on a tortilla.
            2. Add sliced cucumbers, tomatoes, bell peppers, and spinach.
            3. Roll up the tortilla and enjoy.
            """)
    else:
        print("Invalid choice. Please choose a valid lunch option.")

elif prep == '3':
    dinner_options = [
        "Chicken Stir-Fry", "Beef Stroganoff", "Vegetarian Chili", "Lentil Soup", 
        "Grilled Salmon", "Stuffed Bell Peppers", "Chicken Parmesan", "Eggplant Parmesan",
        "Shrimp Scampi", "Chicken Tikka Masala"
    ]
    for index, option in enumerate(dinner_options, start=1):
        print(f"{index} - {option}")

    choice = input("What type of dinner do you want: ")

    if choice.isdigit() and 1 <= int(choice) <= len(dinner_options):
        choice = int(choice)
        if choice == 1:
            print("""
            Chicken Stir-Fry
            Ingredients: 
            - Chicken breast, vegetables (e.g., bell peppers, broccoli, snap peas), soy sauce, garlic, ginger, rice.

            Instructions:
            1. Slice chicken breast into thin strips.
            2. Stir-fry chicken in a hot pan with garlic and ginger until cooked through.
            3. Add vegetables and continue to stir-fry until tender-crisp.
            4. Add soy sauce and toss everything to coat.
            5. Serve over cooked rice.
            """)
        elif choice == 2:
            print("""
            Beef Stroganoff
            Ingredients: 
            - Beef sirloin, onions, mushrooms, beef broth, sour cream, egg noodles.

            Instructions:
            1. Sauté onions and mushrooms in a pan.
            2. Add sliced beef and cook until browned.
            3. Stir in beef broth and simmer until beef is tender.
            4. Mix in sour cream and cook until heated through.
            5. Serve over cooked egg noodles.
            """)
        elif choice == 3:
            print("""
            Vegetarian Chili
            Ingredients: 
            - Beans (e.g., kidney beans, black beans), tomatoes, bell peppers, onions, chili powder, cumin.

            Instructions:
            1. Sauté onions and bell peppers in a pot.
            2. Add beans, tomatoes, chili powder, and cumin.
            3. Simmer for at least 30 minutes to let the flavors meld.
            4. Serve hot.
            """)
        elif choice == 4:
            print("""
            Lentil Soup
            Ingredients: 
            - Lentils, carrots, celery, onions, vegetable broth, spices (e.g., thyme, bay leaf).

            Instructions:
            1. Sauté onions, carrots, and celery in a pot.
            2. Add lentils, vegetable broth, and spices.
            3. Simmer until lentils are tender.
            4. Blend if desired for a smoother texture.
            """)
        elif choice == 5:
            print("""
            Grilled Salmon
            Ingredients: 
            - Salmon fillets, lemon, olive oil, herbs (e.g., dill, parsley).

            Instructions:
            1. Brush salmon with olive oil and season with herbs and lemon.
            2. Grill over medium heat until cooked through.
            3. Serve with a side of vegetables or rice.
            """)
        elif choice == 6:
            print("""
            Stuffed Bell Peppers
            Ingredients: 
            - Bell peppers, ground beef or turkey, rice, tomato sauce, cheese.

            Instructions:
            1. Preheat oven to 375°F (190°C).
            2. Cook rice and mix with ground meat and tomato sauce.
            3. Stuff mixture into halved bell peppers.
            4. Top with cheese and bake for 30 minutes.
            """)
        elif choice == 7:
            print("""
            Chicken Parmesan
            Ingredients: 
            - Chicken breasts, breadcrumbs, marinara sauce, mozzarella cheese, Parmesan cheese.

            Instructions:
            1. Bread chicken breasts and bake or fry until cooked through.
            2. Top with marinara sauce and cheese.
            3. Bake until cheese is melted and bubbly.
            """)
        elif choice == 8:
            print("""
            Eggplant Parmesan
            Ingredients: 
            - Eggplant, marinara sauce, breadcrumbs, mozzarella cheese, Parmesan cheese.

            Instructions:
            1. Slice and bread eggplant slices.
            2. Bake until crispy.
            3. Layer eggplant slices with marinara sauce and cheese.
            4. Bake until cheese is melted and bubbly.
            """)
        elif choice == 9:
            print("""
            Shrimp Scampi
            Ingredients: 
            - Shrimp, garlic, butter, white wine, lemon juice, pasta.

            Instructions:
            1. Sauté garlic in butter.
            2. Add shrimp and cook until pink.
            3. Stir in white wine and lemon juice.
            4. Serve over cooked pasta.
            """)
        elif choice == 10:
            print("""
            Chicken Tikka Masala
            Ingredients: 
            - Chicken, yogurt, tikka masala spice blend, tomatoes, cream.

            Instructions:
            1. Marinate chicken in yogurt and spices, then grill or bake.
            2. Simmer with tomatoes and cream to make the sauce.
            3. Serve with rice or naan.
            """)
    else:
        print("Invalid choice. Please choose a valid dinner option.")

elif prep == '4':
    snack_options = [
        "Fruit Salad", "Cheese and Crackers", "Veggie Sticks with Dip", "Yogurt Parfait",
        "Popcorn", "Energy Balls", "Guacamole and Chips", "Hummus and Pita Bread"
    ]
    for index, option in enumerate(snack_options, start=1):
        print(f"{index} - {option}")

    choice = input("What type of snack do you want: ")

    if choice.isdigit() and 1 <= int(choice) <= len(snack_options):
        choice = int(choice)
        if choice == 1:
            print("""
            Fruit Salad
            Ingredients: 
            - Mixed fruits (e.g., apples, bananas, berries, grapes).

            Instructions:
            1. Chop fruits into bite-sized pieces.
            2. Toss together in a bowl.
            3. Serve immediately or chill before serving.
            """)
        elif choice == 2:
            print("""
            Cheese and Crackers
            Ingredients: 
            - Assorted cheeses, crackers.

            Instructions:
            1. Arrange cheese slices or cubes on a plate.
            2. Serve with crackers.
            """)
        elif choice == 3:
            print("""
            Veggie Sticks with Dip
            Ingredients: 
            - Carrot sticks, celery sticks, bell pepper strips, ranch or hummus dip.

            Instructions:
            1. Arrange veggie sticks on a plate.
            2. Serve with a side of dip.
            """)
        elif choice == 4:
            print("""
            Yogurt Parfait
            Ingredients: 
            - Yogurt, granola, fresh fruit (e.g., berries, bananas).

            Instructions:
            1. Layer yogurt, granola, and fruit in a glass or bowl.
            2. Repeat layers and serve.
            """)
        elif choice == 5:
            print("""
            Popcorn
            Ingredients: 
            - Popcorn kernels, butter or seasoning.

            Instructions:
            1. Pop the kernels using a popcorn maker or on the stovetop.
            2. Season with melted butter or your choice of seasoning.
            """)
        elif choice == 6:
            print("""
            Energy Balls
            Ingredients: 
            - Oats, nut butter, honey, chocolate chips or dried fruit.

            Instructions:
            1. Mix oats, nut butter, honey, and mix-ins.
            2. Roll into balls and chill.
            """)
        elif choice == 7:
            print("""
            Guacamole and Chips
            Ingredients: 
            - Avocados, lime juice, salt, tortilla chips.

            Instructions:
            1. Mash avocados and mix with lime juice and salt.
            2. Serve with tortilla chips.
            """)
        elif choice == 8:
            print("""
            Hummus and Pita Bread
            Ingredients: 
            - Hummus, pita bread.

            Instructions:
            1. Cut pita bread into triangles.
            2. Serve with hummus for dipping.
            """)
    else:
        print("Invalid choice. Please choose a valid snack option.")

else:
    print("Meal type not implemented yet.")