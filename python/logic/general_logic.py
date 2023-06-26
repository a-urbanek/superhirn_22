def calculate_pins(solution, guess):
    black_pins = 0
    white_pins = 0

    # Kopien der Lösung und des Rateversuchs erstellen, um sie zu modifizieren
    solution_copy = solution.copy()
    guess_copy = guess.copy()

    # Berechnung der schwarzen Pins
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            black_pins += 1
            # Markiere die Übereinstimmungen, um sie bei der Berechnung der weißen Pins zu ignorieren
            solution_copy[i] = None
            guess_copy[i] = None

    # Berechnung der weißen Pins
    for i in range(len(guess)):
        if guess_copy[i] is not None and guess_copy[i] in solution_copy:
            white_pins += 1
            # Markiere die Übereinstimmungen, um Doppelzählungen zu vermeiden
            solution_copy[solution_copy.index(guess_copy[i])] = None
            guess_copy[i] = None

    return black_pins, white_pins