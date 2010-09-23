
import types
import module

def classList():
    """function return a list, module_class, which contain name of all the classes
	in the imported module
    """
    module_dir = dir(module)
    module_class = []
    for each in module_dir:
        if type(getattr(module, each)) == types.ClassType:
            module_class.append(each)
    return module_class

def classWithBase(module_class):
    """function return a list, module_base, which contain name of all the functions
        in the class, the class is extended from a particular base class. Final list
	contain functions from all the class which follow the above condition
    """
    module_base = []
    for each in module_class:
        if getattr(module,each).__bases__ == (module.a,):
            module_base.append(each)
    return module_base

def functionActivation(module_base):
    """function that makes all function, which starts with name 'test', to run
    """
    for each in module_base:
        o = getattr(module, each)
        module_fun = dir(o)
        for one in module_fun:
            if type(getattr(o, one)) == types.MethodType and one[:4] == 'test':
	        obj = o()
	        getattr(obj, one)()

module_class = classList()
module_base = classWithBase(module_class)
functionActivation(module_base)
