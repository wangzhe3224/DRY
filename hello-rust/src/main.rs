// sum type
enum Animal {
    Cat { weight: f32, legs: usize },
    Dog { weight: f32, legs: usize },
}

// product type
struct MyProductType {
    character: char, 
    int: i32,
    boolean: bool,
}

struct UnitType;

// recursion
fn fact(num: usize) -> usize {
    return match num {
        0 => 1,
        _ => num * fact(num-1),
    }
}

fn main() {
    let prod: MyProductType;
    let unit: UnitType;
    println!("Hello, world!");
    let res = fact(2);
    // println!(res);
    println!("{}", res);
}
