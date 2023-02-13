"""Tests for flatten_json_util."""

import pytest
from flatten_json_util import flatten, flatten_single, flatten_json


class TestFlattenSingle:
    def test_flat_dict(self):
        data = {"a": 1, "b": "hello"}
        result = flatten_single(data)
        assert result == [{"a": 1, "b": "hello"}]

    def test_nested_dict(self):
        data = {"user": {"name": "Alice", "age": 30}}
        result = flatten_single(data)
        assert result == [{"user_name": "Alice", "user_age": 30}]

    def test_nested_list(self):
        data = {"scores": [10, 20, 30]}
        result = flatten_single(data)
        assert result == [{"scores_0": 10, "scores_1": 20, "scores_2": 30}]

    def test_deeply_nested(self):
        data = {"a": {"b": {"c": "deep"}}}
        result = flatten_single(data)
        assert result == [{"a_b_c": "deep"}]

    def test_mixed_types(self):
        data = {"name": "test", "count": 5, "active": True, "value": None}
        result = flatten_single(data)
        assert result == [{"name": "test", "count": 5, "active": True, "value": None}]

    def test_list_of_dicts(self):
        data = {"items": [{"name": "a"}, {"name": "b"}]}
        result = flatten_single(data)
        assert result == [{"items_0_name": "a", "items_1_name": "b"}]

    def test_empty_dict(self):
        result = flatten_single({})
        assert result == [{}]


class TestFlatten:
    def test_single_dict(self):
        data = {"a": 1}
        result = flatten(data)
        assert result == [{"a": 1}]

    def test_list_of_dicts(self):
        data = [{"a": 1, "b": {"c": 2}}, {"a": 3}]
        result = flatten(data)
        assert result == [{"a": 1, "b_c": 2}, {"a": 3}]

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            flatten("not json")
