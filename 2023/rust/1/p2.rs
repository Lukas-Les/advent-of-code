use std::fs;


const SHORTEST_WORD: u8 = 3; // one, two, six 


fn reverse_str(s: &str) -> String {
    let reversed: String = s.chars().rev().collect();
    reversed
}


fn parse_line(line: &str, result_var: &mut String, words_to_int: &[String; 9]) -> () {
    let mut cache: String = String::new();
    for c in line.chars() { 
        if c.is_numeric() {
            result_var.push(c);
            return
        }
        cache.push(c); 

        if cache.len() >= SHORTEST_WORD as usize {
            if let Some(index) = words_to_int.iter().position(|word| cache.contains(&word as &str)) {
                let number = &index + 1;
                result_var.push_str(&number.to_string());
                return
            }
        }
    }
}

fn main() {
    let contents = fs::read_to_string("task_input.txt")
        .expect("Couldn't open a file!");

    let words_to_int: [String; 9] = [
        String::from("one"), 
        String::from("two"), 
        String::from("three"), 
        String::from("four"), 
        String::from("five"), 
        String::from("six"), 
        String::from("seven"), 
        String::from("eight"), 
        String::from("nine"),
        ];

    let mut words_to_int_reversed = Vec::new();
    for word in words_to_int.iter() {
        let reversed_word = reverse_str(word);
        words_to_int_reversed.push(reversed_word);
    }
    let words_to_int_reversed_array: [String; 9] = words_to_int_reversed.try_into().unwrap();

    let mut result: u32 = 0;
    for line in contents.lines() {
        let mut line_result: String = String::new();

        parse_line(line, &mut line_result, &words_to_int);

        let r_line: String = reverse_str(&line);
        parse_line(&r_line, &mut line_result, &words_to_int_reversed_array);

        let line_result_as_int: u32 = line_result.parse().unwrap();
        println!("{}", line_result);
        result += line_result_as_int;
    }
    println!("Final: {}", result);
}
