# Find string from given list

### Requirement:
* Python
#### Folder Structure:
    --src
      --__init__.py
      --filter.py
    --tests
      --__init__.py
      --test_filter.py
      --test_finder.py
    --run.py
    --test.py
#### Step-1 (Coding task)
1. git clone "https://github.com/sbsanjaybharti/find_string_char_in_list.git"
2. Assuming that python is already install in the system
3. Open the terminal run the command "python run.py" for check the result
4. on the same terminal run command "python test.py" for unit test result 

#### Step-2 (System Design)
1. Available in system_design folder in 2 format
2. PNG image
3. drawio format which can open in http://draw.io application which is free online service 

#### Description:
1. Design pattern:
    a. Creational: Singleton, Factory design pattern
    b. Structural: Decorator
    c. Behaviral: Chain of responsibility design pattern

##### Feature:
1. Converting string in to group of string length

    For e.g. string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm', 'stdo']
    after grouping: 
  ```json
    {
      "3": ["asd", "fre", "glk", "lkm", "stdo"],
      "4": ["asdd", "stdo"]
    }
 ```
 So that we cam minimize the number of iteration.
 Its time complexity will be:
Minimum time complexity is 
```
    T = O(n) + O(1)
    T= O(n)
    Note: when One value in list
```
Average time complexity is
```
    T = O(n) + O(log n)
    T = O(n)
    Note: n number of list with different length of string 
```
Maximum time complexity is
```
    T = O(n) + O(n)
    T = O(n)
    Note: when n number of list with same length of all string
```

2. Same finding can be done in O(n) max execution time also but in that case if object created  single time and multiple time finding the string it will slowdown the process
