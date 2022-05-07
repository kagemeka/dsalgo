from __future__ import annotations

import dsalgo.modular


def garner_form(mod_rem_pairs: list[tuple[int, int]]) -> int | None:
    mod_rem_pairs = [pair for pair in mod_rem_pairs if pair != (1, 0)]
    assert len(mod_rem_pairs) >= 1
    x = 0
    mod_prod = 1
    for mod, rem in mod_rem_pairs:
        inv = dsalgo.modular.invert_extended_euclidean(mod, mod_prod)
        if inv is None:
            return None
        coeff = (rem - x) * inv % mod
        x += coeff * mod_prod
        mod_prod *= mod
        assert 0 <= x < mod_prod
    return x


def garner_modular_form(
    mod: int,
    mod_rem_pairs: list[tuple[int, int]],
) -> int | None:
    mod_rem_pairs = [pair for pair in mod_rem_pairs if pair != (1, 0)]
    n = len(mod_rem_pairs)
    assert n >= 1
    modulos = [mod for mod, _ in mod_rem_pairs] + [mod]
    mod_values = [0] * (n + 1)  # mod_values[i] = x_i \mod modulos[i]
    mod_prod = [1] * (n + 1)
    # mod_prod[i] = (\prod_{j=0}^{j=i-1} modulos[j]) \mod modulos[i]
    for i, (mod, rem) in enumerate(mod_rem_pairs):
        inv = dsalgo.modular.invert_extended_euclidean(mod, mod_prod[i])
        if inv is None:
            return None
        t = (rem - mod_values[i]) * inv % mod
        for j in range(i + 1, n + 1):
            mod_values[j] = (mod_values[j] + t * mod_prod[j]) % modulos[j]
            mod_prod[j] = mod_prod[j] * mod % modulos[j]
    return mod_values[-1]
