from flask import Flask, send_file, request
import os

app = Flask(__name__)

# Set the upload folder.
app.config['UPLOAD_FOLDER'] = '/path/to/your/app/'

@app.route('/download_zip', methods=['GET'])
def download_zip():
    print("download_zip function called")
    # Get the name of the zip file from the request.
    file_name = request.args.get('file_name')

    # Check if the file_name parameter exists.
    if file_name is None:
        return "Error: file_name parameter is missing.", 400

    # Get the full path to the zip file.
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        return "Error: File not found", 404

    # Send the zip file to the client.
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run()
