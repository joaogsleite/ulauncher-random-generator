import random
import string
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


class MyExtension(Extension):
  def __init__(self):
    super(MyExtension, self).__init__()
    self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

  def generate_string(self):
    letters_and_digits = string.ascii_letters + string.digits 
    length = int(self.preferences['length'])
    return ''.join((random.choice(letters_and_digits) for i in range(length)))


class KeywordQueryEventListener(EventListener):
  def on_event(self, event, extension):
    items = []
    for i in range(3):
      generated = extension.generate_string()
      items.append(
        ExtensionResultItem(
          icon="images/icon.png",
          name=generated,
          description="",
          on_enter=CopyToClipboardAction(generated),
        )
      )
    return RenderResultListAction(items)


if __name__ == "__main__":
  MyExtension().run()
