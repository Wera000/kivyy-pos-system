import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

# Set the window size large enough to accommodate the complex form
Window.size = (1000, 700) 

# 1. Define the Main Screen (the one with 6 buttons)
class MainScreen(Screen):
    pass

# 2. Define the Inventory Screen
class InventoryScreen(Screen):
    pass

# 3. Define the Purchase Screen
class PurchaseScreen(Screen):
    pass

# 4. Define the Sale Screen
class SaleScreen(Screen):
    pass

# 5. Define the Employee Management Screen
class EmployeeManagementScreen(Screen):
    pass

# 6. Define the Damaged List Screen
class DamagedListScreen(Screen):
    pass

# 7. Define the Monthly List Screen
class MonthlyListScreen(Screen):
    pass

# 8. Define the Screen Manager
class CustomScreenManager(ScreenManager):
    pass

# 9. Load the Kivy Language (.kv) file to define the design
# IMPORTANT: The design file MUST be named 'app_design.kv' and 
# be in the same directory as this Python script.
Builder.load_file('app_design.kv')

# 10. Define the main application class
class KivyDesignApp(App):
    # The build method returns the root widget, which is our ScreenManager
    def build(self):
        sm = CustomScreenManager()
        # Add all screens to the manager
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(InventoryScreen(name='inventory'))
        sm.add_widget(PurchaseScreen(name='purchase'))
        sm.add_widget(SaleScreen(name='sale'))
        sm.add_widget(EmployeeManagementScreen(name='employee_management'))
        sm.add_widget(DamagedListScreen(name='damaged_list'))
        sm.add_widget(MonthlyListScreen(name='monthly_list'))
        return sm

if __name__ == '__main__':
    KivyDesignApp().run()