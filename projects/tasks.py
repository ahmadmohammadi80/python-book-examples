"""فهرست کارها با JSON و argparse؛ نمونه کامل CLI."""
import argparse
import json
from pathlib import Path
from uuid import uuid4

DATA_PATH = Path('tasks.json')


def load(path=DATA_PATH):
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, list):
        raise ValueError('ساختار فایل نادرست است')
    return data


def save(tasks, path=DATA_PATH):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding='utf-8')
    temp.replace(path)


def add(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError('عنوان نمی‌تواند خالی باشد')
    task = {'id': str(uuid4()), 'title': title, 'done': False}
    tasks.append(task)
    return task


def finish(tasks, task_id):
    for task in tasks:
        if task['id'].startswith(task_id):
            task['done'] = True
            return task
    raise ValueError('شناسه پیدا نشد')


def main(argv=None):
    parser = argparse.ArgumentParser(description='فهرست کارهای شخصی')
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('list', help='نمایش کارها')
    add_parser = sub.add_parser('add', help='افزودن کار')
    add_parser.add_argument('title')
    done_parser = sub.add_parser('done', help='انجام کار')
    done_parser.add_argument('id')
    args = parser.parse_args(argv)
    tasks = load()
    if args.action == 'add':
        task = add(tasks, args.title)
        save(tasks)
        print('افزوده شد:', task['id'][:8])
    elif args.action == 'done':
        task = finish(tasks, args.id)
        save(tasks)
        print('انجام شد:', task['title'])
    else:
        for task in tasks:
            mark = '✓' if task['done'] else '○'
            print(mark, task['id'][:8], task['title'])


if __name__ == '__main__':
    try:
        main()
    except (ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f'خطا: {exc}')
