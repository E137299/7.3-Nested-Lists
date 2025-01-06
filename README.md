# 7.3-Nested-Lists

---

### **Objective:** Update a specific item in a nested shopping list.

**Function: `update_list(list, list_index, item_index, item)`**  
This function updates an item at a given position in a specific shopping list (within a nested list). It does not alter the length of the list, only the item at the specified index.

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
update_list(shopping_cart, 1, 1, "peppers")
```
*Output:*
```python
[['tooth paste', 'q-tips', 'milk'],['milk', 'peppers', 'apples'],['planner', 'pencils', 'q-tips']]
```

---

### **Objective:** View all items in a specific shopping list within a nested list.

**Function: `view_list(list, list_index)`**  
This function retrieves and returns all the items in a specific shopping list from a nested list of shopping lists.

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
view_list(shopping_cart, 0)
```
*Output:*
```python
['tooth paste', 'q-tips', 'milk']
```

---

### **Objective:** Access a specific item in a shopping list at a given index.

**Function: `view_item(list, list_index, item_index)`**  
This function accesses and returns an item from a specific position within a specific shopping list in a nested list.

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
view_item(shopping_cart, 2, 0)
```
*Output:*
```python
'planner'
```

---

### **Objective:** Combine all items from nested shopping lists into a single list.

**Function: `all_in_one(list)`**  
This function flattens a nested list by combining all individual shopping lists into one list.

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
all_in_one(shopping_cart)
```
*Output:*
```python
['tooth paste', 'q-tips', 'milk', 'milk', 'candy', 'apples', 'planner', 'pencils', 'q-tips']
```

---

### **Objective:** Count the occurrences of a specific item across all shopping lists.

**Function: `count_item(list, item)`**  
This function counts how many times a specific item appears across all shopping lists in the nested list.

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
count_item(shopping_cart, "milk")
```
*Output:*
```python
2
```

---

### **Objective:** Add "milk" to every shopping list if it's not already present.

**Function: `drink_more_milk(list)`**  
This function ensures that "milk" is added to each shopping list in the nested list, unless it's already there.

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
drink_more_milk(shopping_cart)
```
*Output:*
```python
[['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips', 'milk']]
```

---

### **Objective:** Modify "milk" to "milk and cookies" in all lists.

**Function: `if_you_give_a_moose_a_cookie(list)`**  
This function updates every occurrence of "milk" in the shopping lists to "milk and cookies."

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
if_you_give_a_moose_a_cookie(shopping_cart)
```
*Output:*
```python
[['tooth paste', 'q-tips', 'milk and cookies'],['milk and cookies', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
```

---

### **Objective:** Reverse the order of both the lists and the items within them.

**Function: `reverse_lists_and_items(list)`**  
This function reverses the order of the shopping lists, as well as the order of items within each shopping list.

**Example:**

*Function call:*
```python
shopping_cart = [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
reverse_lists_and_items(shopping_cart)
```
*Output:*
```python
[['q-tips', 'pencils', 'planner'], ['apples', 'candy', 'milk'], ['milk', 'q-tips', 'tooth paste']]
```

--- 

These objectives clarify the function and expected outcome for each challenge.
