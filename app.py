from flask import Flask, render_template_string, request
import requests
import os

app = Flask(__name__)

# Replace these with your actual values
UIPATH_API_URL = "https://cloud.uipath.com/AlfalakUiPathCloud/AlfalakOrchestrator/orchestrator_/t/f0df05f7-e7c1-4edc-b601-ce711df82e9d/startprocess"
UIPATH_API_HEADERS = {
    "Authorization": "Bearer rt_30D0529B043D20107EEAEC1EDDE43F854E8475F0FA8B0EBB3F67E5F67BDEBA2B-1",
    "Content-Type": "application/json"
}

@app.route('/trigger-process')
def trigger_process():

    username = request.args.get('username')
    stepnumber = request.args.get('stepnumber')
    Details = request.args.get('Details') 

    payload = {
         
                "username": username,
                "Strategy": "Specific",
                "stepnumber": stepnumber,
                "Details": Details
            
        }

    try:
        # Send request to UiPath API
        response = requests.post(UIPATH_API_URL, headers=UIPATH_API_HEADERS, json=payload)

        if response.status_code == 200:
            message = "Process triggered successfully!"
        else:
            message = f"Failed to trigger process. Status: {response.status_code}"

    except Exception as e:
        message = f"Error: {str(e)}"

    # Auto-close HTML
    html = f"""
   <html>
  <body style="font-family: Arial, sans-serif; background: #f0f4f8; color: #333; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0;">
    <div style="background: white; padding: 20px 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center;">
      <p>{message}</p>
      <div style="margin-top: 10px; font-size: 14px; color: #555;">
        Closing in <span id="countdown">2</span> seconds...
      </div>
    </div>
    <script>
      let seconds = 2;
      const countdownElem = document.getElementById('countdown');
      const interval = setInterval(() => {{
        seconds -= 1;
        countdownElem.textContent = seconds;
        if (seconds <= 0) {{
          clearInterval(interval);
          window.close();
        }}
      }}, 1000);
    </script>
  </body>
</html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # <-- Use Render's PORT
    app.run(host="0.0.0.0", port=port)
