#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Matrix<T>(pub Vec<Vec<T>>);
impl<T> std::ops::Index<(usize, usize)> for Matrix<T> {
    type Output = T;

    fn index(&self, index: (usize, usize)) -> &Self::Output {
        &self.0[index.0][index.1]
    }
}
impl<T> std::ops::IndexMut<(usize, usize)> for Matrix<T> {
    fn index_mut(&mut self, index: (usize, usize)) -> &mut Self::Output {
        &mut self.0[index.0][index.1]
    }
}
impl<T> std::ops::Index<usize> for Matrix<T> {
    type Output = [T];

    fn index(&self, i: usize) -> &Self::Output { &self.0[i] }
}
impl<T> std::ops::IndexMut<usize> for Matrix<T> {
    fn index_mut(&mut self, i: usize) -> &mut Self::Output { &mut self.0[i] }
}
impl<T: Default + Clone> Matrix<T> {
    pub fn new(height: usize, width: usize) -> Matrix<T> {
        Matrix(vec![vec![T::default(); width]; height])
    }

    pub fn shape(&self) -> (usize, usize) {
        if self.0.len() == 0 {
            (0, 0)
        } else {
            (self.0.len(), self.0[0].len())
        }
    }

    pub fn transpose(&self) -> Self {
        let (h, w) = self.shape();
        let mut a = Matrix::new(w, h);
        for i in 0..h {
            for j in 0..w {
                a[j][i] = self[i][j].clone();
            }
        }
        a
    }

    pub fn reverse(&self) -> Self {
        let mut a = Self(self.0.clone());
        a.0.reverse();
        a
    }

    pub fn rot90(&self) -> Self { self.transpose().reverse() }

    pub fn rot270(&self) -> Self { self.reverse().transpose() }
}
impl<T: std::fmt::Debug> std::fmt::Display for Matrix<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let format_str = self
            .0
            .iter()
            .map(|row| format!("{:?}", row))
            .collect::<Vec<_>>()
            .join("\n");
        write!(f, "{}", format_str)
    }
}
impl<T> From<Vec<Vec<T>>> for Matrix<T> {
    fn from(data: Vec<Vec<T>>) -> Self {
        let h = data.len();
        if h > 0 {
            let w = data[0].len();
            for i in 1..h {
                assert_eq!(data[i].len(), w);
            }
        }
        Self(data)
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let (height, width) = (3, 4);
        let mut matrix = super::Matrix::<usize>::new(height, width);
        assert_eq!(
            matrix,
            Matrix::<usize>::from(vec![
                vec![0, 0, 0, 0],
                vec![0, 0, 0, 0],
                vec![0, 0, 0, 0],
            ])
        );
        println!("{}", matrix);
        matrix[(1, 1)] += 1;
        matrix[1][1] += 1;
        assert_eq!(
            matrix,
            Matrix::<usize>::from(vec![
                vec![0, 0, 0, 0],
                vec![0, 2, 0, 0],
                vec![0, 0, 0, 0],
            ])
        );
        assert_eq!(
            matrix.transpose(),
            Matrix::<usize>::from(vec![
                vec![0, 0, 0],
                vec![0, 2, 0],
                vec![0, 0, 0],
                vec![0, 0, 0],
            ])
        );
        for row in 0..height {
            for col in 0..width {
                matrix[(row, col)] = row * width + col;
            }
        }
        assert_eq!(
            matrix,
            Matrix::<usize>::from(vec![
                vec![0, 1, 2, 3],
                vec![4, 5, 6, 7],
                vec![8, 9, 10, 11],
            ])
        );
        assert_eq!(
            matrix.reverse(),
            Matrix::<usize>::from(vec![
                vec![8, 9, 10, 11],
                vec![4, 5, 6, 7],
                vec![0, 1, 2, 3],
            ])
        );
        assert_eq!(
            matrix.rot90(),
            Matrix::<usize>::from(vec![
                vec![3, 7, 11],
                vec![2, 6, 10],
                vec![1, 5, 9],
                vec![0, 4, 8],
            ])
        );
        assert_eq!(
            matrix.rot270(),
            Matrix::<usize>::from(vec![
                vec![8, 4, 0],
                vec![9, 5, 1],
                vec![10, 6, 2],
                vec![11, 7, 3],
            ])
        );
    }
}
