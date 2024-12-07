use crate::day1::load_lists;

fn solve() -> i32 {
    let (mut left_side, mut right_side) = load_lists("src/day1/input1.txt");
    let mut result = 0;
    left_side.sort();
    right_side.sort();
    for i in 0..left_side.len() {
        let a = left_side[i];
        let b = right_side[i];
        result += (a - b).abs();
    }
    println!("{}", result);
    result
}

#[cfg(test)]
mod test {

    use super::solve;

    #[test]
    fn test_solve() {
        assert_eq!(solve(), 2000468);
    }
}
