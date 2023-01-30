# print("Hello World!")

#Lists in Python = other language known as Arrays

#here's our first list
#
# shopping_list = ["milk", "bread", "eggs", "bananas"]
#
# #
# # print(type(shopping_list)) #list
# # print(shopping_list[0])
# # print(shopping_list[-1]) # bananas as it starts from 1 in minuses
# #
# # # rewriting a value in our list
# #
# # shopping_list[0] = "sugar"
# # print(shopping_list)
#
# #Add to a list
# # shopping_list.append(("Vegetables"))
# # # print(shopping_list)
# # # print((len(shopping_list)))
# #
# # shopping_list.remove("bread")
# # print(len(shopping_list))
# #
# # #remove last item on list without specifiying it
# #
# # shopping_list.pop()
# # print(shopping_list)
# # shopping_list.pop()
# # print(shopping_list)
#
# # -----Mixed data types lists
#
# mixture = [1,2,3,4, "one", "two", "three"]
# print(mixture)
#
# # List slicing
#
# print(mixture[1:3]) #[2, 3.5]
# print(mixture[-2::]) # double colon should reverse the order
# print(mixture[::2]) #bounces over every other number you enter example: every 2nd index mentioned

#-----Tuples

# Exactly the same as lists, except they are immutable (un-editable)
#Tuples are useful for elements you want to make sure it doesn't change and isn't overwrited

essentials = ("bread", "butter", "milk")
print(essentials)
# essentials[0] = "jam" # will not work for Tuples