#[derive(PartialEq, Eq, PartialOrd, Ord, Clone, Copy, Debug)]
pub struct DefaultData(pub i64);

impl DefaultData {
    const INF: i64 = 1 << 60;
}

impl std::ops::Add<Self> for DefaultData {
    type Output = Self;

    fn add(self, rhs: Self) -> Self {
        let inf = Self::INF;
        if self.0 == inf || rhs.0 == inf {
            Self(inf)
        } else {
            Self(self.0 + rhs.0)
        }
    }
}
