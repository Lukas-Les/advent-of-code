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
    while !left_side.is_empty() {
        let (min_left_index, &min_left) = left_side
            .iter()
            .enumerate()
            .min_by_key(|&(_, &val)| val)
            .unwrap();
        left_side.swap_remove(min_left_index);

        let (min_right_index, &min_right) = right_side
            .iter()
            .enumerate()
            .min_by_key(|&(_, &val)| val)
            .unwrap();
        right_side.swap_remove(min_right_index);

        let diff = (min_left - min_right).abs();
        result += diff;
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
