# importing module1 from another file but in same folder it has both module1 and module2 files
import module1 as mod
mod.square(4)
mod.login("admin","admin")
print(mod.pi)
mod.welcome("soumya","bastwad")


# third way to import a specific func/var/class/etc
from module1 import pi,square,login,welcome
print(pi)
square(4)
login("user","user")
welcome("soumya","bastwad")

# 4th way if you are looking to import everything(all)
from module1 import*
print(pi)
square(4)
login("user","user")
welcome("soumya","bastwad")

