import src.SimAnn as SimAnn
import src.Sudoku as Sudoku

s = Sudoku.Sudoku(9, seed=3)
best = SimAnn.simann(s, mcmc_steps= 10000, anneal_steps= 5, 
                     beta0= 1.0, beta1= 50.0,
                     seed= 1)
 
sdkpzz = Sudoku.Sudoku(best, r=0.5)

sdkpzz.showpuzzle()

bestpzz = SimAnn.simann(sdkpzz, mcmc_steps= 20000, anneal_steps= 30, 
                     beta0= 0.4, beta1= 10.0,
                     seed= 1)

assert bestpzz.cost() == 0
