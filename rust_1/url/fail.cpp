#include <iostream>
#include <experimental/string_view>

using std::experimental::string_view;

std::string get_url() {
  return "http://mit.spbau.ru";
}

string_view get_scheme_from_url(string_view url) {
  unsigned colon = url.find(':');
  return url.substr(0, colon);
}

int main() {
  auto scheme = get_scheme_from_url(get_url());
  std::cout << scheme << std::endl;
  return 0;
}
