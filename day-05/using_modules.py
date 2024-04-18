import simple_module as sm

print(sm.MODULE_CONSTANT)
#simple_module.MODULE_CONSTANT
sm.simple_function()
mod_class = sm.SimpleClass()

from simple_module import simple_function as sf
sf()

