from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser
import os

# La pagina web è in public/, che è anche la cartella di output di Cloudflare Pages.
ROOT = Path(__file__).resolve().parent
PUBLIC_DIR = ROOT / "public"
PORT_START = 10000
PORT_END = 10100

class LocalHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True


def main():
    if not PUBLIC_DIR.is_dir():
        print(f"Cartella non trovata: {PUBLIC_DIR}")
        input("Premi Invio per chiudere...")
        return

    os.chdir(PUBLIC_DIR)
    server = None
    port_used = None

    for port in range(PORT_START, PORT_END + 1):
        try:
            server = LocalHTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler)
            port_used = port
            break
        except OSError:
            # Se la porta è occupata, prova quella successiva.
            continue

    if server is None:
        print(f"Nessuna porta libera trovata tra {PORT_START} e {PORT_END}.")
        input("Premi Invio per chiudere...")
        return

    url = f"http://localhost:{port_used}/"
    print(f"Server locale attivo: {url}")
    if port_used != PORT_START:
        print(f"La porta {PORT_START} era occupata; è stata scelta la porta {port_used}.")
    print("Per fermarlo, premi Ctrl+C in questa finestra.")
    webbrowser.open_new_tab(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer arrestato.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
