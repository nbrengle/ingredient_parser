"""Ingredient Parser and associated logic.

As additional endpoints or parsers are introduced,
much of this logic will merit refactoring into a common
collection of functions usable by other parsers.

The basic idea is simple pipeline as described in `parse`.
A string is lazily matched against a collection of regexes.
The first match, if any, is transformed using the re.match.groupdict()
And then post-processed by a map of fields to post-processing functions.

"""
from functools import partial
import re
from typing import Callable, Dict, Hashable, Iterable, Mapping, Match, Optional, Pattern, TypeVar

from toolz import get, excepts, identity, thread_last, update_in


_ingredient_patterns: Iterable[Pattern] = thread_last(
    [
        r"(?P<quantity>\d*\.?\d+)\s(?P<unit>\w+)\.?\s(of\s)?(?P<ingredient>.+)",
        r"(?P<quantity>\d*\.?\d+)\s(?P<ingredient>.+)",
        r"(?P<ingredient>.+)",
    ],
    (map, re.compile),
    list,
)

_ingredient_cleanup_funcs: Mapping[Hashable, Optional[Callable]] = {
    "quantity": None,
    "unit": lambda s: s[0].lower() if s else None,
    "ingredient": None,
}

A = TypeVar('A')
first_not_none: Callable[[Iterable[A]], Optional[A]] = excepts(
    StopIteration, 
    lambda a: next(filter(None, a)),
    lambda __: None
)


def pattern_match(patterns: Iterable[Pattern], text: str) -> Optional[Match]:
    matching = (p.search(text) for p in patterns)
    return first_not_none(matching)


def groupdict(match: Optional[Match]) -> Dict:
    out: Dict = {}
    if match:
        out = match.groupdict()
    return out


def post_process(
    field_funcs_map: Mapping[Hashable, Optional[Callable]], to_clean: Dict, default=None
) -> Mapping:
    out = to_clean
    for key, func in field_funcs_map.items():
        f = func if func else identity
        out = update_in(out, [key], f, default=default)
    return out


def parse(
    patterns: Iterable[Pattern],
    post_func_map: Mapping[Hashable, Optional[Callable]],
    s: str,
) -> Mapping:
    return thread_last(
        s, (pattern_match, patterns), groupdict, (post_process, post_func_map)
    )


parse_ingredient = partial(parse, _ingredient_patterns, _ingredient_cleanup_funcs)
