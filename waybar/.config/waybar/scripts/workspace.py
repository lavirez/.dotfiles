#!/usr/bin/env python3
"""Waybar custom module for one Hyprland workspace button.

Usage: workspace.py <id> [icon] [--persistent]

Prints a JSON line whenever the workspace state changes. The built-in
hyprland/workspaces module can't switch workspaces on Lua-config Hyprland
(it sends the legacy `dispatch workspace N`), so clicks are handled in
config.jsonc with `hyprctl dispatch 'hl.dsp.focus({ workspace = N })'`.
"""
import json
import os
import socket
import subprocess
import sys
import time

args = [a for a in sys.argv[1:] if a != "--persistent"]
WS = int(args[0])
ICON = args[1] if len(args) > 1 else str(WS)
PERSISTENT = "--persistent" in sys.argv

EVENTS = (
    "workspace", "workspacev2", "createworkspace", "createworkspacev2",
    "destroyworkspace", "destroyworkspacev2", "focusedmon", "focusedmonv2",
    "moveworkspace", "moveworkspacev2", "openwindow", "closewindow",
    "movewindow", "movewindowv2", "monitoradded", "monitorremoved",
)


def hyprctl(what):
    out = subprocess.run(["hyprctl", "-j", what], capture_output=True, text=True)
    return json.loads(out.stdout or "[]")


def state():
    workspaces = {w["id"]: w for w in hyprctl("workspaces")}
    monitors = hyprctl("monitors")
    visible = any(m["activeWorkspace"]["id"] == WS for m in monitors)
    active = any(m.get("focused") and m["activeWorkspace"]["id"] == WS for m in monitors)
    ws = workspaces.get(WS)

    if not ws and not PERSISTENT and not active:
        return {"text": ""}

    classes = []
    if active:
        classes.append("active")
    elif visible:
        classes.append("visible")
    if not ws or ws.get("windows", 0) == 0:
        classes.append("empty")
    return {"text": ICON, "class": classes, "tooltip": f"Workspace {WS}"}


last = None


def emit():
    global last
    try:
        cur = json.dumps(state())
    except (json.JSONDecodeError, KeyError, OSError):
        return
    if cur != last:
        print(cur, flush=True)
        last = cur


def socket_path():
    runtime = os.environ.get("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")
    sig = os.environ["HYPRLAND_INSTANCE_SIGNATURE"]
    return os.path.join(runtime, "hypr", sig, ".socket2.sock")


def main():
    emit()
    while True:
        try:
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
                s.connect(socket_path())
                buf = b""
                while True:
                    chunk = s.recv(4096)
                    if not chunk:
                        break
                    buf += chunk
                    *lines, buf = buf.split(b"\n")
                    if any(l.split(b">>", 1)[0].decode() in EVENTS for l in lines):
                        emit()
        except OSError:
            pass
        time.sleep(1)
        emit()


if __name__ == "__main__":
    main()
