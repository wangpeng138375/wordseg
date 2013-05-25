import maxent.cmaxent as cmaxent

m=cmaxent.MaxentModel()
m.begin_add_event()
m.add_event(['hello'],'A')
m.add_event(['hello'],'B')
m.add_event(['hello'],'C')
m.add_event([('hello',1.0)],'D',2)
m.end_add_event()

m.train(300,'lbfgs',0,1E-05)



print m.eval(['hello'],'A')

print m.eval_all(['hello'])