

def make_module(step=1):

    return {'inc':  lambda x: x + step, 'dec': lambda y: y - step}

m = make_module()
m['inc'](10)
print(m)