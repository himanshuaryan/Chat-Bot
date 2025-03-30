<h1>Telegram AI Chat Bot</h1>
<p>
  This Python program implements a Telegram bot with various functionalities, including handling user messages, providing news updates, and completing tasks like translation and summarization.
<h4><b>Key Features:</b></h4>
  <ul>
    <li><b>User Interaction:</b> The bot responds to user messages, providing information, completing tasks, and engaging in conversation.</li>
    <li><b>News Updates:</b> Users can request news on specific topics using the /news command.</li>
    <li><b>Translation and Summarization:</b> The bot uses the Google Generative AI model to translate text and summarize content.</li>
    <li><b>Other Commands:</b> The bot also includes commands for getting the current time and date, clearing the conversation history, and accessing a help menu.</li>
  </ul>
<h4><b>Overall Structure:</b></h4>
  <ul>
    <li>The code starts by importing necessary libraries and defining global variables for the Telegram bot token and the AI API key.</li>
    <li>Several functions are defined to handle different commands and user interactions.</li>
    <li>The main main() function sets up the Telegram bot and starts the polling loop.</li>
  </ul>
<h4><b>Improvements:</b></h4>
  <ul>
    <li><b>Error Handling:</b> The code includes error handling to catch and report any exceptions that occur during processing.</li>
    <li><b>User Experience:</b> The bot provides user-friendly messages and instructions.</li>
    <li><b>Efficiency:</b> The code uses asynchronous functions to improve responsiveness.</li>
    <li><b>Scalability:</b> The code can be easily scaled to handle more users and requests by adjusting the polling interval and potentially using a more powerful server.</li>
  </ul>
<h4><b>Requirements:</b></h4>
  <ul>
    <li>
      <h3><b>Python Libraries:</b></h3>
      <ol>
        <li><b>python-telegram-bot:</b> This library provides the interface for interacting with the Telegram Bot API. To install this library, run below code on your device terminal:<br>
   <b>pip install python-telegram-bot</b></li>
        <li><b>google-generativeai:</b> This library allows you to use Google's Generative AI models. To install this library, run below code on your device terminal:<br>
   <b>pip install google-generativeai</b></li>
      </ol>
    </li>
    <li>
      <h3><b>API Keys:</b></h3>
      <ol>
        <li><b>Telegram Bot Token:</b> You'll need a Telegram bot token, which you can obtain by creating a bot using <i>BotFather</i> on Telegram. This token is a string that looks like <b><i>"123456789:ABCDEFGhijklmnopqrsTUVWXYZ".</i></b></li>
        <li><b>Google Generative AI API Key:</b> You'll need a Google Generative AI API key to access the AI model. You can obtain this from the <b><i>Google Cloud Console</i></b>.</li>
      </ol>
    </li>
  </ul>
</p>
<hr>
<div><b>Trick:</b> Do not hardcore your <i>telegram-bot-token</i> and <i>ai-api-key</i> directly in the program provided.</div>
<hr>
<div>
  <b>LINKS - </b><br>
  <p>Telegram BOTFATHER : https://t.me/BotFather<br>GEMINI AI API KEY : https://aistudio.google.com/app/apikey</p>
</div>
<hr>
<b>Developer : HIMANSHU ARYAN</b>
<hr>
