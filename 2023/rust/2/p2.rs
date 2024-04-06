use std::fs;


fn parse_line(line: &str) -> Result<Vec<String>, &str> {
    let parts: Vec<&str> = line.split(":").collect();
    let games: Vec<String> = parts[1].split(";").map(|s: &str| s.to_string()).collect();
    Ok(games)
}


fn parse_games(games: Vec<String>) -> Result<u32, &'static str> {
    let mut r: Vec<u32> = Vec::new();
    let mut g: Vec<u32> = Vec::new();
    let mut b: Vec<u32> = Vec::new();

    for game in games.iter() {
        let game: Vec<&str> = game.split(",").collect();
        for item in game {
            let split_item: Vec<&str> = item.trim().split_whitespace().collect();
            let (count, color) = (split_item[0], split_item[1]);
            let count: u32 = count.parse().unwrap();
            match color {
                "red" => r.push(count),
                "green" => g.push(count),
                "blue" => b.push(count),
                _ => continue,
            }
        }
    }

    let mut max_numbers: Vec<u32> = Vec::new();
    for v in [r, g, b].iter() {
        if let Some(max) = v.iter().max() {
            max_numbers.push(*max);
        }
    }
    let result: u32 = max_numbers.iter().fold(1, |acc, x| acc * x);
    Ok(result)
}


fn main() {
    let contents = fs::read_to_string("task_input.txt")
        .expect("Couldn't open a file!");
    let mut result: u32 = 0;
    for line in contents.lines() {
        if let Ok(games) = parse_line(line) {
            result += parse_games(games).unwrap();
        }  
    }
    println!("{}", result);
}
