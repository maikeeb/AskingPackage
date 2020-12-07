def ask(stri, **restrictions):
    val = True
    while val:
        while True:
            try:
                # if there is a type restriction it will check it and if not just asks for input
                ans = input(stri)
                ans = restrictions["type"](ans)  # if "type" in restrictions.keys() else input(stri)
                break
            except ValueError:
                # if not the type they asked for, unless its the break
                if "Break" in restrictions.keys() and ans == restrictions["Break"]:
                    break
                else:
                    print("Not a", restrictions["type"] if "type" in restrictions.keys() else None)
            except KeyError:
                pass

        if "lower" in restrictions.keys() and restrictions["lower"] and restrictions["type"] == str:
            ans = ans.lower()
        if "upper" in restrictions.keys() and restrictions["upper"] and restrictions["type"] == str:
            ans = ans.upper()
        # true if in answers if they exist
        valA = True if "answers" not in restrictions.keys() else False if ans not in restrictions[
            "answers"] else True

        # if not one of the given answers
        if not valA:
            # making a user friendly list
            wordss = ''
            for valu in restrictions['answers']:
                wordss += ", " + str(valu)
            wordss = wordss[1:]
            print('Not one of the answers:' + wordss)

        valB = True
        valC = True
        if "type" in restrictions.keys() and restrictions["type"] == float or int:
            # if there is a max and ans is below max
            valB = True if "max" not in restrictions.keys() else True if ans < restrictions["max"] else False
            if not valB:
                print("Above maximum value:", restrictions["max"] - 1)
            # if there is a min and ans is above min
            valC = True if "min" not in restrictions.keys() else True if ans > restrictions["min"] else False
            if not valC:
                print("Below minimum value:", restrictions["min"] + 1)

        valD = True if "length" not in restrictions.keys() else False if restrictions["length"] != len(ans) else True
        if not valD:
            print("Not a length of %s" % restrictions["length"])
        val = False if valA and valB and valC and valD else True

    return ans


# example
if __name__ == "__main__":
    ask("sd: ", length=3, type=str)
    ask("What kind of tip do you want?\n"
        "1)percentage\n"
        "2)exact value\n"
        "3)none", answer=[str(x) for x in range(1, 4)], type=str)
    print(ask("What numbers: ", type=float, max=10, min=1))
    print(ask("What number: ", type=int, answers=range(1, 10)))
    print(ask("What number: ", answers=[str(x) for x in range(1, 10)]))
    print(ask("Spanish(s), English(e), French(f): ", type=str, answers=["s", "e", "f"], lower=True))
# F -> f then check it in answers

# type argument will make sure the return is that type of variable
# answers is a list of answers if you want to be specific (string or integer use)
# (not recommended for float, but possible)
# for min and max its up to but not including
# upper/lower turns strings to lower or upper when true, this happens BEFORE it checks if the input is in the answers
# length for specific output length

# To do:
# multi answers with one ask function so ie. age name? 12 Henry
# to do this it would be able to use one string then split the answer then check each split for separate restrictions
