from .. import Cli

# Empty cases


def test_has_args_should_return_false_if_caller_has_no_params():
    def foo():
        return Cli.has_args()
    assert not foo()  # False


def test_has_args_should_return_false_if_caller_has_no_arg_values():
    def foo(*args):
        return Cli.has_args()
    assert not foo()  # False


def test_has_args_should_return_false_if_caller_has_no_kwargs_values():
    def foo(**kwargs):
        return Cli.has_args()
    assert not foo()  # False


def test_has_args_should_return_false_if_caller_has_no_args_no_kwargs_values():
    def foo(*args, **kwargs):
        return Cli.has_args()
    assert not foo()  # False

# Single argument in args cases


def test_has_args_should_return_true_if_caller_has_None_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo(None)  # True


def test_has_args_should_return_true_if_caller_has_non_empty_str_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo("a")  # True


def test_has_args_should_return_true_if_caller_has_empty_str_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo("")  # True


def test_has_args_should_return_true_if_caller_has_int_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo(1)  # True


def test_has_args_should_return_true_if_caller_has_float_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo(1.1)  # True


def test_has_args_should_return_true_if_caller_has_empty_dict_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo(dict())  # True


def test_has_args_should_return_true_if_caller_has_populated_dict_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo({"bar": "baz"})  # True


def test_has_args_should_return_true_if_caller_has_empty_set_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo(set())  # True


def test_has_args_should_return_true_if_caller_has_empty_set_literal_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo({})  # True


def test_has_args_should_return_true_if_caller_has_populated_set_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo(set([1, 2]))  # True


def test_has_args_should_return_true_if_caller_has_empty_list_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo(list())  # True


def test_has_args_should_return_true_if_caller_has_empty_list_lit_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo([])  # True


def test_has_args_should_return_true_if_caller_has_populated_list_in_args():
    def foo(*args):
        return Cli.has_args()
    assert foo([1, 2])  # True

# Single argument in kwargs cases


def test_has_args_should_return_true_if_caller_has_None_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=None)  # True


def test_has_args_should_return_true_if_caller_has_string_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a="a")  # True


def test_has_args_should_return_true_if_caller_has_int_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=1)  # True


def test_has_args_should_return_true_if_caller_has_float_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=1.1)  # True


def test_has_args_should_return_true_if_caller_has_empty_dict_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=dict())  # True


def test_has_args_should_return_true_if_caller_has_populated_dict_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a={"bar": "baz"})  # True


def test_has_args_should_return_true_if_caller_has_empty_set_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=set())  # True


def test_has_args_should_return_true_if_caller_has_empty_set_lit_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a={})  # True


def test_has_args_should_return_true_if_caller_has_populated_set_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=set([1, 2]))  # True


def test_has_args_should_return_true_if_caller_has_empty_list_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=list())  # True


def test_has_args_should_return_true_if_caller_has_empty_list_lit_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=[])  # True


def test_has_args_should_return_true_if_caller_has_populated_list_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=[1, 2])  # True


def test_has_args_should_return_true_if_caller_has_empty_dict_in_kwargs():
    def foo(**kwargs):
        return Cli.has_args()
    assert foo(a=dict())  # True

# Multiple argument cases


def test_has_args_should_return_true_if_caller_has_multiple_values_in_args():
    def foo(*args, **kwargs):
        return Cli.has_args()
    assert foo("a", 1)  # True


def test_has_args_should_return_true_if_caller_has_value_in_args_and_kwargs():
    def foo(*args, **kwargs):
        return Cli.has_args()
    assert foo("a", a=1)  # True


def test_has_args_should_return_true_if_caller_has_values_in_args_and_kwargs():
    def foo(*args, **kwargs):
        return Cli.has_args()
    assert foo("a", 0, a=1, b=dict())  # True
