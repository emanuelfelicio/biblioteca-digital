from controllers.library_controller import LibraryController
from views.menu import Menu

def main():
    controller = LibraryController()
    menu = Menu(controller)
    menu.run()

if __name__ == "__main__":
    main()
