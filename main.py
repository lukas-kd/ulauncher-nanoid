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
        try:
            args = event.get_argument() or ""
            args = args.split(' ')

            if len(args) < 1 or args[0].isdigit() == False:
                return
            
            alphabet_type = args[0].lower() if len(args) == 2 else 'default'
            size = int(args[1] if len(args) > 1 else args[1])

            if alphabet_type == "default":
                alphabet = "346789ABCDEFGHJKLMNPQRTUVWXYabcdefghijkmnpqrtwxyz"
            else:
                alphabet = alphabet_type

            nanoid = generate(alphabet, size)
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=nanoid,
                    highlightable=False,
                    on_enter=CopyToClipboardAction(nanoid)
                )
            ])
        except Exception as e:
            return RenderResultListAction([
                ExtensionResultItem(
                    name="Error",
                    desc=f"{e}",
                )
            ])

if __name__ == '__main__':
    NanoIDExtension().run()
