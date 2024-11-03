# def swap_():
#     try:
#         a = int(input("Enter first num :"))
#         b = int(input("Enter second num :"))
#         print("before swapping : ", a, b)
#         a, b = b, a
#         return "after swapping : ", a, b
#     except:
#         return "you have enterted incorrect value "
#
# print(swap_())
import pandas as pd

l = [0,1,2,3,4,5,6,7,8,9]
l1 = ["a","b","c","d","e","f","g","h","i","j"]
l2 = ["A","B","C","D","E","F","G","H","I","J"]
l3 = ["aA","bB","cC","dD","eE","fF","gG","hH","iI","jJ"]

df = pd.DataFrame({
    'Column1': l,
    'Column2': l1,
    'Column3': l2,
    'Column4': l3
})

# Write DataFrame to CSV
df.to_csv('output.csv', index=False)

