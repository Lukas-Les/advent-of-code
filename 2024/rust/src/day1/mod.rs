mod part1;

use std::fs;


fn load_lists(input_location: &str) -> (Vec<i32>, Vec<i32>) {
    let input: String = fs::read_to_string(input_location).expect("failed to read");
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
    (left_side, right_side)
}

