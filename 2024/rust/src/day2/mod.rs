mod part1;

use std::{fs, path::Path};


fn load_reports(file_name: &str) -> Vec<Vec<u32>> {
    let base_dir = Path::new(file!()).parent().expect("failed to determine source file dir");
    let file_path = base_dir.join(file_name);
    let input: String = fs::read_to_string(file_path).expect("failed to read");
    let lines: Vec<Vec<u32>> = input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse::<u32>().expect("failed to parse bumber"))
                .collect()
        })
        .collect();
    lines
}

