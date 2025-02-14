try:
    list = [20,0,30]
    result = list[0] / list[3]
    print(result)
    print("done")
except ZeroDivisionError:
    print("dividing by zero is not possible")
except IndexError:
    print("this is not acceptable")

# we can use also this. this is short curt.
# except(ZeroDivisionError,IndexError):
#     print("wrong input")
finally:
    print('successfull')