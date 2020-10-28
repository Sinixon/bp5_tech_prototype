import app.config as config
from app.service.order_service import OrderService
from app.service.file_reader_factory import FileReaderFactory

def main():
    
    # Read menus from a file
    menus = FileReaderFactory().get_menus(config.MENU_FILE_PATH)

    # Launch the application
    print('----[Menu Recommender Application (Total Menus Loaded = {})]----'.format(len(menus)))

    # Recommend menu options, and make an order
    OrderService(menus).make_order(5)

if __name__ == "__main__":
    main()