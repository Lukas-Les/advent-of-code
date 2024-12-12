use crate::day1::load_lists;

fn solve() -> i32 {
    let (mut left_side, mut right_side) = load_lists("src/day1/input1.txt");
    let mut result: i32 = 0;
    left_side.iter()
        .for_each(
            |&left_n| result += left_n * right_side.iter().filter(|&right_n| left_n == *right_n).count() as i32
        );

    result
}


#[cfg(test)]
mod test {

    use super::solve;

    #[test]
    fn test_d1p2() {
        assert_eq!(solve(), 18567089);
    }
}
