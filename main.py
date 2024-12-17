from svg_concat.ui.app import App
from svg_concat.ui.app_controller import AppController
from svg_concat.ui.models.filters_model import FiltersModel


def main():
    filter_service = FiltersModel()
    app = App()
    controller = AppController(filter_service, app)
    app.mainloop()


if __name__ == "__main__":
    main()
