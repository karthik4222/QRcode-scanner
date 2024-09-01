import cv2
from pyzbar import pyzbar

def decode_qr_codes(image):
    # Decode the QR code(s) in the image
    qr_codes = pyzbar.decode(image)
    for qr_code in qr_codes:
        # Extract QR code data
        qr_code_data = qr_code.data.decode('utf-8')
        # Extract QR code location
        x, y, w, h = qr_code.rect
        # Draw a rectangle around the QR code
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Display the QR code data
        cv2.putText(image, qr_code_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(f'Detected QR code: {qr_code_data}')
        return image, True  # Return the image and a flag indicating a QR code was detected
    return image, False  # Return the image and a flag indicating no QR code was detected

def decode_qr_from_webcam():
    # Start the webcam
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break
        # Decode QR codes
        frame, qr_code_detected = decode_qr_codes(frame)
        # Display the resulting frame
        cv2.imshow('QR Code Scanner', frame)
        # Break the loop if a QR code is detected
        if qr_code_detected:
            break
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # When everything is done, release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

decode_qr_from_webcam()
