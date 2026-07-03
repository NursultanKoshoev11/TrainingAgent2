import json

from app.diagnostics import diagnostics_report
from app.readiness import readiness_report


def main():
    print('DIAGNOSTICS')
    print(json.dumps(diagnostics_report(), indent=2))
    print('READINESS')
    print(json.dumps(readiness_report(), indent=2))


if __name__ == '__main__':
    main()
