from textual.app import App
from textual.widgets import Placeholder
from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.views import GridView
from textual.app import App
from textual.widgets import Button, ButtonPressed


class SimpleApp(App):

    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(), edge="left", size=40, name="Dimensions")
        #await self.view.dock(Placeholder(), Placeholder(), edge="top")
        await self.view.dock(Placeholder(), edge="bottom", size=9, name="Console")
        await self.view.dock(Placeholder(), edge="top", size=70, name="Current Board")
        pass



SimpleApp.run(log="textual.log")

