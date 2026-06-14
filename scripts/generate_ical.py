#!/usr/bin/env python3
"""
生成 iCal 日历文件（支持难度标记、番茄钟事件）
用法: python generate_ical.py --tasks tasks.json --output plan.ics
"""
import json
import sys
from datetime import datetime

def generate_ical(tasks, output_file):
    ical = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Study Planner v4.0//EN\n"
    for task in tasks:
        # 支持 SUMMARY 中包含难度标记和番茄钟标识
        summary = task.get('name', '')
        if task.get('difficulty'):
            summary = f"{task['difficulty']} {summary}"
        if task.get('pomodoro'):
            summary = f"[🍅] {summary}"
        ical += f"BEGIN:VEVENT\nSUMMARY:{summary}\n"
        ical += f"DTSTART:{task['start']}\nDTEND:{task['end']}\n"
        ical += f"DESCRIPTION:{task.get('desc', '')}\nEND:VEVENT\n"
    ical += "END:VCALENDAR"
    with open(output_file, 'w') as f:
        f.write(ical)
    print(f"✅ 已生成 {output_file}，包含 {len(tasks)} 个事件")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_ical.py <tasks.json>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        tasks = json.load(f)
    generate_ical(tasks, "plan.ics")