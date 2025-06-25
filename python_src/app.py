import os
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

MESSAGE = os.getenv("MESSAGE", "Hello from Claude Code Container")
INSTANCE_ID = os.getenv("CLOUDFLARE_DEPLOYMENT_ID", "unknown")


def log_with_context(context: str, message: str, data=None) -> None:
    timestamp = datetime.utcnow().isoformat()
    if data is not None:
        print(f"[{timestamp}] [{context}] {message} {data}")
    else:
        print(f"[{timestamp}] [{context}] {message}")


@app.route("/")
@app.route("/container")
def health():
    log_with_context("HEALTH", "Health check requested")
    response = {
        "status": "healthy",
        "message": MESSAGE,
        "instanceId": INSTANCE_ID,
        "timestamp": datetime.utcnow().isoformat(),
        "claudeCodeAvailable": bool(os.getenv("ANTHROPIC_API_KEY")),
        "githubTokenAvailable": bool(os.getenv("GITHUB_TOKEN")),
    }
    log_with_context("HEALTH", "Health check response", response)
    return jsonify(response)


@app.route("/error")
def error_route():
    log_with_context("ERROR", "Test error triggered")
    raise RuntimeError("This is a test error from the container")


@app.route("/process-issue", methods=["POST"])
def process_issue():
    log_with_context("PROCESS_ISSUE", "Processing issue request")
    issue_context = request.get_json(force=True)
    log_with_context("PROCESS_ISSUE", "Issue context received", issue_context)
    return jsonify({"success": True, "message": "Issue processing not implemented in python version"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    log_with_context("SERVER", "Starting Python container server", {"port": port})
    app.run(host="0.0.0.0", port=port)
