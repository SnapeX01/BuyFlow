# Zero-width Unicode decoder (paste-based)

ZERO_WIDTH_SPACE = "\u200b"      # binary 0
ZERO_WIDTH_NON_JOINER = "\u200c" # binary 1

print("Paste the copied text below. Press ENTER twice when done:\n")

# Read multiline pasted input
lines = []
while True:
    try:
        line = input()
        if line == "":
            break
        lines.append(line)
    except EOFError:
        break

content = "\n".join(lines)

binary = ""
for ch in content:
    if ch == ZERO_WIDTH_SPACE:
        binary += "0"
    elif ch == ZERO_WIDTH_NON_JOINER:
        binary += "1"

decoded = ""
for i in range(0, len(binary), 8):
    byte = binary[i:i+8]
    if len(byte) == 8:
        decoded += chr(int(byte, 2))

print("\nDecoded message:")
print(decoded)
