MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    s, word = "", ""
    skip = -1
    for c in code:
        if c == " " and not word:
            skip += 1
            if skip:
                s += " "
                skip = -1
        elif c == " ":
            s += MORSE[word]
            word = ""
        else:
            word += c
    s += MORSE[word]
    return s.capitalize()


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
        morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
        == "I was born in 1990"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
