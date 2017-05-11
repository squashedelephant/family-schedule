
Design Strategy

1) Python Django Templates
   templates can be layered but it gets tricky so better to load 
   most things needed with empty elements identified by unique id
   and hide them when app starts then display them when needed
2) in JavaScript, always define handlers for any expected user 
   actions but beware that elements must exist in the DOM before
   handlers can be defined 
3) Python Django insists on the re-use of the same URL for both
   HTTP GET and HTTP POST which means that GET will retrieve an
   empty form while POST will submit a populated form so
   in JavaScript define 
   a) functions that match handlers in name.  ie. submitForm, clickElement
   b) additional functions that loadForm
4) in JavaScript, think about tasks that naturally go together and create
   workflow chains where functionA performs a task then calls functionB
   which performs another related task then calls functionC
