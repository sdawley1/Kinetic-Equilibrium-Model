def print_rxn(rxn):
    '''
    Parameters
    ----------
    rxn = dictionary w/ 'rate constant':'value', 'stoich':'stoichiometry of rxn as dictionary'
    'rxns' above is an example of what might be passed into this function
    'initial_concentrations.keys()' is an example of what might be passed for species
    
    Returns
    -------
    string delineating the reaction with rate constant appended at the end
    '''
    reactants = ''
    products = ''
    for species in rxn['stoich']:
        # Test if the species is a reactant or product
        # If the coefficient is < 0, reactant!
        # Otherwise, product!
        if rxn['stoich'][species] < 0:
            if reactants != '':
                reactants += ' + '
            reactants += str(-1*rxn['stoich'][species])+str(species)
        else:
            if products != '':
                products += ' + '
            products += str(rxn['stoich'][species])+str(species)
    print(reactants + ' --> ' + products + '   k=' + str(rxn['k']))
    return
