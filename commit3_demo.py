# commit3_demo.py

from commit2_demo import commit2_demo

def commit3_demo():
    v1, v2 = commit2_demo()  # get the two instances

    data1 = ["1", "2", "-4", "hello"]
    data2 = ["5", "0", "20", "xyz"]

    valid1, invalid1 = v1.validate_positive_integers(data1)
    valid2, invalid2 = v2.validate_positive_integers(data2)

    print("Commit 3 Output:")
    print("Validator 1 results:")
    print("  Valid:", valid1)
    print("  Invalid:", invalid1)

    print("\nValidator 2 results:")
    print("  Valid:", valid2)
    print("  Invalid:", invalid2)
    print("-----------------------------------")

if __name__ == "__main__":
    commit3_demo()
