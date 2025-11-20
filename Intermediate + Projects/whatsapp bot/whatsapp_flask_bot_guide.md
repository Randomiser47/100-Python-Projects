# WhatsApp Automated Reply Bot with Flask and Ultramsg

This guide explains step-by-step how to set up a WhatsApp automated reply bot using **Flask**, **ngrok**, and **Ultramsg**.

---

## 1. Overview

The goal is to create a bot that:
1. Receives WhatsApp messages from users.
2. Prints the message in the terminal.
3. Sends an automatic reply using Ultramsg API.

### Flow Diagram

```
WhatsApp User → Ultramsg → ngrok URL → Flask Server → Prints message + Sends reply
```

- **Ultramsg** handles incoming messages.
- **ngrok** creates a public URL pointing to your local Flask server.
- **Flask** reads messages and replies.

---

## 2. Setting up Flask

Install Flask and Requests if you haven't:

```bash
pip install flask requests
```

Create a file `server.py`:

For code check the .py file

### Explanation

1. **Receiving Messages:**
```python
message = request.json
```
- Flask receives a POST request from ngrok (which forwards Ultramsg messages).
- `request.json` parses the JSON payload.

2. **Extracting Data:**
```python
sender = message['data']['from']
text = message['data']['body']
```
- `sender` = WhatsApp number of the user.
- `text` = message content.

3. **Preparing Reply:**
```python
reply_text = f"Hello! I received your message: {text}"
```
- Customize this later for AI logic or recruiter assistant.

4. **Sending Reply:**
- Uses Ultramsg API.
- Payload encoded as `application/x-www-form-urlencoded`.
- Dynamic: works for any incoming message.

5. **Responding to Ultramsg:**
```python
return "OK", 200
```
- Confirms webhook success.

---

## 3. Running the Bot

1. Start Flask server:
```bash
python3 server.py
```
2. Start ngrok tunnel:
```bash
ngrok http 3000
```
3. Configure Ultramsg webhook to point to your ngrok URL.
4. Send a WhatsApp message to your bot. You should see:
   - Terminal prints the message.
   - WhatsApp receives the automated reply.

---

## 4. Key Points

- **ngrok** is just a tunnel: it forwards public messages to your localhost.
- **Flask** listens for POST requests — no GET needed.
- `message['data']['from']` = sender number, `message['data']['body']` = message text.
- Payload for Ultramsg reply can use the same format as their docs or a Python dictionary; both work.

---


