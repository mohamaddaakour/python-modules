import functools
import operator
from typing import Any, Callable, Dict, List


def spell_reducer(spells: List[int], operation: str) -> int:
    # operator apply specific operation
    ops: Dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in ops:
        raise ValueError(
            "Operation must be 'add', 'multiply', "
            "'max', or 'min'"
        )

    # we take the operation
    # now func is the function and inside it the logic of the operation
    func = ops[operation]

    if operation in ("max", "min"):
        return func(spells)

    # functools.reduce(function, list)
    return functools.reduce(func, spells)


def partial_enchanter(
    base_enchantment: Callable[..., str],
) -> Dict[str, Callable[[str], str]]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment,
            power=50,
            element="Fire",
        ),
        "ice_enchant": functools.partial(
            base_enchantment,
            power=50,
            element="Ice",
        ),
        "lightning_enchant": functools.partial(
            base_enchantment,
            power=50,
            element="Lightning",
        ),
    }


def base_enchant(target: str, power: int, element: str) -> str:
    return f"{element} enchant with {power} power on {target}"


# to memorize the result of the first call and like this
# we will not calculate it again from the beginning
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0

    if n == 1:
        return 1

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


# this will check every input we give it as an argument
# for the cast function
def spell_dispatcher() -> Callable[[Any], Any]:
    @functools.singledispatch
    def cast(spell: Any) -> Any:
        raise TypeError("Unsupported spell type")

    @cast.register
    def _(damage: int) -> str:
        return f"Deals {damage} damage!"

    @cast.register
    def _(enchantment: str) -> str:
        return f"Applies {enchantment} enchantment!"

    @cast.register
    def _(multi_cast: list) -> List[Any]:
        return [cast(s) for s in multi_cast]

    return cast


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting partial enchanter...")
    partials = partial_enchanter(base_enchant)

    print(partials["fire_enchant"]("Dragon"))
    print(partials["ice_enchant"]("Golem"))
    print(partials["lightning_enchant"]("Orc"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()

    print(dispatcher(100))
    print(dispatcher("Frozen"))
    print(dispatcher([50, "Burning", 30]))
