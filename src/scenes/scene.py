def callback_func():
    pass


class Scene:
    callback_func = callback_func

    def on_event(self, func):
        self.callback_func = func

    def emit(self, ev, **args):
        self.callback_func(ev, **args)
