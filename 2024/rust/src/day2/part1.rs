use crate::day2::load_reports;

fn is_breaking(i: u32, j: u32) -> bool {
    i as i32 - j as i32).abs() > 2
}


fn solve() -> u32 {
    let reports = load_reports("input1.txt");
    reports
        .into_iter()
        .map(|report| {
            report
                .windows(2)
               .filter(|pair| !is_breaking(pair[0], pair[1]))
                .count() as u32
        })
        .sum()
}


#[cfg(test)]
mod test {
    use super::solve;
    
    #[test]
    fn test_d2p1() -> () {
        assert_eq!(solve(), 2)
    }
}
