use crate::day2::load_reports;


const LIMIT: u32 = 4;


fn is_breaking(i: u32, j: u32, increasing: bool) -> bool {
    if i == j {
        return true;
    }
    if increasing {
        i < j && (j - i > LIMIT)
    } else {
        j < i && (i - j > LIMIT)
    }
}


fn solve() -> u32 {
    let reports = load_reports("input1.txt");
    let mut result = 0;
    for report in reports.iter() {
        let mut safe = true;
        let mut is_increasing: Option<bool> = None;
        for i in 0..report.len() - 1 {
            if is_increasing.is_none() {
                if report[i] < report[i + 1] {
                    is_increasing = Some(true);
                } else {
                    is_increasing = Some(false);
                }
            }
            if is_breaking(report[i], report[i + 1], is_increasing.unwrap()) {
                safe = false;
                break;
            }
        }
        if safe {
            result += 1;
        }
    }
    result
}


#[cfg(test)]
mod test {
    use super::solve;
    
    #[test]
    fn test_d2p1() -> () {
        assert_eq!(solve(), 2)
    }
}
