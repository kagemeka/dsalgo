pub trait StaticModulusGet {
    type T;
    fn get() -> Self::T;
}

pub trait StaticModulusSet {
    type T;
    fn set(value: Self::T);
}

pub trait StaticModulusTrait: StaticModulusGet {}

impl<T> StaticModulusTrait for T where T: StaticModulusGet {}

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
