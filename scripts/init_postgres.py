import json

from app.postgres_adapter import init_postgres, postgres_status


def main():
    print(json.dumps(postgres_status(), indent=2))
    print(json.dumps(init_postgres(), indent=2))


if __name__ == '__main__':
    main()
