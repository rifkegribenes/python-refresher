grades = [77, 80, 90, 95, 100, 105, 107]
# lists are ordered and mutable
tuple_grades = (77, 80, 90, 95, 100, 105, 107)
# tuples are immutable
# lists can have values appended later
set_grades = {77, 80, 90, 95, 100, 105, 107}
# sets are unique and unordered (dup values will be removed)

grades.append(108)
grades[0] = 60
# you can append and assign to a list, but not to a tuple

set_grades.add(60)
# you can add values to a set but not assign with an index value, since sets are unordered

tuple_grades = tuple_grades + (100,)
# this is how you add values to a tuple. the value in a single tuple needs a comma after it to make it a tuple. single tuples can also be written without parentheses: "100,"

# print(sum(grades) / len(grades))

## Set operations

your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

print(your_lottery_numbers.intersection(winning_numbers)

#intersection returns another set

print(your_lottery_numbers.union(winning_numbers))

#union returns a new set that includes all values from the two sets, concatenated and filtered for unique values

print({1,2,3,4}.difference({{1,2}}))

#difference returns set of elements that exist in one set only
