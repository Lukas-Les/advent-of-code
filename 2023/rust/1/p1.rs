use std::fs;


fn reverse_str(s: &str) -> String {
    let reversed: String = s.chars().rev().collect();
    reversed
}


fn parse_line(line: &str, result_var: &mut String) -> () {
    for c in line.chars() {
        if c.is_numeric() {
            result_var.push(c);
            return
        }
    }
}

fn main() {
    let contents = fs::read_to_string("task_input.txt")
        .expect("Couldn't open a file!");
    let mut result: u32 = 0;
    for line in contents.lines() {
        let mut line_result: String = String::new();

        parse_line(line, &mut line_result);

        let r_line: String = reverse_str(&line);
        parse_line(&r_line, &mut line_result);

        let line_result_as_int: u32 = line_result.parse().unwrap();
        result += line_result_as_int;
    }
    println!("{}", result);
}
