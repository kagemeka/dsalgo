from __future__ import annotations

import dataclasses

import dsalgo.vector_arithmetic


@dataclasses.dataclass
class Segment2D:
    p0: dsalgo.vector_arithmetic.Vector2D
    p1: dsalgo.vector_arithmetic.Vector2D

    def intersect(self, rhs: Segment2D) -> bool:
        return self.across(rhs) & rhs.across(self)

    def across(self, other: Segment2D) -> bool:
        v0 = other.p1 - other.p0
        v1 = self.p0 - other.p0
        v2 = self.p1 - other.p0
        c0 = v0.cross(v1)
        c1 = v0.cross(v2)
        return c0 * c1 <= 0
