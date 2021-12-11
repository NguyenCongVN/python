# Import required packages
import cv2
import pytesseract
from InteractHelper import *


def getTextValueFromImage(path):
    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Read image from which text needs to be extracted
    img = cv2.imread(path)

    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))

    # Appplying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    recognizedText = ""
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        text = text.encode("ascii", errors="ignore").decode()
        text = text.replace('\n', ' ').replace('\f', '')
        recognizedText = recognizedText + text
    return recognizedText


def solveChallengeTelegram(signitureImagePath):
    init_width = 400
    init_height = 20
    result = detectImage(imagePath=signitureImagePath, gioiHan=20)
    time_try = 0
    if result != -1:
        captureScreenChallenge()
        while True:
            path = CropImage(x=result[0], y=result[1] + 20, width=init_width, hieght=init_height)
            text = getTextValueFromImage(path)
            print(text)
            time_try = time_try + 1
            try_ops = None
            if '=' in text:
                math_tokens = []
                if time_try == 10:
                    text = text.replace('=', '')
                    for ops in ['+', '-', 'x', '/']:
                        if ops in text:
                            text = text.replace(ops, " ")
                            try_ops = ops
                tokens = text.split(' ')
                for token in tokens:
                    try:
                        if token in ['+', '-', 'x', '/', '(', ')']:
                            math_tokens.append(token)
                        else:
                            int_token = int(token.strip())
                            math_tokens.append(int_token)
                            if try_ops:
                                math_tokens.append(try_ops)
                                try_ops = None
                    except ValueError:
                        pass
                if len(math_tokens) < 3:
                    init_width = init_width + 20
                    continue
                string_expression = ''
                for math_token in math_tokens:
                    string_expression = string_expression + str(math_token)
                try:
                    result = eval(string_expression)
                    return str(result)
                except:
                    continue
            else:
                init_width = init_width + 20
                init_height = init_height + 5
                try_ops = None
                if time_try == 10:
                    math_tokens = []
                    for ops in ['+', '-', 'x', '/']:
                        if ops in text:
                            text = text.replace(ops, " ")
                            try_ops = ops
                    tokens = text.split(' ')
                    for token in tokens:
                        try:
                            if token in ['+', '-', 'x', '/', '(', ')']:
                                math_tokens.append(token)
                            else:
                                int_token = int(token.strip())
                                math_tokens.append(int_token)
                                if try_ops:
                                    math_tokens.append(try_ops)
                                    try_ops = None
                        except ValueError:
                            pass
                    if len(math_tokens) < 3:
                        init_width = init_width + 20
                        continue
                    string_expression = ''
                    for math_token in math_tokens:
                        string_expression = string_expression + str(math_token)
                    try:
                        result = eval(string_expression)
                        return str(result)
                    except:
                        continue
    else:
        print('Bỏ qua giải')
        return -1

# print(solveChallengeTelegram(fr'{os.getcwd()}\Image\TelegramChallengeStart.png'))
