# 7.3-Nested-Lists

### update_list(list, list_index, item_index, item)
This function updates a shopping list. It takes in an index value for the shopping list the user wants to update, which position it should update, and the new value to update. Does not alter the length of the list. The updated list is updated.

Example:

*Function call:*
```python 
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]

update_list(shopping_cart, 1, 1, "peppers")
```
*Output:*
```python
[['tooth paste', 'q-tips', 'milk'],['milk', 'peppers', 'apples'],['planner', 'pencils', 'q-tips']]
```
<br></br>
### view_list(list, list_index)
This function returns the shopping list the user wants and returns all of the items associated with that shopping list.

Example:

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]

view_list(shopping_cart,0) 
```
*Output:*
```python
['tooth paste', 'q-tips', 'milk']
```

<br></br>
### view_item(list, list_index, item_index)
The functions returns the item stored a particular location within a list. The function takes in a shopping list the item is on and which position it occupies, then returns the items name.

Example:

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
view_item(shopping_cart,2,0) 
```
*Output:8
```python
planner
```
<br></br>

### all_in_one(list)
This function will put all the shopping lists into a single list using a for loop. It will then return the list.

Example:

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]

all_in_one(shopping_cart) 
```
*Output:*
```python
['tooth paste', 'q-tips', 'milk', 'milk', 'candy', 'apples','planner', 'pencils', 'q-tips']
```
<br></br>
### count_item(list, item)
Create a function, count_item(), which will go through all items of the list and keep a count of how many times the item occurs. 

Example:

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]

count_item(shopping_cart, "milk") 
```
*Output:*
```python
2
```
<br></br>
### drink_more_milk(list)
In order to make the shopping lists more calcium rich, write a function, drink_more_milk, that adds 'milk' to each of the lists (unless it's already there). Return new list

Example:

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]

drink_more_milk(shopping_cart) 
```
*Output:*
```python
[['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips', 'milk']]
```
<br></br>
### if_you_give_a_moose_a_cookie(list)
You can't have milk without cookies. Write a function if_you_give_a_moose_a_cookie, that will go through every element of shopping_cart and update 'milk' to be 'milk and cookies'. Return new list.

Example:

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]

if_you_give_a_moose_a_cookie(shopping_cart) 
```
*Output:*
```python
[['tooth paste', 'q-tips', 'milk and cookies'],['milk and cookies', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
```
<br></br>
### reverse_lists_and_items(list)
Write a function to reverse the order of the lists and items in the list. The function return the reversed list with reversed items. Return new list.

Example:

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
reverse_lists_and_items(shopping_cart):
```
*Output:*
```python
[['q-tips','pencil','planner'],['apples','candy','milk'],['milk','q-tips','tooth paste']]
```
