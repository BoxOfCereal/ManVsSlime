import os
import re
import argparse
from PIL import Image, ImageDraw, ImageFont

def generate_images(input_path, output_folder):
    with open(input_path, 'r') as file:
        script_content = file.read()

    script_lines = script_content.split('\n')
    frame_counters = {}
    image_name = ''
    state_name = ''
    frame_index = 0
    frame_number = 0
    updated_script = ''
    image_found = False

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for line in script_lines:
        parts = line.split()
        if len(parts) == 0:
            updated_script += '\n'
            continue

        if parts[0] == 'image' and not image_found:
            image_name = parts[1]
            frame_counters[image_name] = 0
            image_found = True
            updated_script += line + '\n'
        elif parts[0] == 'state':
            state_name = parts[1]
            frame_index = 0
            updated_script += line + '\n'
        elif parts[0] == 'frame' and image_found:
            frame_statement = ' '.join(parts[1:6])
            action = ' '.join(parts[6:])
            text = f"{image_name}\nState: {state_name}\nFrame: {frame_index}\nFrame Statement: {frame_statement}\nAction: {action}"
            image_name_with_number = f"{image_name}{frame_number}.png"
            create_image(text, image_name_with_number, output_folder)

            # Add updated frame line to the script
            updated_script += f"frame {frame_number} {' '.join(parts[2:])}\n"

            frame_index += 1
            frame_number += 1
        else:
            updated_script += line + '\n'

    with open(input_path, 'w') as file:
        file.write(updated_script.strip())

    print(f"Images have been saved to {output_folder} and the script has been updated in place.")

def create_image(text, image_name, output_folder):
    width, height = 400, 200
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    lines = text.split('\n')
    for index, line in enumerate(lines):
        draw.text((10, 20 + index * 20), line, font=font, fill='black')

    image_path = os.path.join(output_folder, image_name)
    image.save(image_path)

def main():
    parser = argparse.ArgumentParser(description="Generate images from a script and save them to a specified folder.")
    parser.add_argument('--input', type=str, required=True, help='Path to the input script file')
    parser.add_argument('--output_folder', type=str, required=True, help='Path to the output folder for images')

    args = parser.parse_args()

    generate_images(args.input, args.output_folder)
    # python gd.py --input C:\Users\SeltT\OneDrive\Desktop\Projects\ManVsSlime\States\gd_test.states --output C:\Users\SeltT\OneDrive\Desktop\Projects\ManVsSlime\Sprites\Decorations

if __name__ == '__main__':
    main()
