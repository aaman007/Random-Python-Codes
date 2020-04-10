import convertersModule
from convertersModule import lbs_to_kg  # we can now directly call the method lbs_to_kg()
from convertersModule import kg_to_lbs
import utillsModule
from utillsModule import find_max


# Usage of convertersModule [ converters is a better name for Module ]
print(convertersModule.kg_to_lbs(56))
print(kg_to_lbs(56))

print(convertersModule.lbs_to_kg(124))
print(lbs_to_kg(124))

# Usage of utillsModule
numbers = [5,3,7,3,10,20,13,19]
print(utillsModule.find_max(numbers))
print(find_max(numbers))

