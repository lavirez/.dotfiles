#!/usr/bin/env python3
"""Clock + calendar tooltip for waybar, with a centered rounded pill on today.

Usage: clock-calendar.py            -> print waybar JSON
       clock-calendar.py shift N    -> move the shown month by N (0 resets)
"""
import calendar
import datetime as dt
import json
import os
import sys

STATE = os.path.join(os.environ.get("XDG_RUNTIME_DIR", "/tmp"), "waybar-calendar-offset")
ACCENT = "#0a84ff"
FONT = "JetBrainsMono Nerd Font"
SIZE = "14pt"
# A cell is 2 chars + 1 separator. The round caps are drawn with letter_spacing so
# they overlap the neighbouring space without taking up width (-2 chars at 14pt = 11px).
SHIFT = -22528
LCAP = f"<span foreground='{ACCENT}' letter_spacing='{SHIFT}'></span> "
RCAP = f" <span foreground='{ACCENT}' letter_spacing='{SHIFT}'></span>"


def read_offset():
    try:
        with open(STATE) as f:
            return int(f.read().strip() or 0)
    except (OSError, ValueError):
        return 0


def shift(n):
    offset = 0 if n == 0 else read_offset() + n
    with open(STATE, "w") as f:
        f.write(str(offset))


def today_cell(day):
    num = f"<span weight='900' foreground='#ffffff' background='{ACCENT}'>{day}</span>"
    # Single digits: the pad space becomes the left cap, so the pill centers on the digit.
    return f" {LCAP}{num}{RCAP}" if day < 10 else f"{LCAP}{num}{RCAP}"


def render(now):
    total = now.year * 12 + now.month - 1 + read_offset()
    year, month = divmod(total, 12)
    month += 1
    cal = calendar.Calendar(firstweekday=0)

    title = f"{calendar.month_name[month]} {year}".center(20).rstrip()
    lines = [f"<span weight='800' foreground='{ACCENT}'>{title}</span>",
             "<span weight='700' alpha='50%'>" + " ".join(calendar.day_abbr[i][:2] for i in range(7)) + "</span>"]
    for week in cal.monthdayscalendar(year, month):
        cells = []
        for d in week:
            if d == 0:
                cells.append("  ")
            elif (year, month, d) == (now.year, now.month, now.day):
                cells.append(today_cell(d))
            else:
                cells.append(f"{d:>2}")
        lines.append(" ".join(cells))
    # One space of margin each side so caps on the edge columns aren't clipped.
    body = "\n".join(f" {l} " for l in lines)
    return f"<span font_family='{FONT}' size='{SIZE}' weight='500'>{body}</span>"


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "shift":
        shift(int(sys.argv[2]))
        return
    now = dt.datetime.now()
    print(json.dumps({"text": now.strftime("%R %a %m/%d"), "tooltip": render(now)}))


if __name__ == "__main__":
    main()
