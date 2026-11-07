"""مدیریت نمرات: نمونه کامل آموزشی فقط با کتابخانه استاندارد."""
import json
from pathlib import Path

DATA_PATH = Path('gradebook.json')


def load(path=DATA_PATH):
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict):
        raise ValueError('ساختار فایل نادرست است')
    return data


def save(data, path=DATA_PATH):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    tmp.replace(path)


def add_student(data, sid, name):
    sid, name = sid.strip(), name.strip()
    if not sid or not name or sid in data:
        raise ValueError('شناسه/نام نامعتبر یا تکراری')
    data[sid] = {'name': name, 'grades': []}


def add_grade(data, sid, grade):
    if sid not in data:
        raise KeyError('دانش‌آموز پیدا نشد')
    if not 0 <= grade <= 20:
        raise ValueError('نمره باید بین صفر تا بیست باشد')
    data[sid]['grades'].append(grade)


def report(data):
    for sid, record in sorted(data.items()):
        grades = record['grades']
        average = f'{sum(grades)/len(grades):.2f}' if grades else 'بدون نمره'
        print(sid, record['name'], '| میانگین:', average)


def main():
    data = load()
    while True:
        print('\n1 افزودن | 2 نمره | 3 گزارش | 4 ذخیره و خروج')
        command = input('انتخاب: ').strip()
        try:
            if command == '1':
                add_student(data, input('شناسه: '), input('نام: '))
            elif command == '2':
                add_grade(data, input('شناسه: ').strip(), float(input('نمره: ')))
            elif command == '3':
                report(data)
            elif command == '4':
                save(data)
                print('داده‌ها ذخیره شد')
                break
            else:
                print('گزینه نامعتبر')
        except (ValueError, KeyError) as exc:
            print('خطا:', exc)


if __name__ == '__main__':
    main()
