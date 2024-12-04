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
            
            alphabet_type = 'default'
            size = 12

            if len(args) == 2:
                alphabet_type = args[0]
                size = int(args[1] if args[1].isdigit() else 12)
            elif len(args) == 1:
                if args[0].isdigit():
                    given_size = int(args[0])
                    size = given_size if given_size > 0 else size
                else:
                    alphabet_type = args[0]

            alphabet = alphabet_type if alphabet_type != "default" else "346789ABCDEFGHJKLMNPQRTUVWXYabcdefghijkmnpqrtwxyz"

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
                    description=f"{e}",
                )
            ])

if __name__ == '__main__':
    NanoIDExtension().run()
