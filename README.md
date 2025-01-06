# 7.1 Nested Lists

---

### View all items in a specific shopping list within a nested list.

**Function: `view_list(list, list_index)`**  
This function retrieves and returns all the items in a specific shopping list from a nested list of shopping lists.

**Example:**

*Function call:*
```python
meals = [
    ['chicken', 'rice', 'broccoli', 'garlic', 'olive oil'],
    ['spaghetti', 'tomato sauce', 'meatballs', 'parmesan cheese', 'olive oil'],
    ['salmon', 'potatoes', 'asparagus', 'lemon', 'butter'],
    ['tofu', 'quinoa', 'spinach', 'peppers', 'soy sauce', 'garlic', 'olive oil']
]
view_list(meals, 0)
```
*Output:*
```python
['chicken', 'rice', 'broccoli', 'garlic', 'olive oil']
```

---

### Access a specific item in a shopping list at a given index.

**Function: `view_item(list, list_index, item_index)`**  
This function accesses and returns an item from a specific position within a specific shopping list in a nested list.

**Example:**

*Function call:*
```python
meals = [
    ['chicken', 'rice', 'broccoli', 'garlic', 'olive oil'],
    ['spaghetti', 'tomato sauce', 'meatballs', 'parmesan cheese', 'olive oil'],
    ['salmon', 'potatoes', 'asparagus', 'lemon', 'butter'],
    ['tofu', 'quinoa', 'spinach', 'peppers', 'soy sauce', 'garlic', 'olive oil']
]
view_item(meals, 2, 0)
```
*Output:*
```python
'salmon'
```

---
### Update a specific item in a nested shopping list.

**Function: `update_list(list, list_index, item_index, item)`**  
This function updates an item at a given position in a specific shopping list (within a nested list). It does not alter the length of the list, only the item at the specified index.

**Example:**

*Function call:*
```python
meals = [
    ['chicken', 'rice', 'broccoli', 'garlic', 'olive oil'],
    ['spaghetti', 'tomato sauce', 'meatballs', 'parmesan cheese', 'olive oil'],
    ['salmon', 'potatoes', 'asparagus', 'lemon', 'butter'],
    ['tofu', 'quinoa', 'spinach', 'peppers', 'soy sauce', 'garlic', 'olive oil']
]
update_list(meals, 2, 2, "peppers")
```
*Output:*
```python
[['chicken', 'rice', 'broccoli', 'garlic', 'olive oil'], ['spaghetti', 'tomato sauce', 'meatballs', 'parmesan cheese', 'olive oil'],['salmon', 'potatoes', 'peppers', 'lemon', 'butter'], ['tofu', 'quinoa', 'spinach', 'peppers', 'soy sauce', 'garlic', 'olive oil']]
```

---
### Combine all items from nested shopping lists into a single list with no duplicate items.

**Function: `all_in_one(list)`**  
This function combines all items from multiple nested shopping lists into a single list, removing any duplicate items.

**Example:**

*Function call:*
```python
meals = [
    ['chicken', 'rice', 'broccoli', 'garlic', 'olive oil'],
    ['spaghetti', 'tomato sauce', 'meatballs', 'parmesan cheese', 'olive oil'],
    ['salmon', 'potatoes', 'asparagus', 'lemon', 'butter'],
    ['tofu', 'quinoa', 'spinach', 'peppers', 'soy sauce', 'garlic', 'olive oil']
]
all_in_one(meals)
```

*Output:*
```python
['chicken', 'rice', 'broccoli', 'garlic', 'olive oil', 'spaghetti', 'tomato sauce', 'meatballs', 'parmesan cheese', 'salmon', 'potatoes', 'asparagus', 'lemon', 'butter', 'tofu', 'quinoa', 'spinach', 'peppers', 'soy sauce']
```

---

### Count the occurrences of a specific item across all shopping lists.

**Function: `count_item(list, item)`**  
This function counts how many times a specific item appears across all shopping lists in the nested list.

**Example:**

*Function call:*
```python
meals = [
    ['chicken', 'rice', 'broccoli', 'garlic', 'olive oil'],
    ['spaghetti', 'tomato sauce', 'meatballs', 'parmesan cheese', 'olive oil'],
    ['salmon', 'potatoes', 'asparagus', 'lemon', 'butter'],
    ['tofu', 'quinoa', 'spinach', 'peppers', 'soy sauce', 'garlic', 'olive oil']
]
count_item(shopping_cart, "olive oil")
```
*Output:*
```python
3
```

---

### Add "milk" to every shopping list if it's not already present.

**Function: `drink_more_milk(list)`**  
This function ensures that "milk" is added to each shopping list in the nested list, unless it's already there.

**Example:**

*Function call:*
```python
meal_plan = [
    ['eggs', 'toast', 'orange juice'],
    ['pancakes', 'bacon', 'milk', 'syrup'],
    ['salad', 'chicken', 'bread'],
    ['cereal', 'milk', 'banana']
]
drink_more_milk(meal_plan)
```
*Output:*
```python
[['eggs', 'toast', 'orange juice', 'milk'],['pancakes', 'bacon', 'milk', 'syrup'],['salad', 'chicken', 'bread', 'milk'],['cereal', 'milk', 'banana']]
```

---

### Modify "milk" to "milk and cookies" in all lists.

**Function: `add_a_cookie(list)`**  
This function updates every occurrence of "milk" in the shopping lists to "milk and cookies."

**Example:**

*Function call:*
```python
meal_plan = [
    ['eggs', 'toast', 'orange juice'],
    ['pancakes', 'bacon', 'milk', 'syrup'],
    ['salad', 'chicken', 'bread'],
    ['cereal', 'milk', 'banana']
]
add_a_cookie(meal_plan)
```
*Output:*
```python
[['eggs', 'toast', 'orange juice'],['pancakes', 'bacon', 'milk and cookies', 'syrup'],['salad', 'chicken', 'bread'],['cereal', 'milk and cookies', 'banana']]
```

---

### Reverse the order of both the lists and the items within them.

**Function: `reverse_lists_and_items(list)`**  
This function reverses the order of the shopping lists, as well as the order of items within each shopping list.

**Example:**

*Function call:*
```python
meal_plan = [
    ['eggs', 'toast', 'orange juice'],
    ['pancakes', 'bacon', 'milk', 'syrup'],
    ['salad', 'chicken', 'bread'],
    ['cereal', 'milk', 'banana']
]
reverse_lists_and_items(meal_plan)
```
*Output:*
```python
[['banana', 'milk', 'cereal'], ['bread', 'chicken', 'salad'], ['syrup', 'milk', 'bacon', 'pancakes'],['orange juice', 'toast', 'eggs']
```
