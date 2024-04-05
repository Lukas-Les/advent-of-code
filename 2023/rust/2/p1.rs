use std::fs;


struct Color {
    name: String,
    limit: u32,
}


struct Config {
    red: Color,
    green: Color,
    blue: Color,
}


impl Config {
    pub fn is_fitting(self: &Self, color_str: &str, count: u32) -> bool {
        for attr in vec![&self.red, &self.green, &self.blue] {
            if color_str == attr.name {
                return count <= attr.limit;
            }
        }
        false
    }
}


fn parse_line(line: &str) -> Result<(String, Vec<String>), &str> {
    let parts: Vec<&str> = line.split(":").collect();
    let game_id: String = parts[0].replace("Game ", "");
    let games: Vec<String> = parts[1].split(";").map(|s: &str| s.to_string()).collect();
    Ok((game_id, games))
}


fn parse_games(games: Vec<String>, cfg: &Config) -> bool{
    for game in games {
        let items: Vec<&str> = game.split(",").map(|s: &str| s.trim()).collect();
        for i in items {
            let splited: Vec<&str> = i.split_whitespace().collect();
            let (count, color_str) = (splited[0], splited[1]);
            let count: u32 = count.parse().unwrap();
            if !cfg.is_fitting(color_str, count) {
                return false;
            }
        } 
    }
    true
}


fn main() {
    let contents = fs::read_to_string("task_input.txt")
        .expect("Couldn't open a file!");

    let cfg: Config = Config{
        red: Color{name: "red".to_string(), limit: 12},
        green: Color{name: "green".to_string(), limit: 13},
        blue: Color{name: "blue".to_string(), limit: 14},
    };

    let mut result: u32 = 0;
    for line in contents.lines() {
        if let Ok((game_id, games)) = parse_line(line) {
            if parse_games(games, &cfg) {
                result += game_id.parse::<u32>().unwrap();
            }
        } else {
            println!("Pasring line '{}' was failed!", line)
        }
    }
    println!("Result: {}", result);
}
