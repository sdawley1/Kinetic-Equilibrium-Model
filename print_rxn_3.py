def kinetic_model_Y(t0, initial_concentrations, species, reactions):
    '''
    Parameters
    ----------
    t0 = float = Time at which to evaluate the system of ODEs
    initial_concentrations = list = List of initial concentrations of all chemicals
    species = list = List of all chemical species involved in the reaction 
    reactions = dict = dictionary containing rate constant and stoichiometric information
    
    Returns
    -------
    Derivatives of each concentration for each species
    '''
    # rv is the dictionary where we'll store all of the concentrations at a certian time t0
    rv = {}
    
    for s in species:
        rv[s] = 0.0 # Start with differential change in concentration = 0
        
        for rxn in reactions:  # Iterate through each reaction in the system
            
            if s in rxn['stoich']: # First test if the species is a part of that reaction
                # If present, partial = (rate constant)*(coefficient of species)
                partial = rxn['k']*rxn['stoich'][s] 
                
                for s2 in rxn['stoich']: # Now find all other species in this particular reaction
                    
                    if rxn['stoich'][s2] < 0: # If the coefficient of the species is < 0, it's a reactant
                        # Add contribution of reactant to the derivative
                        partial *= initial_concentrations[species.index(s2)]**(-rxn['stoich'][s2]) 
                        
                # At this point we have the partial derivative for one species with one reaction.
                # So, we have to add it to the total
                rv[s] += partial  
    return tuple(rv.values())
