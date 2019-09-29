# OOAD-Project2

## Ben Zaeske

### Assumptions

1. As in the first assignment, I made a few assumptions on what animals eat, and what kinds of noises they make. 

2. I also assumed that all animals of the same type would most likely have the same eating behavior, and therefore the constructor of each animal subclass sets the eating behavior for that class. This can optionally be changed at runtime however. (See documentation note 2 for more info)

### Documentation Notes

1. I used a few websites to help me learn how to do object oriented programming in python, and to give me some examples of the Strategy and Observer pattern in python. I listed these websites at the top of the files which defined these classes, not at the top of every file which uses them.
- References for general object oriented python at the top of 'Animal.py'
- References for Observer pattern in python at the top of 'Observer.py'
- References for Strategy pattern in python at the top of 'EatBehavior.py'

2. For the strategy pattern portion of this assignment, I implemented an EatBehavior class. All animals are composed of an eatBehavior which contains the eat() method. This can be dynamically changed at runtime. See 'EatBehavior.py' and 'Animal.py'. Specific eating behaviors for each animal are set at the subclass level.

3. For the observer pattern portion of this assignment I defined all related methods within 'Observer.py' which contains the ZookeeperAnnouncer class, and 'Zookeeper.py'

4. The 'main' method of the program is located in 'Zoo.py' as in the first assignment.

