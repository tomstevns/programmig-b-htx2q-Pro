import random

def strigl_min_hest_100_gange():
    for i in  range(100):
        print("Stringler hesten ",i," gange")


print("Ridetøj på")
print("Tager min hest")

strigl_min_hest_100_gange()

Er_min_hest_beskidt = random.choice([True, False])

if Er_min_hest_beskidt == True:
    strigl_min_hest_100_gange()
    print("Min hest er ikke længere beskidt")
