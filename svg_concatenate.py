from svg_concat.ui.app_controller import AppController
from svg_concat.ui.models.config_service import ConfigService
from svg_concat.merge.concatenate_service import ConcatenateService
from svg_concat.ui.models.filters_model import FiltersModel
from svg_concat.ui.windows import set_dpi_awareness


def main():
    filter_service = FiltersModel()
    concatenate_service = ConcatenateService()
    config_service = ConfigService()
    set_dpi_awareness()
    controller = AppController(filter_service, concatenate_service, config_service)
    controller.create_app()
    app = controller.app
    app.mainloop()


if __name__ == "__main__":
    main()
