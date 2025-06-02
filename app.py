from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Replace these with your actual values
UIPATH_API_URL = "https://cloud.uipath.com/AlfalakUiPathCloud/AlfalakOrchestrator/orchestrator_/t/f0df05f7-e7c1-4edc-b601-ce711df82e9d/startprocess"
UIPATH_API_HEADERS = {
    "Authorization": "Bearer rt_30D0529B043D20107EEAEC1EDDE43F854E8475F0FA8B0EBB3F67E5F67BDEBA2B-1",
    "Content-Type": "application/json"
}

@app.route('/trigger-process')
def trigger_process():
    try:
        # Send request to UiPath API
        response = requests.post(UIPATH_API_URL, headers=UIPATH_API_HEADERS, json={"some": "payload"})

        if response.status_code == 200:
            message = "Process triggered successfully!"
        else:
            message = f"Failed to trigger process. Status: {response.status_code}"

    except Exception as e:
        message = f"Error: {str(e)}"

    # Auto-close HTML
    html = f"""
    <html>
        <body>
            <p>{message}</p>
            <script>
                setTimeout(() => window.close(), 2000);
            </script>
        </body>
    </html>
    """
    return render_template_string(html)
