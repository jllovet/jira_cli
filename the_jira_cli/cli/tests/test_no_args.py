import the_jira_cli.cli as cli

# Empty cases
def test_should_return_true_from_no_args_if_calling_function_has_no_parameters():
    def has_no_params():
        return cli.no_args()
    assert has_no_params() == True

def test_should_return_true_from_no_args_if_calling_function_has_no_argument_values():
    def has_no_arg_values(*args):
        return cli.no_args()
    assert has_no_arg_values() == True

def test_should_return_true_from_no_args_if_calling_function_has_no_kwargs_values():
    def has_no_args_and_no_kwargs_values(**kwargs):
        return cli.no_args()
    assert has_no_args_and_no_kwargs_values() == True

def test_should_return_true_from_no_args_if_calling_function_has_no_args_and_no_kwargs_values():
    def has_no_args_and_no_kwargs_values(*args, **kwargs):
        return cli.no_args()
    assert has_no_args_and_no_kwargs_values() == True

# Single argument in args cases
def test_should_return_false_from_no_args_if_calling_function_has_None_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo(None) == False

def test_should_return_false_from_no_args_if_calling_function_has_non_empty_string_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo("a") == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_string_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo("") == False

def test_should_return_false_from_no_args_if_calling_function_has_int_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo(1) == False

def test_should_return_false_from_no_args_if_calling_function_has_float_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo(1.1) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_dict_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo(dict()) == False

def test_should_return_false_from_no_args_if_calling_function_has_populated_dict_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo({"bar": "baz"}) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_set_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo(set()) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_set_literal_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo({}) == False

def test_should_return_false_from_no_args_if_calling_function_has_populated_set_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo(set([1,2])) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_list_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo(list()) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_list_literal_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo([]) == False

def test_should_return_false_from_no_args_if_calling_function_has_populated_list_passed_to_star_args():
    def foo(*args):
        return cli.no_args()
    assert foo([1,2]) == False

# Single argument in kwargs cases
def test_should_return_false_from_no_args_if_calling_function_has_None_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=None) == False

def test_should_return_false_from_no_args_if_calling_function_has_string_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a="a") == False

def test_should_return_false_from_no_args_if_calling_function_has_int_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=1) == False

def test_should_return_false_from_no_args_if_calling_function_has_float_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=1.1) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_dict_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=dict()) == False

def test_should_return_false_from_no_args_if_calling_function_has_populated_dict_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a={"bar": "baz"}) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_set_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=set()) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_set_literal_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a={}) == False

def test_should_return_false_from_no_args_if_calling_function_has_populated_set_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=set([1,2])) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_list_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=list()) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_list_literal_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=[]) == False

def test_should_return_false_from_no_args_if_calling_function_has_populated_list_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=[1,2]) == False

def test_should_return_false_from_no_args_if_calling_function_has_empty_dict_passed_to_star_kwargs():
    def foo(**kwargs):
        return cli.no_args()
    assert foo(a=dict()) == False

# Multiple argument cases
def test_should_return_false_from_no_args_if_calling_function_has_multiple_values_passed_to_star_args():
    def foo(*args, **kwargs):
        return cli.no_args()
    assert foo("a", 1) == False

def test_should_return_false_from_no_args_if_calling_function_has_value_passed_to_star_args_and_star_kwargs():
    def foo(*args, **kwargs):
        return cli.no_args()
    assert foo("a", a=1) == False

def test_should_return_false_from_no_args_if_calling_function_has_multiple_values_passed_to_star_args_and_star_kwargs():
    def foo(*args, **kwargs):
        return cli.no_args()
    assert foo("a", 0, a=1, b=dict()) == False
