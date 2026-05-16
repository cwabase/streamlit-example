# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

## Speechify MCP server

A local [Model Context Protocol](https://modelcontextprotocol.io) server that
wraps Speechify's official Text-to-Speech API lives in
`mcp_servers/speechify/`. It exposes two tools:

- `list_voices` — list available TTS voices
- `text_to_speech` — synthesize speech and write an audio file

It is registered for MCP clients via `.mcp.json` and launched with `uv`, which
installs its dependencies (`mcp`, `httpx`) on first run.

Set your API key before starting an MCP client (get one at
<https://console.sws.speechify.com/>):

```bash
export SPEECHIFY_API_KEY=your_key_here
```
