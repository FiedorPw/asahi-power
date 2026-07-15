# asahi-power ⚡

htop-style live power monitor for Apple Silicon Macs running [Asahi Linux](https://asahilinux.org/).

Shows the whole power chain as colored meters refreshed 4×/second:

```
  ⚡ power  20:22:19

  Battery     [███████████████████████░░░░░░░░] 65% Charging

  PD contract 139.7 W (USB-PD limit = 100% of bars)
  AC input    [||||||||||||||||||||||||||||||||||  117.5 W]
  System      [|||||||||||                          32.9 W]
  → battery   [||||||||||||||||||||||||||||         85.0 W]

  System power, last 15s
  ▆▇▇▇▇███▇▇
```

- **PD contract** — the negotiated USB-PD power limit (= 100% of the meter axis)
- **AC input** — what actually flows through the charging cable right now
- **System** — the machine's own live power draw
- **→ / ← battery** — charge going into (or drawn from) the battery
- **sparkline** — recent system-power history

Meters share one axis (the PD limit), so proportions are directly comparable.
Colors go green → yellow → red with load, htop-style. When unplugged, the AC
rows disappear and the battery arrow flips direction.

## Requirements

- Apple Silicon Mac with Asahi Linux (reads `macsmc` sensors from
  `/sys/class/power_supply` and SMC power sensors from `/sys/class/hwmon`)
- bash, awk, tput — nothing else

## Install

```bash
git clone https://github.com/FiedorPw/asahi-power.git
cd asahi-power
./power
```

Optionally drop it on your `PATH`:

```bash
ln -s "$PWD/power" ~/.local/bin/power
```

## How the rendering works

No ncurses — just ANSI: alternate screen buffer, hidden cursor, and each frame
composed off-screen then drawn with a single write from the home position.
`ESC[K` per line overwrites leftovers, so there's no full-screen clear between
frames — which means no flicker and no cursor dancing.
