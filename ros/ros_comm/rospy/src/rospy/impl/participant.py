# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_participant', [dirname(__file__)])
        except ImportError:
            import _participant
            return _participant
        if fp is not None:
            try:
                _mod = imp.load_module('_participant', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _participant = swig_import_helper()
    del swig_import_helper
else:
    import _participant
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Listener(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Listener, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Listener, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _participant.new_Listener(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _participant.delete_Listener
    __del__ = lambda self : None;
    def onSubscriptionMatched(self, *args): return _participant.Listener_onSubscriptionMatched(self, *args)
    def onNewDataMessage(self, *args): return _participant.Listener_onNewDataMessage(self, *args)
    def register_callback(self, *args): return _participant.Listener_register_callback(self, *args)
Listener_swigregister = _participant.Listener_swigregister
Listener_swigregister(Listener)

class Participant(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Participant, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Participant, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _participant.new_Participant(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _participant.delete_Participant
    __del__ = lambda self : None;
    def init(self, *args): return _participant.Participant_init(self, *args)
    def init_py(self): return _participant.Participant_init_py(self)
    def cache_msg(self, *args): return _participant.Participant_cache_msg(self, *args)
    def read_msg(self): return _participant.Participant_read_msg(self)
    def send(self, *args): return _participant.Participant_send(self, *args)
Participant_swigregister = _participant.Participant_swigregister
Participant_swigregister(Participant)

# This file is compatible with both classic and new-style classes.

