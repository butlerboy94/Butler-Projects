import tkinter as tk
from tkinter import ttk

class PCBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced PC Builder")

        self.build_type = tk.StringVar(value="Everyday")
        self.rgb_ram = tk.BooleanVar()
        self.rgb_wires = tk.BooleanVar()
        self.rgb_fans = tk.BooleanVar()
        self.current_selection_var = tk.StringVar()

        self.step = 0
        self.total_price = 0
        self.build_data = {}

        self.output = tk.Text(root, height=20, width=70)
        self.output.pack(pady=5)

        self.next_button = ttk.Button(root, text="Start Build", command=self.next_step)
        self.next_button.pack(pady=10)

    def clear_output(self):
        self.output.delete("1.0", tk.END)

    def display_options(self, options, callback):
        self.current_selection_var.set("")
        for widget in self.root.pack_slaves():
            if isinstance(widget, ttk.Radiobutton):
                widget.destroy()

        for item in options:
            name, specs, price = item
            val = f"{name}|{specs}|{price}"
            label = f"{name} - {specs} (${price})"
            ttk.Radiobutton(self.root, text=label, variable=self.current_selection_var, value=val).pack(anchor=tk.W)

        self.next_button.config(text="Next", command=callback)

    def next_step(self):
        self.clear_output()
        steps = [
            self.choose_build_type,
            self.choose_case,
            self.choose_motherboard,
            self.choose_processor,
            self.choose_ram,
            self.choose_storage,
            self.choose_gpu,
            self.choose_psu,
            self.choose_cooling,
            self.choose_rgb,
            self.show_summary
        ]
        if self.step < len(steps):
            steps[self.step]()
        self.step += 1

    def choose_build_type(self):
        self.output.insert(tk.END, "Select a build type:\n")
        for option in ["Performance", "Budget", "Everyday"]:
            ttk.Radiobutton(self.root, text=option, variable=self.build_type, value=option).pack(anchor=tk.W)

    def choose_case(self):
        self.output.insert(tk.END, "Choose a case:\n")
        self.case_options = {
            "Performance": [("Lian Li O11 Dynamic", "ATX", 130),
                            ("Fractal Meshify 2", "ATX", 120),
                            ("NZXT H7 Flow", "ATX", 110)],
            "Budget": [("Cooler Master Q300L", "Micro-ATX", 50),
                       ("Versa H15", "Micro-ATX", 45),
                       ("Rosewill FBM-X1", "Micro-ATX", 40)],
            "Everyday": [("NZXT H510", "ATX", 75),
                         ("Phanteks P300A", "ATX", 70),
                         ("Corsair 200R", "ATX", 60)]
        }
        self.display_options(self.case_options[self.build_type.get()], self.confirm_case_selection)

    def confirm_case_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, form, price = val.split("|")
        self.build_data["case"] = name
        self.build_data["form_factor"] = form
        self.total_price += float(price)
        self.next_step()

    def choose_motherboard(self):
        self.output.insert(tk.END, "Choose a compatible motherboard:\n")
        form = self.build_data['form_factor']
        boards = {
            "ATX": [("MSI Z790", "LGA 1700, Wi-Fi 6, 4x DIMM slots", 200),
                    ("ASUS ROG STRIX B650", "AM5, Wi-Fi 6E, 4x DIMM slots", 220),
                    ("Gigabyte AORUS Elite", "LGA 1700, PCIe 5.0, 4x DIMM slots", 180)],
            "Micro-ATX": [("ASRock B550M", "AM4, Wi-Fi 6, 4x DIMM slots", 100),
                          ("MSI B450M", "AM4, 4x DIMM slots", 90),
                          ("Gigabyte B760M", "LGA 1700, PCIe 4.0, 4x DIMM slots", 110)]
        }
        self.display_options(boards[form], self.confirm_motherboard_selection)

    def confirm_motherboard_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, specs, price = val.split("|")
        self.build_data["motherboard"] = name
        self.build_data["motherboard_specs"] = specs
        self.total_price += float(price)
        self.next_step()

    def choose_processor(self):
        self.output.insert(tk.END, "Choose a processor:\n")
        cpus = {
            "Performance": [("Intel i9-14900K", "16 cores, 24 threads, 3.2 GHz base", 570),
                            ("AMD Ryzen 9 7950X", "16 cores, 32 threads, 4.5 GHz base", 550),
                            ("Intel i7-14700K", "12 cores, 20 threads, 3.6 GHz base", 480)],
            "Budget": [("Intel i3-13100F", "4 cores, 8 threads, 3.4 GHz base", 120),
                       ("AMD Ryzen 3 4100", "4 cores, 4 threads, 3.8 GHz base", 100),
                       ("Intel i5-12400F", "6 cores, 12 threads, 2.5 GHz base", 140)],
            "Everyday": [("Intel i5-13400", "10 cores, 16 threads, 2.5 GHz base", 220),
                         ("AMD Ryzen 5 5600", "6 cores, 12 threads, 3.5 GHz base", 180),
                         ("Intel i5-12600", "10 cores, 16 threads, 3.3 GHz base", 200)]
        }
        self.display_options(cpus[self.build_type.get()], self.confirm_processor_selection)

    def confirm_processor_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, specs, price = val.split("|")
        self.build_data["cpu"] = name
        self.build_data["cpu_specs"] = specs
        self.total_price += float(price)
        self.next_step()

    def choose_ram(self):
        self.output.insert(tk.END, "Choose RAM size:\n")
        ram_options = [("4GB Corsair Vengeance", "DDR4, 2400 MHz", 20),
                       ("8GB Corsair Vengeance", "DDR4, 3200 MHz", 35),
                       ("16GB Corsair Vengeance", "DDR4, 3600 MHz", 60),
                       ("32GB Corsair Vengeance", "DDR4, 3600 MHz", 110)]
        self.display_options(ram_options, self.confirm_ram_selection)

    def confirm_ram_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, specs, price = val.split("|")
        self.build_data["ram"] = name
        self.build_data["ram_specs"] = specs
        self.total_price += float(price)
        self.next_step()

    def choose_storage(self):
        self.output.insert(tk.END, "Choose storage:\n")
        storage_options = [("Samsung 970 EVO 1TB SSD", "NVMe, 3500 MB/s read", 90),
                           ("WD Blue 1TB HDD", "SATA, 7200 RPM", 45),
                           ("Crucial MX500 500GB SSD", "SATA, 560 MB/s read", 60)]
        self.display_options(storage_options, self.confirm_storage_selection)

    def confirm_storage_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, specs, price = val.split("|")
        self.build_data["storage"] = name
        self.build_data["storage_specs"] = specs
        self.total_price += float(price)
        self.next_step()

    def choose_gpu(self):
        self.output.insert(tk.END, "Choose a GPU:\n")
        gpus = {
            "Performance": [("RTX 4080", "16GB GDDR6X, 320W TDP", 1200),
                            ("RX 7900XTX", "24GB GDDR6, 355W TDP", 1000),
                            ("RTX 4070 Ti", "12GB GDDR6X, 285W TDP", 900)],
            "Budget": [("GTX 1660 Super", "6GB GDDR5, 125W TDP", 220),
                       ("RX 6500 XT", "4GB GDDR6, 107W TDP", 180),
                       ("Arc A580", "6GB GDDR6, 170W TDP", 200)],
            "Everyday": [("RTX 3060", "12GB GDDR6, 170W TDP", 320),
                         ("RX 6700 XT", "12GB GDDR6, 230W TDP", 340),
                         ("RTX 4060", "8GB GDDR6, 115W TDP", 310)]
        }
        self.display_options(gpus[self.build_type.get()], self.confirm_gpu_selection)

    def confirm_gpu_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, specs, price = val.split("|")
        self.build_data["gpu"] = name
        self.build_data["gpu_specs"] = specs
        self.total_price += float(price)
        self.next_step()

    def choose_psu(self):
        self.output.insert(tk.END, "Choose a power supply:\n")
        psus = [("Corsair RM750x", "750W, 80+ Gold, Fully Modular", 110),
                ("EVGA 600 BR", "600W, 80+ Bronze, Non-Modular", 60),
                ("Seasonic Focus 750W", "750W, 80+ Gold, Fully Modular", 100)]
        self.display_options(psus, self.confirm_psu_selection)

    def confirm_psu_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, specs, price = val.split("|")
        self.build_data["psu"] = name
        self.build_data["psu_specs"] = specs
        self.total_price += float(price)
        self.next_step()

    def choose_cooling(self):
        self.output.insert(tk.END, "Choose a CPU cooler:\n")
        form = self.build_data['form_factor']
        coolers = {
            "ATX": [("Noctua NH-D15", "Air Cooler, Dual Tower, 6 Heatpipes", 90),
                    ("Cooler Master Hyper 212", "Air Cooler, 4 Heatpipes", 40),
                    ("Corsair iCUE H100i", "AIO, 240mm Radiator", 130)],
            "Micro-ATX": [("Be Quiet Pure Rock 2", "Air Cooler, 4 Heatpipes", 35),
                          ("Arctic Freezer 34", "Air Cooler, 4 Heatpipes", 40),
                          ("DeepCool GAMMAXX 400", "Air Cooler, 4 Heatpipes", 30)]
        }
        self.display_options(coolers[form], self.confirm_cooler_selection)

    def confirm_cooler_selection(self):
        val = self.current_selection_var.get()
        if not val:
            return
        name, specs, price = val.split("|")
        self.build_data["cooler"] = name
        self.build_data["cooler_specs"] = specs
        self.total_price += float(price)
        self.next_step()

    def choose_rgb(self):
        self.output.insert(tk.END, "Choose RGB options:\n")
        ttk.Checkbutton(self.root, text="RGB RAM (+$20)", variable=self.rgb_ram).pack(anchor=tk.W)
        ttk.Checkbutton(self.root, text="RGB Wires (+$15)", variable=self.rgb_wires).pack(anchor=tk.W)
        ttk.Checkbutton(self.root, text="RGB Fans (+$25)", variable=self.rgb_fans).pack(anchor=tk.W)

        self.next_button.config(text="Next", command=self.confirm_rgb_selection)

    def confirm_rgb_selection(self):
        rgb_cost = 0
        if self.rgb_ram.get(): rgb_cost += 20
        if self.rgb_wires.get(): rgb_cost += 15
        if self.rgb_fans.get(): rgb_cost += 25
        self.total_price += rgb_cost

        self.next_step()

    def show_summary(self):
        self.output.insert(tk.END, "Build Summary:\n")
        for part, details in self.build_data.items():
            self.output.insert(tk.END, f"{part.capitalize()}: {details}\n")
        self.output.insert(tk.END, f"Total Price: ${self.total_price:.2f}")
        self.next_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()

# Create the PCBuilderApp object and start the GUI
app = PCBuilderApp(root)
root.mainloop()

