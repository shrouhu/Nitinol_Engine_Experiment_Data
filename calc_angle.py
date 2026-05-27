import math
import glob
import os

base_dir = r'd:\pku\zyy\实验\开放实验\PhotoArchive'
txt_files = glob.glob(os.path.join(base_dir, '*.txt'))

for input_file in txt_files:
    basename = os.path.basename(input_file)
    if basename == '48.1.txt':
        continue

    with open(input_file, 'r') as f:
        lines = f.readlines()

    results = []
    offset = 0.0
    prev_angle = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        if i == 0:
            results.append(stripped + '\n')
            continue

        parts = stripped.split('\t')

        if parts[0] == 't':
            results.append(stripped + '\tangle\n')
            continue

        if len(parts) < 3:
            results.append(line)
            continue

        t_str, y_str, x_str = parts[0], parts[1], parts[2]
        y, x = float(y_str), float(x_str)

        angle = math.atan(y / x)

        if prev_angle is not None:
            diff = angle - prev_angle
            if diff < -math.pi / 2:
                offset += math.pi
            elif diff > math.pi / 2:
                offset -= math.pi

        adjusted_angle = angle + offset
        prev_angle = angle

        results.append(f"{t_str}\t{y_str}\t{x_str}\t{adjusted_angle}\n")

    with open(input_file, 'w') as f:
        f.writelines(results)

    print(f"Done: {basename}")

print("All files processed!")
