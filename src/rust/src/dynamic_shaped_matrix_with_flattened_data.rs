// #[derive(Debug, Clone, PartialEq, Eq)]
// pub struct Matrix<T>(Vec<T>, (usize, usize));
// impl<T> std::ops::Index<(usize, usize)> for Matrix<T> {
//     type Output = T;

//     fn index(&self, index: (usize, usize)) -> &Self::Output {
//         &self.0[index.0][index.1]
//     }
// }
// impl<T> std::ops::IndexMut<(usize, usize)> for Matrix<T> {
//     fn index_mut(&mut self, index: (usize, usize)) -> &mut Self::Output {
//         &mut self.0[index.0][index.1]
//     }
// }
// impl<T: Default + Clone> Matrix<T> {
//     pub fn new(h: usize, w: usize) -> Matrix<T> {
//         Matrix(vec![vec![T::default(); width]; height])
//     }

//     pub fn shape(&self) -> (usize, usize) { self.1 }
// }
// impl<T: std::fmt::Debug> std::fmt::Display for Matrix<T> {
//     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
//         let format_str = self
//             .0
//             .iter()
//             .map(|row| format!("{:?}", row))
//             .collect::<Vec<_>>()
//             .join("\n");
//         write!(f, "{}", format_str)
//     }
// }
// impl<T> From<Vec<Vec<T>>> for Matrix<T> {
//     fn from(data: Vec<Vec<T>>) -> Self {
//         let h = data.len();
//         if h > 0 {
//             let w = data[0].len();
//             for i in 1..h {
//                 assert_eq!(data[i].len(), w);
//             }
//         }
//         Self(data)
//     }
// }
