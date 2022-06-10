pub trait DynamicModulusGet {
    type T;
    fn get(&self) -> Self::T;
}

pub trait DynamicModulusSet {
    type T;
    fn set(&mut self, value: Self::T);
}
pub trait DynamicModulusTrait: DynamicModulusGet {}

impl<T> DynamicModulusTrait for T where T: DynamicModulusGet {}
