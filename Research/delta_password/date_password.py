import time
from datetime import datetime, timedelta


def make_password_from_dt(dt: datetime) -> str:
    year = dt.year * 2
    month = dt.month * 2
    day = dt.day * 2
    hour = dt.hour * 2
    minute = dt.minute * 2
    second = dt.second * 2

    return f"{year:04d}.{month:02d}.{day:02d}.{hour:02d}.{minute:02d}.{second:02d}"


def seconds_until_next_hour(now: datetime) -> float:
    next_hour = (now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1))
    delta = next_hour - now
    return delta.total_seconds()


def run_hourly_job(run_once_immediately=True):
    if run_once_immediately:
        now = datetime.now()
        wait = seconds_until_next_hour(now)
        time.sleep(wait)
        now = datetime.now()
        pw = make_password_from_dt(now)
        return pw  # 别忘了 return
    return None


if __name__ == "__main__":
    try:
        pw = run_hourly_job(run_once_immediately=True)
        print("Generated password:", pw)
    except KeyboardInterrupt:
        print("Stopped by user.")

    user_input = input("Please input your password: ")
    if user_input == pw:
        print("🎉 Congratulations!!!")
    else:
        print("Oh, I’m so sorry...")