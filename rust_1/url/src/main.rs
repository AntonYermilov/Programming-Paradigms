fn get_url() -> String {
    "http://mit.spbau.ru".to_string()
}

fn get_scheme_from_url(url: &str) -> &str {
    let colon = url.find(":").unwrap();
    &url[..colon]
}

fn main() {
    // won't compile
    let scheme2 = get_scheme_from_url(&get_url());
    println!("{}", scheme2);

    // will
    // let url = get_url();
    // let scheme = get_scheme_from_url(&url);
    // println!("{}", scheme);
}
