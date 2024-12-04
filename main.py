from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from nanoid import generate
import string

class NanoIDExtension(Extension):
    def __init__(self):
        super(NanoIDExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, NanoIDQueryEventListener())

class NanoIDQueryEventListener(EventListener):
    def on_event(self, event, extension):
        args = event.get_argument() or ""
        args = args.split()

        # Parse arguments
        alphabet_type = args[0].lower() if len(args) > 0 else "readable"
        size = args[1] if len(args) > 1 else "10"

        # Set default alphabet
        if alphabet_type == "readable":
            alphabet = string.ascii_letters + string.digits
        elif alphabet_type == "custom":
            # Prompt user to provide custom alphabet
            return RenderResultListAction([
                ExtensionResultItem(
                    title="Type your custom alphabet",
                    subtitle="e.g., abcdef123",
                    action=None  # No immediate action; wait for user input
                )
            ])
        else:
            # Invalid alphabet type
            return RenderResultListAction([
                ExtensionResultItem(
                    title="Invalid alphabet type",
                    subtitle="Choose either 'readable' or 'custom'",
                    action=None
                )
            ])

        # Validate size
        try:
            size = int(size)
            if size < 2 or size > 12:
                raise ValueError
        except ValueError:
            return RenderResultListAction([
                ExtensionResultItem(
                    title="Invalid size",
                    subtitle="Enter a number between 2 and 12, or type a larger custom size",
                    action=None
                )
            ])

        # Generate NanoID
        nanoid = generate(alphabet, size)
        return RenderResultListAction([
            ExtensionResultItem(
                title=f"NanoID: {nanoid}",
                subtitle="Click to copy to clipboard",
                action=CopyToClipboardAction(nanoid)
            )
        ])

if __name__ == '__main__':
    NanoIDExtension().run()
