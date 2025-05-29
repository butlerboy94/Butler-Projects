def get_user_input():
    print("Welcome to the PC Builder!")
    print("Please answer the following questions to help us suggest the best parts for your PC.")

    # Ask for budget range
    budget = input("What is your budget range for the PC? (e.g., 1000-1500): ")
    
    # Ask for usage preference
    usage = input("What will you primarily use the PC for? (e.g., Gaming, Productivity, Video Editing, etc.): ").lower()
    
    # Ask for desired components
    cpu_choice = input("Do you prefer Intel or AMD for the CPU? (Intel/AMD): ").lower()
    gpu_choice = input("Do you prefer Nvidia or AMD for the GPU? (Nvidia/AMD): ").lower()
    ram_size = int(input("How much RAM would you like? (in GB, e.g., 16, 32): "))
    storage_size = int(input("How much storage would you like? (in GB, e.g., 512 for SSD, 1024 for HDD): "))
    
    return budget, usage, cpu_choice, gpu_choice, ram_size, storage_size

def suggest_parts(budget, usage, cpu_choice, gpu_choice, ram_size, storage_size):
    # Mock lists of parts (Normally, you'd fetch these from a database or API)
    cpu_options = {
        "intel": ["Intel i9-13900K", "Intel i7-12700K", "Intel i5-12600K"],
        "amd": ["AMD Ryzen 9 7950X", "AMD Ryzen 7 7700X", "AMD Ryzen 5 7600X"]
    }
    
    gpu_options = {
        "nvidia": ["NVIDIA RTX 4090", "NVIDIA RTX 3080", "NVIDIA RTX 3070"],
        "amd": ["AMD Radeon RX 7900 XTX", "AMD Radeon RX 6800 XT", "AMD Radeon RX 6700 XT"]
    }
    
    ram_options = {
        16: ["Corsair Vengeance LPX 16GB", "G.Skill Ripjaws V 16GB", "Kingston Fury 16GB"],
        32: ["Corsair Vengeance 32GB", "G.Skill Trident Z 32GB", "Kingston HyperX 32GB"]
    }
    
    storage_options = {
        512: ["Samsung 970 Evo 500GB SSD", "Western Digital Black 500GB SSD", "Crucial P3 500GB SSD"],
        1024: ["Seagate Barracuda 1TB HDD", "Western Digital Blue 1TB SSD", "Samsung 870 QVO 1TB SSD"]
    }

    # Suggest the parts based on the choices
    print("\nBased on your preferences, here are the suggested parts:")

    print("\nCPU Options:")
    if cpu_choice in cpu_options:
        print(f"Best CPU: {cpu_options[cpu_choice][0]} (Top-tier)")
    else:
        print("Please choose either 'Intel' or 'AMD'.")

    print("\nGPU Options:")
    if gpu_choice in gpu_options:
        print(f"Best GPU: {gpu_options[gpu_choice][0]} (Top-tier)")
    else:
        print("Please choose either 'Nvidia' or 'AMD'.")

    print(f"\nRAM Options: {ram_options[ram_size][0]} (Best for {ram_size}GB configuration)")

    print(f"\nStorage Options: {storage_options[storage_size][0]} (Best for {storage_size}GB storage)")

def main():
    # Step 1: Get user input
    budget, usage, cpu_choice, gpu_choice, ram_size, storage_size = get_user_input()

    # Step 2: Suggest the best parts
    suggest_parts(budget, usage, cpu_choice, gpu_choice, ram_size, storage_size)

if __name__ == "__main__":
    main()
