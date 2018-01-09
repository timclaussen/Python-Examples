#Small Timer example
import time

# take total from the difference and the previous total
print("Let's do the time warp again!!")

now = time.time()
print("The time taken is:", now, " seconds")
input("Enter a letter or press enter to take the second time")
end = time.time()

total = end - now; #time still expressed as float

print("the time recorded was: ", total, " seconds")
