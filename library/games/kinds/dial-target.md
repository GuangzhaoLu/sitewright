## game.dial-target

## English

**Turn the dial.** Problem: A quantity sits on a range, and three labeled sentences throw away the range.

**When:** One dial, slider, or gauge, with a target the brief names, and a tolerance.
**When not:** There are only two answers. Use `game.this-or-that`. No number you can check.

**Steps:**

1. Stepping buttons: less, more. The dial moves by a visible notch, not by a free drag that must hit a pixel.
2. The target can be hidden until the player commits with a Set button, or shown as a mark. The brief says which.
3. Say the result in words: short, on it, past it. Within the tolerance, `mark`.
4. Offer at least the buttons. A slider may sit beside them if it is tall enough to tap.

**Don't:** A stopwatch. Do not require the ones digit.

**Example:** A volume, a year on a short span, or a mix of two amounts. Min, max, step, target, and tolerance are in JSON.

---

## 中文

**把刻度转到目标.** 问题：一个量在一段范围上。三个写好的句子把这段范围丢掉了。

**何时用:** 一个旋钮、滑杆或仪表，简报写明目标和容差。
**何时不用:** 只有两个答案。用 `game.this-or-that`。没有能核对的数。

**步骤:**

1. 用「少一点」「多一点」按钮。刻度按看得见的一格移动，不要靠自由拖动去撞一个像素。
2. 目标可以先藏着，等玩家按「确定」再揭开，或事先标在刻度上。由简报决定。
3. 用文字说结果：不到、到位、过了。在容差内才 `mark`。
4. 至少要有按钮。滑杆可以并排放，但必须够高、点得到。

**反例:** 秒表。不要要求精确到个位。

**实例:** 一个音量、一小段年份，或两种量的混合。最小、最大、步长、目标和容差写在 JSON 里。
