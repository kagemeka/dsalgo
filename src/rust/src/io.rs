fn read_token<R, T>(reader: &mut R) -> Result<T, <T as std::str::FromStr>::Err>
where
    R: std::io::Read,
    T: std::str::FromStr,
{
    use std::io::Read;
    reader
        .by_ref()
        .bytes()
        .map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>()
        .parse::<T>()
}
pub fn read_stdin<T>() -> Result<T, <T as std::str::FromStr>::Err>
where
    T: std::str::FromStr,
{
    read_token(&mut std::io::stdin().lock())
}
pub struct ReadWrapper<R> {
    reader: R,
    tokens: Vec<String>,
}
impl<R> ReadWrapper<R> {
    pub fn new(reader: R) -> Self { Self { reader, tokens: vec![] } }
}
impl<R: std::io::BufRead> ReadWrapper<R> {
    pub fn read<T: std::str::FromStr>(
        &mut self,
    ) -> Result<T, <T as std::str::FromStr>::Err> {
        while self.tokens.is_empty() {
            let mut buf = String::new();
            self.reader.read_line(&mut buf).unwrap();
            self.tokens =
                buf.split_whitespace().map(str::to_string).rev().collect();
        }
        self.tokens.pop().unwrap().parse::<T>()
    }
}
pub fn locked_stdin_reader() -> ReadWrapper<std::io::StdinLock<'static>> {
    let stdin = Box::leak(Box::new(std::io::stdin()));
    ReadWrapper::new(stdin.lock())
}
pub fn locked_stdout_buf_writer()
-> std::io::BufWriter<std::io::StdoutLock<'static>> {
    let stdout = Box::leak(Box::new(std::io::stdout()));
    std::io::BufWriter::new(stdout.lock())
}
#[macro_export]
#[allow(unused_macros)]
macro_rules! write_vec {
    ($writer:ident, $values:expr) => {
        write_vec!($writer, $values, sep: ' ');
    };

    ($writer:ident, $values:expr,sep: $sep:expr) => {
        let n = $values.len();
        if n == 0 {
            writeln!($writer).unwrap();
            return;
        }
        for i in 0..n - 1 {
            write!(
                $writer,
                "{}{}",
                $values[i], $sep
            )
            .unwrap();
        }
        writeln!($writer, "{}", $values[n - 1]).unwrap();
    };
}
#[macro_export]
#[allow(unused_macros)]
macro_rules! write_all {
    ($writer:ident) => {
        writeln!($writer).unwrap();
    };

    ($writer:ident, $v:expr) => {
        writeln!($writer, "{}", $v).unwrap();
    };

    ($writer:ident, $v:expr, $($values:expr),+) => {
        write!($writer, "{} ", $v).unwrap();
        write_all!($writer, $($values),*);
    };
}
#[macro_export]
#[allow(unused_macros)]
macro_rules! read_vec {
    ($reader:ident, $type:ty, $n:expr) => {
        (0..$n)
            .map(|_| $reader.read::<$type>())
            .collect::<Result<Vec<_>, _>>()
            .unwrap()
    };
}
#[allow(dead_code)]
pub(crate) fn debug_print<T: std::fmt::Debug>(data: &T) {
    eprintln!("{:#?} ", data);
}
/// reference
/// https://users.rust-lang.org/t/show-value-only-in-debug-mode/43686/3
#[macro_export]
// #[allow(unused_macros)]
macro_rules! dbg {
    ($($x:tt)*) => {
        {
            // default in debug mode
            #[cfg(debug_assertions)]
            {
                std::dbg!($($x)*)
            }

            // default in release mode
            #[cfg(not(debug_assertions))]
            {
                ($($x)*)
            }
        }
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test_read_wrapper() {
        use super::ReadWrapper;
        let stdin = std::io::stdin();
        let _reader = ReadWrapper::new(stdin.lock());
    }
    #[test]
    fn test_locked_stdin_buf_writer() {
        use std::io::Write;

        use super::locked_stdout_buf_writer;
        let mut writer = locked_stdout_buf_writer();
        writeln!(writer, "Hello, world!").unwrap();
        writer.flush().unwrap();
    }
    #[test]
    fn write_macro() {
        use std::io::Write;

        use super::locked_stdout_buf_writer;
        let mut writer = locked_stdout_buf_writer();
        let mut v = vec![];
        write_vec!(writer, v);
        v.push(1);
        v.push(2);
        write_vec!(writer, v, sep: '\n');
        write_vec!(writer, v, sep: ' ');
        write_all!(writer);
        write_all!(writer, 1, 2, 3);
        write_all!(writer, 1);
        writer.flush().unwrap();
    }
    #[test]
    fn test_dbg() {
        // use super::*;
        let a = 1;
        dbg!(dbg!(a) + 1);
    }
}
// template of main function.
// fn main() -> Result<(), Box<dyn std::error::Error>> {
//     use std::io::Write;
//     let mut reader = locked_stdin_reader();
//     let mut writer = locked_stdout_buf_writer();
//     writer.flush()?;
//     Ok(())
// }
