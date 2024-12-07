use std::fs;


fn solve() -> () {
    let input: String = fs::read_to_string("src/day1/input.txt").expect("failed to read");
    let lines: Vec<String> = input.lines().map(String::from).collect();
    let mut left_side: Vec<i32> = Vec::new();
    let mut right_side: Vec<i32> = Vec::new();
    lines
        .iter()
        .for_each(
            |s| {
                let nums: Vec<&str> = s.split_whitespace().collect();
                left_side.push(nums[0].parse().unwrap());
                right_side.push(nums[1].parse().unwrap());
            }
        );
    let mut result = 0;
    left_side.sort();
    right_side.sort();
    for i in 0..left_side.len() {
        let a = left_side[i];
        let b = right_side[i];
        result += (a - b).abs();
    }
    println!("{}", result);
}

#[cfg(test)]
mod test {

    use super::solve;

    #[test]
    fn test_solve() {
        solve();
    }
}
