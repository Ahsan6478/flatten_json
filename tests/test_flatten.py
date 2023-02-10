"""Tests for flatten_json_util."""

from flatten_json_util import flatten_single


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
