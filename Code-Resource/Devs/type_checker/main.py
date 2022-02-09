
def giveType(object):
    obj_type = type(object)
    return obj_type


def checkVarType(var, var_type):
    instance_type = isinstance(var, var_type)
    try:
        assert instance_type is True
    except AssertionError as error:
        # print(
        #     f'The variable has a different type that the required one -> {giveType(var)} | {var_type}')
        return -1
    else:
        # print(f'All good -> {giveType(var)} | {var_type}')
        return 1
