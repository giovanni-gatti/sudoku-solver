import numpy as np

def accept(delta_c, beta):
    if delta_c <= 0: 
        return True
    if beta == np.inf: 
        return False
    p = np.exp(-beta * delta_c)
    return np.random.rand() < p 

def simann(probl, 
           anneal_steps = 10,
           mcmc_steps = 100,
           beta0 = 0.1, 
           beta1 = 10.0, 
           seed = None):
    
    if seed is not None:
        np.random.seed(seed)
        
    probl.init_config()
    c = probl.cost()
    print(f'initial cost = {c}')

    best_probl = probl.copy()
    best_c = c
    
    beta_list = np.zeros(anneal_steps)
    beta_list[:-1] = np.linspace(beta0, beta1, (anneal_steps-1))
    beta_list[-1] = np.inf
    
    for beta in beta_list:
        
        accepted = 0
        for t in range(mcmc_steps):
            move = probl.propose_move()
            delta_c = probl.compute_delta_cost(move)
            
            if accept(delta_c, beta):
                probl.accept_move(move)
                c += delta_c
                accepted += 1
                if c < best_c: 
                    best_c = c
                    best_probl = probl.copy()
                    
        print(f'acc. rate = {accepted/mcmc_steps}, beta = {beta}, c = {c}, [best = {best_c}]')
        
    best_probl.display()
    print(f"best cost = {best_c}")
    return best_probl

