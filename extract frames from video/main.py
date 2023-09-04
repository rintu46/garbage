import cv2
import os

def extract_frames(video_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    video_capture = cv2.VideoCapture(video_file)

    # Initialize frame counter
    frame_count = 0

    # Loop through the video frames
    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()

        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # Define the name of the image file to save
        image_name = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')

        # Save the frame as an image
        cv2.imwrite(image_name, frame)

        # Increment the frame counter
        frame_count += 1

    # Release the video capture object
    video_capture.release()

    print(f'{frame_count} frames extracted and saved in {output_folder}.')

if __name__ == "__main__":
    input_video_file = 'received_310676851510799.mp4'  # Set the input video file path here
    output_image_folder = 'output_images'  # Set the output image folder here

    extract_frames(input_video_file, output_image_folder)
