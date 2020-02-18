# import random
# import pytest

# import src.algorithms_and_data_structures.array_search as array_search
# AS = array_search.ArraySearch()


# def test_binary_search():
#         pass

# def test_quickselect():
#         arr1 = [1,2,3,4,5,6,7,8]
#         arr2 = [-1,0]
#         arr3 = [100.5]
#         arr4 = []
#         arr5 = ["F"]
#         arr6 = [5, "G"]
#         arr7 = sorted(random.sample(range(100**2), 100))
#         k1, k2, k3, k4, k5 = 0, 1, 100, -1, "Y"

#         assert AS.quickselect(arr1, k1) == 1
#         assert AS.quickselect(arr1, k2) == 2
#         with pytest.raises(ValueError):
#                 AS.quickselect(arr1, k3)
#         with pytest.raises(ValueError):
#                 AS.quickselect(arr1, k4)
#         with pytest.raises(ValueError):
#                 AS.quickselect(arr1, k5)

#         assert AS.quickselect(arr2, k1) == -1
#         assert AS.quickselect(arr3, k1) == 100.5
#         with pytest.raises(ValueError):
#                 AS.quickselect(arr4, k1)
#         with pytest.raises(TypeError):
#                 AS.quickselect(arr5, k1)
#         with pytest.raises(TypeError):
#                 AS.quickselect(arr6, k1)
#         assert AS.quickselect(arr7, k1) == min(arr7)
