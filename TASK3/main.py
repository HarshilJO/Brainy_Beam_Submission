from PIL import Image, ImageDraw, ImageFont
import inflect

def number_to_word(number):
    p = inflect.engine()  # Correct instantiation of the inflect engine
    return p.number_to_words(number)

def res(word): 
    img = Image.new('RGB', (400, 200), color='white')
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Draw the text
    d.text((10, 10), word, fill=(0, 0, 0), font=font)

    return img

def number_to_image(number):
    word = number_to_word(number)
    img = res(word)
    img.save(f"{number}.png")  # Use 'save' instead of 'Save'
    return f"{number}.png"
    
input_number = int(input("Enter a number: "))
output_file = number_to_image(input_number)
print(f"Image saved as {output_file}")
