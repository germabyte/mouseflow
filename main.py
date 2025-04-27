import time
import threading
from pynput import mouse, keyboard

# Global states
events = []
recording = False
playing = False
stop_program = False

# Controllers
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()
keyboard_listener = None

def record_mouse():
    global recording, events
    recording = True
    events.clear()
    print("[Recording] Press 'Esc' to stop...")

    def on_click(x, y, button, pressed):
        if pressed and recording:
            timestamp = time.time()
            events.append((timestamp, x, y, button.name))
            print(f"Recorded click at ({x}, {y}) with {button.name}")

    listener = mouse.Listener(on_click=on_click)
    listener.start()

    while recording and not stop_program:
        time.sleep(0.1)

    listener.stop()
    print("[Recording stopped]")

def play_mouse_loop():
    global playing
    if not events:
        print("[Playback] No events to play.")
        return

    playing = True
    print("[Playback] Starting in 3 seconds... Press 'Esc' to stop.")
    time.sleep(3)

    while playing and not stop_program:
        start_time = events[0][0]
        for timestamp, x, y, button in events:
            if not playing or stop_program:
                break
            # Calculate delay relative to previous event
            delay = timestamp - start_time
            time.sleep(max(0, delay))
            mouse_controller.position = (x, y)
            btn = mouse.Button.left if button == 'left' else mouse.Button.right
            mouse_controller.click(btn)
            start_time = timestamp  # Update start_time for next delay
        if playing:
            print("[Playback] One loop finished. Restarting...")

    print("[Playback stopped]")

def on_key_press(key):
    global recording, playing, stop_program

    try:
        if key.char == 'r' and not recording:
            threading.Thread(target=record_mouse, daemon=True).start()
        elif key.char == 'p' and events and not playing:
            threading.Thread(target=play_mouse_loop, daemon=True).start()
        elif key.char == 'q':
            print("[Exiting] Stopping all threads...")
            stop_program = True
            recording = False
            playing = False
            return False  # Stop keyboard listener
    except AttributeError:
        if key == keyboard.Key.esc:
            if recording:
                recording = False
            if playing:
                playing = False

def main():
    global keyboard_listener

    print("Instructions:\n"
          "- Press 'r' to start recording\n"
          "- Press 'p' to start playback loop\n"
          "- Press 'Esc' during recording/playback to stop them\n"
          "- Press 'q' to quit\n")

    with keyboard.Listener(on_press=on_key_press) as listener:
        keyboard_listener = listener
        listener.join()

if __name__ == "__main__":
    main()
