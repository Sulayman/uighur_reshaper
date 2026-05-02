# Uighur Reshaper

A Python tool that converts Uyghur text between the basic Arabic Unicode block
(U+0600–U+06FF) and the Arabic Presentation Forms (U+FB50–U+FEFC). It picks
the correct isolated / initial / medial / final glyph for every letter and
handles the Lam-Alef (ﻻ / ﻼ) ligature.

Useful when you need to render Uyghur in environments that don't perform Arabic
shaping themselves (e.g. some terminals, image / PDF generators, or legacy
displays), or when you need to round-trip presentation-form text back to its
basic-block representation for storage and search.

---

## English

### Installation

```bash
pip install uighur_reshaper
```

### Library usage

```python
from uighur_reshaper import UighurReshaper

reshaper = UighurReshaper()

# Basic Arabic block → contextual presentation forms
shaped = reshaper.basic2extend("ئۇيغۇرچە خەت")
print(shaped)

# Presentation forms → basic Arabic block (round-trip)
print(reshaper.extend2basic(shaped))
```

The lowercase `reshaper` and `uighur_reshaper` names are kept as backward-
compatible aliases for the class, so existing code like
`from uighur_reshaper import reshaper; reshaper()` continues to work.

### Command line

```bash
# Reshape an argument
uighur_reshaper "ئۇيغۇرچە خەت"

# Reshape from stdin (useful in pipelines)
echo "ئۇيغۇرچە خەت" | uighur_reshaper

# Reverse: presentation forms → basic block
uighur_reshaper -r "ﺋﯘﻳﻐﯘﺭﭼﻪ ﺧﻪﺕ"
```

### API

| Method | Description |
| --- | --- |
| `UighurReshaper().basic2extend(text)` | Convert basic-block characters to their contextual presentation forms. Non-Uyghur characters pass through unchanged. |
| `UighurReshaper().extend2basic(text)` | Convert presentation-form characters back to the basic Arabic block, including the Lam-Alef ligature. |

### Development

```bash
git clone https://github.com/Sulayman/uighur_reshaper.git
cd uighur_reshaper
python -m unittest discover -v
```

### License

MIT

---

## 中文

### 简介

`uighur_reshaper` 是一个用于在基本阿拉伯字符块（U+0600–U+06FF）与阿拉伯文呈现形式块
（U+FB50–U+FEFC）之间转换维吾尔文文本的 Python 工具。它会为每个字母选择正确的独立 /
词首 / 词中 / 词末字形，并正确处理 Lam-Alef（ﻻ / ﻼ）连字。

适用于不会自行进行阿拉伯文整形的渲染环境（如部分终端、图片 / PDF 生成器、旧式显示设备），
或需要将呈现形式文本还原回基本字符块以便存储与检索的场景。

### 安装

```bash
pip install uighur_reshaper
```

### 使用

```python
from uighur_reshaper import UighurReshaper

reshaper = UighurReshaper()
shaped = reshaper.basic2extend("ئۇيغۇرچە خەت")
print(shaped)
print(reshaper.extend2basic(shaped))
```

### 命令行

```bash
uighur_reshaper "ئۇيغۇرچە خەت"
echo "ئۇيغۇرچە خەت" | uighur_reshaper
uighur_reshaper -r "ﺋﯘﻳﻐﯘﺭﭼﻪ ﺧﻪﺕ"
```

### 许可证

MIT

---

## ئۇيغۇرچە

### چۈشەندۈرۈش

`uighur_reshaper` ئۇيغۇر تېكىستىنى ئاساسىي ئەرەب ھەرپ رايونى (U+0600–U+06FF) بىلەن
ئەرەب كۆرۈنۈش شەكىللىرى رايونى (U+FB50–U+FEFC) ئارىسىدا ئايلاندۇرۇپ بېرىدىغان Python
قورالى. ئۇ ھەربىر ھەرپكە ماس ھالدا يەككە / باش / ئوتتۇرا / ئاخىرلىق شەكىللىرىنى تاللايدۇ
ۋە Lam-Alef (ﻻ / ﻼ) قوشۇلما ھەرپىنى توغرا بىر تەرەپ قىلىدۇ.

بۇ قورال ئۆزى ئەرەب ھەرپ شەكىللەندۈرۈشىنى قىلالمايدىغان كۆرۈنمە مۇھىتلار (بەزى تېرمىناللار،
رەسىم/PDF ھاسىللاش قورالى، كونا كۆرسىتىش ئۈسكۈنىلىرى) ئۈچۈن، شۇنداقلا كۆرۈنۈش شەكىلدىكى
تېكىستنى ساقلاش/ئىزدەش ئۈچۈن ئاساسىي ھەرپ رايونىغا قايتۇرۇش لازىم بولغاندا قول كېلىدۇ.

### ئورنىتىش

```bash
pip install uighur_reshaper
```

### ئىشلىتىش

```python
from uighur_reshaper import UighurReshaper

reshaper = UighurReshaper()
shaped = reshaper.basic2extend("سىزنىڭ ئۇيغۇرچە تېكىستىڭىز")
print(shaped)
print(reshaper.extend2basic(shaped))
```

### بۇيرۇق قۇرى

```bash
uighur_reshaper "سىزنىڭ ئۇيغۇرچە تېكىستىڭىز"
echo "سىزنىڭ ئۇيغۇرچە تېكىستىڭىز" | uighur_reshaper
uighur_reshaper -r "..."
```

### ئىجازەتنامە

MIT
