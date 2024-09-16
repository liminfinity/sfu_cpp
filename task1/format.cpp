#include <string>
#include <sstream>
#include <regex>
#include <iostream>
#include "date.cpp"

using namespace std;

string format_invalid_input_message(const string& format)
{
    ostringstream oss;
    oss << "Неверный ввод! Формат ввода: " << format;
    return oss.str();
}

string date_to_str(const Date& date)
{
    return to_string(date.yyyy) + "." + to_string(date.mm) + "." + to_string(date.dd);
}

Date get_date(const string& dateStr)
{
    regex datePattern(R"((\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))");
    smatch matches;
    regex_match(dateStr, matches, datePattern);
    int yyyy = stoi(matches[1]);
    int mm = stoi(matches[2]);
    int dd = stoi(matches[3]);
    Date date;
    date.yyyy = yyyy;
    date.mm = mm;
    date.dd = dd;

    return date;
}