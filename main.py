from js import document


def element_checker(event=None):
  """Retrieves transition metal information based on the entered symbol

  and displays it in the result container.
  """
  symbol_input = document.getElementById("element_name").value.strip()

  # THis dict stores all info about transition metals, I skipped anthanum, lutetium, actinium, and lawrencium  cuz if they're in group 3 or not is being debated up to now
  transition_metals = {
      "Sc": {
          "name": "Scandium",
          "atomic_number": 21,
          "atomic_mass": "44.956",
      },
      "Ti": {"name": "Titanium", "atomic_number": 22, "atomic_mass": "47.867"},
      "V": {"name": "Vanadium", "atomic_number": 23, "atomic_mass": "50.942"},
      "Cr": {"name": "Chromium", "atomic_number": 24, "atomic_mass": "51.996"},
      "Mn": {"name": "Manganese", "atomic_number": 25, "atomic_mass": "54.938"},
      "Fe": {"name": "Iron", "atomic_number": 26, "atomic_mass": "55.845"},
      "Co": {"name": "Cobalt", "atomic_number": 27, "atomic_mass": "58.933"},
      "Ni": {"name": "Nickel", "atomic_number": 28, "atomic_mass": "58.693"},
      "Cu": {"name": "Copper", "atomic_number": 29, "atomic_mass": "63.546"},
      "Zn": {"name": "Zinc", "atomic_number": 30, "atomic_mass": "65.38"},
      "Y": {"name": "Yttrium", "atomic_number": 39, "atomic_mass": "88.906"},
      "Zr": {"name": "Zirconium", "atomic_number": 40, "atomic_mass": "91.224"},
      "Nb": {"name": "Niobium", "atomic_number": 41, "atomic_mass": "92.906"},
      "Mo": {"name": "Molybdenum", "atomic_number": 42,"atomic_mass": "95.95"}, 
      "Tc": {"name": "Technetium", "atomic_number": 43, "atomic_mass": "[98]"},
      "Ru": {"name": "Ruthenium", "atomic_number": 44, "atomic_mass": "101.07"},
      "Rh": {"name": "Rhodium", "atomic_number": 45, "atomic_mass": "102.91"},
      "Pd": {"name": "Palladium", "atomic_number": 46, "atomic_mass": "106.42"},
      "Ag": {"name": "Silver", "atomic_number": 47, "atomic_mass": "107.87"},
      "Cd": {"name": "Cadmium", "atomic_number": 48, "atomic_mass": "112.41"},
      "Hf": {"name": "Hafnium", "atomic_number": 72, "atomic_mass": "178.49"},
      "Ta": {"name": "Tantalum", "atomic_number": 73, "atomic_mass": "180.95"},
      "W": {"name": "Tungsten", "atomic_number": 74, "atomic_mass": "183.84"},
      "Re": {"name": "Rhenium", "atomic_number": 75, "atomic_mass": "186.21"},
      "Os": {"name": "Osmium", "atomic_number": 76, "atomic_mass": "190.23"},
      "Ir": {"name": "Iridium", "atomic_number": 77, "atomic_mass": "192.22"},
      "Pt": {"name": "Platinum", "atomic_number": 78, "atomic_mass": "195.08"},
      "Au": {"name": "Gold", "atomic_number": 79, "atomic_mass": "196.97"},
      "Hg": {"name": "Mercury", "atomic_number": 80, "atomic_mass": "200.59"},
  }

  result_div = document.getElementById("result")

  # so that it looks clean, I chose this to capitalize first letters
  formatted_symbol = symbol_input.capitalize()

  # to check if the element exists in the transition metals dict
  if formatted_symbol in transition_metals:
    element = transition_metals[formatted_symbol]
    result_div.innerHTML = f"""
            <b>Symbol:</b> {formatted_symbol}<br>
            <b>Element:</b> {element['name']}<br>
            <b>Atomic Number:</b> {element['atomic_number']}<br>
            <b>Atomic Mass:</b> {element['atomic_mass']}
        """
  else:
    result_div.innerHTML = (
        f'<span class="text-danger">Error: "{symbol_input}" does not exist in'
        " the transition metals list. Please enter a valid symbol (e.g., Fe,"
        " Cu, Au, Ti).</span>"
    )