from typing import List, TypeVar, Hashable, Iterable, Any
from collections.abc import Sequence
import logging

T = TypeVar('T', bound=Hashable)


class DuplicateRemover:
    def __init__(self, preserve_order: bool = True):
        self.preserve_order = preserve_order

    def remove_duplicates(self, sequence: Iterable[T]) -> List[T]:
        if not isinstance(sequence, Iterable):
            raise TypeError(f"Expected iterable, got {type(sequence).__name__}")

        if not sequence:
            return []

        if self.preserve_order:
            return self._remove_with_order(sequence)
        else:
            return list(set(sequence))

    def _remove_with_order(self, sequence: Iterable[T]) -> List[T]:
        seen = set()
        result = []

        for item in sequence:
            if item not in seen:
                seen.add(item)
                result.append(item)

        return result


def remove_duplicates(
        arr: Iterable[T],
        preserve_order: bool = True,
        return_type: type = list
) -> List[T]:
    remover = DuplicateRemover(preserve_order=preserve_order)
    result = remover.remove_duplicates(arr)

    if return_type != list:
        try:
            return return_type(result)
        except TypeError as e:
            logging.warning(f"Could not convert to {return_type}, returning list: {e}")

    return result


def remove_duplicates_simple(arr: List[T]) -> List[T]:
    if not arr:
        return []

    seen = set()
    result = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


class CollectionProcessor:
    @staticmethod
    def process_collection(collection: Iterable, strategy: str = "ordered") -> List:
        strategies = {
            "ordered": remove_duplicates_simple,
            "unordered": lambda x: list(set(x)),
            "fast": lambda x: list(dict.fromkeys(x))
        }

        processor = strategies.get(strategy, remove_duplicates_simple)
        return processor(collection)


if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]

    result1 = remove_duplicates_simple(numbers)
    result2 = CollectionProcessor.process_collection(numbers, "ordered")
    result3 = remove_duplicates(numbers, preserve_order=True)

    print(result1)
    print(result2)
    print(result3)