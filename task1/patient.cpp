#include <string>
#include <iostream>
#include <regex>
#include "validation.cpp"
#include "format.cpp"

using namespace std;

struct Patient {
    string passport;    // ss ss-nnnnnn
    string name;        // any string
    Date birth_date;    // yyyy-mm-dd
    string phone;       // +X(XXX) XXX-XX-XX or X(XXX) XXX-XXXX
    double temperature; // XX.XX
public:
    void print()
    {
        cout << "Имя: " << name << endl;
        cout << "Паспорт: " << passport << endl;
        cout << "Дата рождения: " << date_to_str(birth_date) << endl;
        cout << "Номер телефона: " << phone << endl;
        cout << "Температура: " << temperature << endl;
    }
};

string get_input_name() {
    string name;
    while (true)
    {

        cout << "Введите имя: ";
        getline(cin, name);

        if (is_name(name)) {
            return name;
        }
        else
        {
            cerr << format_invalid_input_message("Кириллица, латиница, тире и апостроф.") << endl;
            continue;
        }
    }
}

string get_input_passport() {
    string passport;
    while (true)
    {
        cout << "Введите паспорт (формат: ss ss-nnnnnn): ";
        getline(cin, passport);

        if (is_passport(passport)) {
            return passport;
        }
        else
        {
            cerr << format_invalid_input_message("ss ss-nnnnnn.") << endl;
            continue;
        }
    }
}

Date get_input_birth_date() {
    string birth_date;
    while (true)
    {
        cout << "Введите дату рождения (формат: yyyy-mm-dd): ";
        getline(cin, birth_date);

        if (is_date(birth_date)) {
            Date date = get_date(birth_date);
            return date;
        }
        else
        {
            cerr << format_invalid_input_message("yyyy-mm-dd.") << endl;
            continue;
        }
    }
}

string get_input_phone() {
    string phone;
    while (true)
    {

        cout << "Введите номер телефона (формат: +X(XXX) XXX-XX-XX или X(XXX) XXX-XXXX): ";
        getline(cin, phone);

        if (is_phone(phone)) {
            return phone;
            break;
        }
        else
        {
            cerr << format_invalid_input_message("+X(XXX) XXX-XX-XX или X(XXX) XXX-XXXX.") << endl;
            continue;
        }
    }
}

double get_input_temperature() {
    string temperature;
    while (true)
    {
        cout << "Введите температуру тела (формат: XX.XX): ";
        getline(cin, temperature);

        if (is_temperature(temperature)) {
            return stod(temperature);
        }
        else
        {
            cerr << format_invalid_input_message("XX.XX.") << endl;
            continue;
        }
    }
}


Patient create_patient() {
    Patient new_patient;
    new_patient.name = get_input_name();
    new_patient.passport = get_input_passport();
    new_patient.birth_date = get_input_birth_date();
    new_patient.phone = get_input_phone();
    new_patient.temperature = get_input_temperature();

    return new_patient;
}

