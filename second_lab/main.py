from tum_system import Tum_system

def main():
    """This is the main function of the TUM student management system"""
    #Create a Tum_system object
    system = Tum_system()
    #Initialize the TUM system
    system.initialize_tum_system()
    #Start the interaction with the TUM system
    system.start_tum_system_interaction()
    

if __name__ == "__main__":
    main()
