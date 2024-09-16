#include <regex>
#include <string>

using namespace std;

bool is_name(const string& name) {
    regex pattern(R"([a-z][a-z\s'-]+)", regex_constants::icase);
    return regex_match(name, pattern);
}
bool is_passport(const string& passport) {
    regex passportPattern(R"(\d{2}\s\d{2}-\d{6})");
    return regex_match(passport, passportPattern);
}
bool is_date(const string& date) {
    regex datePattern(R"((\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))");
    smatch matches;
    if (regex_match(date, matches, datePattern)) {
        int yyyy = stoi(matches[1]);
        int mm = stoi(matches[2]);
        int dd = stoi(matches[3]);

        if (yyyy < 1900 || yyyy > 2024) return false;
        if (mm < 1 || mm > 12) return false;
        if (dd < 1 || dd > 31) return false;

        if ((mm == 4 || mm == 6 || mm == 9 || mm == 11) && dd > 30) return false;
        if (mm == 2) {
            bool isLeap = (yyyy % 4 == 0 && yyyy % 100 != 0) || (yyyy % 400 == 0);
            if (dd > (isLeap ? 29 : 28)) return false;
        }
        return true;
    }
    else return false;
}
bool is_phone(const string& phone) {
    regex phonePattern(R"((\+7|8)\(\d{3}\)\s\d{3}-(\d{2}-\d{2}|\d{4}))");
    return regex_match(phone, phonePattern);
}
bool is_temperature(const string& temperature) {
    regex temperaturePattern(R"((3[2-9]|4[0-2]).\d{2})");
    return regex_match(temperature, temperaturePattern);
}