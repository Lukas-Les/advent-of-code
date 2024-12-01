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
                let nums: Vec<&str> = s.split("   ").collect();
                left_side.push(nums[0].parse().unwrap());
                right_side.push(nums[1].parse().unwrap());
            }
        );
    let mut result = 0;
    while !left_side.is_empty() {
        let min_left = left_side.iter().min().cloned(); 
        let min_right = right_side.iter().min().cloned(); 

        left_side.retain(|&x| x != min_left);
        right_side.retain(|&x| x != min_right);

        let diff = (min_left - min_right).abs();
        result += diff;
        println!("{}", result);
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
